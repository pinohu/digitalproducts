import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const statePath = path.join(__dirname, "..", "governance", "release-state.json");
const state = JSON.parse(fs.readFileSync(statePath, "utf8"));

const checks = [
  ["qualityEvidence.storybookBuilt", state.qualityEvidence.storybookBuilt],
  ["qualityEvidence.playwrightPassed", state.qualityEvidence.playwrightPassed],
  ["qualityEvidence.axePassed", state.qualityEvidence.axePassed],
  ["qualityEvidence.pa11yPassed", state.qualityEvidence.pa11yPassed],
  ["qualityEvidence.lighthousePassed", state.qualityEvidence.lighthousePassed],
  ["releaseReadiness.gumroadProductUrlWired", state.releaseReadiness.gumroadProductUrlWired],
  ["releaseReadiness.checkoutFlowTested", state.releaseReadiness.checkoutFlowTested],
  ["releaseReadiness.automationFlowsLive", state.releaseReadiness.automationFlowsLive],
  ["releaseReadiness.domainLinked", state.releaseReadiness.domainLinked],
  ["releaseReadiness.firstSaleEvidenceCaptured", state.releaseReadiness.firstSaleEvidenceCaptured],
  ["releaseReadiness.manualApprovalRecorded", state.releaseReadiness.manualApprovalRecorded],
  ["observability.mobileHandoffReady", state.observability.mobileHandoffReady],
  ["observability.manualActionLedgerReady", state.observability.manualActionLedgerReady],
  ["observability.paperclipHeartbeatActive", state.observability.paperclipHeartbeatActive]
];

const failed = checks.filter(([, passed]) => !passed).map(([label]) => label);

if (state.releaseReadiness.testimonialsCount < 3) {
  failed.push(
    `releaseReadiness.testimonialsCount (${state.releaseReadiness.testimonialsCount}/3)`
  );
}

if (failed.length) {
  console.error("Release gate is still blocked:");
  for (const label of failed) {
    console.error(`- ${label}`);
  }
  process.exit(1);
}

console.log("Release gate is satisfied.");
