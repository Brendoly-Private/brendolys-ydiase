---
document_id: "YD-DOC-CON-PRF-002-K3-BASELINE"
title: "YD-MS-PRF-002 — K3 Contract Baseline"
document_type: "contract-baseline"
document_role: "Fixe la baseline contractuelle K3 applicable à YD-MS-PRF-002."
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

# YD-MS-PRF-002 — K3 Contract Baseline

> **Rôle du document**
> Fixe la baseline contractuelle K3 applicable à YD-MS-PRF-002.
> **Usage développement :** référence contractuelle obligatoire pour les implémentations et intégrations concernées.

Statut : K3-CONTRACT-BASELINE / IMPLEMENTATION-PENDING
Nature : AUTH
Criticité : C1

## Portée
PRF-002 est l'autorité YDIASE de l'historique éducatif et professionnel individuel, des réalisations déclarées, des liens de preuve et des états de vérification propres.

## Objets autoritatifs
EducationRecord, ExperienceRecord, AchievementClaim, ProfileEvidenceLink, états de vérification, temporalité, versions et provenance associées.

PRF-002 ne possède ni identité IAM, ni profil courant PRF-001, ni référentiels EDU, ni taxonomies SKL, ni décisions Privacy CNS.

## Contrats
Entrées gouvernées : IdentityRef minimal, données minimales PRF-001 lorsque requises, décisions CNS, CountryConfig, références EDU/SKL et provenance DAT.

Sortie canonique : YD-CTR-PRF-HISTORY-v1. Toute projection est minimisée, versionnée et ne peut jamais restaurer l'autorité PRF-002.

## Invariants
- PRF-002 est AUTH et non reconstructible depuis consommateurs ou dépendances.
- PRF-001 et PRF-002 ne partagent aucune base.
- déclaration, preuve et vérification restent distinctes.
- une preuve ne crée pas automatiquement une compétence autoritative.
- toute correction conserve une histoire interprétable.
- une décision Privacy obligatoire non vérifiable entraîne fail-closed.
- replay après restore est idempotent.

## Exigences
PRF2-REQ-001 maintenir l'autorité exclusive.
PRF2-REQ-002 préserver temporalité, versions, provenance et preuves.
PRF2-REQ-003 séparer déclaration et vérification.
PRF2-REQ-004 préserver les frontières externes.
PRF2-REQ-005 minimiser les projections.
PRF2-REQ-006 représenter corrections/retraits sans réécriture silencieuse.
PRF2-REQ-007 supporter replay idempotent.
PRF2-REQ-008 permettre restore indépendant.
PRF2-REQ-009 réappliquer Privacy après restore.
PRF2-REQ-010 préserver portabilité/migration de l'historique.

## Versionnement
Tout agrégat expose une version. Tout changement incompatible exige une version majeure. Les migrations préservent IDs, temporalité, provenance et preuves.

## Limites
K3 ne ferme pas schémas physiques, datastore, IAM physique, rétention détaillée, PITR, tests de contrats ou restore exécuté.

## Verdict
K3-PASS / PHYSICAL-CONTRACTS-PENDING.
