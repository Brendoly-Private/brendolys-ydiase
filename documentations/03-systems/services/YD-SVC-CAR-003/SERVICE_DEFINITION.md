---
document_id: "YD-DOC-SVC-CAR-003-DEF"
title: "YD-SVC-CAR-003 — Career Transition Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-CAR-003, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-CAR-003 — Career Transition Service

> **Rôle du document**
> Définit le service logique YD-SVC-CAR-003, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: metiers-carrieres` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`TransitionCase`, `TransitionGap`, `TransitionPlan`, `TransitionOption`.

## Source autoritative
YD-SVC-CAR-003.

## Données consommées
Current/target occupation (CAR-001), user skills (SKL-002), learning/program options (LRN/EDU), labor intelligence (LAB-002).

## Incohérences
La frontière avec CAR-002 doit rester nette: CAR-003 traite la transition entre états, CAR-002 la trajectoire.
