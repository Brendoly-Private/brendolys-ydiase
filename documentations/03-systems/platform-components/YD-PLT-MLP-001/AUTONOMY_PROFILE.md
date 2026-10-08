---
document_id: "YD-DOC-PLT-MLP-001-AUT"
title: "YD-PLT-MLP-001 — Model Lifecycle & Registry"
document_type: "platform-component-autonomy-profile"
document_role: "Définit l’autonomie, les responsabilités et les limites documentées du composant YD-PLT-MLP-001."
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
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-PLT-MLP-001 — Model Lifecycle & Registry

> **Rôle du document**
> Définit l’autonomie, les responsabilités et les limites documentées du composant YD-PLT-MLP-001.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de ce composant.

Statut : `autonomy-profile-draft`

- Autorité : références modèles, versions, évaluations, approbations, déploiements et retraits.
- C1, backup AUTH. I/M2M uniquement.
- Dépendances : stockage artefacts/modèles et services AI consommateurs.
- Panne : dernier modèle approuvé peut continuer si politique le permet; nouveau déploiement/retrait non vérifiable bloqué.
- Sécurité : séparation builder/approver/deployer, artefacts signés/traçables, provenance dataset/evaluation, rollback.
- Repo : `brendolys-ydiase-model-lifecycle-registry`.
- Gate : workflow approbation, registry artefacts, critères évaluation, SLO/RPO/RTO, restore.