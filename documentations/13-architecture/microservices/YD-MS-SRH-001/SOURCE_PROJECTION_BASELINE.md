# SRH-001 — Source Projection Baseline

Statut : `DEPENDENCY-BASELINE`

## Familles v1

| Contrat | Owner | Objets candidats | États critiques |
|---|---|---|---|
| `YD-CTR-EDU-SEARCHABLE-v1` | EDU | institutions, programmes, modules publiables | publish/unpublish/version |
| `YD-CTR-CAR-SEARCHABLE-v1` | CAR | métiers et objets carrière publiables | publish/withdraw/version |
| `YD-CTR-OPP-SEARCHABLE-v1` | OPP-001 | opportunités | publish/suspend/expire/withdraw/close |
| `YD-CTR-CNT-SEARCHABLE-v1` | CNT-001 | contenus | publish/unpublish/moderation effect |
| `YD-CTR-LRN-SEARCHABLE-v1` | LRN-001 | ressources learning publiables | active/limited/stale/withdraw/retire |
| `YD-CTR-KNW-SRH-SEARCH-ENRICHMENT-v1` | KNW-001 | enrichissements sémantiques dérivés | upsert/delete/revoke/stale |

## Obligations communes

Chaque projection permet de déterminer : projection id/version, source owner, source object/version, opération, effective time, publication/visibility state, language, territory lorsque pertinent, provenance minimale, replay position et freshness.

Pour les données non publiques : access labels, tenant/finality/privacy requirements applicables.

## Priorités de convergence

1. REVOKE / privacy restriction / moderation block
2. DELETE / WITHDRAW / UNPUBLISH / EXPIRE
3. correction/version
4. UPSERT
5. KNW enrichment

Cette priorité est logique : elle n'impose pas un broker ou topic physique.

## Reconstruction

Chaque owner fournit soit une fenêtre de replay suffisante, soit un snapshot autoritatif + catch-up. Sans preuve compatible, SRH reste `REBUILD-BLOCKED`.

## Règle de validation métier

Search peut filtrer selon la projection mais ne remplace jamais une validation synchrone de l'owner lorsqu'une commande sensible exige l'état courant.

Statut : `SEARCH-SOURCE-DEPENDENCIES-DEFINED / PHYSICAL-CONTRACTS-PENDING`.
