---
document_id: "YD-DOC-SVC-ORI-001-DEF"
title: "YD-SVC-ORI-001 — Orientation Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-ORI-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-ORI-001 — Orientation Service

> **Rôle du document**
> Définit le service logique YD-SVC-ORI-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: orientation-recommandation` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`OrientationCase`, `OrientationObjective`, `OrientationConstraintSet`, `OrientationDecisionRecord`.

## Source autoritative
YD-SVC-ORI-001 pour le dossier d’orientation.

## Données consommées
Profile, education, skills, assessments, programs, occupations, labor intelligence, recommendation outputs, consent.

## Incohérences
Orientation orchestre une décision mais ne doit pas absorber Recommendation ni les sources métier.
