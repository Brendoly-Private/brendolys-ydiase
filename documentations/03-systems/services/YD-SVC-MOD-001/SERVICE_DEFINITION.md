# YD-SVC-MOD-001 — Moderation Service

`domain: plateforme-gouvernance` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`ModerationPolicy`, `ModerationPolicyVersion`, `ModerationCase`, `ModerationDecision`, `PolicyViolation`, `Appeal`.

## Source autoritative
YD-SVC-MOD-001 est autoritatif pour la politique opérationnelle de modération, ses versions, les dossiers, décisions, violations et recours.

## Données consommées
Content/community/marketplace/sponsored objects, identity refs, country/legal constraints depuis CFG-001 et décisions de conformité applicables, audit depuis AUD-001.

## Frontière de gouvernance
La gouvernance documentaire approuve et trace les décisions de politique. CFG-001 fournit les paramètres pays. MOD-001 traduit les règles approuvées en politique de modération versionnée et exécutable. Aucun autre service ne maintient une copie normative concurrente.

## Incohérences
Ownership de `ModerationPolicy` résolu en D2. Les workflows de recours et contrats avec les domaines modérés seront définis en D3.
