---
document_id: "YD-DOC-META-K4-GOVERNANCE-GATE"
title: "YDIASE Knowledge Gate — K4 Gouverné"
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
---

# YDIASE Knowledge Gate — K4 Gouverné

> **Rôle du document**
> Documente une référence de maturité, de gate ou d’ontologie utilisée pour qualifier le corpus YDIASE.
> **Usage développement :** référence de support pour la gouvernance et la qualification documentaire.

Statut : `PILOT-CLOSED / K4-PASS`

## Objet

K4 signifie qu'une entité K3 possède les règles de gouvernance, sécurité, conformité et exploitation nécessaires pour préparer une implémentation exploitable sans laisser les responsabilités critiques implicites.

K4 ne signifie ni préproduction validée ni production.

## Critères obligatoires

1. `dataClassification` — les données et objets manipulés sont classifiés, avec traitement attendu selon leur sensibilité.
2. `securityControls` — contrôles d'accès, authentification service-à-service, intégrité, secrets, isolation et journalisation applicables sont définis.
3. `privacyAndRetentionWhenApplicable` — finalités, minimisation, rétention, suppression, droits et contraintes territoriales/personnelles sont définis ou `N/A` avec justification.
4. `sloOrCriticality` — criticité et objectifs opérationnels nécessaires sont définis au niveau adapté à la phase. Les valeurs numériques peuvent rester `TBD-PREPROD` si leur méthode de fixation et leur gate sont documentés.
5. `observability` — logs, métriques, traces, signaux métier, alertes et corrélation nécessaires sont définis.
6. `backupRecoveryWhenStateful` — stratégie de sauvegarde, restauration, reconstruction et responsabilités est définie pour tout état non reconstructible.
7. `runbookOrOperationalProcedure` — incidents principaux, modes dégradés, reprise, rollback et escalade disposent d'une procédure exploitable.
8. `namedOwners` — owner métier/technique et responsabilités de revue sont identifiables par rôle ou registre gouverné.

## Règles

- `UNKNOWN` bloque K4.
- `PARTIAL` bloque K4.
- `N/A` exige une justification vérifiable.
- Une criticité sans stratégie de reprise ne satisfait pas K4 pour un service stateful.
- Un document générique de sécurité ne suffit pas s'il ne peut pas être relié au composant.
- K4 peut être atteint avant code si les contrôles sont spécifiés et testables, mais K5 exigera les preuves d'exécution correspondantes.
- Les valeurs numériques dépendantes de charge ou préproduction peuvent rester ouvertes si le mécanisme de décision, le responsable et le gate de fermeture sont définis.

## Sortie attendue

Pour chaque microservice :
- matrice de classification ;
- baseline sécurité/conformité ;
- baseline exploitation/résilience ;
- owner matrix ;
- liste explicite des paramètres `TBD-PREPROD` ;
- critères qui permettront K5.

## État du pilote

| Microservice | Nature | K4 | Preuve canonique |
|---|---|---|---|
| `YD-MS-KNW-001` | DERIVED | PASS | `06-trust/governance/YD-MS-KNW-001/K4_GOVERNANCE_BASELINE.md` |
| `YD-MS-SKL-001` | AUTH | PASS | `06-trust/governance/YD-MS-SKL-001/K4_GOVERNANCE_BASELINE.md` |
| `YD-MS-REC-001` | MIXED | PASS | `06-trust/governance/YD-MS-REC-001/K4_GOVERNANCE_BASELINE.md` |
| `YD-MS-LRN-001` | MIXED | PASS | `06-trust/governance/YD-MS-LRN-001/K4_GOVERNANCE_BASELINE.md` |

Le pilote K4 est **fermé** pour ces quatre microservices. Cette fermeture reste documentaire : elle n'implique ni PREPROD, ni tests K5 exécutés, ni production.

La continuation canonique du pilote se fait au niveau **K5 — Vérifié**, en commençant par `YD-MS-KNW-001`.
