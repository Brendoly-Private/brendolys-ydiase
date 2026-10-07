---
document_id: "YD-DOC-CON-SKL-001-K3-BASELINE"
title: "YD-MS-SKL-001 — K3 Contract Baseline"
document_type: "contract-baseline"
document_role: "Fixe la baseline contractuelle K3 applicable à YD-MS-SKL-001."
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

# YD-MS-SKL-001 — K3 Contract Baseline

> **Rôle du document**
> Fixe la baseline contractuelle K3 applicable à YD-MS-SKL-001.
> **Usage développement :** référence contractuelle obligatoire pour les implémentations et intégrations concernées.

Statut : `K3-CONTRACT-BASELINE / IMPLEMENTATION-PENDING`
Nature : `AUTH`

## 1. Portée

SKL-001 est l'autorité YDIASE sur les compétences, concepts de connaissance, taxonomies et relations sémantiques gouvernées. K3 fixe les contrats logiques nécessaires sans choisir protocole, broker, datastore ou format physique.

## 2. Objets autoritatifs

- `Skill`
- `KnowledgeConcept`
- `SkillRelation`
- `SkillTaxonomyMapping`

Chaque objet canonique conserve un ID durable, une version, son statut, sa provenance de gouvernance et sa temporalité applicable.

SKL-001 ne possède jamais `UserSkill`, un profil individuel ou un curriculum Education.

## 3. Contrats entrants

### Education

SKL peut recevoir des références de curricula/modules et des evidence candidates depuis `YD-MS-EDU-003`. Ces entrées peuvent proposer des relations ou besoins de mapping. Elles ne mutent jamais automatiquement une compétence canonique.

### Career

Les signaux métiers/carrières peuvent proposer des besoins de compétences, relations ou mappings. Ils restent evidence jusqu'à validation SKL.

### Data

Les sources DAT peuvent fournir provenance, qualité, taxonomies externes et evidence. Une source externe n'obtient aucun ownership canonique SKL.

Entrée minimale :
- `source_ref`
- `source_version`
- `source_domain`
- `evidence_type`
- `observed_at` ou temporalité applicable
- provenance
- qualité/confiance si disponible
- territoire si applicable

Une entrée incompatible, non versionnée ou sans provenance requise est rejetée ou isolée pour revue.

## 4. Contrats sortants

SKL publie des références versionnées vers ses objets autoritatifs et des événements de cycle de vie.

Sortie minimale applicable :
- ID canonique SKL
- version
- type d'objet
- statut
- validité
- version de taxonomie
- provenance de gouvernance applicable

Les consommateurs ne doivent pas reconstruire l'autorité SKL depuis une projection locale.

## 5. Contrat de données

### Skill

Identité canonique d'une compétence gouvernée, versionnée et non personnelle.

### KnowledgeConcept

Concept de connaissance gouverné pouvant être relié à des Skills sans devenir un profil utilisateur.

### SkillRelation

Relation sémantique gouvernée entre objets SKL. Elle conserve type, source de décision, version et temporalité.

### SkillTaxonomyMapping

Mapping versionné entre référentiels. Il conserve les deux références, la méthode/decision de mapping, provenance, statut et version.

## 6. Invariants

- Aucun `UserSkill` n'est possédé par SKL-001.
- EDU/CAR/DAT peuvent fournir evidence, jamais publier seuls une mutation canonique SKL.
- Une IA peut proposer, jamais publier seule un objet canonique.
- Toute mutation canonique est versionnée et traçable.
- Provenance obligatoire pour les mappings et relations dérivés d'une source externe.
- Aucune transaction distribuée n'est requise avec EDU, CAR ou DAT.
- Les boucles inter-domaines restent asynchrones/evidence-driven.
- Une projection consommateur ne devient jamais source de reconstruction de SKL.

## 7. Exigences traçables

| ID | Exigence |
|---|---|
| SKL-REQ-001 | Maintenir l'autorité exclusive sur les objets canoniques SKL. |
| SKL-REQ-002 | Conserver IDs durables et versions. |
| SKL-REQ-003 | Conserver provenance des evidence, mappings et relations applicables. |
| SKL-REQ-004 | Empêcher une mutation canonique automatique depuis EDU/CAR/DAT. |
| SKL-REQ-005 | Empêcher une publication canonique autonome par IA. |
| SKL-REQ-006 | Isoler ou rejeter les entrées incompatibles/non traçables. |
| SKL-REQ-007 | Publier des changements versionnés consommables sans transaction distribuée. |
| SKL-REQ-008 | Garder UserSkill et profils individuels hors ownership SKL. |
| SKL-REQ-009 | Conserver un store autoritatif indépendant de ses caches/projections. |
| SKL-REQ-010 | Préserver une taxonomie précédente exploitable lorsqu'une nouvelle version/mapping est invalide. |

## 8. Versionnement

- ID canonique stable pendant la vie logique de l'objet.
- Mutation sémantique : nouvelle version de l'objet.
- Changement incompatible de contrat : nouvelle version majeure du contrat.
- Ajout compatible : évolution compatible documentée.
- Taxonomie, objet métier et contrat possèdent des versions distinctes.
- Les consommateurs doivent connaître la version qu'ils utilisent.

## 9. Compatibilité et dépréciation

- Une version consommée n'est pas retirée sans règle de migration.
- Une relation supprimée/invalidée est publiée comme telle, pas effacée silencieusement de l'historique gouverné.
- Les consommateurs ne doivent pas interpréter un type de relation inconnu comme équivalent à un type connu.
- Une nouvelle taxonomie peut coexister avec la précédente pendant une migration.
- La durée physique de coexistence reste `TBD-PREPROD`.

## 10. ADR

Les décisions structurelles sont enregistrées dans `ADR-SKL-001-AUTHORITATIVE-SKILLS-KNOWLEDGE.md`.

## 11. Limites

K3 ne ferme pas gouvernance taxonomique opérationnelle, IAM physique, RPO/RTO/SLO, rétention physique, restore test, format de schéma, protocole, broker ou datastore.

Ces éléments restent à traiter aux niveaux de gouvernance, vérification ou implémentation applicables.
