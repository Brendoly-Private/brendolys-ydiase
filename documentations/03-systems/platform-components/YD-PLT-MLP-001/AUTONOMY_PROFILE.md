# YD-PLT-MLP-001 — Model Lifecycle & Registry

Statut : `autonomy-profile-draft`

- Autorité : références modèles, versions, évaluations, approbations, déploiements et retraits.
- C1, backup AUTH. I/M2M uniquement.
- Dépendances : stockage artefacts/modèles et services AI consommateurs.
- Panne : dernier modèle approuvé peut continuer si politique le permet; nouveau déploiement/retrait non vérifiable bloqué.
- Sécurité : séparation builder/approver/deployer, artefacts signés/traçables, provenance dataset/evaluation, rollback.
- Repo : `brendolys-ydiase-model-lifecycle-registry`.
- Gate : workflow approbation, registry artefacts, critères évaluation, SLO/RPO/RTO, restore.