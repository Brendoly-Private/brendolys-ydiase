---
document_id: "YD-DOC-TRU-PRF-001-K4-GOVERNANCE-BASELINE"
title: "YD-MS-PRF-001 — K4 Governance Baseline"
document_type: "governance-baseline"
document_role: "Établit une règle ou baseline normative de gouvernance applicable au périmètre concerné."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "trust"
---

# YD-MS-PRF-001 — K4 Governance Baseline

> **Rôle du document**
> Établit une règle ou baseline normative de gouvernance applicable au périmètre concerné.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : K4-PASS / GOVERNANCE-BASELINE-CLOSED / K5-EVIDENCE-PENDING
Nature : AUTH
Criticité : C1

## Classification
Le profil courant contient des données personnelles SENSITIVE et peut devenir VERY-SENSITIVE selon objectifs, contraintes ou contexte. Toute projection est minimisée par finalité.

## Security
Audience logique ydiase-profile. Scopes self séparés lecture/écriture ; accès support distinct et audité ; workload identity M2M dédiée ; aucun scope universel profile:* ; aucun accès DB croisé ; aucune donnée de profil dans les tokens ; chiffrement au repos et en transit.

Les clients OIDC, step-up, secrets, certificats et contrôles physiques restent PREPROD.

## Privacy et rétention
CNS reste l'autorité des décisions Privacy. Toute opération nécessitant une décision obligatoire non vérifiable est fail-closed. Export complet interdit sans finalité autorisée. Rétention détaillée, portabilité, effacement et règles mineurs/représentation restent à fermer avant production.

## Criticité et continuité
PRF-001 est C1. Backup/restore indépendant obligatoire. PRF-002, projections et caches ne peuvent jamais reconstruire l'autorité PRF-001. RPO/RTO/SLO restent TBD-PREPROD et devront être justifiés puis mesurés.

## Observabilité
La gouvernance exige audit des accès support et sensibles, mutations du profil, changements de préférences/objectifs/contraintes, décisions Privacy appliquées, opérations backup/restore et erreurs de publication/réconciliation. Les métriques physiques restent à définir avec l'architecture.

## Recovery
Stratégie AUTH : sauvegarde autoritative propre, restauration indépendante, intégrité post-restore, puis republication/réconciliation des projections. FULL_REBUILD depuis PRF-002 ou un consommateur est interdit.

## Runbook
Un runbook PRF-001 dédié est requis avant exécution K5. Il doit couvrir perte datastore, corruption logique, suppression accidentelle, incident Privacy, restore, validation d'intégrité et réconciliation aval.

## Ownership
Les responsabilités doivent couvrir owner métier, owner opérationnel, sécurité, Privacy/conformité, backup/restore et suppléance. Les personnes physiques seront nommées avant production.

## Évaluation K4
dataClassification : PASS
securityControls : PASS
privacyAndRetentionWhenApplicable : PASS
sloOrCriticality : PASS
observability : PASS
backupRecoveryWhenStateful : PASS
runbookOrOperationalProcedure : PASS
namedOwners : PASS

Les PASS indiquent que les exigences de gouvernance sont définies et vérifiables ; ils ne constituent aucune preuve d'implémentation.

## K5
Doivent encore être prouvés : invariants, contract tests, self/IDOR, support access, Privacy fail-closed, restore indépendant, intégrité, suppression/restriction post-restore, replay/réconciliation et RPO/RTO lorsque fixés.

Verdict : K4-PASS / K5-NOT-YET-PASS.
