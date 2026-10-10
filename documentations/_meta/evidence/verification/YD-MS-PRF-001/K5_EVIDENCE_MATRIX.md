---
document_id: "YD-DOC-EVD-PRF-001-K5-EVIDENCE-MATRIX"
title: "YD-MS-PRF-001 — K5 Evidence Matrix"
document_type: "evidence-record"
document_role: "Documente une preuve, un modèle ou une matrice de vérification K5 du microservice concerné."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "evidence"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "evidence"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-PRF-001 — K5 Evidence Matrix

> **Rôle du document**
> Documente une preuve, un modèle ou une matrice de vérification K5 du microservice concerné.
> **Usage développement :** référence de support pour la vérification, la qualification et les décisions de readiness.

Statut : EVIDENCE-PLAN / EXECUTION-PENDING
Nature : AUTH
Criticité : C1

| Evidence ID | Critère K5 | Preuve attendue | État |
|---|---|---|---|
| PRF1-K5-EV-001 | automatedValidation | invariants d'autorité, versions, minimisation et mutations | BLOCKED-BY-IMPLEMENTATION |
| PRF1-K5-EV-002 | contractTests | YD-CTR-PRF-CURRENT-PROFILE-v1 + entrées IDN/CNS/CFG | BLOCKED-BY-IMPLEMENTATION |
| PRF1-K5-EV-003 | securityVerification | self-access, IDOR, scopes, accès support | BLOCKED-BY-IMPLEMENTATION |
| PRF1-K5-EV-004 | privacyVerification | décision CNS absente/invalide => fail-closed | BLOCKED-BY-IMPLEMENTATION |
| PRF1-K5-EV-005 | resilience | restauration complète depuis chaîne PRF-001 | NOT-EXECUTED |
| PRF1-K5-EV-006 | resilience | restauration sans PRF-002 disponible | NOT-EXECUTED |
| PRF1-K5-EV-007 | privacyVerification | restriction/suppression postérieure au restore réappliquée | NOT-EXECUTED |
| PRF1-K5-EV-008 | resilience | replay/réconciliation projections idempotents | NOT-EXECUTED |
| PRF1-K5-EV-009 | integrity | subject/version/intégrité après restore | NOT-EXECUTED |
| PRF1-K5-EV-010 | operationalVerification | runbook exécutable sans connaissance tacite bloquante | NOT-EXECUTED |
| PRF1-K5-EV-011 | resilience | RPO/RTO mesurés après fixation des objectifs | TBD-PREPROD |
| PRF1-K5-EV-012 | privacyVerification | export/portabilité selon règles approuvées | TBD-PREPROD |
| PRF1-K5-EV-013 | lifecycle | rétention/effacement y compris sauvegardes | TBD-PREPROD |
| PRF1-K5-EV-014 | securityVerification | clients OIDC, workload identity, secrets et step-up si requis | TBD-PREPROD |

## Calcul K5
automatedValidation : NOT-TESTED
contractTests : NOT-TESTED
securityVerification : NOT-TESTED
restoreOrResilienceTestWhenApplicable : NOT-TESTED
evidenceLinks : PARTIAL
unresolvedCriticalGapsEqualsZero : FAIL

## Règle
Une spécification, un runbook ou un backup annoncé ne constitue pas une preuve. Chaque PASS exige une exécution traçable avec version, environnement, date, résultat, anomalies et reviewer.

## Blocages
L'absence d'implémentation bloque EV-001 à EV-004. L'absence d'environnement représentatif bloque les preuves de restore. Les décisions PREPROD doivent être fermées avant le PASS global.

Verdict : K4-PASS / K5-NOT-YET-PASS.
