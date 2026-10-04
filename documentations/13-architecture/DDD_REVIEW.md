# Revue DDD cible — BRENDOLYS YDIASE

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
| PRF-002 | REVIEW-SPLIT |
| EDU-001 | KEEP-SEPARATE |
| EDU-002 | KEEP-SEPARATE |
| EDU-003 | KEEP-SEPARATE |
| EDU-004 | KEEP-SEPARATE |
| SKL-001 | KEEP-SEPARATE |
| SKL-002 | KEEP-SEPARATE |
| CAR-001 | KEEP-SEPARATE |
| CAR-002 | KEEP-LOGICAL |
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
| OPP-002 | KEEP-LOGICAL |
| REC-002 | KEEP-SEPARATE |
| EMP-001 | KEEP-SEPARATE |
| EMP-002 | KEEP-SEPARATE |
| CNT-001 | KEEP-SEPARATE |
| CNT-002 | KEEP-SEPARATE |
| COM-001 | KEEP-SEPARATE |
| LRN-001 | KEEP-LOGICAL |
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
| AI-002 | KEEP-LOGICAL |
| AI-003 | MERGE-CANDIDATE → AI-001 au pilote |
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

## Lecture du nombre de microservices

La revue ne valide pas 61 microservices physiques. À ce stade, environ 45 à 50 frontières ont un argument sérieux pour une autonomie à grande échelle. Les autres restent des contextes logiques, produits, BFF ou candidats à fusion. Ce nombre doit encore passer par la revue des agrégats, dépendances, sécurité, charge, équipes et contrats.

## Règles de la prochaine passe

1. Chaque service passe de D1 à D2 avec données possédées et consommées.
2. Toute propriété concurrente d’un même agrégat bloque la validation.
3. Toute dépendance circulaire exige correction ou ADR.
4. Les services `MERGE-CANDIDATE` restent documentés mais ne reçoivent pas un déploiement autonome sans justification.
5. Les services BFF et plans d’administration n’entrent pas automatiquement dans le comptage des microservices métier.
6. Les produits Analytics et Intelligence peuvent partager des moteurs internes tout en gardant leurs contrats et droits propres.
7. Le pilote Burkina active uniquement le sous-ensemble nécessaire sans supprimer les frontières de la cible panafricaine.