---
document_id: "YD-DOC-SVC-MKT-001-DEF"
title: "YD-SVC-MKT-001 — Learning Marketplace Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-MKT-001, son périmètre, ses responsabilités et ses dépendances documentées."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "service"
---

# YD-SVC-MKT-001 — Learning Marketplace Service

> **Rôle du document**
> Définit le service logique YD-SVC-MKT-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: economie-produit` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`MarketplaceListing`, `MarketplaceOffer`, `ConversionAttribution`, `MarketplaceOrder`.

## Source autoritative
YD-SVC-MKT-001.

## Données consommées
Learning resources, partner/provider, billing, entitlements, consented profile context.

## Incohérences
MKT-001 ne doit pas posséder `LearningResource`; il commercialise une offre référencée.
