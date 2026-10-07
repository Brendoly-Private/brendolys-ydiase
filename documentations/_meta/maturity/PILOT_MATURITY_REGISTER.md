---
document_id: "YD-DOC-META-PILOT-MATURITY-REGISTER"
title: "YDIASE — Pilot Maturity Register"
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

# YDIASE — Pilot Maturity Register

> **Rôle du document**
> Documente une référence de maturité, de gate ou d’ontologie utilisée pour qualifier le corpus YDIASE.
> **Usage développement :** référence de support pour la gouvernance et la qualification documentaire.

Statut : `CANONICAL-VIEW / PILOT-PREIMPLEMENTATION-CLOSED`

## Objet

Vue transversale de maturité pour YD-MS-KNW-001, YD-MS-SKL-001, YD-MS-REC-001 et YD-MS-LRN-001. Cette vue ne remplace aucune baseline canonique et ne transforme aucune preuve planifiée en preuve exécutée.

| Microservice | Nature | K3 | K4 | K5 | Documentation readiness |
|---|---|---|---|---|---|
| YD-MS-KNW-001 | DERIVED | PASS | PASS | NOT-YET-PASS | DOCUMENTATION-READY |
| YD-MS-SKL-001 | AUTH | PASS | PASS | NOT-YET-PASS | DOCUMENTATION-READY |
| YD-MS-REC-001 | MIXED | PASS | PASS | NOT-YET-PASS | DOCUMENTATION-READY |
| YD-MS-LRN-001 | MIXED | PASS | PASS | NOT-YET-PASS | DOCUMENTATION-READY |

## Lecture

K3 signifie que les frontières, contrats logiques, invariants, exigences et règles de compatibilité nécessaires sont contractualisés.

K4 signifie que classification, sécurité, Privacy/rétention, criticité, observabilité, recovery, procédures et ownership sont définis.

K5 reste bloqué tant que les preuves applicables ne sont pas réellement exécutées et enregistrées.

`DOCUMENTATION-READY` signifie qu'une équipe peut commencer l'implémentation sans devoir inventer les frontières structurantes du composant. Ce statut n'est pas un niveau de maturité supplémentaire.

## Profils de résilience

- KNW — DERIVED : FULL_REBUILD/convergence/replay constituent la preuve de résilience centrale.
- SKL — AUTH : backup/restore indépendant du store autoritatif est obligatoire.
- REC — MIXED : restore des états REC + reproductibilité des runs, sans appropriation des sources.
- LRN — MIXED : restore des objets LRN + réconciliation/freshness des références externes.

## Gaps K5 encore ouverts

KNW : contract tests physiques, sécurité implémentée, reconstruction réelle et convergence.

SKL : contrôles de mutation, publication, provenance, backup/restore et intégrité après restauration.

REC : contract tests, IAM/IDOR, anti-influence SPN, fairness applicable, dérive/rollback, reproductibilité et restore.

LRN : contract tests, droits d'usage, IAM/IDOR, freshness EDU/MKT, mappings réels, fairness si applicable, restore et retraits.

## Règle de maintien

Toute contradiction avec une source canonique, régression de preuve ou changement structurel impose de recalculer cette vue. Les PASS ne sont jamais conservés par convention.
