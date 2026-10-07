---
document_id: "YD-DOC-MS-MOD-001-AUT"
title: "YD-MS-MOD-001 — Moderation"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie et l’ownership de Moderation, avec autorité : politiques, dossiers et décisions de modération; owner métier applique l’effet sur son objet."
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
---

# YD-MS-MOD-001 — Moderation

> **Rôle du document**
> Définit l’autonomie et l’ownership de Moderation, avec autorité : politiques, dossiers et décisions de modération; owner métier applique l’effet sur son objet.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Autorité : politiques, dossiers et décisions de modération; owner métier applique l’effet sur son objet.
- Owner métier de politique : fonction Gouvernance & Trust/Safety YDIASE. Elle possède le référentiel transverse de modération, les règles de décision, les procédures d’appel et les critères d’escalade. Les domaines CNT, COM, MKT et SPN restent propriétaires de leurs objets et appliquent les décisions à leurs agrégats.
- Séparation de responsabilités : l’équipe technique MOD implémente et exploite le service sans pouvoir modifier seule la politique métier; toute évolution de politique suit une approbation métier tracée et auditée.
- C1, backup AUTH. C/N pour signalement limité, I modérateurs, M2M.
- Dépendances : CNT, COM, MKT, SPN, AUD.
- Panne : objet explicitement bloqué reste fail-closed; décisions vers owners en retry; aucun accès DB direct aux objets.
- Sécurité : séparation policy/décision, RBAC modérateur, audit complet, protection contre abus internes.
- Repo : `brendolys-ydiase-moderation`.
- Gate : nomination nominative du responsable et du suppléant Gouvernance & Trust/Safety, appels/recours, SLA décision, SLO/RPO/RTO, restore.