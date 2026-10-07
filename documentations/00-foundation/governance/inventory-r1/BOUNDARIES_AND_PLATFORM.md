---
document_id: "YD-DOC-FND-INV-002"
title: "R1 — Boundaries & Platform Inventory"
document_type: "boundary-inventory-view"
document_role: "Inventorie la population de frontières métier et composants plateforme observée lors de R1 et leur classification documentaire."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "view"
canonical: false
development_usage: "informational"
owners:
  - "Documentation Governance"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "foundation"
  - "documentation-migration"
---

# R1 — Boundaries & Platform Inventory

> **Rôle du document**
> Inventorie la population de frontières métier et composants plateforme observée lors de R1 et leur classification documentaire.
> **Usage développement :** vue d’inventaire et d’orientation ; elle ne crée pas de vérité normative.

Statut : `ACTIVE-R1 / REGISTER-BASED-POPULATION`

## 1. Source
Population tirée de `13-architecture/AUTONOMY_PROFILE_REGISTER.md` et réconciliée avec `MICROSERVICE_BOUNDARY_REVIEW.md`.

## 2. Baseline
- 48 microservices métier YD-MS ;
- 4 composants plateforme YD-PLT ;
- 52 frontières autonomes ;
- BRENDOLYS Identity externe ;
- CAR-004, LAB-003, AI-004 deferred.

## 3. Microservices enregistrés

### Identité / Education / Skills / Careers
PRF-001, PRF-002, EDU-001, EDU-002, EDU-003, EDU-004, SKL-001, SKL-002, CAR-001, CAR-002.

### Orientation / Search / Labor
ASM-001, ORI-001, REC-001, SRH-001, LAB-001, LAB-002.

### Opportunities / Employment
OPP-001, OPP-002, APP-001, EMP-001, EMP-002.

### Content / Community / Learning / Notifications
CNT-001, CNT-002, COM-001, LRN-001, NTF-001.

### Partners
PRT-001, AMB-001.

### Data / Knowledge / Analytics / AI
DAT-001, DAT-002, DAT-003, DAT-004, DAT-005, KNW-001, ANL-001, ANL-002, ANL-003, AI-002, AI-003.

### Economy / Products / Governance
BIL-001, BIL-002, MKT-001, SPN-001, DPR-001, INT-001, MOD-001, CFG-001, CNS-001.

## 4. Platform components
YD-PLT-AI-001, YD-PLT-MLP-001, YD-PLT-API-001, YD-PLT-AUD-001.

## 5. Classification locale des fichiers
Pour chaque frontière :
- AUTONOMY_PROFILE → governance/
- PHASE_CLOSURE → governance/
- business/domain policies → policies/
- owned/consumed data → authority/
- inbound/outbound projection/API/event docs → contracts/
- privacy/security spécifique → security/
- BIA/continuity/backup/restore → resilience/
- runbooks → operations/
- test plans/matrices → validation/
- résultats exécutés datés → evidence/ (index global + référence locale)

Les sous-dossiers ne sont créés que si le contenu existe.

## 6. Frontières riches déjà identifiées
PRF-002 possède plusieurs documents BIA/continuity/backup/DR/test/evidence/nomination et justifie une hiérarchie locale.

ANL-001 possède policy métrique, source-contract register, phase closure et autonomy profile ; il justifie policies/contracts/governance.

KNW-001 et SRH-001 possèdent des politiques/projections spécialisées et justifient une séparation contracts/policies/governance.

## 7. Non-1:1
Voir `../../LOGICAL_TO_PHYSICAL_BOUNDARY_REGISTER.md` pour CAR-003, ORI-002, RSH-001, INS-001, EMP-003, ADM-001, IDN-001, REC-002 et les deferred.

## 8. Gate physique
La population est `P-REGISTERED`. L'existence de chaque fichier local est vérifiée par lots ; une absence dans code search n'est pas une preuve d'absence.

Verdict : `BOUNDARY-POPULATION-CANONICALLY-REGISTERED / LOCAL-FILE-TREE-PENDING`.
