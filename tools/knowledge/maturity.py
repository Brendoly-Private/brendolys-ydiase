#!/usr/bin/env python3
"""YDIASE knowledge maturity engine.

Calculates K0-K6 from explicit machine-readable evidence. Missing evidence is UNKNOWN.
The engine is conservative by design: it never infers a PASS from prose alone.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

K_LEVELS = ["K0", "K1", "K2", "K3", "K4", "K5", "K6"]
E_LEVELS = ["E0", "E1", "E2", "E3", "E4"]
VALID_STATES = {"PASS", "FAIL", "N/A", "UNKNOWN"}

K_CRITERIA = {
    "K0": ["stableId", "kind", "name", "responsibilityOrPurpose"],
    "K1": ["ownerOrAuthority", "domainOrScope", "boundaries", "sourceDocuments"],
    "K2": ["logicalRelations", "dependencies", "upstreamDownstream", "authoritativeOwnership", "impactTraceability"],
    "K3": ["apiOrEventContractsWhenApplicable", "dataContracts", "invariants", "requirements", "adrForStructuralDecisions", "versioningRules", "compatibilityRules"],
    "K4": ["dataClassification", "securityControls", "privacyAndRetentionWhenApplicable", "sloOrCriticality", "observability", "backupRecoveryWhenStateful", "runbookOrOperationalProcedure", "namedOwners"],
    "K5": ["automatedValidation", "contractTests", "securityVerification", "restoreOrResilienceTestWhenApplicable", "evidenceLinks", "unresolvedCriticalGapsEqualsZero"],
    "K6": ["implementationTrace", "deploymentTrace", "productionObservabilityWhenDeployed", "changeImpactProcess", "reviewCadence", "deprecationAndRetirementRules", "driftDetection"],
}

E_CRITERIA = {
    "E0": [],
    "E1": ["sourceIdentified"],
    "E2": ["authoritativeOrCorroborated"],
    "E3": ["reproducibleVerification"],
    "E4": ["runtimeOrOperationalObservation", "observationFreshness"],
}

@dataclass
class LevelResult:
    level: str
    passed: bool
    criteria: dict[str, str]


def _state(value: Any) -> str:
    if isinstance(value, str) and value in VALID_STATES:
        return value
    if isinstance(value, dict):
        state = value.get("state")
        if state in VALID_STATES:
            return state
    return "UNKNOWN"


def _passes(state: str) -> bool:
    return state in {"PASS", "N/A"}


def calculate_continuous(evidence: dict[str, Any], criteria_by_level: dict[str, list[str]], levels: list[str]) -> tuple[str | None, list[LevelResult]]:
    achieved = None
    results: list[LevelResult] = []
    for level in levels:
        criteria = {criterion: _state(evidence.get(criterion)) for criterion in criteria_by_level[level]}
        passed = all(_passes(state) for state in criteria.values())
        results.append(LevelResult(level, passed, criteria))
        if not passed:
            break
        achieved = level
    return achieved, results


def calculate_knowledge(entity: dict[str, Any]) -> dict[str, Any]:
    spec = entity.get("spec", {}) if isinstance(entity.get("spec"), dict) else {}
    evidence = spec.get("knowledgeEvidence", {}) if isinstance(spec.get("knowledgeEvidence"), dict) else {}
    achieved, results = calculate_continuous(evidence, K_CRITERIA, K_LEVELS)
    declared = spec.get("knowledgeMaturity")
    errors = []
    if declared in K_LEVELS:
        if achieved is None or K_LEVELS.index(declared) > K_LEVELS.index(achieved):
            errors.append(f"declared {declared} exceeds calculated {achieved or 'NONE'}")
    return {"declared": declared, "calculated": achieved, "levels": [asdict(r) for r in results], "errors": errors}


def calculate_evidence(assertion: dict[str, Any]) -> dict[str, Any]:
    evidence = assertion.get("evidenceConfidence", {}) if isinstance(assertion.get("evidenceConfidence"), dict) else {}
    achieved, results = calculate_continuous(evidence, E_CRITERIA, E_LEVELS)
    declared = assertion.get("confidence")
    errors = []
    if declared in E_LEVELS and E_LEVELS.index(declared) > E_LEVELS.index(achieved or "E0"):
        errors.append(f"declared {declared} exceeds calculated {achieved or 'E0'}")
    return {"declared": declared, "calculated": achieved or "E0", "levels": [asdict(r) for r in results], "errors": errors}
