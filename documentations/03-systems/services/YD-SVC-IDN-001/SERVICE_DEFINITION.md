---
document_id: "YD-DOC-SVC-IDN-001-DEF"
title: "YD-SVC-IDN-001 — Identity & Access Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-IDN-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-IDN-001 — Identity & Access Service

> **Rôle du document**
> Définit le service logique YD-SVC-IDN-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: identite` · `documentation: D2` · `implementation: not-started`

## Mission
Porter l’identité technique, les comptes, sessions et principaux d’accès.

## Agrégats possédés
`Identity`, `CredentialBinding`, `Account`, `Session`, `AccessPrincipal`.

## Source autoritative
YD-SVC-IDN-001 pour l’identité technique et les comptes.

## Données consommées
Consent status (CNS-001), country policy (CFG-001), audit policy (AUD-001).

## Incohérences
Aucune propriété concurrente détectée. Ne doit pas absorber `UserProfile`.
