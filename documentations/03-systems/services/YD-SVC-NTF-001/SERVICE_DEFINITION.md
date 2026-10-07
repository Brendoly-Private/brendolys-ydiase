---
document_id: "YD-DOC-SVC-NTF-001-DEF"
title: "YD-SVC-NTF-001 — Notification Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-NTF-001, son périmètre, ses responsabilités et ses dépendances documentées."
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

# YD-SVC-NTF-001 — Notification Service

> **Rôle du document**
> Définit le service logique YD-SVC-NTF-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: plateforme` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`Notification`, `DeliveryAttempt`, `NotificationPreferenceProjection`, `NotificationTemplate`.

## Source autoritative
YD-SVC-NTF-001 pour notification/livraison; préférences maîtres restent PRF/CNS selon type.

## Données consommées
Identity/contact route, user preferences/consent, événements des domaines producteurs.

## Incohérences
`NotificationPreferenceProjection` doit rester une projection et ne jamais concurrencer PRF/CNS.
