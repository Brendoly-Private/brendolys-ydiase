# YD-SVC-PRF-001 — Profile Service

`domain: identite-profils` · `phase: P1` · `documentation: D1` · `implementation: not-started` · `activation: inactive`

## Mission
Porter le profil courant, les préférences, objectifs et contraintes déclarées d’une personne.

## Frontière DDD
Propriétaire candidat de `UserProfile`, `Preference` et `Goal`. Ne possède ni identité d’accès, ni historique académique détaillé, ni compétences validées.

## Dépendances
Identity & Access, Consent & Privacy, Country Configuration.

## Verdict DDD
`KEEP-SEPARATE`. Frontière métier stable entre identité technique et profil métier.

## Activation
Après règles de consentement, modèle de profil et droits d’accès validés.