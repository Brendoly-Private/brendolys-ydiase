---
document_id: "YD-DOC-MS-SPN-001-AUT"
title: "YD-MS-SPN-001 — Sponsored Placement"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-SPN-001."
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

# YD-MS-SPN-001 — Sponsored Placement

> **Rôle du document**
> Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-SPN-001.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Autorité : campagnes sponsorisées, placements, budgets référencés et deliveries.
- C2, backup AUTH. C annonceurs, I, M2M.
- Dépendances : BIL-002, MOD, surfaces d’affichage.
- Panne : aucun sponsoring affiché si service/policy indisponible; ranking organique reste inchangé.
- Sécurité : séparation stricte organique/sponsorisé, transparence du placement, audit budgets/delivery.
- Repo : `brendolys-ydiase-sponsored-placement`.
- Gate : règles d’éligibilité, labeling, budget reconciliation, SLO/RPO/RTO, restore.