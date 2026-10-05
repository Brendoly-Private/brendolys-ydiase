# YD-MS-REC-001 — Recommendation — Baseline C1

Statut : `DOCUMENTATION-BASELINE-C1 / RANKING-SEMANTICS-DEFINED`
Nature : `MIXED`
Criticité : `C1`

## Autorité
REC-001 possède RecommendationRun, RecommendationSet, RecommendationItem, RecommendationExplanation et RecommendationEvidenceSnapshot. Il ne possède aucune donnée source utilisée par le calcul.

## Politique normative
Voir `RECOMMENDATION_RANKING_POLICY.md`, `SPONSORED_NON_INFLUENCE_TEST_POLICY.md` et `FAIRNESS_EVALUATION_POLICY.md`.

La politique ferme : eligibility, scoring organique, ranking, pondérations versionnées, evidence snapshot, abstention, explicabilité, incertitude, principes de biais/équité, correction/reproductibilité et séparation stricte entre organique et sponsoring.

## Invariant commercial
SPN-001 ne peut jamais modifier score, rang, pondération, exclusion ou explication organique. Un placement sponsorisé est un objet/canal séparé, étiqueté et mesuré séparément.

## Invariants C1
- finalité et minimisation ;
- contrôle objet/horizontal ;
- historique non destructif ;
- fail-closed lorsque Privacy requise n'est pas vérifiable ;
- projections locales ne deviennent jamais autorités ;
- backup/restore propre au service.

## Avant ACTIVE
- coefficients/seuils validés ;
- seuils numériques d'équité et preuves sur données représentatives ;
- tests de biais et dérive ;
- exécution préproduction de la suite anti-influence SPN avec preuves ;
- règles mineurs ;
- Privacy/rétention ;
- IAM/IDOR ;
- BIA, RPO/RTO/SLO et restore ;
- contrats/runtime/observabilité.

## RSH-001
Le module Research reste logique. Toute autorité académique durable déclenche la revue d'extraction prévue.

Statut final : `C1-BASELINE-ESTABLISHED — RANKING-FAIRNESS-SPONSOR-ISOLATION-DEFINED / PREPROD-EVIDENCE-PENDING`.
