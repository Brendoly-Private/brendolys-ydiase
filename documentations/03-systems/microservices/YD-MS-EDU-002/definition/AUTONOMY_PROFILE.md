---
document_id: "YD-DOC-MS-EDU-002-AUT"
title: "YD-MS-EDU-002 — Program Catalog"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie Program & Curriculum Catalog et son autorité sur programmes, curricula, modules et versions."
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

# YD-MS-EDU-002 — Program Catalog

> **Rôle du document**
> Définit l’autonomie Program & Curriculum Catalog et son autorité sur programmes, curricula, modules et versions.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Logique : EDU-002. Autorité sur programmes, versions, rattachements et conditions d’accès.
- Criticité : C2. Backup AUTH.
- IAM : I/N pour gestion autorisée, C lecture, M2M.
- Exposition : EDGE lecture, INT mutations/intégrations.
- Dépendances : EDU-001 validation institution, EDU-004 qualifications, CFG. Consomme CurriculumPublished sans transaction inverse.
- Panne : catalogue publié lisible; nouvelle publication bloquée si institution ou qualification requise non validable.
- Résilience : aucune transaction distribuée avec Curriculum; événements versionnés et réconciliation.
- Sécurité : audit des publications/retraits; contributeur institutionnel limité à son périmètre.
- Repo : `brendolys-ydiase-program-catalog`; datastore et migrations privés.
- Gate : RPO/RTO/SLO, scopes institutionnels, politique version/retrait, restore et contrats.