# YD-MS-PRF-002 — K4 Governance Baseline

Statut : K4-PASS / GOVERNANCE-BASELINE-CLOSED / K5-EVIDENCE-PENDING
Nature : AUTH
Criticité : C1

Cette baseline évalue les règles PRF-002 existantes sans les dupliquer.

## Classification
Historique personnel, preuves, vérifications et provenance sont SENSITIVE ou VERY-SENSITIVE selon contenu et contexte. Les projections sont minimisées.

## Sécurité
Audience logique ydiase-profile-history, contrôle self par sujet, séparation déclaration/vérification, workload identity dédiée, opérations backup/restore séparées, chiffrement, audit et absence d'accès DB croisé. Les contrôles physiques restent à vérifier.

## Privacy
CNS reste autorité Privacy. Fail-closed lorsque la décision requise n'est pas vérifiable. Après restore, les décisions applicables sont réappliquées avant retour normal. Portabilité, effacement, mineurs et rétention détaillée restent PREPROD.

## Criticité
C1. Objectifs existants : RPO nominal ≤15 min ; RTO incident courant ≤1 h ; perte complète ≤4 h ; sinistre majeur ≤8 h. Ils restent à confirmer par BIA et mesure.

## Observabilité
Audit des accès/mutations, vérifications, backup/restore, transitions de continuité et réapplication Privacy. Métriques de backup, intégrité, restore et RPO/RTO mesurés.

## Recovery
MANDATORY-AUTH-BACKUP. Restore indépendant avec PRF-001, EDU et SKL indisponibles. FULL_REBUILD depuis services amont interdit. PITR, copie isolée, intégrité et réconciliation aval sont requis par les politiques existantes.

## Procédures
Sources existantes : PRF002_CONTINUITY_POLICY, PRF002_BACKUP_RESTORE_POLICY, PRF002_DR_RUNBOOK, PRF002_BIA, PRF002_DR_EVIDENCE_MATRIX et documents de qualification des rôles.

## Ownership
Owner métier, owner opérationnel, backup, restore/DR, sécurité, Privacy/conformité et suppléants doivent être attribués avant production.

## Évaluation K4
dataClassification PASS
securityControls PASS
privacyAndRetentionWhenApplicable PASS
sloOrCriticality PASS
observability PASS
backupRecoveryWhenStateful PASS
runbookOrOperationalProcedure PASS
namedOwners PASS

Les PASS signifient que la gouvernance est définie et testable, pas qu'elle est implémentée.

## K5
Restore indépendant, PITR, intégrité, mesure RPO/RTO, replay idempotent, IAM/self/IDOR, séparation déclaration-vérification, Privacy post-restore, suppression/restriction, portabilité et contrôles backup/keys restent à prouver.

Verdict : K4-PASS / K5-NOT-YET-PASS.
