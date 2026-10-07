# YD-MS-ENT-006 — Venture Progression

Statut : autonomy-profile-target
Nature : AUTH
Criticité candidate : C1

## Ownership
VenturePlan, Milestone, Experiment, Assumption, ValidationResult, ProgressSnapshot.

## Dépendances
ENT-001/SKL/EDU/LRN/ORI. Aucun accès DB externe. Les échanges interservices passent par contrats, événements ou projections gouvernées.

## Frontière
Ce service ne réécrit aucune autorité PRF, SKL, LAB, PRT, ORI, REC, EMP ou OPP. Les projections Data/Search/Knowledge/Analytics/IA ne deviennent pas autorité de ses agrégats.

## Recovery
Backup autoritatif et restauration indépendante requis. La restauration ne dépend pas d'un consommateur, de Search, Analytics, Knowledge ou IA.

## Privacy et sécurité
CNS/IAM sont appliqués selon finalité. Les accès sensibles sont auditables. Les données personnelles consommées sont minimisées. Aucune décision IA ne contourne consentement, visibilité ou ownership.

## Hyperscale / Capacity
partition par VentureId; historique à forte croissance; projections lecture; progression indépendante de REC/AI. Un Capacity Profile chiffré est obligatoire avant MICROSERVICE-READY-FOR-DEVELOPMENT et doit contribuer à la cible agrégée 5–15 M utilisateurs simultanément actifs.

## Dégradation
Une panne d'un moteur dérivé ou d'IA ne doit pas corrompre l'autorité métier. Les dépendances indisponibles utilisent fail-closed lorsque sécurité/privacy/éligibilité l'exigent, sinon dernier snapshot suffisamment frais ou traitement asynchrone selon contrat.

## Autonomie technique
Datastore privé si état persistant, migrations, secrets, workload identity, quotas, observabilité, pipeline, rollback et responsabilité opérationnelle propres. Aucun datastore partagé entre ENT.

## Gates
Capacity Profile chiffré, contrats physiques, IAM physique, SLO/RPO/RTO, rétention, observabilité, restore/rebuild tests, sécurité/privacy et tests de charge restent à fermer par conception détaillée et preuves.
