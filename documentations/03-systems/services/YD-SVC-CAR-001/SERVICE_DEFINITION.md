---
document_id: "YD-DOC-SVC-CAR-001-DEF"
title: "YD-SVC-CAR-001 — Occupation & Career Graph Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-CAR-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-CAR-001 — Occupation & Career Graph Service

> **Rôle du document**
> Définit le service logique YD-SVC-CAR-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: metiers-carrieres` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`Occupation`, `OccupationVersion`, `OccupationSkillRequirement`, `OccupationRelation`, `CareerTransitionEdge`.

## Source autoritative
YD-SVC-CAR-001.

## Données consommées
Skills (SKL-001), qualifications (EDU-004), labor signals (LAB-001), taxonomies (DAT-005), provenance (DAT-003).

## Incohérences
Le nom « Graph » ne lui donne pas la propriété du Knowledge Graph transversal KNW-001.
