---
document_id: "YD-DOC-EVD-K5-EVIDENCE-MATRIX"
title: "YD-MS-EDU-001 — K5 Evidence Matrix"
document_type: "evidence-record"
document_role: "Documente une preuve, un protocole ou une matrice de vérification de la fondation YDIASE."
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

# YD-MS-EDU-001 — K5 Evidence Matrix

> **Rôle du document**
> Documente une preuve, un protocole ou une matrice de vérification de la fondation YDIASE.
> **Usage développement :** référence de support pour la gouvernance ou la vérification documentaire.

Statut : EVIDENCE-PLAN / EXECUTION-PENDING
Nature : AUTH
Criticité : C2

| Evidence ID | Critère K5 | Preuve attendue | État |
|---|---|---|---|
| EDU1-K5-EV-001 | automatedValidation | invariants Institution/Campus, identifiants, versions et statuts | BLOCKED-BY-IMPLEMENTATION |
| EDU1-K5-EV-002 | contractTests | YD-CTR-EDU-INSTITUTION-v1 et entrées gouvernées CFG/DAT | BLOCKED-BY-IMPLEMENTATION |
| EDU1-K5-EV-003 | securityVerification | droits lecture/mutation/contribution/validation/publication | BLOCKED-BY-IMPLEMENTATION |
| EDU1-K5-EV-004 | governanceVerification | séparation contributeur/validateur et absence d'auto-publication | BLOCKED-BY-IMPLEMENTATION |
| EDU1-K5-EV-005 | governanceVerification | publication bloquée si pays/source/validation obligatoire inconnue | BLOCKED-BY-IMPLEMENTATION |
| EDU1-K5-EV-006 | provenanceVerification | source, provenance, contexte territorial et version conservés | BLOCKED-BY-IMPLEMENTATION |
| EDU1-K5-EV-007 | resilience | restauration complète depuis chaîne EDU-001 | NOT-EXECUTED |
| EDU1-K5-EV-008 | resilience | restore sans EDU-002/Search/KNW/Analytics | NOT-EXECUTED |
| EDU1-K5-EV-009 | integrity | identifiants, versions, statuts et campus intègres après restore | NOT-EXECUTED |
| EDU1-K5-EV-010 | lifecycle | retrait/correction postérieur au point restauré réappliqué | NOT-EXECUTED |
| EDU1-K5-EV-011 | resilience | republication/réconciliation idempotente | NOT-EXECUTED |
| EDU1-K5-EV-012 | operationalVerification | runbook exécuté sans connaissance tacite bloquante | NOT-EXECUTED |
| EDU1-K5-EV-013 | resilience | RPO/RTO mesurés après fixation des objectifs | TBD-PREPROD |
| EDU1-K5-EV-014 | lifecycle | rétention/versioning historique conforme aux règles approuvées | TBD-PREPROD |
| EDU1-K5-EV-015 | multiCountryVerification | règles pays contextualisées sans hypothèse nationale globale | TBD-PREPROD |
| EDU1-K5-EV-016 | securityVerification | clients IAM, workload identities, secrets et politiques réseau | TBD-PREPROD |

## Calcul K5
automatedValidation : NOT-TESTED
contractTests : NOT-TESTED
securityVerification : NOT-TESTED
restoreOrResilienceTestWhenApplicable : NOT-TESTED
evidenceLinks : PARTIAL
unresolvedCriticalGapsEqualsZero : FAIL

## Règle de preuve
Une baseline, un workflow décrit, un backup SUCCESS ou un runbook non exécuté ne vaut pas preuve K5. Chaque PASS exige une exécution traçable : version, environnement, date, résultat, anomalies et reviewer.

## Points bloquants
Les règles de publication et de provenance doivent être exécutées, pas seulement décrites. Le restore doit démontrer que l'autorité EDU-001 est récupérable sans consommateur aval et que les retraits/corrections postérieurs au point restauré sont réappliqués avant retour normal.

Verdict : K4-PASS / K5-NOT-YET-PASS.
