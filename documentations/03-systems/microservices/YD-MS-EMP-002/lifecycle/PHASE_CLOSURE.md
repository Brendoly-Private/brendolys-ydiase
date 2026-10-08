---
document_id: "YD-DOC-MS-EMP-002-CLS"
title: "YD-MS-EMP-002 — Recruitment — Baseline C1"
document_type: "microservice-phase-closure"
document_role: "Consigne la fermeture documentaire Employer Workspace et les gates tenant, permissions, sécurité et recovery."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "evidence"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "microservice"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-EMP-002 — Recruitment — Baseline C1

> **Rôle du document**
> Consigne la fermeture documentaire Employer Workspace et les gates tenant, permissions, sécurité et recovery.
> **Usage développement :** preuve de maturité ou de fermeture ; le profil canonique et les politiques référencées restent autoritatifs.

Statut : `DOCUMENTATION-BASELINE-C1 / TALENT-RECRUITMENT-SEMANTICS-CLOSED`

## Politique normative
Voir `TALENT_ACCESS_RECRUITMENT_POLICY.md`.

## Invariants
- Employer, Opportunity, Match, Application et Recruitment restent des autorités distinctes ;
- vérification organisationnelle ne confère pas automatiquement un droit recruteur ;
- APP-001 seul possède l'état officiel d'une candidature ;
- EMP-002 n'est pas une base de profils librement interrogeable ;
- accès talent = tenant + principal + finalité + contexte + scopes + Privacy applicables ;
- profils/skills restent PRF/SKL et seules projections minimisées sont consommées ;
- MatchScore/RecommendationScore ne constitue jamais une décision de recrutement ;
- historique/audit non destructifs ;
- fuite cross-tenant/IDOR est release-blocking.

## Avant ACTIVE
policy sourcing proactif, fairness, rôles/scopes, rétention pays, BIA/RPO/RTO, restore et contrats APP.

Statut final : `C1-BASELINE-ESTABLISHED — TALENT-RECRUITMENT-SEMANTICS-CLOSED / IMPLEMENTATION-AND-EVIDENCE-PENDING`.
