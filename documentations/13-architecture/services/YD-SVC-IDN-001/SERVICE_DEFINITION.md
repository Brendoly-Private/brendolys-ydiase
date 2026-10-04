# YD-SVC-IDN-001 — Identity & Access Service

`domain: identite-profils` · `phase: P1` · `documentation: D1` · `implementation: not-started`

## Mission
Porter comptes, identités techniques, authentification, sessions et autorisations d’accès.

## Frontière DDD
Propriétaire candidat de `Account`, `CredentialBinding`, `Session` et identifiants techniques. Ne possède ni profil métier, ni consentements, ni compétences.

## Dépendances
Consent & Privacy, Audit & Trace, Country Configuration.

## Verdict DDD
`KEEP-SEPARATE`. Frontière de sécurité forte et cycle de vie propre.

## Activation
Avant tout compte utilisateur ou organisationnel.