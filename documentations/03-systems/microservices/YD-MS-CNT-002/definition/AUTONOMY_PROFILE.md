---
document_id: "YD-DOC-AUTO-22C09297C1D3532A"
title: "AUTONOMY PROFILE"
document_type: "documentation-reference"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-CNT-002 — Feed

Statut : `autonomy-profile-draft`

- Classification : `DERIVED`, criticité C3. État actuel : `REBUILD-UNVERIFIED`.
- Autorité : aucune vérité métier; feed, ranking et caches sont dérivés. SPN reste une entrée sponsorisée séparée du score organique.
- Sources : CNT, COM et décisions MOD; SPN uniquement comme placement explicitement étiqueté. Contrats/versions et rétention à inscrire au Contract Registry.
- Checkpoint/watermark : position distincte par flux/partition; le feed ne peut pas déclarer FRESH si CNT/COM/MOD requis n’ont pas convergé.
- Replay : idempotent, supporte doublons, hors ordre, suppressions de contenu, retraits/modération et corrections. Les décisions de retrait priment sur un ancien ranking.
- Reconstruction : FULL_REBUILD des projections/rankings; PARTIAL_REBUILD par partition/surface/cohorte autorisée; CATCH_UP depuis checkpoints.
- Fraîcheur : `FRESH`, `STALE-ACCEPTABLE`, `EXPIRED`, `UNKNOWN`; seuils TBD-PREPROD. Un feed stale peut basculer vers une surface simplifiée seulement dans la limite documentée.
- Intégrité : absence d’objets supprimés/modérés, pas de doublons, séparation sponsorisé/organique, cohérence des versions de contenu.
- Panne : feed chronologique/simplifié ou indisponibilité contrôlée; aucune dépendance au Feed pour valider un fait métier.
- Sécurité : minimisation du profilage, aucune copie durable inutile de PII, suppressions/modération prioritaires.
- Scaling : lecture élevée, caches/partitions reconstruisibles, capacité de rebuild séparée.
- IAM : C/N/I/M2M. Repo : `brendolys-ydiase-feed`.
- DR/test : perte totale de l’état + FULL_REBUILD testé avant production.
- Gates : contrats/versions/rétention sources; ranking; séparation SPN; watermark; FULL_REBUILD; `REBUILDABLE`; fraîcheur; RTO/SLO.