# YD-SVC-ASM-001 — Assessment Service

`domain: orientation-recommandation` · `phase: P2` · `documentation: D1` · `implementation: not-started`

## Mission
Administrer évaluations, réponses, scores et versions d’instruments autorisés.

## Frontière DDD
Propriétaire candidat de `Assessment`, `AssessmentVersion`, `ResponseSet` et `Score`. Ne produit pas seul la décision d’orientation.

## Dépendances
Profile, Consent & Privacy, Audit & Trace.

## Verdict DDD
`KEEP-SEPARATE`. Versionnement, sensibilité et reproductibilité exigent une frontière dédiée.

## Activation
Après validation méthodologique, sécurité et règles applicables aux mineurs.