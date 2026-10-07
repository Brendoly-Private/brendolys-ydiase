---
document_id: "YD-DOC-PLT-AI-001-AUT"
title: "YD-PLT-AI-001 — AI Gateway"
document_type: "platform-component-autonomy-profile"
document_role: "Définit l’autonomie, les responsabilités et les limites documentées du composant YD-PLT-AI-001."
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

# YD-PLT-AI-001 — AI Gateway

> **Rôle du document**
> Définit l’autonomie, les responsabilités et les limites documentées du composant YD-PLT-AI-001.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de ce composant.

Statut : `autonomy-profile-draft`

- Rôle : point de contrôle des usages AI, policy gate et routage; aucune vérité métier.
- Criticité : C1. Reprise MIXED des policies/config et métadonnées nécessaires; contenu utilisateur selon minimisation/rétention.
- Audience IAM : `ydiase-ai-gateway`.
- Realms : `brendolys-customers` selon produit/entitlement; `brendolys-networks` uniquement cas d’usage explicitement autorisés; `brendolys-internal` pour administration, diagnostic, évaluation et usages internes; M2M par workload identity.
- Scopes : `ai:invoke`, `ai:grounded:invoke`, `ai:verify:invoke`, `ai:usage:read:self`, `ai:policy:read`, `ai:policy:manage`, `ai:model:route`.
- Autorisation : intersection realm + scope + use-case policy + purpose CNS + entitlement si applicable + modèle approuvé MLP + tenant/pays. Aucun scope ne contourne l’autorisation du domaine.
- Claims : identité, audience, scopes et contexte tenant minimal. Prompt et données métier sont interdits dans le token.
- Dépendances : BRENDOLYS Identity, CNS, AI-002/003, modèles approuvés MLP et BIL lorsque l’usage est soumis à entitlement.
- Panne : fail-closed si policy, consentement/finalité, entitlement ou approbation modèle obligatoire n’est pas vérifiable.
- Sécurité : rate limits, quotas, contrôles input/prompt, redaction, journalisation minimisée, isolation tenant/use case.
- Repo : `brendolys-ydiase-ai-gateway`.
- Gate Contract Registry : `CLOSED` pour PLT-AI-IAM.
- Gates préproduction : clients OIDC physiques, step-up si requis, SLO/RPO/RTO, secrets/certificats, DR, quotas numériques et contrats physiques.