# YD-SVC-REC-002 — Application Service

`domain: opportunites-recrutement` · `phase: P4` · `documentation: D1` · `implementation: not-started`

## Mission
Porter candidatures, statuts, historique et interactions de suivi autorisées.

## Frontière DDD
Propriétaire candidat de `Application`. Ne possède ni l’opportunité ni le profil candidat.

## Dépendances
Opportunity, Profile, Employer, Notification, Consent & Privacy.

## Verdict DDD
`KEEP-SEPARATE`. Données personnelles et workflow transactionnel distincts.

## Activation
Après règles de conservation, accès candidat/employeur et audit validés.