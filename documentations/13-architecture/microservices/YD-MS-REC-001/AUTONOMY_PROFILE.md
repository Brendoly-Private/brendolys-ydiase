# YD-MS-REC-001 — Recommendation

Statut : `autonomy-profile-draft`

- Logique : REC-001 + module RSH-001. Gate Research avant fonctions académiques avancées.
- Autorité : RecommendationRun/Set, scores, explications et evidence snapshot; aucune autorité sur données sources.
- C1, backup MIXED. C via ORI/edge, I diagnostic contrôlé, M2M.
- Dépendances : EDU, CAR, LAB, PRF, SKL, ASM, CNS; projections locales privilégiées pour éviter fan-out synchrone.
- Panne : abstention ou dernier run explicitement daté; jamais de ranking fabriqué. Freshness/evidence sous seuil bloque le run selon politique.
- Sécurité : finalité, minimisation, explicabilité, snapshot de preuves, version algorithme/modèle; sponsoring interdit dans ranking organique.
- Repo : `brendolys-ydiase-recommendation`.
- Gate : seuils qualité/fraîcheur, politique abstention, revue RSH, SLO/RPO/RTO, restore et contrats.