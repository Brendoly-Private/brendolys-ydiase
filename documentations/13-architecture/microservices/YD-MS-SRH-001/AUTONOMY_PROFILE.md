# YD-MS-SRH-001 — Search & Discovery

Statut : `autonomy-profile-draft`

- Autorité : index seulement; jamais autorité sur objets métier.
- C2, backup DERIVED. C/N/I/M2M selon surface.
- Dépendances : EDU, CAR, OPP, CNT, LRN. Index reconstruisible depuis projections versionnées.
- Panne : recherche partielle ou indisponibilité contrôlée; aucun résultat Search ne vaut validation métier.
- Sécurité : indexation minimale, suppression/révocation propagée, aucun secret/PII inutile dans index.
- Scaling : lectures élevées et indexation asynchrone; scaling indépendant attendu.
- Repo : `brendolys-ydiase-search-discovery`.
- Gate : freshness, reconstruction complète testée, SLO, politique suppression et contrats.