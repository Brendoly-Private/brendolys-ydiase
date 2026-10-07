---
document_id: "YD-DOC-SVC-INS-001-DEF"
title: "YD-SVC-INS-001 — Institution Workspace Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-INS-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-INS-001 — Institution Workspace Service

> **Rôle du document**
> Définit le service logique YD-SVC-INS-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: partenaires-ecosysteme` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`InstitutionWorkspace`, `InstitutionMembership`, `InstitutionSubmission`, `ValidationWorkflow`.

## Source autoritative
YD-SVC-INS-001 pour workspace/workflow; EDU reste autoritatif après publication.

## Données consommées
Institution catalog, identity/access, partner agreement, data submissions, audit.

## Incohérences
Toute modification d’Institution/Program doit passer par validation puis publication dans EDU, pas par écriture directe.
