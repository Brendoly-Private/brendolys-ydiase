# YD-SVC-EMP-001 — Employer Service

`domain: opportunites-recrutement` · `phase: P4` · `documentation: D1` · `implementation: not-started`

## Mission
Référencer les organisations employeuses et leurs informations validées.

## Frontière DDD
Propriétaire candidat de `Employer`. Ne possède ni opportunités ni campagnes de recrutement.

## Dépendances
Partner, Country Configuration, Data Provenance.

## Verdict DDD
`KEEP-SEPARATE`. Référentiel organisationnel réutilisé par plusieurs contextes.

## Activation
Après règles de validation des organisations.