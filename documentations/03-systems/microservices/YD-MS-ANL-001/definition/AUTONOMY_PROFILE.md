---
document_id: "YD-DOC-MS-ANL-001-AUT"
title: "YD-MS-ANL-001 — Analytics"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie Analytics, son caractère DERIVED, ses règles de reconstruction et sa baseline sémantique."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "microservice"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
---

# YD-MS-ANL-001 — Analytics

> **Rôle du document**
> Définit l’autonomie Analytics, son caractère DERIVED, ses règles de reconstruction et sa baseline sémantique.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de la frontière concernée.

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
