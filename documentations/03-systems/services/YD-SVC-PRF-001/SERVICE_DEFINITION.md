---
document_id: "YD-DOC-SVC-PRF-001-DEF"
title: "YD-SVC-PRF-001 — Profile Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-PRF-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-PRF-001 — Profile Service

> **Rôle du document**
> Définit le service logique YD-SVC-PRF-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: identite-profils` · `phase: P1` · `documentation: D2` · `implementation: not-started` · `activation: inactive`

## Mission
Porter le profil courant, les préférences, objectifs et contraintes déclarées d’une personne.

## Agrégats possédés
`UserProfile`, `Preference`, `Goal`, `DeclaredConstraint`.

## Source autoritative
YD-SVC-PRF-001.

## Données consommées
IdentityRef (IDN-001), consent/privacy (CNS-001), country configuration (CFG-001).

## Frontière DDD
Ne possède ni identité d’accès, ni historique académique détaillé, ni compétences individuelles.

## Incohérences
Aucune propriété concurrente détectée. Toute préférence de confidentialité doit rester CNS-001.
