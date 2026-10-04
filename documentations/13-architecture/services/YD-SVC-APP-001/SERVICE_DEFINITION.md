# YD-SVC-APP-001 — Application Service

`domain: opportunites-recrutement` · `documentation: D2` · `status: candidate` · `implementation: not-started`

## Identifiant historique
Succède à `YD-SVC-REC-002`, conservé en `SUPERSEDED` pour traçabilité.

## Agrégats possédés
`Application`, `ApplicationStatusHistory`, `ApplicationSubmission`, `CandidateResponse`.

## Source autoritative
YD-SVC-APP-001 est l’unique source autoritative interne des candidatures et de leur historique d’état.

## Données consommées
`OpportunityRef` depuis OPP-001, références candidat depuis IDN/PRF, références employeur depuis EMP-001, consentement et règles de confidentialité depuis CNS-001.

## Frontières
Ne possède ni `Opportunity`, ni `UserProfile`, ni `Employer`. Talent & Recruitment consomme les candidatures sans en devenir propriétaire.

## Incohérences
Aucune incohérence D2 ouverte sur l’ownership. Les contrats et transitions d’état seront définis en D3.
