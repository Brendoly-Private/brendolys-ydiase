---
document_id: "YD-DOC-SVC-PRF-002-DEF"
title: "YD-SVC-PRF-002 — Education & Experience Profile Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-PRF-002, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-PRF-002 — Education & Experience Profile Service

> **Rôle du document**
> Définit le service logique YD-SVC-PRF-002, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: identite-profils` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`EducationRecord`, `ExperienceRecord`, `AchievementClaim`, `ProfileEvidenceLink`.

## Source autoritative
YD-SVC-PRF-002 pour l’historique individuel déclaré ou vérifié.

## Données consommées
ProfileRef (PRF-001), Institution/Program/Qualification (EDU), Skill taxonomy (SKL-001), provenance (DAT-003).

## Incohérences
Ne doit pas devenir propriétaire des établissements, programmes, qualifications ou compétences de référence.
