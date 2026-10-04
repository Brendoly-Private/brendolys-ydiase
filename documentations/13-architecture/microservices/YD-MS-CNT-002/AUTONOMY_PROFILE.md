# YD-MS-CNT-002 — Feed

Statut : `autonomy-profile-draft`

- Autorité : aucune vérité métier; feed et ranking dérivés.
- C3, backup DERIVED. C/N/I/M2M.
- Dépendances : CNT, COM, MOD; SPN injecté comme placement séparé, jamais dans score organique.
- Panne : feed chronologique/simplifié ou indisponibilité contrôlée; reconstruction depuis projections.
- Sécurité : suppression/modération prioritaire, minimisation profilage, aucune copie durable inutile de PII.
- Scaling : lecture élevée, cache et partitions reconstruisibles.
- Repo : `brendolys-ydiase-feed`.
- Gate : règles ranking, séparation sponsoring, freshness, reconstruction, SLO.