# YD-SVC-NTF-001 — Notification Service

`domain: plateforme` · `phase: P2` · `documentation: D1` · `implementation: not-started`

## Mission
Distribuer des notifications selon préférences, canaux et règles de priorité.

## Frontière DDD
Ne décide pas des événements métier à produire. Consomme des demandes de notification et maintient leur état de livraison.

## Dépendances
Identity, Profile, Consent & Privacy.

## Verdict DDD
`KEEP-SEPARATE`. Intégrations externes et charge asynchrone spécifiques.

## Activation
Après politique de canaux et consentement validés.