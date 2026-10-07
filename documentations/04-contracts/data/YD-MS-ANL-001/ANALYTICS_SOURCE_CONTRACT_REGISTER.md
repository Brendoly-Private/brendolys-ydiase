---
document_id: "YD-DOC-CON-ANL-001-SOURCE-REGISTER"
title: "ANL-001 — Analytics Source Contract Register"
document_type: "contract-register"
document_role: "Enregistre les familles de contrats sources autorisables pour ANL-001."
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

# ANL-001 — Analytics Source Contract Register

> **Rôle du document**
> Enregistre les familles de contrats sources autorisables pour ANL-001.
> **Usage développement :** référence contractuelle obligatoire pour les implémentations et intégrations concernées.

Statut : `SOURCE-FAMILIES-REGISTERED / METRIC-INSTANCES-PENDING`

## 1. Règle

ANL-001 n'a pas le droit de consommer « tous les événements ». Une source n'est autorisée que si une `MetricDefinition` ACTIVE référence explicitement un contrat ci-dessous, sa finalité, son grain, sa version et ses règles Privacy.

Le placeholder `YD-CTR-<DOMAIN>-ANALYTICS-v1` du Contract Registry représente cette famille gouvernée ; les instances ci-dessous sont ses familles sources candidates autorisées. Elles ne signifient pas que toutes les données du domaine sont automatiquement exportables.

## 2. Familles enregistrées

| Instance ID | Owner source | Finalités candidates | Données minimales candidates | Privacy | Criticité | État |
|---|---|---|---|---|---|---|
| `YD-CTR-EDU-ANALYTICS-v1` | EDU | couverture programmes/curricula, catalogues et tendances éducatives | refs/version, institution/program/curriculum/qualification dimensions autorisées, timestamps, territory | PUBLIC/INTERNAL | K2 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-SKL-ANALYTICS-v1` | SKL | agrégats de compétences/connaissances | skill/taxonomy refs/version, agrégats autorisés, territory/period | CONTEXTUAL | K2 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-CAR-ANALYTICS-v1` | CAR | structure occupations/parcours/gaps agrégés | occupation/path refs/version, dimensions autorisées, period/territory | CONTEXTUAL | K2 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-ASM-ANALYTICS-v1` | ASM | qualité/usage agrégé des assessments | definition/method refs/version, result aggregates, validity/coverage; pas de réponse brute par défaut | SENSITIVE/AGGREGATED | K1 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-ORI-ANALYTICS-v1` | ORI | parcours d'orientation agrégés | case state/objective type/decision state/timestamps/version; subject_ref exclu sauf nécessité autorisée | SENSITIVE/AGGREGATED | K1 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-REC-ANALYTICS-v1` | REC | qualité/couverture/stabilité des recommandations | run/policy/model refs, recommendation type, abstention/coverage/uncertainty aggregates, version | SENSITIVE/AGGREGATED | K1 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-LAB-ANALYTICS-v1` | LAB | séries/indicateurs marché du travail | signal/indicator refs, territory, period, methodology, coverage, uncertainty, version | INTERNAL/AGGREGATED | K2 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-OPP-ANALYTICS-v1` | OPP | stock/flux d'opportunités, délais et exigences agrégées | opportunity type/status, territory, timestamps, requirement dimensions autorisées, version | INTERNAL/AGGREGATED | K2 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-APP-ANALYTICS-v1` | APP | funnel candidature agrégé | application state transitions/timestamps, opportunity/employer dimensions autorisées, version; subject minimisé | VERY-SENSITIVE/AGGREGATED | K1 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-EMP-ANALYTICS-v1` | EMP | activité recrutement/employeurs agrégée | employer/campaign/selection dimensions autorisées, states/timestamps/version | CONFIDENTIAL/AGGREGATED | K1 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-LRN-ANALYTICS-v1` | LRN | disponibilité/découverte de ressources | resource/type/provider/skills/language/modality/availability/version | INTERNAL/AGGREGATED | K2 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-CNT-ANALYTICS-v1` | CNT/COM/MOD | contenu/engagement/modération agrégés | content/activity/moderation dimensions autorisées, states/timestamps/version | CONTEXTUAL/AGGREGATED | K2 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-NTF-ANALYTICS-v1` | NTF | qualité de livraison notification | channel/status/attempt/timestamps/template class; recipient exclu des métriques standards | SENSITIVE-MIN/AGGREGATED | K2 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-CFG-ANALYTICS-v1` | CFG | contextualisation pays/territoire | country/territory/framework/config version | INTERNAL/PUBLIC | K2 | REGISTERED-NOT-ACTIVATED |
| `YD-CTR-DAT-ANALYTICS-v1` | DAT | provenance/qualité/couverture data | source/provenance/quality/validation refs, states, timestamps, versions | CONTEXTUAL | K2 | REGISTERED-NOT-ACTIVATED |

## 3. Sources non autorisées par défaut

Aucune ingestion analytique automatique n'est accordée par ce registre à :
- données brutes DAT-002 ;
- payloads complets PRF-001/002 ;
- consent records complets CNS ;
- secrets/credentials ;
- contenu privé intégral ;
- réponses d'assessment détaillées ;
- documents de candidature ;
- données de paiement détaillées ;
- corpus AI.

Si une métrique future en a réellement besoin, une extension explicite avec Privacy/purpose/minimisation/retention est obligatoire.

## 4. Activation d'une instance

`REGISTERED-NOT-ACTIVATED → ACTIVE-FOR-METRIC` seulement lorsqu'au moins une MetricDefinition approuvée déclare :
- instance contract ID ;
- champs exacts ;
- grain ;
- finalité ;
- version ;
- rétention ;
- Privacy/purpose ;
- correction/delete/revoke semantics ;
- snapshot/replay ;
- quality/freshness.

Une activation peut être limitée à une seule métrique. Elle n'autorise pas les autres champs du domaine.

## 5. Publication sortante

ANL-001 publie ses snapshots via `YD-CTR-ANL-SNAPSHOT-v1`. ANL-002/003, INT et DPR restent responsables de leurs propres produits dérivés.

Statut : `ANALYTICS-SOURCE-FAMILIES-REGISTERED / NO-BLANKET-DOMAIN-INGESTION`.
