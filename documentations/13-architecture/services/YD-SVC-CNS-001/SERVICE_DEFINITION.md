# YD-SVC-CNS-001 — Consent & Privacy Service

`domain: plateforme-gouvernance` · `documentation: D2` · `implementation: not-started`

## Agrégats possédés
`ProcessingPurpose`, `ProcessingPurposeVersion`, `ConsentRecord`, `PurposeGrant`, `PrivacyPreference`, `DataSubjectRequest`, `RetentionInstruction`.

## Source autoritative
YD-SVC-CNS-001 est autoritatif pour le registre opérationnel des finalités de traitement, les consentements, autorisations par finalité, préférences de confidentialité, demandes des personnes et instructions de rétention.

## Données consommées
IdentityRef depuis IDN-001, country/legal configuration depuis CFG-001, décisions de conformité approuvées, catégories de données déclarées par les domaines, audit depuis AUD-001.

## Règle de finalité
Chaque traitement de données personnelles doit référencer un `ProcessingPurpose` versionné et actif. Les services métier ne créent pas librement leurs propres finalités. Ils demandent ou référencent une finalité gouvernée par CNS-001.

## Frontière juridique
CNS-001 porte le registre opérationnel et les états applicatifs. Les textes juridiques externes et décisions de conformité restent attribués à leurs sources et documents de gouvernance.

## Incohérences
Ownership du Processing Purpose Registry résolu en D2. Les contrats de propagation des changements de finalité et de rétention seront définis en D3.
