# YD-SVC-CNS-001 — Consent & Privacy Service

`domain: plateforme-gouvernance` · `phase: P1` · `documentation: D1` · `implementation: not-started`

## Mission
Porter consentements, finalités, préférences de confidentialité, restrictions et demandes liées aux droits applicables.

## Frontière DDD
Ne remplace pas Identity. Produit les décisions et états de confidentialité consommés par les autres services.

## Dépendances
Identity & Access, Country Configuration, Audit & Trace.

## Verdict DDD
`KEEP-SEPARATE`. Données personnelles et multi-pays imposent une frontière forte.

## Activation
Avant traitement de données personnelles du pilote.