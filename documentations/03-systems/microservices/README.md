---
document_id: "YD-DOC-SYS-MS-000"
title: "Microservices physiques YDIASE"
document_type: "microservice-navigation"
document_role: "Définit la séparation documentaire entre services logiques, frontières physiques et composants plateforme et oriente le corpus microservices."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "view"
canonical: false
development_usage: "informational"
metadata_adopted_at: "2026-10-07"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "systems"
  - "microservice"
---

# Microservices physiques YDIASE

> **Rôle du document**
> Définit la séparation documentaire entre services logiques, frontières physiques et composants plateforme et oriente le corpus microservices.
> **Usage développement :** document de navigation ; il ne crée pas de vérité normative.

Ce dossier documente les frontières physiques confirmées. Il complète `../services/`, qui reste le catalogue des services logiques DDD.

## Séparation documentaire

- `../services/` : service logique, responsabilité métier, agrégats, données possédées/consommées, règles DDD.
- `./` : frontière physique `YD-MS-*`, services logiques contenus, autonomie d’exploitation, contrats physiques, IAM, datastore, backup/restore, DNS, sécurité, observabilité, CI/CD, SLO et DR.
- `../platform-components/` : composants autonomes `YD-PLT-*`.

Une fiche physique ne remplace jamais une fiche de service logique. Une fusion de services logiques pointe vers une seule frontière physique.

## Cible actuelle

48 microservices métier confirmés. Les 48 frontières possèdent un `AUTONOMY_PROFILE.md` individuel, dont `YD-MS-PRF-002` créé après l'ADR de séparation Profile/History. Les 4 composants de plateforme possèdent également leur profil individuel. La cible autonome actuelle compte donc 52 frontières. `AUTONOMY_PROFILE_REGISTER.md` reste la vue consolidée et le contrôle de cohérence.

Les valeurs chiffrées RPO/RTO/SLO, moteurs de stockage, protocoles, DNS finaux et quotas restent à fermer par analyse de criticité et ADR avant production. Les profils ne doivent pas inventer ces valeurs.