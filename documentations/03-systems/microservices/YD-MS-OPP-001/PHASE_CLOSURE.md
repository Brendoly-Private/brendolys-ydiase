# YD-MS-OPP-001 — Opportunity — Baseline C1

Statut : `DOCUMENTATION-BASELINE-C1 / OPPORTUNITY-SEMANTICS-CLOSED`

## Politique normative
Voir `OPPORTUNITY_LIFECYCLE_POLICY.md`.

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
policies par type, anti-fraude/modération, SLO retrait, IAM/tenant, BIA/RPO/RTO, restore et contrats.

Statut final : `C1-BASELINE-ESTABLISHED — OPPORTUNITY-SEMANTICS-CLOSED / IMPLEMENTATION-AND-EVIDENCE-PENDING`.
