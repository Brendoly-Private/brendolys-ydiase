---
document_id: "YD-DOC-SVC-CAR-004-DEF"
title: "YD-SVC-CAR-004 — Career Simulation Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-CAR-004, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-CAR-004 — Career Simulation Service

> **Rôle du document**
> Définit le service logique YD-SVC-CAR-004, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: metiers-carrieres` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`CareerSimulation`, `SimulationScenario`, `SimulationAssumption`, `SimulationResult`.

## Source autoritative
YD-SVC-CAR-004 pour les simulations, jamais pour les faits source.

## Données consommées
Career paths (CAR-002), transitions (CAR-003), labor intelligence/forecast (LAB), user state (PRF/SKL), education (EDU).

## Incohérences
Les résultats doivent conserver hypothèses et versions des entrées afin d’éviter une fausse vérité prédictive.
