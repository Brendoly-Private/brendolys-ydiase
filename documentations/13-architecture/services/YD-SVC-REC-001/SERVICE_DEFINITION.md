# YD-SVC-REC-001 — Recommendation Service

`domain: orientation-recommandation` · `phase: P2` · `documentation: D1` · `implementation: not-started`

## Mission
Calculer des recommandations classées et explicables à partir de données autorisées.

## Frontière DDD
Ne possède aucune source métier. Possède seulement les résultats de recommandation nécessaires à la traçabilité et à l’évaluation.

## Dépendances
Profile, Education, Skills, Careers, Assessment selon le cas.

## Verdict DDD
`KEEP-SEPARATE`. Évaluation, classement et évolution algorithmique ont un cycle propre.

## Activation
Après métriques de qualité, explication et biais validées.