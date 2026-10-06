# YD-MS-KNW-001 — K4 Governance Baseline

Statut : K4-GOVERNANCE-BASELINE / PREPROD-VALIDATION-PENDING
Nature : DERIVED
Criticité : C2

## Classification
KNW est un graphe partagé dérivé. La règle par défaut est l'absence de PII.
- PUBLIC : faits déjà publiables par leur autorité source.
- INTERNAL : topologie, versions, watermarks et métadonnées internes.
- SENSITIVE : provenance non publique, qualité, confiance et règles de résolution.
- RESTRICTED-PII : données personnelles identifiantes, interdites dans le graphe partagé par défaut.
La classification source prévaut lorsqu'elle est plus restrictive.

## Sécurité
Authentification service-à-service, autorisation selon identité/finalité/classe, validation schéma-version-provenance avant ingestion, secrets hors payload, journalisation des mutations/rebuilds/quarantaines, isolation des données restreintes et mêmes règles pour GraphRAG. Les mécanismes physiques restent à sélectionner à l'implémentation.

## Privacy et rétention
Minimisation et purpose limitation. DELETE, WITHDRAW et REVOKE source invalident les projections dépendantes. Une donnée non publiable ne reste pas découvrable. Les durées numériques de rétention restent TBD-PREPROD et doivent être fixées avant activation selon classe, source et pays.

## Criticité et SLO
Criticité C2. KNW n'est jamais fallback autoritatif. Mesurer fraîcheur par source/watermark, échecs d'ingestion, backlog, provenance, convergence de rebuild et disponibilité des lectures. Seuils numériques disponibilité, freshness et RTO : TBD-PREPROD, à mesurer puis approuver avant ACTIVE.

## Observabilité
Logs : ingestion, validation, rejet, projection, retrait, entity resolution, rebuild et changements de version.
Métriques : événements acceptés/rejetés, lag, backlog, volumes par classe, provenance invalide, âge des projections, durée/convergence rebuild, erreurs de résolution et contrat KNW vers Search.
Alertes : provenance manquante, source bloquée, backlog croissant, divergence, retrait non propagé, schéma incompatible, freshness dépassée.

## Backup et recovery
L'état est DERIVED. Reprise primaire par reconstruction depuis sources autoritatives, snapshots/replay et règles versionnées. Modes FULL_REBUILD, PARTIAL_REBUILD et CATCH_UP. Protéger les règles, configurations, checkpoints et métadonnées non reconstructibles. Un backup du graphe ne devient jamais autorité métier.

## Procédure
Le runbook associé couvre incompatibilité de source, provenance manquante, retrait non propagé, divergence, indisponibilité et erreur d'entity resolution.

## Ownership
Rôles : Business/Knowledge Owner, Technical Owner, Data Governance Owner, Security/Privacy Reviewer et owners des domaines sources. Les noms sont gérés dans le registre organisationnel plutôt que figés ici.

## TBD-PREPROD
Freshness par source, disponibilité cible, RTO/RPO, rétention, capacité/backlog, seuils confidence, mécanismes IAM et délais d'escalade. Leur méthode, owner et gate sont définis; les preuves seront exigées à K5/ACTIVE.

## Gate K5
Validation automatisée, tests de contrats, vérification sécurité, FULL_REBUILD/convergence, DELETE/REVOKE/out-of-order/entity-resolution, preuves observables et zéro gap critique.
