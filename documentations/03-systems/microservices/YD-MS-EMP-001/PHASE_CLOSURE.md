# YD-MS-EMP-001 — Recruitment — Baseline C2

Statut : `DOCUMENTATION-BASELINE-C2 / EMPLOYER-SEMANTICS-CLOSED`

## Politique normative
Voir `EMPLOYER_VERIFICATION_POLICY.md`.

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
règles de vérification par pays, modèle tenant/scopes, IAM/IDOR, SLO/RPO/RTO, restore.

Statut final : `C2-BASELINE-ESTABLISHED — EMPLOYER-SEMANTICS-CLOSED / IMPLEMENTATION-AND-EVIDENCE-PENDING`.
