# YD-SVC-CFG-001 — Country Configuration Service

`domain: plateforme-gouvernance` · `phase: P1` · `documentation: D1` · `implementation: not-started`

## Mission
Porter paramètres pays, territoires, langues, monnaies et références vers les cadres locaux validés.

## Frontière DDD
Ne contient pas toute la réglementation. Fournit la configuration gouvernée nécessaire aux domaines.

## Dépendances
Country Frameworks, Reference & Taxonomy, Audit & Trace.

## Verdict DDD
`KEEP-SEPARATE`. Condition de l’expansion multi-pays sans coder le Burkina comme norme générale.

## Activation
Avec le premier pays.