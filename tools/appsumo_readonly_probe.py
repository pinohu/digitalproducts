#!/usr/bin/env python3
"""Read-only connector spike for verified AppSumo operating tools.

Currently supports small GET-only probes for Agiled, AgenticFlow,
AITable.ai/APITable, Boost.space, CallScaler, Certopus, Dadan, Emailit, Flotiq, Flowlu, Formaloo, Late/Zernio, and Procesio.
The script never writes to external systems and never persists secrets.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib.parse import quote

import requests
from dotenv import load_dotenv

TOOLS_ROOT = Path(__file__).resolve().parent
DEFAULT_ENV_FILES = [TOOLS_ROOT / ".env"]

PLATFORMS: dict[str, dict[str, Any]] = {
    "agiled": {
        "base_url": "https://app.agiled.app/api/v1",
        "secret": "AGILED_API_KEY",
        "resources": {
            "users": "/users",
            "projects": "/projects",
            "clients": "/clients",
            "tasks": "/tasks",
        },
    },
    "agenticflow": {
        "base_url": "https://api.agenticflow.ai",
        "secret": "AGENTICFLOW_API_KEY",
        "auth": "bearer",
        "resources": {
            # Lowest-risk documented REST read. Requires workspace scope and, for
            # the current AppSumo key, project scope before returning agent data.
            "agents": "/v1/agents/",
        },
    },
    "aitable": {
        "base_url": "https://aitable.ai/fusion/v1",
        "secret": "AITABLE_API_KEY",
        "resources": {
            "spaces": "/spaces",
            "nodes": "/spaces/{space_id}/nodes",
            "records": "/datasheets/{datasheet_id}/records",
        },
    },
    "boostspace": {
        # Official OpenAPI servers are tenant-shaped:
        # https://{system}.boost.space/api. Do not guess the system name.
        "base_url": None,
        "secret": "BOOST_SPACE_API_KEY",
        "auth": "bearer",
        "requires_base_url": True,
        "resources": {
            "activities": "/activities",
            "address-countries": "/address/country",
        },
    },
    "callscaler": {
        "base_url": "https://callscaler.com/api/v1",
        "secret": "CALLSCALER_API_KEY",
        "auth": "bearer",
        "resources": {
            # DIG-64: guarded metadata-first reads only. Calls/numbers can expose
            # sensitive phone/caller data, so use --page-size 1 and
            # --summary-only unless a future issue approves deeper inspection.
            "account": "/account",
            "analytics-summary": "/analytics/summary",
            "calls": "/calls",
            "dashboard-stats": "/dashboard/stats",
            "me": "/me",
            "numbers": "/numbers",
            "user": "/user",
        },
    },
    "certopus": {
        "base_url": "https://api.certopus.com",
        "secret": "CERTOPUS_API_KEY",
        "auth": "x_api_key",
        "resources": {
            "organisations": "/v1/organisations",
            "smtp": "/v1/smtp",
            "templates": "/v1/templates",
            "wallet": "/v1/wallet",
        },
    },
    "dadan": {
        "base_url": "https://app.dadan.io/api/v1/usedadan",
        "secret": "DADAN_API_KEY",
        "auth": "x_dadan_api_key",
        "resources": {
            # Requires a request created by the same API key. This is a GET-only
            # status/detail check; creating request links is a POST and remains out of scope.
            "recording-request": "/requestrecording/{request_code}",
        },
    },
    "emailit": {
        "base_url": "https://api.emailit.com/v2",
        "secret": "EMAILIT_API_KEY",
        "auth": "bearer",
        "resources": {
            "api-keys": "/api-keys",
            "audiences": "/audiences",
            "contacts": "/contacts",
            "domains": "/domains",
            "emails": "/emails",
            "events": "/events",
            "suppressions": "/suppressions",
            "templates": "/templates",
            "webhooks": "/webhooks",
        },
    },
    "flowlu": {
        # Official OpenAPI servers are tenant-shaped:
        # https://{company}.flowlu.com/api/v1/module. Do not guess the company subdomain.
        "base_url": None,
        "secret": "FLOWLU_API_KEY",
        "auth": "query_api_key",
        "requires_base_url": True,
        "resources": {
            "agile-projects": "/agile/projects/list",
            "crm-accounts": "/crm/account/list",
            "invoices": "/fin/invoice/list",
            "tasks": "/task/tasks/list",
        },
    },
    "flotiq": {
        # Official docs: https://flotiq.com/docs/API/
        # Use X-AUTH-TOKEN and keep reads metadata-first. Content object
        # endpoints can expose private CMS payloads, so the default resource set
        # is limited to content-type definitions and a zero/low-risk media count
        # smoke check unless a future issue approves specific content types.
        "base_url": "https://api.flotiq.com",
        "secret": "FLOTIQ_API_KEY",
        "auth": "x_auth_token",
        "resources": {
            "content-types": "/api/v1/internal/contenttype",
            "media": "/api/v1/content/_media",
        },
    },
    "formaloo": {
        # Official docs: https://docs.formaloo.com/#/ and
        # https://help.formaloo.com/en/articles/8143469-how-to-use-formaloo-api-keys-in-formaloo-api
        # Use POST only to obtain the short-lived JWT token, then GET-only
        # metadata reads. Do not submit forms or export rows/submissions here.
        "base_url": "https://api.formaloo.me/v3.0",
        "secret": "FORMALOO_API_KEY",
        "secondary_secret": "FORMALOO_API_SECRET",
        "auth": "formaloo_jwt",
        "resources": {
            "forms": "/forms/",
            "profile": "/profile/",
        },
    },
    "late": {
        # Late rebranded its public docs to Zernio; docs.getlate.dev redirects
        # to docs.zernio.com. The legacy getlate.dev API base still works with
        # GETLATE_DEV_API_KEY and keeps the AppSumo/operator naming stable.
        "base_url": "https://getlate.dev/api/v1",
        "secret": "GETLATE_DEV_API_KEY",
        "auth": "bearer",
        "resources": {
            "account-health": "/accounts/health",
            "accounts": "/accounts",
            "posts": "/posts",
            "profiles": "/profiles",
            "usage-stats": "/usage-stats",
            "users": "/users",
        },
    },
    "procesio": {
        "base_url": "https://webapi.procesio.app",
        "secret": "PROCESIO_API_KEY",
        "auth": "procesio_api_key",
        "resources": {
            "users-me": "/api/Users/me",
            "workspaces": "/api/Workspaces",
            "projects-count": "/api/Projects/count",
            "projects": "/api/Projects",
        },
    },
}

REDACT_FIELD_FRAGMENTS = {
    "token",
    "secret",
    "password",
    "authorization",
    "api_key",
    "apikey",
    "cookie",
    "handle",
    "url",
    "username",
}

REDACT_FIELD_NAMES = {
    "caller",
    "caller_id",
    "cc",
    "bcc",
    "email",
    "from",
    "name",
    "number",
    "phone",
    "recipient",
    "recipients",
    "recording",
    "reply_to",
    "reply-to",
    "sender",
    "subject",
    "to",
    "transcript",
    "url",
    "username",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run GET-only connector probes for verified AppSumo tools without storing secrets."
    )
    parser.add_argument("platform", choices=sorted(PLATFORMS), help="External platform to probe")
    parser.add_argument("resource", nargs="?", help="Resource to fetch; omit with --list-resources")
    parser.add_argument("--env-file", action="append", type=Path, help="Additional dotenv file to load")
    parser.add_argument("--base-url", help="Override the default API base URL for tenant-specific APIs")
    parser.add_argument(
        "--secret-name",
        help="Override the default environment variable name for the API key without printing the secret",
    )
    parser.add_argument("--space-id", help="AITable space ID for resources that require it")
    parser.add_argument("--datasheet-id", help="AITable datasheet ID for record reads")
    parser.add_argument("--workspace-id", help="AgenticFlow workspace UUID for project-scoped reads")
    parser.add_argument("--project-id", help="AgenticFlow project UUID for project-scoped reads")
    parser.add_argument("--workspace", help="Procesio workspace header value for workspace-scoped reads")
    parser.add_argument("--api-key-name", help="Procesio API key name for the required key/value header pair")
    parser.add_argument("--request-code", help="Dadan recording request code for the read-only detail endpoint")
    parser.add_argument("--page-size", type=int, default=10, help="Limit/page-size query parameter where supported")
    parser.add_argument("--timeout", type=int, default=20, help="Request timeout in seconds")
    parser.add_argument("--list-resources", action="store_true", help="List supported read-only resources")
    parser.add_argument("--json", action="store_true", help="Emit compact JSON instead of a human summary")
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Emit only aggregate counts/statuses and omit raw record samples for Paperclip-safe reporting",
    )
    return parser.parse_args()


def load_environment(extra_env_files: list[Path] | None) -> None:
    for env_file in DEFAULT_ENV_FILES:
        if env_file.exists():
            load_dotenv(env_file, override=False)
    for env_file in extra_env_files or []:
        if env_file.exists():
            # Explicit --env-file is operator intent and should override stale shell/tools values.
            load_dotenv(env_file, override=True)


def build_path(template: str, args: argparse.Namespace) -> str:
    replacements = {
        "space_id": args.space_id,
        "datasheet_id": args.datasheet_id,
        "request_code": args.request_code,
    }
    path = template
    for key, value in replacements.items():
        placeholder = "{" + key + "}"
        if placeholder in path:
            if not value:
                raise SystemExit(f"Resource requires --{key.replace('_', '-')}")
            path = path.replace(placeholder, quote(value, safe=""))
    return path


def redacted(value: Any) -> Any:
    if isinstance(value, dict):
        cleaned = {}
        for key, nested in value.items():
            key_lower = str(key).lower()
            if key_lower in REDACT_FIELD_NAMES or any(fragment in key_lower for fragment in REDACT_FIELD_FRAGMENTS):
                cleaned[key] = "<redacted>"
            else:
                cleaned[key] = redacted(nested)
        return cleaned
    if isinstance(value, list):
        return [redacted(item) for item in value]
    return value


def extract_records(cleaned: Any, resource: str) -> list[Any]:
    if isinstance(cleaned, dict):
        if isinstance(cleaned.get("data"), list):
            return cleaned["data"]
        if isinstance(cleaned.get("data"), dict) and isinstance(cleaned["data"].get("records"), list):
            return cleaned["data"]["records"]
        if isinstance(cleaned.get("data"), dict) and isinstance(cleaned["data"].get("spaces"), list):
            return cleaned["data"]["spaces"]
        if isinstance(cleaned.get("data"), dict) and isinstance(cleaned["data"].get("nodes"), list):
            return cleaned["data"]["nodes"]
        if isinstance(cleaned.get(resource), list):
            return cleaned[resource]
        merged_records: list[Any] = []
        for value in cleaned.values():
            if isinstance(value, list):
                merged_records.extend(value)
        if merged_records:
            return merged_records
    if isinstance(cleaned, list):
        return cleaned
    return []


def normalized_record_fields(record: Any) -> dict[str, Any]:
    if not isinstance(record, dict):
        return {}
    fields = record.get("fields")
    if isinstance(fields, dict):
        merged = {**record, **fields}
        merged.pop("fields", None)
        return merged
    return record


def aggregate_records(records: list[Any]) -> dict[str, Any]:
    status_counts: dict[str, int] = {}
    visible_field_names: set[str] = set()
    for record in records:
        fields = normalized_record_fields(record)
        for key, value in fields.items():
            key_lower = str(key).lower()
            if key_lower in REDACT_FIELD_NAMES or any(fragment in key_lower for fragment in REDACT_FIELD_FRAGMENTS):
                continue
            visible_field_names.add(str(key))
            if key_lower in {"status", "state", "stage", "type"} and value not in (None, ""):
                status = str(value)[:80]
                status_counts[status] = status_counts.get(status, 0) + 1
    return {
        "status_counts": dict(sorted(status_counts.items())) if status_counts else {},
        "visible_field_names": sorted(visible_field_names)[:50],
    }


def summarize_payload(
    platform: str, resource: str, payload: Any, page_size: int, summary_only: bool = False
) -> dict[str, Any]:
    cleaned = redacted(payload)
    top_level_keys = sorted(str(key) for key in cleaned.keys())[:50] if isinstance(cleaned, dict) else []
    if platform == "dadan" and summary_only:
        # Dadan's detail endpoint can expose private recording-request and
        # submission/video metadata. In summary mode, report only coarse access
        # signals and safe aggregate counts instead of generic list extraction.
        submission_count = None
        if isinstance(cleaned, dict):
            for key, value in cleaned.items():
                if "submission" in str(key).lower() and isinstance(value, list):
                    submission_count = len(value)
                    break
        return {
            "platform": platform,
            "resource": resource,
            "record_count_visible": 0,
            "status_counts": {},
            "visible_field_names": [],
            "success": cleaned.get("success") if isinstance(cleaned, dict) and isinstance(cleaned.get("success"), bool) else None,
            "submission_count": submission_count,
        }
    if platform == "flotiq" and summary_only:
        records = extract_records(cleaned, resource)
        safe_summary = {
            "platform": platform,
            "resource": resource,
            "record_count_visible": len(records),
            **aggregate_records(records),
        }
        # Flotiq content-type records include schema/meta definition keys. The
        # values are already omitted in summary-only mode, but keep even field
        # names out of n8n/Paperclip summaries to avoid encouraging schema export.
        safe_summary["visible_field_names"] = [
            name
            for name in safe_summary.get("visible_field_names", [])
            if name not in {"schemaDefinition", "metaDefinition"}
        ]
        if isinstance(cleaned, dict):
            for count_key in ("total_count", "total", "count"):
                if count_key in cleaned and isinstance(cleaned[count_key], (int, float)):
                    safe_summary[count_key] = cleaned[count_key]
        return safe_summary

    if platform == "formaloo" and summary_only:
        data = cleaned.get("data") if isinstance(cleaned, dict) and isinstance(cleaned.get("data"), dict) else {}
        if resource == "forms":
            forms = data.get("forms") if isinstance(data.get("forms"), list) else []
            return {
                "platform": platform,
                "resource": resource,
                "record_count_visible": len(forms),
                "total_count": data.get("count"),
                **aggregate_records(forms),
            }
        if resource == "profile":
            profile = data.get("profile") if isinstance(data.get("profile"), dict) else {}
            safe_fields = {
                key: value
                for key, value in profile.items()
                if key in {"verified_email", "score", "balance", "total_credit", "used_trial", "connected_to_hubspot"}
            }
            team = profile.get("team") if isinstance(profile.get("team"), dict) else {}
            if team:
                safe_fields["team_fields_visible"] = sorted(str(key) for key in team.keys())
            return {
                "platform": platform,
                "resource": resource,
                "record_count_visible": 1 if profile else 0,
                "status_counts": {},
                "visible_field_names": sorted(safe_fields.keys()),
                "profile_summary": safe_fields,
            }

    records = extract_records(cleaned, resource)
    summary = {
        "platform": platform,
        "resource": resource,
        "record_count_visible": len(records),
        **aggregate_records(records),
    }
    if isinstance(cleaned, dict):
        for count_key in ("total_count", "total", "count"):
            if count_key in cleaned and isinstance(cleaned[count_key], (int, float)):
                summary[count_key] = cleaned[count_key]
    if not summary_only:
        summary["sample"] = records[:page_size] if records else cleaned
    return summary


def fetch(args: argparse.Namespace) -> tuple[int, dict[str, str], Any]:
    platform_cfg = PLATFORMS[args.platform]
    if not args.resource:
        raise SystemExit("resource is required unless --list-resources is used")
    if args.resource not in platform_cfg["resources"]:
        raise SystemExit(
            f"Unsupported resource {args.resource!r}. Use --list-resources to see supported reads."
        )

    secret_name = args.secret_name or platform_cfg["secret"]
    api_key = os.getenv(secret_name)
    if not api_key:
        raise SystemExit(f"Missing {secret_name}. Put it in tools/.env or pass --env-file for a secure dotenv file.")

    if platform_cfg.get("requires_base_url") and not args.base_url:
        raise SystemExit(
            f"{args.platform} requires --base-url with the verified tenant API base; "
            "do not guess tenant/system subdomains."
        )
    base_url = (args.base_url or platform_cfg["base_url"]).rstrip("/")
    path = build_path(platform_cfg["resources"][args.resource], args)
    url = f"{base_url}{path}"
    headers = {"Accept": "application/json"}
    params: dict[str, Any] = {}
    auth_shape = platform_cfg.get("auth", "bearer")
    if auth_shape == "query_api_key":
        params["api_key"] = api_key
    elif auth_shape == "x_api_key":
        headers["X-API-KEY"] = api_key
    elif auth_shape == "x_dadan_api_key":
        headers["X-Dadan-API-Key"] = api_key
    elif auth_shape == "x_auth_token":
        headers["X-AUTH-TOKEN"] = api_key
    elif auth_shape == "formaloo_jwt":
        secret_name_2 = platform_cfg["secondary_secret"]
        api_secret = os.getenv(secret_name_2)
        if not api_secret:
            raise SystemExit(
                f"Missing {secret_name_2}. Formaloo requires FORMALOO_API_KEY plus FORMALOO_API_SECRET "
                "to mint a short-lived authorization token."
            )
        token_response = requests.post(
            f"{base_url}/oauth2/authorization-token/",
            headers={"x-api-key": api_key, "Authorization": f"Basic {api_secret}"},
            data={"grant_type": "client_credentials"},
            timeout=args.timeout,
        )
        try:
            token_payload = token_response.json()
        except ValueError:
            token_payload = {}
        token = token_payload.get("authorization_token")
        if not token_response.ok or not token:
            raise SystemExit(f"Formaloo token request failed with HTTP {token_response.status_code}")
        headers["x-api-key"] = api_key
        headers["Authorization"] = f"JWT {token}"
    elif auth_shape == "procesio_api_key":
        if not args.api_key_name:
            raise SystemExit(
                "procesio requires --api-key-name because the Web API uses separate key/value headers; "
                "PROCESIO_API_KEY supplies only the value."
            )
        headers["key"] = args.api_key_name
        headers["value"] = api_key
        if args.workspace:
            headers["workspace"] = args.workspace
    else:
        headers["Authorization"] = f"Bearer {api_key}"
    if args.page_size:
        # Common names used by these APIs; unsupported APIs generally ignore them.
        params.update({"limit": args.page_size, "pageSize": args.page_size})
    if args.platform == "agenticflow":
        if not args.workspace_id:
            raise SystemExit("agenticflow agents requires --workspace-id from the AgenticFlow UI or CLI auth state")
        params["workspace_id"] = args.workspace_id
        if args.project_id:
            params["project_id"] = args.project_id

    response = requests.get(url, headers=headers, params=params, timeout=args.timeout)
    response_headers = {
        "content_type": response.headers.get("content-type", ""),
        "request_url": response.url.replace(api_key, "<redacted>"),
    }
    try:
        payload: Any = response.json()
    except ValueError:
        payload = {"text": response.text[:1000]}
    return response.status_code, response_headers, payload


def main() -> int:
    args = parse_args()
    platform_cfg = PLATFORMS[args.platform]
    if args.list_resources:
        print("\n".join(sorted(platform_cfg["resources"])))
        return 0

    load_environment(args.env_file)
    status_code, response_headers, payload = fetch(args)
    summary = summarize_payload(args.platform, args.resource, payload, args.page_size, args.summary_only)
    safe_response_headers = dict(response_headers)
    if args.summary_only:
        # Summary mode is intended for Paperclip/n8n notifications. Avoid
        # emitting even safe request URLs because some platforms' content/media
        # URLs are deliberately banned by downstream redaction guards.
        safe_response_headers.pop("request_url", None)
    summary.update({"status_code": status_code, **safe_response_headers})

    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        print(f"{args.platform}/{args.resource}: HTTP {status_code}")
        print(f"visible records: {summary['record_count_visible']}")
        if summary["status_counts"]:
            print("status counts:")
            print(json.dumps(summary["status_counts"], indent=2, ensure_ascii=False))
        if args.summary_only:
            print("visible field names:")
            print(json.dumps(summary["visible_field_names"], indent=2, ensure_ascii=False))
        else:
            print(json.dumps(summary["sample"], indent=2, ensure_ascii=False)[:4000])

    return 0 if 200 <= status_code < 300 else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.RequestException as exc:
        print(f"Request failed: {exc}", file=sys.stderr)
        raise SystemExit(2)
