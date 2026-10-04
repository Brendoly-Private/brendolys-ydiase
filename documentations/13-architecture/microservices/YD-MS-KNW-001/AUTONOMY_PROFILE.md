# YD-MS-KNW-001 — Knowledge Graph

Statut : `autonomy-profile-draft`

- Autorité : aucune vérité métier primaire; graphe dérivé, mappings et watermarks.
- C2, backup DERIVED; reconstruction obligatoire testée. I/M2M.
- Dépendances : EDU, SKL, CAR, LAB et provenance DAT.
- Panne : version précédente datée ou reconstruction; jamais source autoritative de secours.
- Sécurité : provenance de chaque relation, suppression propagée, minimisation PII.
- Scaling : stockage/compute spécialisé permis par ADR; indépendant des sources.
- Repo : `brendolys-ydiase-knowledge-graph`.
- Gate : stratégie rebuild, freshness, provenance, SLO et seuils d’usage.