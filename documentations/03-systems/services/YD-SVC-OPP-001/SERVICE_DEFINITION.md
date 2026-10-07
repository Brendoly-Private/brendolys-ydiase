---
document_id: "YD-DOC-SVC-OPP-001-DEF"
title: "YD-SVC-OPP-001 — Opportunity Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-OPP-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-OPP-001 — Opportunity Service

> **Rôle du document**
> Définit le service logique YD-SVC-OPP-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: opportunites-recrutement` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`Opportunity`, `OpportunityVersion`, `OpportunityRequirement`, `OpportunityPublication`.

## Source autoritative
YD-SVC-OPP-001.

## Données consommées
Employer (EMP-001), occupation/skills, location/config, provenance/quality, partner feeds.

## Incohérences
Les offres externes gardent leur provenance; OPP-001 devient autoritatif seulement pour la représentation YDIASE publiée.
