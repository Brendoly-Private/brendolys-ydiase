---
document_id: "YD-DOC-META-K5-VERIFICATION-GATE"
title: "YDIASE Knowledge Gate — K5 Vérifié"
document_type: "governance-reference"
document_role: "Documente une référence de maturité, de gate ou d’ontologie utilisée pour qualifier le corpus YDIASE."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "meta"
created_at: "2026-10-06"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YDIASE Knowledge Gate — K5 Vérifié

> **Rôle du document**
> Documente une référence de maturité, de gate ou d’ontologie utilisée pour qualifier le corpus YDIASE.
> **Usage développement :** référence de support pour la gouvernance et la qualification documentaire.

Statut : `BASELINE / PILOT-KNW`

## Objet

K5 signifie qu'une entité K4 possède des **preuves reproductibles** montrant que ses contrats, contrôles et exigences applicables ont été effectivement vérifiés.

K5 ne signifie ni production ni déploiement. Un composant non activé peut atteindre K5 avec des vérifications hors production lorsque celles-ci sont réellement exécutables et leurs preuves conservées.

## Critères obligatoires

1. `automatedValidation` — validations automatisées applicables exécutées avec résultat traçable.
2. `contractTests` — contrats critiques testés, y compris compatibilité, versions et comportements d'erreur applicables.
3. `securityVerification` — contrôles de sécurité applicables vérifiés, pas seulement décrits.
4. `restoreOrResilienceTestWhenApplicable` — restauration, reconstruction ou résilience effectivement testée selon la nature AUTH/DERIVED/MIXED.
5. `evidenceLinks` — chaque PASS renvoie vers une preuve reproductible et identifiable.
6. `unresolvedCriticalGapsEqualsZero` — aucun gap critique applicable ne reste UNKNOWN, PARTIAL ou NOT-TESTED.

## Règles de preuve

- Une baseline K4 n'est pas une preuve K5.
- Une procédure de test non exécutée vaut `DEFINED-NOT-EXECUTED`, jamais PASS.
- Un résultat manuel peut constituer une preuve si protocole, entrées, version, résultat et reviewer sont traçables.
- Une preuve automatisée doit conserver au minimum commande/suite, version ou commit, date/exécution et verdict.
- `TBD-PREPROD` peut rester ouvert seulement s'il ne bloque pas le critère testé ; sinon K5 reste bloqué.
- Toute régression ou invalidation d'une preuve peut faire redescendre le niveau calculé.

## Pilote K5 — YD-MS-KNW-001

KNW est le premier pilote car sa nature `DERIVED` rend la reconstruction et la convergence centrales.

### Matrice initiale

| Critère | État initial | Preuve attendue |
|---|---|---|
| automatedValidation | PARTIAL | Knowledge Gate + validations KNW dédiées |
| contractTests | NOT-TESTED | entrées versionnées, KNW→Search, incompatibilité/quarantaine |
| securityVerification | NOT-TESTED | provenance, PII/default-deny, accès/finalité applicables |
| restoreOrResilienceTestWhenApplicable | NOT-TESTED | FULL_REBUILD + convergence + CATCH_UP/PARTIAL selon protocole |
| evidenceLinks | PARTIAL | rapports versionnés sous `_meta/evidence/` |
| unresolvedCriticalGapsEqualsZero | FAIL | tests critiques ci-dessus non exécutés |

### Scénarios minimaux KNW

- FULL_REBUILD depuis sources/snapshots gouvernés ;
- comparaison de convergence avec l'état attendu ;
- DELETE, WITHDRAW et REVOKE propagés ;
- événements hors ordre et replay idempotent ;
- entity resolution incorrecte/corrigée ;
- provenance absente ou contrat incompatible rejeté/quarantiné ;
- KNW indisponible sans promotion d'un cache consommateur en autorité ;
- vérification que la donnée non publiable/PII interdite ne reste pas exposée ;
- contrat KNW→Search compatible et découplage Search primaire préservé.

## Verdict initial KNW

`K4-PASS / K5-NOT-YET-PASS`.

La documentation nécessaire au lancement du K5 est définie, mais aucune preuve d'exécution ne doit être inventée. KNW restera `REBUILD-UNVERIFIED` jusqu'à réussite du protocole applicable et enregistrement des preuves.

## Sortie attendue

Le passage KNW à K5 exige une matrice finale PASS, des liens de preuves reproductibles et zéro gap critique. Ensuite le patron de vérification pourra être appliqué à SKL, REC et LRN en adaptant les tests à leur nature.
