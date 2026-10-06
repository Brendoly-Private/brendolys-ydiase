# YD-MS-REC-001 — K4 Governance Baseline

Statut : `K4-PASS / GOVERNANCE-BASELINE-CLOSED / K5-EVIDENCE-PENDING`
Nature : `MIXED`
Criticité : `C1`

## Classification

REC traite des résultats et snapshots pouvant refléter des données personnelles sensibles.

- `INTERNAL` : policy/configuration non sensible et métadonnées techniques.
- `CONFIDENTIAL` : paramètres internes, évaluations et éléments de gouvernance.
- `SENSITIVE` / `VERY-SENSITIVE` : runs personnalisés, contraintes, evidence snapshots, explications et données permettant d'inférer un profil.
- les classifications des sources restent applicables ; REC ne les abaisse pas.

L'evidence snapshot privilégie références/version IDs et valeurs dérivées minimales plutôt que copies de dossiers sources.

## Sécurité

Authentification service-à-service, autorisation par finalité/objet, contrôle horizontal des runs, séparation des droits policy/review/activation, secrets hors payload, audit des changements et fail-closed lorsque Privacy requise n'est pas vérifiable.

SPN-001 ne possède aucun droit permettant de modifier score/rang/pondération/exclusion/explication organique. Une IA/LLM peut participer au calcul ou reformuler une explication selon policy, jamais inventer une justification ni contourner les contraintes HARD.

IAM/IDOR physiques restent à vérifier à K5/PREPROD.

## Privacy et rétention

Toute personnalisation est liée à une finalité déterminable et à une décision Privacy applicable. Minimisation, correction, retrait et territorialité sont conservés. Un ancien run n'est pas réécrit : il peut être invalidé/stale puis remplacé par un nouveau run.

Les durées numériques de conservation des runs, evidence snapshots, traces et données d'évaluation restent `TBD-PREPROD`, à fixer par finalité, classification, pays, audit/reproductibilité et exigences de suppression avant ACTIVE.

## Criticité et SLO

Criticité `C1`. REC peut influencer des décisions importantes et doit préférer abstention à un résultat non fiable.

À mesurer avant ACTIVE : disponibilité, latence par type de recommandation, fraîcheur des entrées, taux d'abstention, erreurs, RPO/RTO, reproductibilité, propagation des invalidations et performance des modes dégradés. Seuils numériques : `TBD-PREPROD`.

## Observabilité

Logs : run/policy/model versions, décision d'abstention, erreurs de source, contrôles Privacy, activation/rollback de policy et accès gouvernés.

Métriques : taux de runs/abstention/erreurs, fraîcheur/qualité, distributions de score/rang, couverture, dérive, indicateurs fairness approuvés, latence, invalidations et échecs de reproductibilité.

Alertes : influence commerciale détectée, Privacy non vérifiable, hausse anormale d'abstention, dérive, disparité au-delà des critères approuvés, source critique stale, version non approuvée et échec restore/reproductibilité.

## Backup et recovery

REC possède ses runs/résultats mais pas ses sources. Les données autoritatives d'entrée restent chez leurs owners. Backup/restore couvre les états REC persistants, snapshots minimisés, policies/configurations et preuves nécessaires à l'audit.

Après restore : intégrité des versions, références sources, décisions Privacy et reproductibilité doivent être vérifiées avant reprise. RPO/RTO et cadence de test restent `TBD-PREPROD`.

## Procédure

Runbook canonique : `07-operations/runbooks/YD-MS-REC-001/RUNBOOK.md`.

Politiques de contrôle :
- `RECOMMENDATION_RANKING_POLICY.md`
- `FAIRNESS_EVALUATION_POLICY.md`
- `SPONSORED_NON_INFLUENCE_TEST_POLICY.md`

## Ownership

Rôles : Recommendation/Product Owner, Technical Owner, Data/Model Governance Owner, Security/Privacy Reviewer et owners des sources. Les identités nominatives restent dans le registre organisationnel.

## TBD-PREPROD

Coefficients/seuils approuvés, critères numériques fairness, datasets représentatifs, règles mineurs, rétention, IAM/IDOR physiques, RPO/RTO/SLO, capacité/latence, cadence restore, seuils dérive/alerting et critères d'activation/rollback.

## Évaluation du gate K4

| Critère K4 | État | Preuve principale |
|---|---|---|
| dataClassification | PASS | Classification |
| securityControls | PASS | Sécurité + séparation SPN |
| privacyAndRetentionWhenApplicable | PASS | Privacy/rétention ; valeurs numériques gouvernées en PREPROD |
| sloOrCriticality | PASS | C1 + méthode de fermeture des seuils |
| observability | PASS | logs, métriques, alertes |
| backupRecoveryWhenStateful | PASS | Backup/recovery |
| runbookOrOperationalProcedure | PASS | runbook canonique |
| namedOwners | PASS | rôles gouvernés |

### Verdict

`YD-MS-REC-001` satisfait le gate documentaire **K4 — Gouverné**.

Ce verdict ne signifie ni fairness validée sur données représentatives, ni suite anti-influence exécutée, ni restore testé, ni PREPROD/production. Ces preuves appartiennent à K5 et aux gates d'activation.

## Gate K5

K5 exige notamment validations automatisées, contract tests, IAM/IDOR vérifié, suite anti-influence SPN exécutée, fairness évaluée sur données représentatives, tests de dérive/reproductibilité, backup/restore, preuves observables et zéro gap critique.
