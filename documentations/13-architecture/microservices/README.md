# Microservices physiques YDIASE

Ce dossier documente les frontières physiques confirmées. Il complète `../services/`, qui reste le catalogue des services logiques DDD.

## Séparation documentaire

- `../services/` : service logique, responsabilité métier, agrégats, données possédées/consommées, règles DDD.
- `./` : frontière physique `YD-MS-*`, services logiques contenus, autonomie d’exploitation, contrats physiques, IAM, datastore, backup/restore, DNS, sécurité, observabilité, CI/CD, SLO et DR.
- `../platform-components/` : composants autonomes `YD-PLT-*`.
- `../AUTONOMY_PROFILE_REGISTER.md` : baseline spécifique des 51 frontières, utilisée pour créer/contrôler les profils individuels.

Une fiche physique ne remplace jamais une fiche de service logique. Une fusion de services logiques pointe vers une seule frontière physique.

## Cible actuelle

47 microservices métier confirmés. Le registre d’autonomie fixe pour chacun population IAM admissible, exposition, nature du backup, criticité candidate, données possédées, dépendances structurantes et mode dégradé. Les paramètres d’exploitation non justifiables avant capacity planning, analyse de criticité ou Contract Registry restent explicitement ouverts et bloquent le gate production.

## Profils individuels

Chaque frontière reçoit un `AUTONOMY_PROFILE.md`. Les profils critiques sont détaillés en priorité. Aucun profil ne doit recopier le standard sans spécialiser données, IAM, panne, backup, sécurité et dépendances du service.