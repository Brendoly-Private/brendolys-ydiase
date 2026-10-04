# Microservices physiques YDIASE

Ce dossier documente les frontières physiques confirmées. Il complète `../services/`, qui reste le catalogue des services logiques DDD.

## Séparation documentaire

- `../services/` : service logique, responsabilité métier, agrégats, données possédées/consommées, règles DDD.
- `./` : frontière physique `YD-MS-*`, services logiques contenus, autonomie d’exploitation, contrats physiques, IAM, datastore, backup/restore, DNS, sécurité, observabilité, CI/CD, SLO et DR.
- `../platform-components/` : composants autonomes `YD-PLT-*`.

Une fiche physique ne remplace jamais une fiche de service logique. Une fusion de services logiques pointe vers une seule frontière physique.

## Cible actuelle

47 microservices métier confirmés. Les profils individuels seront créés à partir du template d’autonomie après validation du standard et du registre physique.
