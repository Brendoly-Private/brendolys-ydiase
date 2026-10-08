---
document_id: "YD-DOC-SYS-ARC-REV-003"
title: "Revue DDD cible — BRENDOLYS YDIASE"
document_type: "ddd-review"
document_role: "Évalue les services logiques candidats et consigne leur traitement DDD sans confondre service logique et déploiement physique."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "architecture"
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# Revue DDD cible — BRENDOLYS YDIASE

> **Rôle du document**
> Évalue les services logiques candidats et consigne leur traitement DDD sans confondre service logique et déploiement physique.
> **Usage développement :** support de décision, preuve ou traçabilité ; la cible canonique active reste autoritative.

## Objet

Cette revue évalue les 61 services logiques candidats de `SERVICE_MAP.md`. Elle ne transforme pas automatiquement chaque ligne en microservice physique. Elle fixe une première décision DDD à réexaminer avec les exigences et les données.

## Résultat global

- `KEEP-SEPARATE` : frontière forte, candidat sérieux à un microservice autonome.
- `KEEP-LOGICAL` : bounded context utile, déploiement autonome non encore justifié.
- `KEEP-PRODUCT-BOUNDARY` : contrat produit distinct, moteur interne potentiellement partagé.
- `MERGE-CANDIDATE` : conserver la responsabilité documentaire, mais éviter un déploiement séparé au début.
- `KEEP-AS-BFF-CANDIDATE` ou `KEEP-AS-ADMIN-PLANE` : couche d’expérience ou d’orchestration, pas nécessairement microservice métier.
- `KEEP-FUTURE` : frontière conservée dans la cible, activation conditionnée à un besoin mesuré.

## Décisions par service

| Service | Décision DDD |
|---|---|
| IDN-001 | KEEP-SEPARATE |
| PRF-001 | KEEP-SEPARATE |
| PRF-002 | KEEP-SEPARATE — confirmé par `ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY.md` |
| EDU-001 | KEEP-SEPARATE |
| EDU-002 | KEEP-SEPARATE |
| EDU-003 | KEEP-SEPARATE |
| EDU-004 | KEEP-SEPARATE |
| SKL-001 | KEEP-SEPARATE |
| SKL-002 | KEEP-SEPARATE |
| CAR-001 | KEEP-SEPARATE |
| CAR-002 | KEEP-SEPARATE — reconciled to physical boundary |
| CAR-003 | KEEP-LOGICAL |
| ASM-001 | KEEP-SEPARATE |
| ORI-001 | KEEP-SEPARATE |
| REC-001 | KEEP-SEPARATE |
| ORI-002 | MERGE-CANDIDATE → ORI-001 |
| CAR-004 | MERGE-CANDIDATE → CAR-002 |
| SRH-001 | KEEP-SEPARATE |
| LAB-001 | KEEP-SEPARATE |
| LAB-002 | KEEP-SEPARATE |
| LAB-003 | KEEP-SEPARATE-FUTURE |
| OPP-001 | KEEP-SEPARATE |
| OPP-002 | KEEP-SEPARATE — reconciled to physical boundary |
| REC-002 | SUPERSEDED → APP-001 |
| EMP-001 | KEEP-SEPARATE |
| EMP-002 | KEEP-SEPARATE |
| CNT-001 | KEEP-SEPARATE |
| CNT-002 | KEEP-SEPARATE |
| COM-001 | KEEP-SEPARATE |
| LRN-001 | KEEP-SEPARATE — reconciled to physical boundary |
| RSH-001 | MERGE-CANDIDATE → REC-001 |
| NTF-001 | KEEP-SEPARATE |
| PRT-001 | KEEP-SEPARATE |
| AMB-001 | KEEP-SEPARATE |
| INS-001 | KEEP-SEPARATE |
| EMP-003 | KEEP-AS-BFF-CANDIDATE |
| DAT-001 | KEEP-SEPARATE |
| DAT-002 | KEEP-SEPARATE |
| DAT-003 | KEEP-SEPARATE |
| DAT-004 | KEEP-SEPARATE |
| DAT-005 | KEEP-SEPARATE |
| KNW-001 | KEEP-SEPARATE |
| ANL-001 | KEEP-SEPARATE |
| ANL-002 | KEEP-PRODUCT-BOUNDARY |
| ANL-003 | KEEP-PRODUCT-BOUNDARY |
| AI-001 | KEEP-SEPARATE |
| AI-002 | KEEP-SEPARATE — reconciled to physical boundary |
| AI-003 | KEEP-SEPARATE — reconciled to physical boundary |
| AI-004 | KEEP-FUTURE |
| BIL-001 | KEEP-SEPARATE |
| BIL-002 | KEEP-SEPARATE |
| MKT-001 | KEEP-SEPARATE |
| SPN-001 | KEEP-SEPARATE |
| API-001 | KEEP-SEPARATE |
| DPR-001 | KEEP-SEPARATE |
| INT-001 | KEEP-PRODUCT-BOUNDARY |
| ADM-001 | KEEP-AS-ADMIN-PLANE |
| MOD-001 | KEEP-SEPARATE |
| AUD-001 | KEEP-SEPARATE |
| CFG-001 | KEEP-SEPARATE |
| CNS-001 | KEEP-SEPARATE |

## Correction PRF

La décision historique `PRF-002 = REVIEW-SPLIT` est close. Le domaine 02 a confirmé des responsabilités sémantiques distinctes et l'ADR de frontière physique a retenu deux microservices autonomes. L'ancienne validation de fusion est superseded.

## Lecture du nombre de microservices

Cette revue reste une revue des services logiques. Le comptage physique canonique appartient à `MICROSERVICE_BOUNDARY_REVIEW.md`. Après la décision PRF, la cible physique compte 48 microservices métier et 4 composants de plateforme autonomes, soit 52 frontières autonomes, hors BRENDOLYS Identity.

## Règles de la prochaine passe

1. Chaque service passe de D1 à D2 avec données possédées et consommées.
2. Toute propriété concurrente d’un même agrégat bloque la validation.
3. Toute dépendance circulaire exige correction ou ADR.
4. Les services `MERGE-CANDIDATE` restent documentés mais ne reçoivent pas un déploiement autonome sans justification.
5. Les services BFF et plans d’administration n’entrent pas automatiquement dans le comptage des microservices métier.
6. Les produits Analytics et Intelligence peuvent partager des moteurs internes tout en gardant leurs contrats et droits propres.
7. Le pilote Burkina active uniquement le sous-ensemble nécessaire sans supprimer les frontières de la cible panafricaine.

## Réconciliation transversale 2026-10

La revue transversale des 48 microservices confirme que `MICROSERVICE_BOUNDARY_REVIEW.md` est canonique pour la frontière physique. Les anciennes décisions exploratoires DDD ont été réconciliées pour CAR-002, OPP-002, LRN-001, AI-002, AI-003 et REC-002.

Deux points restent volontairement non tranchés ici :
- INS-001 : conflit entre LOGICAL_ONLY/BFF sans agrégat et ownership de workflow durable ; ADR requis avant implémentation.
- AI-004 : frontière DEFERRED ; les cartes qui la montrent dans le flux IA décrivent une topologie future et doivent être séparées de la topologie active avant implémentation.


## Extension Entrepreneurship — réconciliation

La revue dédiée `ENTREPRENEURSHIP_DDD_REVIEW.md` ajoute six frontières logiques à la cible : ENT-001 à ENT-006. Verdict : KEEP-SEPARATE pour les six frontières, avec ownership et dépendances réconciliés.

Le comptage historique de 52 frontières autonomes décrit la baseline antérieure à l'extension Entrepreneurship. Il ne doit plus être interprété comme le nombre final de la Target Architecture. Le nouveau comptage physique canonique devra être recalculé après intégration des six frontières dans `MICROSERVICE_BOUNDARY_REVIEW.md` et validation des ADR nécessaires.
