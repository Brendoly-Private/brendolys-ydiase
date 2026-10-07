---
document_id: "YD-DOC-CON-KNW-001-K5-CONTRACT-TEST-SPEC"
title: "YD-MS-KNW-001 — K5 Contract Test Specification"
document_type: "contract-test-spec"
document_role: "Définit le contrat ou dispositif de validation K5 CONTRACT TEST SPEC dans le périmètre documentaire des contrats YDIASE."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "contracts"
---

# YD-MS-KNW-001 — K5 Contract Test Specification

> **Rôle du document**
> Définit le contrat ou dispositif de validation K5 CONTRACT TEST SPEC dans le périmètre documentaire des contrats YDIASE.
> **Usage développement :** référence contractuelle obligatoire pour les implémentations, intégrations ou validations concernées.

Statut : `TEST-SPEC-DEFINED / EXECUTION-PENDING`

## Objet

Définir les tests contractuels nécessaires à K5 sans imposer prématurément Avro, JSON Schema, Protobuf, broker ou datastore.

## Entrées autoritatives

### KNW-CT-001 — Champs minimaux
Une entrée acceptée doit identifier source_domain, source_ref, source_version, operation, temporalité/état de publication applicable et watermark/replay position.

### KNW-CT-002 — Opérations
UPSERT, DELETE, WITHDRAW et REVOKE sont reconnues. Une opération inconnue est rejetée ou mise en quarantaine.

### KNW-CT-003 — Version incompatible
Une version non supportée ne doit jamais être interprétée silencieusement. Résultat attendu : rejet/quarantaine observable.

### KNW-CT-004 — Provenance
Lorsqu'une relation exige une provenance, son absence empêche son exposition comme relation fiable.

### KNW-CT-005 — Priorité retrait
DELETE/WITHDRAW/REVOKE prennent priorité sur enrichissement/recalcul et invalident les projections dépendantes selon leur sémantique.

## Sortie KNW vers Search

### KNW-CT-006 — Enrichment minimal
Vérifier graph_version, source_watermarks, source refs/versions, relation type/class, provenance, freshness et opération applicables.

### KNW-CT-007 — Search indépendant
SRH doit pouvoir indexer et servir la vérité primaire sans enrichment KNW.

### KNW-CT-008 — Enrichment stale
Un enrichment stale peut être désactivé sans supprimer un document source encore valide.

### KNW-CT-009 — Retrait
DELETE/REVOKE doit retirer ou invalider l'enrichment concerné sans transformer KNW en autorité du document primaire.

## Versionnement et compatibilité

### KNW-CT-010 — Ajout compatible
Un ajout optionnel compatible ne casse pas un consommateur de la version courante.

### KNW-CT-011 — Breaking change
Suppression/changement de sens/ownership ou nouveau champ obligatoire incompatible exige une nouvelle version majeure.

### KNW-CT-012 — Coexistence
Si deux versions coexistent pendant migration, leur interprétation reste non ambiguë et leur version est traçable.

## Preuve attendue

Chaque test exécuté doit produire : Test ID, commit/version, fixture/dataset, contrat/règle version, résultat attendu, résultat observé, artefact/log et verdict.

Tant que ces tests ne sont pas exécutés contre une représentation contractuelle réellement testable, le critère K5 `contractTests` reste `NOT-TESTED`.
