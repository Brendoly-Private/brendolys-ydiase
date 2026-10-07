---
document_id: "YD-DOC-OPS-PRF-002-PRF002-DR-EVIDENCE-MATRIX"
title: "PRF002_DR_EVIDENCE_MATRIX — Matrice de preuves DR"
document_type: "operations-reference"
document_role: "Documente une référence opérationnelle de résilience, reprise, preuve ou qualification."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "operations"
---

# PRF002_DR_EVIDENCE_MATRIX — Matrice de preuves DR

> **Rôle du document**
> Documente une référence opérationnelle de résilience, reprise, preuve ou qualification.
> **Usage développement :** référence de support pour la conception et la préparation opérationnelle.

Statut : `READY-FOR-PREPROD-EVIDENCE`
Service : `YD-MS-PRF-002 — Education & Experience Profile`
Criticité : `C1`
Référence principale : `PRF002_DR_TEST_PLAN.md`

## 1. Objet

Cette matrice définit, pour chaque exercice DR, les preuves minimales nécessaires pour produire un résultat auditable. Un test sans preuve suffisante reste `PENDING`, même si l'opérateur affirme qu'il a réussi.

## 2. Règles de preuve

Toute preuve doit être :
- liée à un Test ID et à une exécution précise ;
- horodatée avec une source de temps cohérente ;
- attribuable à une identité nominative ou workload identity ;
- reliée à la version PRF-002, au runbook et à l'environnement ;
- protégée contre les modifications non tracées ;
- conservée dans l'emplacement gouverné prévu ;
- référencée ici sans exposer de secret.

Les secrets, tokens, clés privées, dumps sensibles et données personnelles brutes ne sont jamais copiés dans ce registre.

## 3. Matrice

| Test | Preuves minimales | Mesures | Validations | Gate |
|---|---|---|---|---|
| DR-001 | alerte, timeline, logs instance, health/readiness | RPO attendu 0 ; RTO ≤1h | OPS + observateur | REC |
| DR-002 | état cluster, failover logs, cohérence autorité | RPO attendu 0 ; RTO ≤1h | OPS/DR | REC |
| DR-003 | incident injecté, backup source, restore logs, intégrité agrégats | RPO ≤15m ; RTO ≤4h | DR + OPS + BUS | BLOCKING |
| DR-004 | point de corruption, point sain, PITR logs, intégrité | RTO cible ≤4h après point sain identifié | DR + BUS | BLOCKING |
| DR-005 | objets supprimés, état avant/après, contrôle des mutations non concernées | perte résiduelle = 0 sur périmètre attendu | DR + BUS | REC |
| DR-006 | version fautive, rollback logs, migrations, readiness | RPO attendu 0 ; RTO ≤1h | OPS + ARCH | REC |
| DR-007 | perte périmètre, activation DR, copie utilisée, réseau, intégrité | RPO ≤15m ; RTO ≤8h | DR + OPS + BUS + SEC + INFRA | BLOCKING |
| DR-008 | preuve backup invalide, génération de fallback, restore | RPO réel + RTO cible ≤8h | DR + BKP + OPS | BLOCKING |
| DR-009 | règles de blocage PRF-001/EDU/SKL, network logs, restore, intégrité | RPO/RTO du scénario applicable | DR + BUS + OPS + ARCH | REC-BLOCKING |
| DR-010 | décision Privacy post-restore-point, état restauré, réapplication | délai de réapplication | PRIV + BUS | BLOCKING |
| DR-011 | watermark projection, divergence, resync, état final | lag avant/après | ARCH + CONTRACT | REC |
| DR-012 | IDs événements/commandes, replay logs, contrôles doublons | doublon métier = 0 | CONTRACT + BUS | BLOCKING |
| DR-013 | identité utilisée, permissions, audit trail | accès hors périmètre = 0 | SEC + DR | BLOCKING |
| DR-014 | procédure de récupération de clés, accès déchiffrement, audit | restauration sans contournement | SEC + DR | REC |
| DR-015 | preuve d'indisponibilité primaire, accès copie isolée, blast-radius check | disponibilité de la copie | INFRA + SEC + DR | BLOCKING |
| DR-016 | opérateur indépendant, version runbook, écarts/questions | blocage par connaissance tacite = 0 | OPS/DR + observateur | BLOCKING |
| DR-017 | schéma source/cible, migrations, contrôles compatibilité | erreurs bloquantes = 0 | ARCH + DR | REC |
| DR-018 | alerte sécurité, QUARANTINE, confinement, point sain, décision | timeline qualification/confinement | SEC + DR + OPS | REC |
| DR-019 | erreur propagée, point sain, PITR/correction, intégrité | perte réelle documentée | DR + BUS | REC |
| DR-020 | checklist promotion, signatures, readiness, Privacy/Security si applicable | temps jusqu'à NORMAL-RESTORED | DR + BUS + OPS + conditionnels | BLOCKING |

## 4. Preuve d'intégrité commune

Pour DR-003, 004, 007, 008, 009, 019 et tout restore complet, conserver une preuve de contrôle de :
- EducationRecord ;
- ExperienceRecord ;
- AchievementClaim ;
- ProfileEvidenceLink ;
- identifiants durables ;
- versions temporelles ;
- états de vérification ;
- références de provenance ;
- contraintes d'unicité et relations ;
- absence de duplication métier inattendue.

## 5. Dossier de preuve par exécution

Convention recommandée :

`PRF002/DR/<TEST-ID>/<YYYY-MM-DD>/<EXECUTION-ID>/`

Contenu logique :
- `manifest.md` ou équivalent ;
- timeline ;
- paramètres non secrets ;
- logs pertinents ;
- mesures RPO/RTO ;
- rapport d'intégrité ;
- anomalies ;
- décisions ;
- approbations ;
- actions correctives.

Le stockage physique définitif reste `TBD-IMPLEMENTATION` jusqu'à décision d'architecture documentaire/sécurité.

## 6. Manifest minimal

| Champ | Valeur |
|---|---|
| Execution ID | À RENSEIGNER |
| Test ID | DR-XXX |
| Date | À RENSEIGNER |
| Environnement | À RENSEIGNER |
| Version service | À RENSEIGNER |
| Version runbook | À RENSEIGNER |
| Exécutant | À RENSEIGNER |
| Observateur | À RENSEIGNER |
| Incident start | À RENSEIGNER |
| Recovery start | À RENSEIGNER |
| Service usable | À RENSEIGNER |
| Last confirmed mutation | À RENSEIGNER |
| Last recovered mutation | À RENSEIGNER |
| RPO | À CALCULER |
| RTO | À CALCULER |
| Integrity result | À RENSEIGNER |
| Evidence location | À RENSEIGNER |
| Result | PENDING/PASS/PASS-WITH-NONBLOCKING-FINDINGS/FAIL |
| Approvals | À RENSEIGNER |

## 7. Critères de recevabilité

Une preuve est rejetée si :
- son origine ne peut pas être attribuée ;
- les timestamps nécessaires au calcul RPO/RTO manquent ;
- les logs sont tronqués au point d'empêcher la conclusion ;
- le scénario exécuté diffère matériellement du scénario déclaré sans justification ;
- un secret est exposé dans le dossier ;
- une approbation obligatoire est absente ;
- l'architecture testée n'est plus représentative ;
- DR-009 ne démontre pas effectivement l'indisponibilité simultanée de PRF-001, EDU et SKL.

## 8. Registre d'exécution

| Execution ID | Test | Date | Résultat | RPO | RTO | Evidence ref | Findings | Approbations |
|---|---|---|---|---|---|---|---|---|
| À RENSEIGNER | DR-XXX | AAAA-MM-JJ | PENDING | — | — | À RENSEIGNER | — | — |

Une ligne distincte est créée pour chaque exécution/retest.

## 9. Fermeture

Le gate REC ne peut utiliser que des preuves `ACCEPTED`. Les preuves `REJECTED`, expirées ou non représentatives doivent être rejouées.

Statut actuel : `EVIDENCE-MATRIX-READY — NO PREPROD EVIDENCE YET`.
