# YD-MS-CAR-002 — Career Path & Transition — Baseline

Statut : `DOCUMENTATION-BASELINE / IMPLEMENTATION-GATES-OPEN`
Nature : `MIXED`
Criticité : `C2`

## Frontière
YD-MS-CAR-002 héberge actuellement deux responsabilités logiques :
- CAR-002 Career Path ;
- CAR-003 Career Transition.

La fusion physique reste valide tant que dataset, modèle, SLO, charge, équipe, Privacy/rétention et cycle de déploiement ne divergent pas durablement.

## Autorité
Le microservice possède les trajectoires et transitions persistées qu'il produit. Il ne possède aucune des vérités source utilisées pour les calculer.

## Invariants
- chaque résultat conserve les versions/snapshots minimaux de ses entrées ;
- hypothèses et explications accompagnent le résultat ;
- résultat partiel ou indisponibilité sont explicitement signalés ;
- aucune donnée manquante n'est inventée ;
- une transition suggérée n'est ni une garantie d'emploi ni un fait futur ;
- CAR-001, PRF, SKL, EDU/LRN et LAB restent owners de leurs données ;
- les résultats personnalisés ne réécrivent pas les sources.

## Extraction CAR-003
ADR obligatoire si Transition acquiert durablement son propre dataset/stockage, modèle, SLO, charge, équipe/ownership, politique Privacy/rétention ou cycle de déploiement.

## Récupération
Les trajectoires/transitions persistées sont restaurées depuis la chaîne propre de YD-MS-CAR-002. Les services sources ne servent pas de backup. Réconciliation des références après restore.

## Gates avant implémentation/ACTIVE
- modèle de gap et de transition ;
- règles d'incertitude et explicabilité ;
- Privacy/finalités/rétention des snapshots ;
- contrats physiques ;
- IAM ;
- RPO/RTO/SLO ;
- restore test.

Statut : `BASELINE-ESTABLISHED — TRANSITION/EXPLAINABILITY GATES OPEN`.
