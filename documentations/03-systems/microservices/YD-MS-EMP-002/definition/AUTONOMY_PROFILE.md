---
document_id: "YD-DOC-MS-EMP-002-AUT"
title: "YD-MS-EMP-002 — Talent & Recruitment"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie Employer Workspace et les droits d’action recruteur sans transférer l’autorité des profils candidats."
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

# YD-MS-EMP-002 — Talent & Recruitment

> **Rôle du document**
> Définit l’autonomie Employer Workspace et les droits d’action recruteur sans transférer l’autorité des profils candidats.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `C1-BASELINE / TALENT-RECRUITMENT-SEMANTICS-CLOSED`

- Autorité : campagnes, viviers autorisés et décisions de sélection; APP reste owner de l’état candidature.
- C1, backup AUTH. C organisations, I, M2M.
- Dépendances : EMP-001, APP, OPP-002, CNS.
- Panne : campagnes consultables; décision mise en attente si Application indisponible; jamais d’état candidature concurrent.
- Sécurité : tenant isolation, accès recruteur, minimisation des profils candidats, audit des décisions.
- Repo : `brendolys-ydiase-talent-recruitment`.
- Gate : permissions recruteur, finalités traitement candidats, SLO/RPO/RTO, restore, contrats APP.

- Politique normative : `TALENT_ACCESS_RECRUITMENT_POLICY.md`.
- Gates restant : policy sourcing proactif, fairness, rôles/scopes, rétention pays, BIA/RPO/RTO, restore et contrats APP.
