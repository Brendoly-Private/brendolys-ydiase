---
document_id: "YD-DOC-MS-EDU-003-AUT"
title: "YD-MS-EDU-003 — Curriculum & Module"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie Education Record et l’autorité sur les parcours et enregistrements éducatifs individuels."
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
---

# YD-MS-EDU-003 — Curriculum & Module

> **Rôle du document**
> Définit l’autonomie Education Record et l’autorité sur les parcours et enregistrements éducatifs individuels.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Autorité : curricula, modules, versions, mappings pédagogiques.
- Criticité C2, backup AUTH. Version publiée conservée et restaurable.
- IAM : I/N gestion autorisée, C lecture, M2M.
- Dépendances : EDU-002 et SKL-001. Publication exige Program valide; Skill inconnu ne devient jamais canonique ici.
- Contrats : CurriculumPublished et CurriculumSkillEvidence; aucun accès DB de Program/Skills.
- Panne : brouillon possible; publication bloquée sans Program valide; dernière version publiée reste lisible.
- Sécurité : provenance, historique, séparation brouillon/publication, audit des changements structurants.
- Repo : `brendolys-ydiase-curriculum-module`; datastore/migrations/backup propres.
- Gate : SLO/RPO/RTO, workflow publication, tailles/versioning modules, restore et contrats.