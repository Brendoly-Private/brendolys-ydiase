---
document_id: "YD-DOC-SVC-ASM-001-DEF"
title: "YD-SVC-ASM-001 — Assessment Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-ASM-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-ASM-001 — Assessment Service

> **Rôle du document**
> Définit le service logique YD-SVC-ASM-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: orientation-recommandation` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`AssessmentDefinition`, `AssessmentSession`, `AssessmentResponse`, `AssessmentResult`.

## Source autoritative
YD-SVC-ASM-001.

## Données consommées
Identity/Profile refs, consent (CNS-001), skills taxonomy (SKL-001), country rules (CFG-001).

## Incohérences
Un résultat d’évaluation n’est pas une compétence acquise; SKL-002 décide de son intégration dans l’état de compétence.
