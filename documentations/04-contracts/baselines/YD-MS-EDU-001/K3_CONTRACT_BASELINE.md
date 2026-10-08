---
document_id: "YD-DOC-CON-EDU-001-K3-BASELINE"
title: "YD-MS-EDU-001 — K3 Contract Baseline"
document_type: "contract-baseline"
document_role: "Fixe la baseline contractuelle K3 applicable à YD-MS-EDU-001."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "contracts"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-EDU-001 — K3 Contract Baseline

> **Rôle du document**
> Fixe la baseline contractuelle K3 applicable à YD-MS-EDU-001.
> **Usage développement :** référence contractuelle obligatoire pour les implémentations et intégrations concernées.

Statut : K3-CONTRACT-BASELINE / IMPLEMENTATION-PENDING
Nature : AUTH
Criticité : C2

## Autorité
EDU-001 est l'autorité des objets Institution, Campus, InstitutionStatus, InstitutionPresence et de leurs versions.

EDU-001 ne possède pas Program, Curriculum, Qualification, Skill, EducationRecord individuel ni configuration pays.

## Contrats entrants
- YD-CTR-CFG-COUNTRY-CONFIG-v1 : contexte territorial et paramètres pays applicables.
- DAT : provenance, qualité et validation selon les contrats gouvernés applicables.
- workflows institutionnels/partenaires : contributions ou claims gouvernés ; une contribution externe ne transfère jamais l'autorité.

## Contrat sortant
YD-CTR-EDU-INSTITUTION-v1 est le contrat logique canonique EDU-001 vers EDU-002 et les consommateurs autorisés.

Données minimales : InstitutionRef, CampusRef lorsque pertinent, status et version. Les attributs publics et internes sont séparés selon leur finalité.

## Invariants
- identifiants Institution et Campus durables ;
- aucun Program possédé par EDU-001 ;
- publication bloquée si pays, source ou validation obligatoire est inconnue ;
- contributeur et validateur séparables ;
- provenance et contexte territorial conservés ;
- aucune base partagée ni accès DB croisé ;
- un consommateur ne modifie jamais directement un agrégat EDU-001 ;
- cache, Search, KNW, Analytics ou projection aval non autoritatifs ;
- anciennes versions publiées interprétables ;
- restauration depuis la chaîne EDU-001.

## Exigences
EDU1-REQ-001 préserver l'autorité institutionnelle.
EDU1-REQ-002 garantir des références durables.
EDU1-REQ-003 gouverner contribution, validation et publication.
EDU1-REQ-004 préserver provenance, source et versions.
EDU1-REQ-005 contextualiser les éléments dépendant d'un territoire.
EDU1-REQ-006 empêcher une contribution externe de devenir autorité implicite.
EDU1-REQ-007 séparer données publiables et informations internes de gouvernance.
EDU1-REQ-008 maintenir les versions nécessaires à l'interprétation des références existantes.
EDU1-REQ-009 restaurer l'autorité sans dépendre d'un consommateur.
EDU1-REQ-010 propager les changements/retraits de manière gouvernée et idempotente.

## Multi-pays
Aucune règle nationale n'est une vérité globale. Les attributs territoriaux conservent contexte, version et source. CFG reste l'autorité de configuration pays.

## Versionnement
Ajout optionnel compatible. Changement de sens, suppression ou modification incompatible d'un champ requis impose une version majeure. Les consommateurs ne doivent pas interpréter librement une valeur inconnue.

## Limites K3
Restent PREPROD/implémentation : endpoints et schémas physiques, protocole, datastore, IAM physique, workflow concret de validation, RPO/RTO/SLO, rétention, contract tests et restore tests.

## Verdict
K3-PASS / PHYSICAL-CONTRACTS-PENDING.
