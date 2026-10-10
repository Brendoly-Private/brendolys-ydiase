---
document_id: "YD-DOC-DOM-EDU-002"
title: "Frontières et dépendances — Éducation et institutions"
document_type: "domain-boundaries-dependencies"
document_role: "Définit les quatre frontières Education, leurs ownerships, dépendances, invariants multi-pays et règles de récupération."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "domain"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# Frontières et dépendances — Éducation et institutions

> **Rôle du document**
> Définit les quatre frontières Education, leurs ownerships, dépendances, invariants multi-pays et règles de récupération.
> **Usage développement :** référence obligatoire pour les conceptions et décisions relevant de son périmètre.

Statut : `DOMAIN-REVIEW-CANDIDATE`

## Frontières autoritatives

### EDU-001 — Institution Catalog
Possède `Institution`, `Campus`, `InstitutionStatus`, `InstitutionPresence` et leurs versions. Consomme CFG, provenance/validation et claims institutionnels gouvernés. Ne possède pas les programmes.

### EDU-002 — Program Catalog
Possède `Program`, `ProgramVersion`, `ProgramOffering`, `AdmissionRuleSet`. Référence EDU-001, EDU-004 et le curriculum publié EDU-003. Ne possède pas le contenu détaillé du curriculum.

### EDU-003 — Curriculum & Module
Possède `Curriculum`, `CurriculumVersion`, `Module`, `TeachingUnit`, `ModuleSequence` et mappings pédagogiques. Référence Program et SKL-001. Une Skill inconnue ne devient jamais canonique ici.

### EDU-004 — Qualification Framework
Possède `Qualification`, `QualificationLevel`, `QualificationFramework`, `EquivalenceRule`, `PrerequisiteRule` et versions/contextes pays. Consomme CFG et référentiels gouvernés.

## Dépendances internes

| Producteur | Consommateur | Contrat minimal | Cohérence / panne |
|---|---|---|---|
| EDU-001 | EDU-002 | InstitutionRef, CampusRef, status | validation forte à création ; versions publiées conservées |
| EDU-002 | EDU-003 | ProgramRef, ProgramVersionRef | publication Curriculum bloquée sans Program valide |
| EDU-003 | EDU-002 | CurriculumRef/version publiée | événement/projection ; dernier publié conservé |
| EDU-004 | EDU-002 | QualificationRef, niveau/prérequis | publication dépendante bloquée si référence obligatoire inconnue |

La relation EDU-002 ↔ EDU-003 n'autorise aucune transaction distribuée.

## Dépendances externes

- CFG-001 reste l'autorité de configuration pays.
- DAT-003/004/005 fournissent provenance, qualité/validation et référentiels selon leurs ownerships.
- SKL-001 reste l'autorité des Skills/Knowledge.
- PRF-002 consomme les références Education pour l'historique individuel mais ne modifie aucun catalogue.
- Search, Knowledge, Orientation, Recommendation et Analytics sont consommateurs/projections, jamais autorités Education.

## Invariants multi-pays

- aucune règle du type « Licence = 3 ans » n'est une vérité globale hardcodée ;
- niveaux, durées, prérequis, équivalences et terminologies sont contextualisables et versionnés ;
- toute équivalence gouvernée conserve provenance, portée, validité et contexte ;
- une qualification officielle externe conserve son attribution ;
- les anciennes versions restent interprétables après changement de cadre.

## Interdictions

- base partagée ou accès DB croisé entre EDU-001/002/003/004 ;
- EDU-002 modifiant Institution ;
- EDU-003 modifiant Program ;
- EDU-002 créant une Qualification canonique ;
- EDU-003 créant une Skill canonique ;
- PRF-002 créant Institution/Program/Qualification ;
- IA générant une équivalence comme vérité autoritative ;
- projection aval devenant autorité Education.

## Récupération

Chaque frontière AUTH restaure son autorité depuis sa propre chaîne de backup/recovery. Aucune base d'une autre frontière n'est une dépendance de reconstruction. Les références externes peuvent rester temporairement non résolues jusqu'à réconciliation.

## Verdict

Les quatre frontières sont cohérentes avec leurs ownerships et cycles de vie. Aucun besoin de fusion n'est démontré.

Statut : `BOUNDARIES-STABLE-CANDIDATE`.
