---
document_id: "YD-DOC-SVC-LAB-002-DEF"
title: "YD-SVC-LAB-002 — Labor Market Intelligence Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-LAB-002, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-LAB-002 — Labor Market Intelligence Service

> **Rôle du document**
> Définit le service logique YD-SVC-LAB-002, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: marche-travail` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`LaborMarketIndicator`, `LaborMarketSnapshot`, `DemandSupplyMeasure`, `TensionMeasure`, `SectorTerritoryAnalysis`.

## Source autoritative
YD-SVC-LAB-002 pour les indicateurs dérivés publiés.

## Données consommées
Labor signals, occupations, skills, opportunities, analytics aggregates, territory/reference data.

## Incohérences
Doit exposer méthodologie/version des indicateurs; ne réécrit jamais LAB-001.
