---
document_id: "YD-DOC-MS-OPP-001-AUT"
title: "YD-MS-OPP-001 — Opportunity"
document_type: "microservice-autonomy-profile"
document_role: "Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-OPP-001."
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
---

# YD-MS-OPP-001 — Opportunity

> **Rôle du document**
> Définit l’autonomie, l’autorité et les responsabilités documentées de YD-MS-OPP-001.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de cette frontière.

Statut : `C1-BASELINE / OPPORTUNITY-SEMANTICS-CLOSED`

- Autorité : opportunités, exigences, validité et politiques de candidature.
- C1, backup AUTH. C/N/I/M2M selon création/consultation autorisée.
- Dépendances : EMP-001, CFG, MOD. Fournit projection à Matching, Application, Search, Recommendation.
- Panne : lecture du dernier état connu; candidature revalide synchroniquement l’opportunité; publication sensible bloquée si employeur/modération requis non validables.
- Sécurité : anti-fraude, provenance de l’annonce, contrôle organisation, audit publication/retrait.
- Repo : `brendolys-ydiase-opportunity`.
- Gate : vérification employeur, expiration, modération, SLO/RPO/RTO, restore et contrats.

- Politique normative : `OPPORTUNITY_LIFECYCLE_POLICY.md`.
- Gates restant : policies par type, anti-fraude/modération, SLO retrait, IAM/tenant, BIA/RPO/RTO, restore et contrats.
