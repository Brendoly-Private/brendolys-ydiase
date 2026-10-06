# YD-MS-LRN-001 — K4 Governance Baseline

Statut : `K4-PASS / GOVERNANCE-BASELINE-CLOSED / K5-EVIDENCE-PENDING`
Nature : `MIXED`
Criticité : `C2`

## Classification

LRN possède des LearningResource et résultats spécialisés, tout en référant des autorités EDU/SKL/MKT.

- `PUBLIC` : ressources explicitement publiables et métadonnées publiques autorisées.
- `INTERNAL` : mappings, policies et métadonnées de fonctionnement non publiées.
- `CONFIDENTIAL` : droits d'usage, provenance restreinte, évaluations qualité et informations fournisseur non publiques.
- `SENSITIVE` / `VERY-SENSITIVE` : RecommendationSet personnalisés, gaps/profils minimisés et evidence snapshots lorsqu'ils permettent d'inférer une situation individuelle.

La classification source prévaut lorsqu'elle est plus restrictive.

## Sécurité

Authentification service-à-service pour mutations/intégrations, autorisation par objet/finalité, contrôle horizontal des résultats personnalisés, séparation lecture/proposition/revue/publication, secrets hors payload et audit des changements.

LRN ne peut pas modifier l'autorité EDU, SKL ou MKT. Les droits d'usage d'une ressource doivent être vérifiables avant exposition/usage. Une donnée commerciale ne peut influencer le rang organique learning.

IAM/IDOR physiques restent à vérifier à K5/PREPROD.

## Privacy et rétention

La personnalisation utilise uniquement les données nécessaires à une finalité autorisée. Les evidence snapshots privilégient références/version IDs et valeurs dérivées minimales. Les règles mineurs/territoires sont appliquées via les autorités/policies concernées.

Une correction n'efface pas silencieusement un ancien résultat : il devient stale/invalidated lorsque nécessaire.

Les durées numériques de conservation des résultats, evidence snapshots, logs, mappings et ressources retirées restent `TBD-PREPROD`, à fixer selon classification, droits d'usage, pays, finalité, audit et obligations de suppression.

## Criticité et SLO

Criticité `C2`.

En panne, les ressources propres encore valides peuvent rester lisibles selon leur fraîcheur. Une offre commerciale non vérifiable est masquée. LRN ne fabrique jamais coût, durée, bourse, place ou disponibilité.

À mesurer avant ACTIVE : disponibilité, latence, fraîcheur EDU/MKT, taux d'abstention/UNKNOWN, propagation des retraits, RPO/RTO, succès restore et qualité des mappings. Valeurs numériques : `TBD-PREPROD`.

## Observabilité

Logs : mutations de ressources/mappings, versions, provenance, droits d'usage, décisions de publication/retrait, personnalisation, erreurs de source et opérations restore.

Métriques : ressources par état, mappings invalides/inconnus, âge des projections EDU/MKT, droits expirants, RecommendationSet/abstentions, erreurs de référence, latence, invalidations et état backup/restore.

Alertes : droit d'usage invalide, source critique stale, offre affichée sans fraîcheur vérifiable, mapping/provenance incohérent, influence commerciale détectée, accès indu et échec restore.

## Backup et recovery

LRN est `MIXED` : ses LearningResource/mappings applicables et résultats persistants sont protégés, mais les autorités EDU/SKL/MKT restent chez leurs owners et ne sont pas recréées par LRN.

Le restore doit préserver versions, provenance, droits d'usage et références externes, puis réconcilier les projections devenues stale. RPO/RTO, cadence, technologie et rétention backup restent `TBD-PREPROD`.

## Procédure

Runbook canonique : `07-operations/runbooks/YD-MS-LRN-001/RUNBOOK.md`.

Politique normative : `03-systems/policies/YD-MS-LRN-001/LEARNING_DISCOVERY_POLICY.md`.

## Ownership

Rôles gouvernés : Learning/Product Owner, Technical Owner, Content/Data Governance Owner, Security/Privacy Reviewer et owners EDU/SKL/MKT pour leurs données respectives. Les identités nominatives restent dans le registre organisationnel.

## TBD-PREPROD

Taxonomie réelle des ressources, règles/seuils de mapping, droits d'usage opérationnels, seuils freshness EDU/MKT, fairness si personnalisation, règles mineurs, IAM/IDOR, rétention, RPO/RTO/SLO, capacité, cadence restore et seuils d'alerting.

## Évaluation du gate K4

| Critère K4 | État | Preuve principale |
|---|---|---|
| dataClassification | PASS | Classification |
| securityControls | PASS | Sécurité |
| privacyAndRetentionWhenApplicable | PASS | Privacy/rétention ; valeurs numériques gouvernées en PREPROD |
| sloOrCriticality | PASS | C2 + méthode de fermeture des seuils |
| observability | PASS | logs, métriques, alertes |
| backupRecoveryWhenStateful | PASS | Backup/recovery |
| runbookOrOperationalProcedure | PASS | runbook canonique |
| namedOwners | PASS | rôles gouvernés |

### Verdict

`YD-MS-LRN-001` satisfait le gate documentaire **K4 — Gouverné**.

Ce verdict ne signifie ni mappings réels validés, ni droits d'usage opérationnels prouvés, ni fairness exécutée, ni restore testé, ni PREPROD/production. Ces preuves appartiennent à K5 et aux gates d'activation.

## Gate K5

K5 exigera notamment validations automatisées, contract tests, IAM/IDOR vérifié, tests des droits d'usage et freshness, validation des mappings, fairness lorsque personnalisation, backup/restore, propagation des retraits, preuves observables et zéro gap critique.
