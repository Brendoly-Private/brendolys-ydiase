# YD-MS-EDU-001 — K4 Governance Baseline

Statut : K4-PASS / GOVERNANCE-BASELINE-CLOSED / K5-EVIDENCE-PENDING
Nature : AUTH
Criticité : C2

## Classification
Les données institutionnelles publiées peuvent être PUBLIC/INTERNAL. Contributions, provenance, décisions de validation et éléments de gouvernance sont classifiés selon leur contenu et ne sont pas exposés par défaut.

## Security
Lecture publique/client uniquement via les surfaces gouvernées. Mutations réservées aux identités et workloads autorisés. Aucun accès DB croisé. Contribution et validation sont des capacités distinctes. Toute mutation sensible est attribuable et auditée.

IAM physique, clients, scopes détaillés, secrets et certificats restent PREPROD.

## Gouvernance de publication
Une contribution n'est jamais une publication automatique. La publication est bloquée lorsqu'une référence pays, une source ou une validation obligatoire manque ou n'est pas vérifiable. Le statut publié et sa version sont explicites. Un retrait ou changement de statut doit être propagé aux consommateurs sans transfert d'autorité.

## Provenance et multi-pays
Toute donnée nécessitant une source gouvernée conserve provenance et version. Les règles dépendantes d'un territoire référencent CFG ; aucune hypothèse nationale n'est transformée en règle globale.

## Criticité
EDU-001 est C2. Les cibles RPO/RTO/SLO seront fixées à partir de l'impact métier réel avant production.

## Observabilité
Doivent être observables : mutations, validations/rejets, publications/retraits, erreurs de référence pays, anomalies de provenance, erreurs de projection, échecs de backup/restore et dérives de version. Les métriques physiques restent à définir avec l'implémentation.

## Backup et recovery
Chaîne AUTH indépendante, chiffrée et restaurable. La restauration ne dépend ni d'EDU-002 ni de Search, KNW, Analytics ou d'une projection. Après restore, les références externes peuvent être réconciliées sans changer l'ownership.

## Runbook
Un runbook EDU-001 dédié couvre perte datastore, corruption, publication erronée, incident de provenance/validation, restore, contrôle d'intégrité et réconciliation aval.

## Ownership
Les rôles gouvernés couvrent owner métier, owner opérationnel, contributeur, validateur, sécurité et recovery. Les personnes physiques et suppléances sont nommées avant production.

## Évaluation K4
dataClassification : PASS
securityControls : PASS
privacyAndRetentionWhenApplicable : PASS
sloOrCriticality : PASS
observability : PASS
backupRecoveryWhenStateful : PASS
runbookOrOperationalProcedure : PASS
namedOwners : PASS

Les PASS signifient que les contrôles sont définis et vérifiables ; ils ne prouvent aucune exécution.

Verdict : K4-PASS / K5-NOT-YET-PASS.
