---
document_id: "YD-DOC-SVC-CAR-002-DEF"
title: "YD-SVC-CAR-002 — Career Path Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-CAR-002, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-CAR-002 — Career Path Service

> **Rôle du document**
> Définit le service logique YD-SVC-CAR-002, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: metiers-carrieres` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`CareerPath`, `CareerPathStep`, `PathScenario`, `PathComparisonState`.

## Source autoritative
YD-SVC-CAR-002 pour les trajectoires construites.

## Données consommées
Occupations/edges (CAR-001), profile/skills (PRF/SKL-002), programs (EDU-002), labor intelligence (LAB-002).

## Incohérences
Ne doit pas dupliquer les fonctions de simulation CAR-004 ni de reconversion CAR-003.
