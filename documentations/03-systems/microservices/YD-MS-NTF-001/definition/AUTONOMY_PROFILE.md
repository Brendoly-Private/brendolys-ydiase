---
document_id: "YD-DOC-MS-NTF-001-AUT"
title: "YD-MS-NTF-001 — Notification"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie et l’ownership de Notification, avec autorité : demandes de livraison, tentatives et états de livraison; jamais état métier source."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "microservice"
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-NTF-001 — Notification

> **Rôle du document**
> Définit l’autonomie et l’ownership de Notification, avec autorité : demandes de livraison, tentatives et états de livraison; jamais état métier source.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Autorité : demandes de livraison, tentatives et états de livraison; jamais état métier source.
- C2, backup AUTH pour preuve/livraison selon rétention. M2M principal; I support.
- Dépendances : CNS/PRF préférences et providers externes.
- Panne : queue/retry/DLQ; panne notification ne rollback pas une transaction métier sauf règle explicite documentée.
- Sécurité : contenu minimal, secrets provider isolés, marketing fail-closed si permission inconnue, logs sans tokens.
- Repo : `brendolys-ydiase-notification`.
- Gate : canaux/providers, idempotence, rétention, SLO/RPO/RTO, DR et contrats.