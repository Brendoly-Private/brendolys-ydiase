---
document_id: "YD-DOC-MS-AI-003-AUT"
title: "YD-MS-AI-003 — AI Verification"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie et la séparation de vérification de AI Verification, notamment son indépendance vis-à-vis du générateur."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "microservice"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
---

# YD-MS-AI-003 — AI Verification

> **Rôle du document**
> Définit l’autonomie et la séparation de vérification de AI Verification, notamment son indépendance vis-à-vis du générateur.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de la frontière concernée.

Statut : `autonomy-profile-draft`

- Autorité : décisions de vérification AI, evidence refs, règles/version de vérification.
- C1, backup AUTH. M2M, I diagnostic.
- Dépendances : outputs AI, grounding et sources de preuve. Indépendance obligatoire du générateur.
- Panne : fail-closed pour usage exigeant vérification; aucun générateur ne s’auto-valide.
- Sécurité : séparation des rôles, audit des overrides, evidence immutable/versionnée, tests adversariaux.
- Repo : `brendolys-ydiase-ai-verification`.
- Gate : classes d’usage exigeant vérification, seuils, SLO/RPO/RTO, restore, politique override.