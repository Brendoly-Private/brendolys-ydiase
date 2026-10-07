---
document_id: "YD-DOC-SVC-ANL-001-DEF"
title: "YD-SVC-ANL-001 — Analytics Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-ANL-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-ANL-001 — Analytics Service

> **Rôle du document**
> Définit le service logique YD-SVC-ANL-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: analytics` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`MetricDefinition`, `AnalyticalDataset`, `AggregateSnapshot`, `AnalysisRun`.

## Source autoritative
YD-SVC-ANL-001 pour métriques et datasets dérivés.

## Données consommées
Projections gouvernées des domaines autorisés, provenance/quality, country/reference data.

## Incohérences
Les datasets analytiques ne doivent pas devenir source opérationnelle des domaines.
