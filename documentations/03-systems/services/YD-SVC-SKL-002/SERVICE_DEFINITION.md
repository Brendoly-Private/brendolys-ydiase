---
document_id: "YD-DOC-SVC-SKL-002-DEF"
title: "YD-SVC-SKL-002 — User Skills Profile Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-SKL-002, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-SKL-002 — User Skills Profile Service

> **Rôle du document**
> Définit le service logique YD-SVC-SKL-002, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: competences-connaissances` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`UserSkill`, `SkillEvidence`, `SkillAssessmentState`, `SkillHistory`.

## Source autoritative
YD-SVC-SKL-002 pour l’état individuel de compétence.

## Données consommées
ProfileRef (PRF), SkillRef (SKL-001), assessments (ASM-001), education/experience evidence (PRF-002), consent (CNS-001).

## Incohérences
Les résultats d’assessment restent ASM-001; SKL-002 ne conserve que l’état de compétence dérivé et sa preuve.
