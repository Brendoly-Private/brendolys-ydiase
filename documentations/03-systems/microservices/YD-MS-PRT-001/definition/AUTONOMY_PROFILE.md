---
document_id: "YD-DOC-MS-PRT-001-AUT"
title: "YD-MS-PRT-001 — Partner"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-PRT-001."
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

# YD-MS-PRT-001 — Partner

> **Rôle du document**
> Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-PRT-001.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Autorité : partenaires, accords, rôles, scopes contractuels et statuts.
- C1, backup AUTH. N/I/M2M.
- Dépendances : CFG, CNS pour contacts; alimente DAT/AMB/workspaces.
- Panne : nouvelle action nécessitant un droit contractuel suspendue si accord non vérifiable; lecture bornée possible.
- Sécurité : documents/contacts protégés, séparation organisations, audit des droits et dates de validité.
- Repo : `brendolys-ydiase-partner`.
- Gate : modèle accords/scopes, rétention, SLO/RPO/RTO, restore, permissions networks.