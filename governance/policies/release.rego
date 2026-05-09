package release

default allow := false

required_flags := {
  "quality.storybookBuilt": input.qualityEvidence.storybookBuilt,
  "quality.playwrightPassed": input.qualityEvidence.playwrightPassed,
  "quality.axePassed": input.qualityEvidence.axePassed,
  "quality.pa11yPassed": input.qualityEvidence.pa11yPassed,
  "quality.lighthousePassed": input.qualityEvidence.lighthousePassed,
  "release.gumroadProductUrlWired": input.releaseReadiness.gumroadProductUrlWired,
  "release.checkoutFlowTested": input.releaseReadiness.checkoutFlowTested,
  "release.automationFlowsLive": input.releaseReadiness.automationFlowsLive,
  "release.domainLinked": input.releaseReadiness.domainLinked,
  "release.firstSaleEvidenceCaptured": input.releaseReadiness.firstSaleEvidenceCaptured,
  "release.manualApprovalRecorded": input.releaseReadiness.manualApprovalRecorded,
  "observability.mobileHandoffReady": input.observability.mobileHandoffReady,
  "observability.manualActionLedgerReady": input.observability.manualActionLedgerReady,
  "observability.paperclipHeartbeatActive": input.observability.paperclipHeartbeatActive
}

allow if {
  every key, value in required_flags {
    value
  }
  input.releaseReadiness.testimonialsCount >= 3
}

deny[msg] if {
  some key
  required_flags[key] == false
  msg := sprintf("%s must be true before release", [key])
}

deny[msg] if {
  input.releaseReadiness.testimonialsCount < 3
  msg := sprintf("release.testimonialsCount must be at least 3 (current: %d)", [input.releaseReadiness.testimonialsCount])
}
