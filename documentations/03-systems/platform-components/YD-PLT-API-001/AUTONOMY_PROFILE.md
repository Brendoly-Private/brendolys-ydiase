---
document_id: "YD-DOC-PLT-API-001-AUT"
title: "YD-PLT-API-001 — External API Management"
document_type: "platform-component-autonomy-profile"
document_role: "Définit l’autonomie, les responsabilités et les limites documentées du composant YD-PLT-API-001."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "platform"
---

# YD-PLT-API-001 — External API Management

> **Rôle du document**
> Définit l’autonomie, les responsabilités et les limites documentées du composant YD-PLT-API-001.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de ce composant.

Statut : `autonomy-profile-draft`

- Rôle : exposition API externe, registre clients, quotas techniques, routage/policies; aucune donnée métier autoritative.
- Criticité : C1. Reprise MIXED pour configuration clients, quotas et état nécessaire.
- Audience IAM : `ydiase-external-api`.
- Clients : identité distincte par client/organisation; credentials partagés entre organisations interdits. M2M par identité dédiée; délégation utilisateur conservée lorsqu’un appel agit au nom d’un utilisateur.
- Realms : `brendolys-customers` pour clients prévus; `brendolys-internal` pour administration/support; `brendolys-networks` uniquement contrat explicitement destiné au réseau.
- Scopes : scopes par contrat `api:<contract-id>:read` / `api:<contract-id>:write` ou granularité plus stricte. Aucun scope global `api:*` ne donne accès aux backends.
- Autorisation : API Management contrôle identité, statut client, scope, quota et entitlement BIL. Le backend garde l’autorisation métier et objet.
- Onboarding client : owner, organisation/tenant, contrats, scopes, entitlement, quotas, territoires si applicables, méthode auth, création/expiration, statut, contact sécurité et audit.
- Statuts client : `PENDING`, `ACTIVE`, `SUSPENDED`, `REVOKED`, `EXPIRED`. Suspension/révocation prend effet avant routage.
- Dépendances : BRENDOLYS Identity, BIL entitlements, backends exposés.
- Panne : Identity/entitlement requis non vérifiable => fail-closed; throttling; backend défaillant isolé sans cascade.
- Sécurité : workload identity/mTLS selon ADR, rate limits, contrôles edge, rotation credentials et audit accès.
- Repo : `brendolys-ydiase-external-api-management`.
- Gate Contract Registry : `CLOSED` pour PLT-API-IAM.
- Gates préproduction : méthodes M2M physiques, rotation/durée credentials, quotas numériques, SLO/RPO/RTO, DR et contrats physiques.