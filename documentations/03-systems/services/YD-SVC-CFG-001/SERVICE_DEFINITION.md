---
document_id: "YD-DOC-SVC-CFG-001-DEF"
title: "YD-SVC-CFG-001 — Country Configuration Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-CFG-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-CFG-001 — Country Configuration Service

> **Rôle du document**
> Définit le service logique YD-SVC-CFG-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: plateforme-gouvernance` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`CountryConfiguration`, `Territory`, `LanguageConfiguration`, `CurrencyConfiguration`, `CountryFrameworkBinding`, `LocalPolicyParameter`.

## Source autoritative
YD-SVC-CFG-001 pour configuration opérationnelle YDIASE; sources officielles externes restent attribuées.

## Données consommées
Reference datasets, official country sources, legal/compliance decisions, provenance.

## Incohérences
Ne doit pas absorber Qualification Framework EDU-004 ni taxonomies DAT-005; il les lie au pays.
