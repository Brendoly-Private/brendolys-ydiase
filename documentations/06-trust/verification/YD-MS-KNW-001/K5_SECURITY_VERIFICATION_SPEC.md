---
document_id: "YD-DOC-TRU-KNW-001-K5-SECURITY-VERIFICATION-SPEC"
title: "YD-MS-KNW-001 — K5 Security Verification Specification"
document_type: "verification-specification"
document_role: "Définit un protocole ou une spécification de vérification servant de preuve contrôlée."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "evidence"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "trust"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-KNW-001 — K5 Security Verification Specification

> **Rôle du document**
> Définit un protocole ou une spécification de vérification servant de preuve contrôlée.
> **Usage développement :** référence de vérification obligatoire pour le périmètre concerné.

Statut : `TEST-SPEC-DEFINED / EXECUTION-PENDING`

## Objet

Définir les vérifications de sécurité et Privacy nécessaires pour transformer les contrôles K4 de KNW en preuves K5.

## Scénarios

### KNW-SEC-001 — Provenance obligatoire
Une projection dont la classe exige une provenance suffisante ne peut pas être exposée comme fiable lorsque cette provenance manque ou est invalide.

### KNW-SEC-002 — PII default-deny
Une donnée personnelle interdite au graphe partagé est rejetée, isolée ou rendue non exposable. Sa présence dans une source n'autorise jamais automatiquement sa projection.

### KNW-SEC-003 — Classification source
KNW ne peut pas abaisser la classification d'une donnée par rapport à sa source.

### KNW-SEC-004 — Retrait Privacy
DELETE/WITHDRAW/REVOKE ou restriction source rend la donnée concernée non découvrable dans KNW et dans les enrichissements dépendants applicables.

### KNW-SEC-005 — Accès horizontal
Lorsque des projections restreintes existent, un principal non autorisé ne peut ni lire ni inférer leur contenu par identifiant, relation ou voisinage.

### KNW-SEC-006 — Service-to-service
Les mutations/ingestions protégées refusent une identité service absente ou non autorisée lorsque l'implémentation IAM existe.

### KNW-SEC-007 — Secrets
Aucun secret/credential ne doit être accepté comme donnée métier normale ni apparaître dans les preuves/logs exposés.

### KNW-SEC-008 — GraphRAG
Un consommateur GraphRAG ne peut contourner classification, finalité, retrait ou provenance. Les faits retournés restent reliés aux sources autorisées.

## Niveaux de preuve

Les scénarios 001-004 peuvent commencer par des tests logiques, mais ne ferment pas à eux seuls la vérification runtime. Les scénarios dépendant d'IAM, stockage, API ou GraphRAG restent `BLOCKED-BY-IMPLEMENTATION` tant que ces mécanismes n'existent pas.

## PASS K5 sécurité

Le critère `securityVerification` ne devient PASS que lorsque tous les scénarios critiques applicables à l'implémentation visée ont une preuve exécutée, reproductible et reliée à un Evidence Record. Une spécification seule ne vaut jamais PASS.
