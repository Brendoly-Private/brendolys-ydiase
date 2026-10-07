---
document_id: "YD-DOC-MS-MKT-001-AUT"
title: "YD-MS-MKT-001 — Learning Marketplace"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie et l’ownership de Learning Marketplace, avec autorité : listings commerciaux, commandes et états marketplace; contenu learning reste lrn/edu."
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

# YD-MS-MKT-001 — Learning Marketplace

> **Rôle du document**
> Définit l’autonomie et l’ownership de Learning Marketplace, avec autorité : listings commerciaux, commandes et états marketplace; contenu learning reste lrn/edu.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Autorité : listings commerciaux, commandes et états marketplace; contenu learning reste LRN/EDU.
- C1, backup AUTH. C, N/I opérateurs autorisés, M2M.
- Dépendances : LRN, BIL-002, MOD.
- Panne : consultation possible; nouvelle commande suspendue si billing ou contrôle critique indisponible.
- Sécurité : seller/operator scopes, audit commandes, séparation catalogue commercial/contenu pédagogique.
- Repo : `brendolys-ydiase-learning-marketplace`.
- Gate : modèle vendeur/commande, remboursements, pays/fiscalité, SLO/RPO/RTO, restore.