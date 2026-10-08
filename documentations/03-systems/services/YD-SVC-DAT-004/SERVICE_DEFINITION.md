---
document_id: "YD-DOC-SVC-DAT-004-DEF"
title: "YD-SVC-DAT-004 — Data Quality & Validation Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-DAT-004, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-DAT-004 — Data Quality & Validation Service

> **Rôle du document**
> Définit le service logique YD-SVC-DAT-004, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: data` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`QualityAssessment`, `ValidationCase`, `Anomaly`, `CorroborationCase`, `ValidationDecision`.

## Source autoritative
YD-SVC-DAT-004 pour qualité et décisions de validation, jamais pour l’objet métier.

## Données consommées
Raw/domain records, provenance, validation rules, reference taxonomies.

## Incohérences
À D3, préciser qui possède les règles de validation métier: domaine ou DAT-004. Recommandation: domaine définit, DAT-004 exécute les contrôles transversaux.
