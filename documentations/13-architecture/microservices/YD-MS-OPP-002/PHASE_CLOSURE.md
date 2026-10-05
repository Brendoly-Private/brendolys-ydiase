# YD-MS-OPP-002 — Opportunity — Baseline C2

Statut : `DOCUMENTATION-BASELINE-C2 / OPPORTUNITY-MATCHING-SEMANTICS-CLOSED`

## Politique normative
Voir `OPPORTUNITY_MATCHING_POLICY.md`.

## Invariants
- source externe, représentation YDIASE, matching, recommandation et candidature restent distincts ;
- OPP-001 seul possède l'état autoritatif de l'Opportunity ;
- OPP-002 possède uniquement le résultat de matching ;
- APP-001 seul possède Application et ses transitions ;
- provenance, versions, validité et fraîcheur restent visibles ;
- UNKNOWN/NOT-ASSESSABLE ne deviennent pas validation positive ;
- sponsoring/partenariat ne contourne ni publication ni score organique ;
- correction et retrait sont non destructifs et propagés.

## Avant ACTIVE
coefficients/seuils, métriques d'équité, règles par type, IAM/IDOR, rétention runs, BIA/RPO/RTO, restore et contrats.

Statut final : `C2-BASELINE-ESTABLISHED — OPPORTUNITY-MATCHING-SEMANTICS-CLOSED / IMPLEMENTATION-AND-EVIDENCE-PENDING`.
