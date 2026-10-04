# YD-SVC-ORI-001 — Orientation Service

`domain: orientation-recommandation` · `phase: P2` · `documentation: D1` · `implementation: not-started`

## Mission
Orchestrer un dossier d’orientation éducative ou professionnelle et conserver ses décisions explicables.

## Frontière DDD
Propriétaire candidat de `OrientationCase` et `OrientationDecision`. Consomme profils, évaluations, Education, Careers et Recommendation.

## Verdict DDD
`KEEP-SEPARATE`. C’est le contexte métier central d’orientation, distinct du moteur de classement.

## Activation
Après critères d’orientation, explication et audit validés.