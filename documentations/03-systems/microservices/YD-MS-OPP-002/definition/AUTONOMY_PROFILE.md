---
document_id: "YD-DOC-MS-OPP-002-AUT"
title: "YD-MS-OPP-002 — Opportunity Matching"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-OPP-002."
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
---

# YD-MS-OPP-002 — Opportunity Matching

> **Rôle du document**
> Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-OPP-002.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `C2-BASELINE / OPPORTUNITY-MATCHING-SEMANTICS-CLOSED`

- Autorité : MatchRun/Match, score et explication; aucune autorité sur profil ou opportunité.
- C2, backup MIXED. C/I/M2M.
- Dépendances : OPP-001, PRF, SKL-002, CNS.
- Panne : abstention si inputs minimum absents; ancien match uniquement daté; snapshot de calcul versionné.
- Sécurité : profilage minimisé, finalité contrôlée, sponsoring interdit dans score organique.
- Repo : `brendolys-ydiase-opportunity-matching`.
- Gate : seuils/freshness, explication, SLO/RPO/RTO, rétention runs, restore et contrats.

- Politique normative : `OPPORTUNITY_MATCHING_POLICY.md`.
- Gates restant : coefficients/seuils, métriques d'équité, règles par type, IAM/IDOR, rétention runs, BIA/RPO/RTO, restore et contrats.
