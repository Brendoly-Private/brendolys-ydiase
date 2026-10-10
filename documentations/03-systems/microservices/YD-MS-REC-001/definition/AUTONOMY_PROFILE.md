---
document_id: "YD-DOC-MS-REC-001-AUT"
title: "YD-MS-REC-001 — Recommendation"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-REC-001."
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
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-REC-001 — Recommendation

> **Rôle du document**
> Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-REC-001.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Logique : REC-001 + module RSH-001. Gate Research avant fonctions académiques avancées.
- Autorité : RecommendationRun/Set, scores, explications et evidence snapshot; aucune autorité sur données sources.
- C1, backup MIXED. C via ORI/edge, I diagnostic contrôlé, M2M.
- Dépendances : EDU, CAR, LAB, PRF, SKL, ASM, CNS; projections locales privilégiées pour éviter fan-out synchrone.
- Panne : abstention ou dernier run explicitement daté; jamais de ranking fabriqué. Freshness/evidence sous seuil bloque le run selon politique.
- Sécurité : finalité, minimisation, explicabilité, snapshot de preuves, version algorithme/modèle; sponsoring interdit dans ranking organique.
- Repo : `brendolys-ydiase-recommendation`.
- Gate : seuils qualité/fraîcheur, politique abstention, revue RSH, SLO/RPO/RTO, restore et contrats.