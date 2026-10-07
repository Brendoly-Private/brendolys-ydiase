---
document_id: "YD-DOC-SYS-ARC-REG-001"
title: "Autonomy Profile Register — BRENDOLYS YDIASE"
document_type: "autonomy-profile-register"
document_role: "Indexe les profils d’autonomie des frontières physiques sans dupliquer leurs exigences détaillées."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "architecture"
---

# Autonomy Profile Register — BRENDOLYS YDIASE

> **Rôle du document**
> Indexe les profils d’autonomie des frontières physiques sans dupliquer leurs exigences détaillées.
> **Usage développement :** référence obligatoire pour les conceptions, frontières, contrats et développements relevant de son périmètre.

Statut : `D3-autonomy-profile-baseline`

## Objet

Ce registre est l'index canonique des profils d'autonomie. Les exigences détaillées vivent dans chaque `AUTONOMY_PROFILE.md` afin d'éviter deux sources concurrentes.

Cible actuelle : **48 microservices métier + 4 composants plateforme = 52 frontières autonomes**.

La séparation `PRF-001 / PRF-002` est régie par `ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY.md`.

## Règles

- `AUTH` : état autoritatif, backup et restauration indépendants obligatoires.
- `DERIVED` : reconstruction selon le standard DERIVED.
- `MIXED` : état autoritatif et projections reconstruisibles séparés.
- `C1`, `C2`, `C3` restent des classes candidates jusqu'à validation exploitation.
- chaque frontière possède repo/artefact, datastore ou état privé si nécessaire, migrations, identité machine, secrets, réseau, observabilité, CI/CD, rollback, runbook et cycle de retrait propres selon `MICROSERVICE_AUTONOMY_STANDARD.md`.
- les valeurs RPO/RTO/SLO et choix physiques non décidés restent `TBD-PREPROD` ou `ADR-REQUIRED`, jamais inventés.

## Microservices métier

| Boundary | Nature | Crit. | Profil | État |
|---|---|---:|---|---|
| YD-MS-PRF-001 | AUTH | C1 | `microservices/YD-MS-PRF-001/AUTONOMY_PROFILE.md` | RECONCILED-PRF-SPLIT |
| YD-MS-PRF-002 | AUTH | C1 | `microservices/YD-MS-PRF-002/AUTONOMY_PROFILE.md` | NEW-RECONCILED |
| YD-MS-EDU-001 | AUTH | C2 | `microservices/YD-MS-EDU-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-EDU-002 | AUTH | C2 | `microservices/YD-MS-EDU-002/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-EDU-003 | AUTH | C2 | `microservices/YD-MS-EDU-003/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-EDU-004 | AUTH | C2 | `microservices/YD-MS-EDU-004/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-SKL-001 | AUTH | C2 | `microservices/YD-MS-SKL-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-SKL-002 | AUTH | C1 | `microservices/YD-MS-SKL-002/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-CAR-001 | AUTH | C2 | `microservices/YD-MS-CAR-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-CAR-002 | MIXED | C2 | `microservices/YD-MS-CAR-002/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-ASM-001 | AUTH | C1 | `microservices/YD-MS-ASM-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-ORI-001 | AUTH | C1 | `microservices/YD-MS-ORI-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-REC-001 | MIXED | C1 | `microservices/YD-MS-REC-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-SRH-001 | DERIVED | C2 | `microservices/YD-MS-SRH-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-LAB-001 | AUTH | C2 | `microservices/YD-MS-LAB-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-LAB-002 | MIXED | C2 | `microservices/YD-MS-LAB-002/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-OPP-001 | AUTH | C1 | `microservices/YD-MS-OPP-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-OPP-002 | MIXED | C2 | `microservices/YD-MS-OPP-002/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-APP-001 | AUTH | C1 | `microservices/YD-MS-APP-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-EMP-001 | AUTH | C2 | `microservices/YD-MS-EMP-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-EMP-002 | AUTH | C1 | `microservices/YD-MS-EMP-002/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-CNT-001 | AUTH | C2 | `microservices/YD-MS-CNT-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-CNT-002 | DERIVED | C3 | `microservices/YD-MS-CNT-002/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-COM-001 | AUTH | C2 | `microservices/YD-MS-COM-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-LRN-001 | MIXED | C2 | `microservices/YD-MS-LRN-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-NTF-001 | AUTH | C2 | `microservices/YD-MS-NTF-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-PRT-001 | AUTH | C1 | `microservices/YD-MS-PRT-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-AMB-001 | AUTH | C1 | `microservices/YD-MS-AMB-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-DAT-001 | AUTH | C1 | `microservices/YD-MS-DAT-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-DAT-002 | AUTH | C2 | `microservices/YD-MS-DAT-002/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-DAT-003 | AUTH | C1 | `microservices/YD-MS-DAT-003/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-DAT-004 | AUTH | C1 | `microservices/YD-MS-DAT-004/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-DAT-005 | AUTH | C2 | `microservices/YD-MS-DAT-005/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-KNW-001 | DERIVED | C2 | `microservices/YD-MS-KNW-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-ANL-001 | DERIVED | C2 | `microservices/YD-MS-ANL-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-ANL-002 | MIXED | C2 | `microservices/YD-MS-ANL-002/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-ANL-003 | MIXED | C2 | `microservices/YD-MS-ANL-003/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-AI-002 | DERIVED | C2 | `microservices/YD-MS-AI-002/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-AI-003 | AUTH | C1 | `microservices/YD-MS-AI-003/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-BIL-001 | AUTH | C1 | `microservices/YD-MS-BIL-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-BIL-002 | AUTH | C1 | `microservices/YD-MS-BIL-002/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-MKT-001 | AUTH | C1 | `microservices/YD-MS-MKT-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-SPN-001 | AUTH | C2 | `microservices/YD-MS-SPN-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-DPR-001 | AUTH | C1 | `microservices/YD-MS-DPR-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-INT-001 | AUTH | C1 | `microservices/YD-MS-INT-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-MOD-001 | AUTH | C1 | `microservices/YD-MS-MOD-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-CFG-001 | AUTH | C1 | `microservices/YD-MS-CFG-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-MS-CNS-001 | AUTH | C1 | `microservices/YD-MS-CNS-001/AUTONOMY_PROFILE.md` | BASELINE |

## Composants plateforme

| Boundary | Nature | Crit. | Profil | État |
|---|---|---:|---|---|
| YD-PLT-AI-001 | MIXED | C1 | `platform-components/YD-PLT-AI-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-PLT-MLP-001 | AUTH | C1 | `platform-components/YD-PLT-MLP-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-PLT-API-001 | MIXED | C1 | `platform-components/YD-PLT-API-001/AUTONOMY_PROFILE.md` | BASELINE |
| YD-PLT-AUD-001 | AUTH-APPEND-ONLY | C1 | `platform-components/YD-PLT-AUD-001/AUTONOMY_PROFILE.md` | BASELINE |

## Frontières différées

`YD-MS-CAR-004`, `YD-MS-LAB-003` et `YD-PLT-AI-004` ne comptent pas dans les 52 tant qu'un ADR n'active pas leur extraction.

## Réconciliation PRF

`YD-MS-PRF-001` ne possède plus EducationRecord, ExperienceRecord, AchievementClaim ou ProfileEvidenceLink. `YD-MS-PRF-002` possède ces agrégats et dispose de son propre datastore, backup/restore, audience IAM, secrets, réseau, observabilité, CI/CD, runbook et DR.

Aucune base n'est partagée entre les deux frontières. Leurs échanges passent par des contrats gouvernés. Le futur Contract Registry doit matérialiser cette séparation.

## Gate global

Aucun profil ne passe `ready-for-production` tant que ses champs obligatoires `TBD-PREPROD` et `ADR-REQUIRED` applicables ne sont pas fermés. La présence dans ce registre confirme une frontière documentaire, pas son activation au pilote Burkina.