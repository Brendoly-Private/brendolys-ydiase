# YD-SVC-EMP-002 — Talent & Recruitment Service

`domain: opportunites-recrutement` · `phase: P5` · `documentation: D1` · `implementation: not-started`

## Mission
Gérer viviers, recherches de talents et campagnes de recrutement côté organisation.

## Frontière DDD
Propriétaire candidat de `RecruitmentCampaign` et `TalentPoolDefinition`. Ne possède pas les profils individuels.

## Dépendances
Employer, Application, Opportunity Matching, Consent & Privacy.

## Verdict DDD
`KEEP-SEPARATE`. Workflow B2B et règles d’accès spécifiques.

## Activation
Après politique d’accès recruteur et finalités de traitement validées.