import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const statePath = path.join(__dirname, "..", "governance", "release-state.json");
const state = JSON.parse(fs.readFileSync(statePath, "utf8"));

console.log(`${state.product} status`);
console.log(`Environment: ${state.environment}`);
console.log(`Last updated: ${state.lastUpdated}`);
if (state.launchTruth) {
  console.log(`Launch truth: ${state.launchTruth}`);
}
if (state.shippedGate) {
  console.log(
    `Shipped gate: ${state.shippedGate.issue} (${state.shippedGate.status}) — ${state.shippedGate.evidenceLedgerPath}`
  );
}
console.log("");
console.log("Owners:");
for (const [area, owner] of Object.entries(state.owners)) {
  console.log(`- ${area}: ${owner}`);
}
console.log("");
console.log("Blocked release checks:");

const blocked = [];
for (const [key, value] of Object.entries(state.releaseReadiness)) {
  if (key === "testimonialsCount") {
    if (value < 3) {
      blocked.push(`${key}: ${value}/3`);
    }
  } else if (!value) {
    blocked.push(`${key}: pending`);
  }
}

for (const [key, value] of Object.entries(state.qualityEvidence)) {
  if (!value) {
    blocked.push(`${key}: pending`);
  }
}

if (!blocked.length) {
  console.log("- none");
} else {
  for (const line of blocked) {
    console.log(`- ${line}`);
  }
}

console.log("");
console.log(
  `Manual-action source of truth: ${state.manualActions?.ledgerPath ?? "00-foundation/operator-system/manual-actions-ledger.md"}`
);
if (state.manualActions?.highestPriorityLaunchInputs?.length) {
  console.log("Highest-priority manual launch inputs:");
  for (const item of state.manualActions.highestPriorityLaunchInputs) {
    console.log(`- ${item}`);
  }
}
console.log(
  `Mobile handoff packet: ${state.observability?.mobileControlCenterPath ?? "00-foundation/operator-system/mobile-control-center.md"}`
);
