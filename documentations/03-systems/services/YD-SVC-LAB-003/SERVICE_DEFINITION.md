---
document_id: "YD-DOC-SVC-LAB-003-DEF"
title: "YD-SVC-LAB-003 — Labor Forecasting Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-LAB-003, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-LAB-003 — Labor Forecasting Service

> **Rôle du document**
> Définit le service logique YD-SVC-LAB-003, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: marche-travail` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`LaborForecast`, `ForecastScenario`, `ForecastModelRun`, `ForecastAssumption`, `ForecastEvaluation`.

## Source autoritative
YD-SVC-LAB-003 pour prévisions et évaluations.

## Données consommées
Historical labor intelligence/signals, economic signals, occupation/skill refs, analytics datasets.

## Incohérences
Une prévision n’est jamais un fait observé. Hypothèses, horizon et incertitude doivent être conservés.
