---
document_id: "YD-DOC-EVD-PRF-002-K5-EVIDENCE-MATRIX"
title: "YD-MS-PRF-002 — K5 Evidence Matrix"
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

# YD-MS-PRF-002 — K5 Evidence Matrix

> **Rôle du document**
> Documente une preuve, un modèle ou une matrice de vérification K5 du microservice concerné.
> **Usage développement :** référence de support pour la vérification, la qualification et les décisions de readiness.

Statut : EVIDENCE-PLAN / EXECUTION-PENDING
Nature : AUTH
Criticité : C1

Cette matrice relie le gate K5 aux plans DR et Privacy existants. Elle ne remplace pas PRF002_DR_TEST_PLAN ni PRF002_DR_EVIDENCE_MATRIX.

| Evidence ID | Critère K5 | Preuve attendue | Source d'exécution | État |
|---|---|---|---|---|
| PRF2-K5-EV-001 | automatedValidation | invariants agrégats, versions, temporalité, provenance | CI/tests PRF-002 | BLOCKED-BY-IMPLEMENTATION |
| PRF2-K5-EV-002 | contractTests | YD-CTR-PRF-HISTORY-v1 + entrées gouvernées | contract tests | BLOCKED-BY-IMPLEMENTATION |
| PRF2-K5-EV-003 | securityVerification | self-access, IDOR, scopes et séparation déclaration/vérification | security suite | BLOCKED-BY-IMPLEMENTATION |
| PRF2-K5-EV-004 | securityVerification | identités backup/restore et séparation des pouvoirs | DR-013 | NOT-EXECUTED |
| PRF2-K5-EV-005 | resilience | perte complète datastore, RPO/RTO et intégrité | DR-003 | NOT-EXECUTED |
| PRF2-K5-EV-006 | resilience | PITR après corruption logique | DR-004 | NOT-EXECUTED |
| PRF2-K5-EV-007 | resilience | sinistre majeur depuis copie de reprise | DR-007 | NOT-EXECUTED |
| PRF2-K5-EV-008 | resilience | backup récent inutilisable, fallback génération saine | DR-008 | NOT-EXECUTED |
| PRF2-K5-EV-009 | resilience | restore avec PRF-001 + EDU + SKL indisponibles | DR-009 | NOT-EXECUTED |
| PRF2-K5-EV-010 | privacyVerification | réapplication décision Privacy post-restore | DR-010 | NOT-EXECUTED |
| PRF2-K5-EV-011 | resilience | replay/republication idempotent | DR-012 | NOT-EXECUTED |
| PRF2-K5-EV-012 | securityVerification | récupération clés sans contournement | DR-014 | NOT-EXECUTED |
| PRF2-K5-EV-013 | resilience | copie isolée disponible hors blast radius | DR-015 | NOT-EXECUTED |
| PRF2-K5-EV-014 | operationalVerification | runbook exécuté sans connaissance tacite bloquante | DR-016 | NOT-EXECUTED |
| PRF2-K5-EV-015 | privacyVerification | donnée supprimée/restreinte non durablement réactivée | DR-010 + contrôle ciblé | NOT-EXECUTED |
| PRF2-K5-EV-016 | operationalVerification | promotion NORMAL-RESTORED gouvernée | DR-020 | NOT-EXECUTED |
| PRF2-K5-EV-017 | privacyVerification | portabilité/export selon règles approuvées | test Privacy | TBD-PREPROD |
| PRF2-K5-EV-018 | privacyVerification | rétention/destruction backups conforme | test lifecycle backup | TBD-PREPROD |

## Critères K5 calculés

automatedValidation : NOT-TESTED
contractTests : NOT-TESTED
securityVerification : NOT-TESTED
restoreOrResilienceTestWhenApplicable : NOT-TESTED
evidenceLinks : PARTIAL — protocoles et emplacements de preuve définis, aucune exécution acceptée
unresolvedCriticalGapsEqualsZero : FAIL

## Règle de preuve

Une ligne ne passe à PASS que si l'exécution possède une Evidence ref recevable dans PRF002_DR_EVIDENCE_MATRIX ou dans le registre de preuve correspondant. Un test annoncé oralement ou un job de backup SUCCESS sans restauration ne compte pas.

## Focus suppression/restauration

PRF2-K5-EV-010 et PRF2-K5-EV-015 sont bloquants. Le scénario doit créer une décision d'effacement/restriction postérieure au point restauré, restaurer un état antérieur, réappliquer la décision puis démontrer que la donnée interdite n'est pas durablement réactivée avant NORMAL.

Verdict : K4-PASS / K5-NOT-YET-PASS.
