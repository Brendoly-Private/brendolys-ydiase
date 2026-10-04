# Microservices physiques YDIASE

Ce dossier documente les frontières physiques confirmées. Il complète `../services/`, qui reste le catalogue des services logiques DDD.

## Séparation documentaire

- `../services/` : service logique, responsabilité métier, agrégats, données possédées/consommées, règles DDD.
- `./` : frontière physique `YD-MS-*`, services logiques contenus, autonomie d’exploitation, contrats physiques, IAM, datastore, backup/restore, DNS, sécurité, observabilité, CI/CD, SLO et DR.
- `../platform-components/` : composants autonomes `YD-PLT-*`.

Une fiche physique ne remplace jamais une fiche de service logique. Une fusion de services logiques pointe vers une seule frontière physique.

## Cible actuelle

47 microservices métier confirmés. Les 47 frontières possèdent désormais un `AUTONOMY_PROFILE.md` individuel. Les 4 composants de plateforme possèdent également leur profil individuel. `AUTONOMY_PROFILE_REGISTER.md` reste la vue consolidée et le contrôle de cohérence.

Les valeurs chiffrées RPO/RTO/SLO, moteurs de stockage, protocoles, DNS finaux et quotas restent à fermer par analyse de criticité et ADR avant production. Les profils ne doivent pas inventer ces valeurs.
