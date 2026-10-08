---
document_id: "YD-DOC-SVC-REC-002-DEF"
title: "YD-SVC-REC-002 — Application Service — SUPERSEDED"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-REC-002, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-REC-002 — Application Service — SUPERSEDED

> **Rôle du document**
> Définit le service logique YD-SVC-REC-002, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: opportunites-recrutement` · `documentation: D2` · `status: SUPERSEDED` · `implementation: not-started`

## Décision
Cet identifiant historique est retiré avant implémentation afin de supprimer la collision sémantique entre `REC` (Recommendation) et Application.

## Successeur obligatoire
`YD-SVC-APP-001 — Application Service`.

## Règle de compatibilité documentaire
`YD-SVC-REC-002` ne doit plus être utilisé dans une nouvelle exigence, dépendance, API, événement ou implémentation. Il reste conservé uniquement pour la traçabilité des documents antérieurs.

## Agrégats historiques
`Application`, `ApplicationStatusHistory`, `ApplicationSubmission`, `CandidateResponse` sont transférés à `YD-SVC-APP-001` avant toute implémentation.
