# YD-MS-REC-001 — Runbook

Statut : `OPERATIONAL-PROCEDURE-BASELINE / IMPLEMENTATION-PENDING`

## Triage

Identifier run, policy/model versions, evidence snapshot, purpose/privacy decision, sources et versions, fraîcheur, état d'abstention, contexte pays et consommateurs impactés.

## Incidents

### Ranking incohérent ou non reproductible
Geler la policy/version concernée si nécessaire, conserver le run et ses preuves, reproduire avec les mêmes versions, comparer sources/composantes/tie-breaks et ne jamais réécrire silencieusement l'historique.

### Influence commerciale suspectée
Suspendre la version concernée, exécuter la suite `SPONSORED_NON_INFLUENCE_TEST_POLICY.md`, isoler tout chemin SPN→ranking organique et revenir à une policy approuvée si l'invariant est violé.

### Privacy/finalité non vérifiable
Fail-closed pour la personnalisation ou utiliser uniquement un mode non personnalisé explicitement autorisé. Conserver la décision et l'incident sans exposer davantage de données personnelles.

### Source critique stale, conflictuelle ou indisponible
Appliquer abstention/dégradation définie par policy. Ne jamais fabriquer un ranking. Un ancien run n'est utilisable qu'avec son état de fraîcheur explicite.

### Dérive ou disparité injustifiée
Suspendre le déploiement/activation de la policy concernée, exécuter l'évaluation fairness, documenter la population et les versions puis rollback si les critères approuvés échouent.

### Service REC indisponible
Ne pas promouvoir une projection ou un cache comme autorité. Les consommateurs utilisent leur mode dégradé documenté ; les runs non calculables restent indisponibles/abstention.

## Backup / Restore

Protéger runs persistants, evidence snapshots minimisés, versions de policy/configuration et métadonnées nécessaires à l'audit. Restaurer puis vérifier intégrité, liens de versions et reproductibilité d'un échantillon gouverné avant reprise.

RPO/RTO, technologie, cadence et rétention restent `TBD-PREPROD`.

## Escalade

Technical Owner pilote l'incident. Recommendation/Product Owner arbitre policy et comportement métier. Data/Model Governance intervient sur qualité, dérive et reproductibilité. Security/Privacy Reviewer intervient sur finalité, accès et données protégées. Les identités nominatives restent dans le registre organisationnel.
