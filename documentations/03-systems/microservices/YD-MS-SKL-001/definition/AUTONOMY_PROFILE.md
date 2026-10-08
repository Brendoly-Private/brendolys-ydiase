---
document_id: "YD-DOC-MS-SKL-001-AUT"
title: "YD-MS-SKL-001 — Skills Knowledge"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-SKL-001."
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

# YD-MS-SKL-001 — Skills Knowledge

> **Rôle du document**
> Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-SKL-001.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Autorité : skills, concepts de connaissance, taxonomie et relations sémantiques.
- C2, backup AUTH. I mutation, C lecture, M2M.
- Dépendances : DAT-005; reçoit evidence EDU/CAR sans leur céder son ownership.
- Panne : dernière taxonomie versionnée; nouveaux mappings inconnus bloqués.
- Sécurité : provenance et version obligatoires; IA peut proposer, jamais publier seule un Skill canonique.
- Scaling : lectures/projections nombreuses; cache reconstruisible séparé du store autoritatif.
- Repo : `brendolys-ydiase-skills-knowledge`.
- Gate : gouvernance taxonomique, workflow validation, SLO/RPO/RTO, restore et contrats.