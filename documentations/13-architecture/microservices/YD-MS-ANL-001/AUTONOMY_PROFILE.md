# YD-MS-ANL-001 — Analytics

Statut : `C2-BASELINE / ANALYTICS-SEMANTICS-CLOSED`

- Classification : `DERIVED`, criticité C2. État actuel : `REBUILD-UNVERIFIED`.
- Autorité : métriques, agrégats et snapshots analytiques dérivés uniquement; aucune écriture transactionnelle vers les domaines.
- Sources : événements/projections métier autorisés. Avant production, chaque métrique doit référencer ses sources, contrats, versions, méthodologie et fenêtre de rétention.
- Checkpoint/watermark : positions par flux/partition et watermark par dataset analytique. Une métrique ne peut être FRESH si une source obligatoire est en retard inconnu.
- Replay : idempotent, gère doublons, hors ordre, corrections rétroactives, suppressions et changements de classification/privacy.
- Reconstruction : FULL_REBUILD des datasets/métriques reconstructibles; PARTIAL_REBUILD par période/territoire/dataset; CATCH_UP depuis checkpoint.
- Fraîcheur : FRESH/STALE-ACCEPTABLE/EXPIRED/UNKNOWN, seuils propres à chaque famille de métriques et TBD-PREPROD.
- Intégrité : contrôles de volumes, périodes, cardinalités, trous, doublons, méthodologie/version et rapprochement avec sources gouvernées.
- Panne : dernière édition datée si autorisée, sinon recalcul ou indisponibilité contrôlée.
- Sécurité : agrégation/minimisation, finalité d’accès, privacy analytique et provenance des métriques.
- Scaling : batch/stream selon ADR; capacité de rebuild/catch-up séparée du trafic analytique normal.
- IAM : I/M2M. Repo : `brendolys-ydiase-analytics`.
- DR/test : perte contrôlée d’un dataset puis FULL_REBUILD; mesurer durée, fraîcheur, convergence et ressources.
- Gates : catalogue métriques; sources/versions/rétention; watermark; privacy analytique; FULL_REBUILD; `REBUILDABLE`; fraîcheur; RTO/SLO.

## Baseline sémantique fermée
- Normatif : `ANALYTICS_METRIC_POLICY.md`, `ANALYTICS_SOURCE_CONTRACT_REGISTER.md`, `PHASE_CLOSURE.md`.
- Une métrique n'est calculable que si sa MetricDefinition versionnée déclare finalité, grain, dimensions, contrats sources, méthodologie, Privacy et traitement corrections/revocations.
- Aucun flux « tous événements YDIASE » n'est autorisé.
- UNKNOWN ≠ 0 ≠ NOT-APPLICABLE ≠ MISSING.
- Un snapshot historique est restauré, jamais recalculé silencieusement avec une méthodologie courante.
- Les familles sources sont REGISTERED-NOT-ACTIVATED jusqu'à association à une MetricDefinition approuvée.
- État recovery maintenu : `REBUILD-UNVERIFIED`.
