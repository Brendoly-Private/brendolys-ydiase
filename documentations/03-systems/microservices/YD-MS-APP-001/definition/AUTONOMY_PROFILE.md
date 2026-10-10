---
document_id: "YD-DOC-AUTO-D2D79B4A266344EC"
title: "AUTONOMY PROFILE"
document_type: "documentation-reference"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
product: "BRENDOLYS YDIASE"
document_role: "Autonomie et ownership."
authority_level: "canonical-source"
development_usage: "mandatory-reference"
---

# YD-MS-APP-001 — Application

Statut : `C1-BASELINE / APPLICATION-LIFECYCLE-SEMANTICS-CLOSED`

- Autorité : candidatures, états et transitions.
- C1, backup AUTH; PII et données de recrutement sensibles.
- IAM : C candidat, C organisation via permissions explicites, I support, M2M.
- Dépendances : OPP validation, EMP-002 commandes de décision, CNS, NTF.
- Panne : nouvelle soumission bloquée si opportunité non validable; dernier état consultable; commandes idempotentes.
- Sécurité : contrôle candidat/employeur par objet, audit complet des transitions, aucune écriture directe par Employer Workspace.
- Repo : `brendolys-ydiase-application`.
- Gate : machine d’état, rétention légale, scopes, SLO/RPO/RTO, restore et tests d’idempotence.

- Politique normative : `APPLICATION_LIFECYCLE_POLICY.md`.
- Gates restant : transitions par type, rétention pays, rôles/scopes, idempotence/concurrence, BIA/RPO/RTO, restore.
