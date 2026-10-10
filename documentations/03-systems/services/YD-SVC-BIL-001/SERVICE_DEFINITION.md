---
document_id: "YD-DOC-SVC-BIL-001-DEF"
title: "YD-SVC-BIL-001 — Subscription & Entitlement Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-BIL-001, son périmètre, ses responsabilités et ses dépendances documentées."
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
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-SVC-BIL-001 — Subscription & Entitlement Service

> **Rôle du document**
> Définit le service logique YD-SVC-BIL-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: economie-produit` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`CommercialProduct`, `CommercialProductVersion`, `Plan`, `Subscription`, `Entitlement`, `Quota`, `EntitlementGrant`.

## Source autoritative
YD-SVC-BIL-001 est autoritatif pour le catalogue commercial transversal, les plans, abonnements, droits et quotas commerciaux.

## Données consommées
Account/organization refs, références d’offres techniques ou métier depuis API-001/DPR-001/INT-001/MKT-001, billing status depuis BIL-002, country config depuis CFG-001.

## Frontière commerciale
Les services API, Data Product, Intelligence Product et Marketplace possèdent le contenu et la définition métier de leurs offres. BIL-001 possède leur représentation commerciale commune : identifiant vendable, version commerciale, plan, entitlement et quota. Il ne duplique pas les datasets, API contracts, rapports ou listings marketplace.

## Incohérences
Ownership du catalogue commercial résolu en D2. La relation exacte entre quota commercial BIL-001 et quota technique API-001 reste un contrat D3, sans double décision d’autorisation.
