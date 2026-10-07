---
document_id: "YD-DOC-SVC-ADM-001-DEF"
title: "YD-SVC-ADM-001 — Administration Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-ADM-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-ADM-001 — Administration Service

> **Rôle du document**
> Définit le service logique YD-SVC-ADM-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: plateforme-gouvernance` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`AdminCase`, `AdministrativeActionRequest`, `OperationalOverride`.

## Source autoritative
YD-SVC-ADM-001 pour workflow administratif; jamais pour objets administrés.

## Données consommées
Domain admin contracts, identity/access, audit, moderation, configuration.

## Incohérences
Un override doit être audité et ne doit pas contourner les invariants du domaine cible.
