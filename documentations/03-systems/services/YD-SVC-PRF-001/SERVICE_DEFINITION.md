# YD-SVC-PRF-001 — Profile Service

`domain: identite-profils` · `phase: P1` · `documentation: D2` · `implementation: not-started` · `activation: inactive`

## Mission
Porter le profil courant, les préférences, objectifs et contraintes déclarées d’une personne.

## Agrégats possédés
`UserProfile`, `Preference`, `Goal`, `DeclaredConstraint`.

## Source autoritative
YD-SVC-PRF-001.

## Données consommées
IdentityRef (IDN-001), consent/privacy (CNS-001), country configuration (CFG-001).

## Frontière DDD
Ne possède ni identité d’accès, ni historique académique détaillé, ni compétences individuelles.

## Incohérences
Aucune propriété concurrente détectée. Toute préférence de confidentialité doit rester CNS-001.
