---
document_id: "YD-DOC-SVC-SKL-001-DEF"
title: "YD-SVC-SKL-001 — Skills Knowledge Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-SKL-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-SKL-001 — Skills Knowledge Service

> **Rôle du document**
> Définit le service logique YD-SVC-SKL-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: competences-connaissances` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`Skill`, `KnowledgeConcept`, `SkillRelation`, `SkillTaxonomyMapping`.

## Source autoritative
YD-SVC-SKL-001.

## Données consommées
Taxonomies (DAT-005), curricula/modules (EDU-003), occupations (CAR-001), provenance (DAT-003).

## Incohérences
Ne doit jamais posséder `UserSkill`. Risque de boucle sémantique avec CAR-001 à limiter par références stables.
