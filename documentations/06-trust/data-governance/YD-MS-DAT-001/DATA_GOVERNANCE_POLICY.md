---
document_id: "YD-DOC-TRU-DAT-001-DATA-GOVERNANCE-POLICY"
title: "DAT-001 — Source & Usage Rights Policy"
document_type: "trust-policy"
document_role: "Établit une règle normative de gouvernance, confiance ou données applicable au périmètre concerné."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "trust"
---

# DAT-001 — Source & Usage Rights Policy

> **Rôle du document**
> Établit une règle normative de gouvernance, confiance ou données applicable au périmètre concerné.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-BASELINE / PREPROD-PENDING`

DAT-001 répond avant acquisition à : **quelle est la source, qui l'attribue, où/quand peut-on l'utiliser et pour quelles finalités ?**

## Autorité
Possède DataSource, SourceContract, UsageRight, SourceTerritoryScope et SourceAccessPolicy. Il référence contrats/accords/preuves ; PRT, CFG, CNS et sources juridiques gardent leurs autorités respectives.

## États
Une source/version est au minimum `DRAFT`, `ACTIVE`, `RESTRICTED`, `SUSPENDED`, `EXPIRED`, `REVOKED`, `RETIRED`.

UsageRight conserve source_ref, usage/purpose scope, territory, permitted operations, redistribution/derivation constraints, effective dates, evidence_ref et version.

## Décision d'acquisition
DAT-002 reçoit une décision versionnée `ALLOW`, `DENY`, `ALLOW-WITH-RESTRICTIONS` ou `NOT-DETERMINABLE`.
Si droit, territoire ou validité obligatoire ne peut être prouvé : **fail-closed pour nouvelle acquisition**.

Un droit expiré/révoqué n'est jamais prolongé par cache. Une acquisition antérieure conserve le droit/version alors évalué pour audit, sans autoriser automatiquement un nouvel usage.

## Séparation
Enregistrer une source ne prouve ni qualité ni vérité. DAT-001 autorise l'usage ; DAT-003 prouve l'origine ; DAT-004 évalue/valide ; le domaine métier publie sa vérité.

## Gates
DEFINED : source identity, rights scope, temporal/territorial validity, fail-closed, versioning.
TBD : modèles contractuels réels, approbateurs, IAM, SLO/RPO/RTO, restore.

Statut final : `SOURCE-RIGHTS-SEMANTICS-CLOSED / IMPLEMENTATION-EVIDENCE-PENDING`.
