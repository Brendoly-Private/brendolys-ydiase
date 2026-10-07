---
document_id: "YD-DOC-FND-GOV-REG-002"
title: "Matrice de traçabilité — BRENDOLYS YDIASE"
document_type: "traceability-matrix"
document_role: "Contrôle la traçabilité entre intentions, capacités, exigences, décisions, frontières, contrats et vérifications."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "view"
canonical: false
development_usage: "supporting-reference"
owners:
  - "Documentation Governance"
depends_on:
  - "YD-DOC-FND-GOV-001"
  - "YD-STD-DOC-META-001"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "foundation"
  - "governance-register"
---

# Matrice de traçabilité — BRENDOLYS YDIASE

> **Rôle du document**
> Contrôle la traçabilité entre intentions, capacités, exigences, décisions, frontières, contrats et vérifications.
> **Usage développement :** support de traçabilité ; les sources canoniques référencées restent autoritatives.

Statut : `ACTIVE-BASELINE`

## 1. Objet

Cette matrice vérifie que les décisions techniques importantes peuvent remonter vers une intention, un domaine/capacité et une exigence. Elle reste volontairement au niveau baseline tant que les dossiers 01 à 12 ne sont pas entièrement revus.

Une case `À ÉTABLIR 01-12` signifie que la relation métier doit être créée pendant la revue correspondante. Elle ne doit pas être inventée ici.

| Intention / vision | Domaine / capacité | Exigence | Règle / décision | Frontière ou composant | Contrat / interface | Vérification | État |
|---|---|---|---|---|---|---|---|
| Données fiables et traçables | Data Governance | YD-REQ-GOV-001, YD-REQ-DATA-001 | owner + provenance obligatoires | `YD-MS-DAT-*` + owners métier | contrats source à formaliser | registre autoritatif + provenance | PARTIAL |
| Respect des personnes | Privacy | YD-REQ-GOV-002 | CNS reste autorité privacy | `YD-MS-CNS-001` | PrivacyDecision | revue conformité | PARTIAL |
| Orientation fondée sur des faits | Orientation | YD-REQ-DATA-003 | offres ≠ marché réel | ORI/REC/LAB/ANL | À ÉTABLIR 01-12 | méthodologie + tests produit | PARTIAL |
| IA sous contrôle | AI/Data | YD-REQ-DATA-001 | IA non source de vérité | `YD-PLT-AI-001`, `YD-MS-AI-002/003` | grounding/verification contracts | évaluation + provenance | PARTIAL |
| Autonomie des frontières | Architecture | YD-REQ-SVC-001, YD-REQ-SVC-002 | 51 frontières D3 candidate | 47 MS + 4 PLT | Dependency/Event Map puis Registry | AUTONOMY_PROFILE | DEFINED-D3 |
| Reprise des projections | Data/Resilience | YD-REQ-DER-001, YD-REQ-DER-002 | règle DERIVED | SRH, CNT-002, KNW, ANL-001, AI-002 | familles source v1 | FULL_REBUILD | PREPROD |
| Identité centralisée sans fusion des rôles | IAM | YD-REQ-IAM-001, 002, 003 | 3 realms séparés | Identity externe + consommateurs | audiences/scopes par contrat | tests authN/authZ | PARTIAL |
| Protection réseau | Security | YD-REQ-SEC-001 | deny-by-default | 51 frontières | flux Dependency Map | policy tests | ADR/PREPROD |
| Secrets protégés | Security | YD-REQ-SEC-002 | secrets hors Git/logs | 51 frontières | n/a | scans/revue logs | PREPROD |
| Continuité mesurable | Resilience | YD-REQ-RES-001, 002 | test avant déclaration valide | 51 frontières | n/a | restore/DR/rebuild | PREPROD |
| Distribution Data gouvernée | Data Products | YD-REQ-DPR-001, 002 | DPR + CNS + droits source + BIL | `YD-MS-DPR-001`, CNS, BIL | LicenseManifest/PrivacyDecision | gate publication | DEFINED-D3 |
| Contrats évolutifs | Contract Governance | YD-REQ-CTR-001, 002 | Registry candidat autorisé | producteurs/consommateurs | Contract Registry à construire | contract review | NEXT |
| Expansion panafricaine | Multi-pays | YD-REQ-CTY-001 | Country Framework obligatoire | domaines concernés | contrats localisés si nécessaire | revue pays | PARTIAL |

## 2. Chaîne cible

La chaîne cible complète est :

`vision → problème → partie prenante → domaine → capacité → exigence → règle métier → décision → bounded context → service logique → frontière physique → donnée/agrégat → contrat API/événement/projection → vérification → phase/pays`.

Toutes les relations ne sont pas encore remplies. Le remplissage métier se fait pendant l'audit des dossiers 01 à 12. La matrice ne doit pas rétro-inventer des justifications pour préserver une architecture existante.

## 3. Gate de reprise architecture

Avant de considérer l'architecture comme confirmée après revue métier :

1. les capacités produit critiques doivent être tracées
2. les domaines doivent confirmer leurs frontières
3. les exigences nouvelles doivent être propagées
4. les 51 frontières doivent être comparées aux résultats métier
5. les divergences doivent produire maintien, modification, fusion, scission ou retrait documenté

## 4. Dette documentaire connue

- fondations produit encore insuffisantes
- exigences métier détaillées à créer dans 02→11
- taxonomie Data/Knowledge/Analytics/AI à confirmer dans 12
- contrats individuels non encore enregistrés
- vérifications opérationnelles préproduction non exécutées

Cette dette est explicite et ne remet pas en cause la baseline de gouvernance du dossier 00.
