# Logical-to-Physical Boundary Register — BRENDOLYS YDIASE

Statut : `R1-CANONICAL-NAVIGATION-BASELINE`

## 1. Rôle

Ce registre fournit la navigation canonique entre :
- `YD-SVC-*` : responsabilité/service logique cible ;
- `YD-MS-*` : frontière physique métier ;
- `YD-PLT-*` : frontière plateforme ;
- capacités `LOGICAL_ONLY` / BFF ;
- plateformes externes ;
- identifiants superseded ;
- frontières deferred.

Il ne remplace ni `SERVICE_MAP.md` ni `MICROSERVICE_BOUNDARY_REVIEW.md`. Il matérialise leur relation pour les humains et les IA.

## 2. Relations non 1:1

| Service logique | Statut physique | Destination | Règle |
|---|---|---|---|
| YD-SVC-IDN-001 | EXTERNAL_PLATFORM | BRENDOLYS Identity | IAM hors YDIASE |
| YD-SVC-CAR-003 | MERGED | YD-MS-CAR-002 | responsabilité Career Transition conservée comme partie de Career Path & Transition |
| YD-SVC-ORI-002 | MERGED | YD-MS-ORI-001 | Decision Support intégré à Orientation |
| YD-SVC-RSH-001 | LOGICAL_ONLY | YD-MS-REC-001 | module logique, aucune autorité physique propre |
| YD-SVC-INS-001 | LOGICAL_ONLY | Edge/BFF institution | façade ; EDU reste autoritatif |
| YD-SVC-EMP-003 | LOGICAL_ONLY | Edge/BFF employeur | façade ; EMP/OPP/APP restent owners |
| YD-SVC-ADM-001 | LOGICAL_ONLY | Admin plane | commandes vers owners ; aucune DB métier |
| YD-SVC-REC-002 | SUPERSEDED | YD-SVC-APP-001 / YD-MS-APP-001 | interdit pour nouvelle implémentation |
| YD-SVC-CAR-004 | DEFERRED | capacité initiale CAR-002 | extraction uniquement par ADR |
| YD-SVC-LAB-003 | DEFERRED | LAB-002/Analytics | extraction uniquement par ADR |
| YD-SVC-AI-001 | PLATFORM_COMPONENT | YD-PLT-AI-001 | AI Gateway transverse |
| YD-SVC-MLP-001 | PLATFORM_COMPONENT | YD-PLT-MLP-001 | model lifecycle/registry |
| YD-SVC-API-001 | PLATFORM_COMPONENT | YD-PLT-API-001 | external API management |
| YD-SVC-AUD-001 | PLATFORM_COMPONENT | YD-PLT-AUD-001 | audit/trace append-only |
| YD-SVC-AI-004 | DEFERRED-PLATFORM | YD-PLT-AI-004 candidate | non compté avant ADR |

## 3. Relations 1:1 confirmées

Sauf exceptions de la section 2, les services logiques ci-dessous se matérialisent dans la frontière de même suffixe :

- PRF-001 → YD-MS-PRF-001
- PRF-002 → YD-MS-PRF-002
- EDU-001..004 → YD-MS-EDU-001..004
- SKL-001..002 → YD-MS-SKL-001..002
- CAR-001..002 → YD-MS-CAR-001..002
- ASM-001 → YD-MS-ASM-001
- ORI-001 → YD-MS-ORI-001
- REC-001 → YD-MS-REC-001
- SRH-001 → YD-MS-SRH-001
- LAB-001..002 → YD-MS-LAB-001..002
- OPP-001..002 → YD-MS-OPP-001..002
- APP-001 → YD-MS-APP-001
- EMP-001..002 → YD-MS-EMP-001..002
- CNT-001..002 → YD-MS-CNT-001..002
- COM-001 → YD-MS-COM-001
- LRN-001 → YD-MS-LRN-001
- NTF-001 → YD-MS-NTF-001
- PRT-001 → YD-MS-PRT-001
- AMB-001 → YD-MS-AMB-001
- DAT-001..005 → YD-MS-DAT-001..005
- KNW-001 → YD-MS-KNW-001
- ANL-001..003 → YD-MS-ANL-001..003
- AI-002..003 → YD-MS-AI-002..003
- BIL-001..002 → YD-MS-BIL-001..002
- MKT-001 → YD-MS-MKT-001
- SPN-001 → YD-MS-SPN-001
- DPR-001 → YD-MS-DPR-001
- INT-001 → YD-MS-INT-001
- MOD-001 → YD-MS-MOD-001
- CFG-001 → YD-MS-CFG-001
- CNS-001 → YD-MS-CNS-001

## 4. Comptage

Baseline physique confirmée :
- 48 `YD-MS-*` métier ;
- 4 `YD-PLT-*` plateforme ;
- 52 frontières autonomes au total ;
- BRENDOLYS Identity externe ;
- CAR-004, LAB-003 et AI-004 deferred.

Les surfaces Web/mobile/portails/BFF ne sont pas ajoutées au comptage des microservices métier sans décision explicite.

## 5. Consigne documentaire

Toute fiche `YD-SVC-*` devra à terme référencer cette relation.
Toute fiche `YD-MS-*` devra lister les services logiques qu'elle matérialise.

Une IA ne doit jamais déduire `YD-SVC-X = YD-MS-X` par convention de nom lorsque la relation n'est pas présente dans ce registre.

## 6. Sources de décision

- `03-systems/architecture/target/SERVICE_MAP.md` : catalogue logique cible ;
- `03-systems/architecture/reviews/MICROSERVICE_BOUNDARY_REVIEW.md` : décisions de frontière physique ;
- `03-systems/architecture/registers/AUTONOMY_PROFILE_REGISTER.md` : index des frontières autonomes.

En cas de contradiction, ouvrir `CONTRADICTION-OPEN` et vérifier ADR/supersession ; ne pas résoudre par heuristique de nom.
