---
document_id: "YD-DOC-MS-EMP-001-AUT"
title: "YD-MS-EMP-001 — Employer"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie Employer et son autorité sur organisations employeuses, états et références gouvernées."
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

# YD-MS-EMP-001 — Employer

> **Rôle du document**
> Définit l’autonomie Employer et son autorité sur organisations employeuses, états et références gouvernées.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `C2-BASELINE / EMPLOYER-SEMANTICS-CLOSED`

- Autorité : employeurs, vérification et statut organisationnel.
- C2, backup AUTH. C organisations, I, M2M.
- Dépendances : PRT, CFG, validation Data selon source.
- Panne : lecture possible; mutation/validation sensible bloquée si preuve requise indisponible.
- Sécurité : isolation organisation, preuve de représentation, audit vérification et changement de statut.
- Repo : `brendolys-ydiase-employer`.
- Gate : modèle organisation/tenant, vérification, scopes, SLO/RPO/RTO, restore.

- Politique normative : `EMPLOYER_VERIFICATION_POLICY.md`.
- Gates restant : règles de vérification par pays, modèle tenant/scopes, IAM/IDOR, SLO/RPO/RTO, restore.
