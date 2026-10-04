# YD-SVC-AUD-001 — Audit & Trace Service

`domain: plateforme-gouvernance` · `phase: P1` · `documentation: D1` · `implementation: not-started`

## Mission
Conserver les traces fonctionnelles des actions sensibles et preuves nécessaires à l’audit.

## Frontière DDD
Ne remplace pas l’observabilité technique. Les traces sont protégées contre modification non autorisée.

## Dépendances
Identity & Access, services critiques.

## Verdict DDD
`KEEP-SEPARATE`. Responsabilité transverse et exigences de conservation propres.

## Activation
Dès le pilote pour les actions sensibles.