---
document_id: "YD-DOC-MS-SKL-002-AUT"
title: "YD-MS-SKL-002 — User Skills Profile"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-SKL-002."
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

# YD-MS-SKL-002 — User Skills Profile

> **Rôle du document**
> Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-SKL-002.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `autonomy-profile-draft`

- Autorité : compétences individuelles, niveaux, preuves et versions.
- C1, backup AUTH, PII/profilage sensible.
- IAM : C propriétaire, I support strict, M2M. N sans accès par défaut.
- Dépendances : PRF, SKL-001, CNS, Identity.
- Panne : lecture bornée possible; écriture/évaluation sensible suspendue si identité ou privacy requise non vérifiable.
- Sécurité : contrôle objet par sujet, minimisation des projections, audit accès, rétention par finalité.
- Repo : `brendolys-ydiase-user-skills-profile`; datastore/secrets/workload identity propres.
- Gate : DPIA/privacy si applicable, scopes, SLO/RPO/RTO, rétention, restore et tests d’accès horizontal.