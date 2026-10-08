---
document_id: "YD-DOC-MS-EDU-004-AUT"
title: "YD-MS-EDU-004 — Qualification Framework"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie Qualification & Credential Catalog et son autorité sur qualifications, credentials et équivalences gouvernées."
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
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-EDU-004 — Qualification Framework

> **Rôle du document**
> Définit l’autonomie Qualification & Credential Catalog et son autorité sur qualifications, credentials et équivalences gouvernées.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Autorité : qualifications, niveaux, équivalences, prérequis et versions par pays.
- Criticité C2, backup AUTH.
- IAM : I mutation, C lecture, M2M. N uniquement si rôle futur explicitement autorisé.
- Dépendances : CFG et DAT-005. Fournit projections à Program, Profile et Career.
- Panne : dernière version valide reste disponible; nouveaux mappings/équivalences bloqués si référentiel pays absent.
- Sécurité : provenance obligatoire des équivalences, audit et historisation; aucune équivalence générée par IA comme vérité.
- Repo : `brendolys-ydiase-qualification-framework`; datastore privé.
- Gate : Country Framework Burkina, règles de validation, RPO/RTO/SLO, restore et contrats.