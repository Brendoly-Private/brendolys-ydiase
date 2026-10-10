---
document_id: "YD-DOC-POL-ANL-001-ANALYTICS-METRIC"
title: "YD-MS-ANL-001 — Analytics Metric Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de analytics metric pour YD-MS-ANL-001."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "policy"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-ANL-001 — Analytics Metric Policy

> **Rôle du document**
> Établit les règles normatives de analytics metric pour YD-MS-ANL-001.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `ANALYTICS-SEMANTICS-DEFINED / METRIC-CATALOG-REGISTRATION-REQUIRED`

## 1. Rôle

ANL-001 transforme des faits/projections gouvernés en métriques, datasets analytiques, snapshots et runs reproductibles.

ANL-001 est `DERIVED`. Il n'est jamais autorité sur un fait métier source et ne réécrit jamais EDU, SKL, CAR, LAB, OPP, APP, EMP, CNT, LRN, CNS, CFG ou un autre domaine.

Chaîne normative :

`Source autoritative → contrat Analytics enregistré → AnalyticalDataset → AnalysisRun → MetricDefinition appliquée → AggregateSnapshot`.

## 2. Agrégats possédés

ANL-001 possède uniquement :
- `MetricDefinition` ;
- `AnalyticalDataset` ;
- `AnalysisRun` ;
- `AggregateSnapshot`.

Le fait qu'une métrique soit autoritative dans ANL signifie uniquement que **la définition/calcul/édition analytique** appartient à ANL. Le fait métier sous-jacent reste autoritatif dans son domaine source.

## 3. MetricDefinition

Toute métrique calculable doit déclarer au minimum :
- `metric_ref` et version ;
- nom et définition métier ;
- finalité analytique ;
- population/univers ;
- grain ;
- dimensions autorisées ;
- mesure/agrégation ;
- période/fenêtre temporelle ;
- contrats sources exacts et versions compatibles ;
- traitement des UNKNOWN/NULL/non-applicable ;
- traitement corrections, suppressions et révocations ;
- méthodologie/version ;
- règles de qualité minimales ;
- classification Privacy ;
- règle de fraîcheur ;
- owner analytique ;
- état de publication.

Une métrique sans contrat source, grain, finalité ou méthodologie déterminable est `NOT-REGISTERED` et ne doit pas être publiée.

## 4. États d'une MetricDefinition

`DRAFT → REVIEWED → ACTIVE → DEPRECATED → RETIRED`.

`SUSPENDED` peut interrompre le calcul/publication sans supprimer l'historique.

Une modification de formule, population, grain, définition d'une dimension ou traitement des UNKNOWN qui change le sens de la métrique crée une nouvelle version méthodologique. Aucun recalcul historique silencieux.

## 5. AnalyticalDataset

Un dataset analytique est une projection gouvernée et reconstructible. Il conserve :
- dataset/version ;
- source contract IDs ;
- source schema/version ;
- source watermarks/checkpoints ;
- période couverte ;
- territoire/contexte CFG ;
- purpose/privacy binding ;
- transformations/version ;
- quality/provenance refs ;
- freshness state.

Il n'est ni une sauvegarde du domaine source ni un canal alternatif d'écriture métier.

## 6. AnalysisRun

Chaque run conserve :
- run_ref ;
- metric/methodology versions ;
- dataset/input snapshot refs ;
- source watermarks ;
- période/scope ;
- started/completed timestamps ;
- quality checks ;
- résultat ou failure state ;
- code/transformation version lorsqu'applicable.

Rejouer un ancien `AggregateSnapshot` restaure son édition historique ; cela ne signifie pas recalculer avec la méthodologie actuelle.

## 7. AggregateSnapshot

Un snapshot publié contient au minimum :
- snapshot_ref ;
- metric refs/versions ;
- scope et période ;
- valeurs/agrégats ;
- methodology version ;
- source snapshot/watermark refs ;
- produced_at ;
- freshness ;
- quality/coverage ;
- uncertainty/limitations lorsque pertinentes ;
- privacy/access class.

Une correction crée une nouvelle édition/version. L'ancienne reste traçable selon politique de rétention.

## 8. UNKNOWN, absence et zéro

`UNKNOWN ≠ 0 ≠ NOT-APPLICABLE ≠ MISSING`.

ANL ne transforme jamais automatiquement une donnée absente en zéro. La règle d'imputation, si autorisée, appartient à la méthodologie versionnée et doit être visible dans la provenance du résultat.

## 9. Comparabilité

Deux métriques/snapshots ne sont comparables que si la MetricDefinition l'autorise au regard des versions de méthodologie, populations, grains, périodes, territoires, couvertures et sources.

Si la comparabilité ne peut être démontrée : `NOT-COMPARABLE`.

Un changement de pays, cadre CFG ou source ne doit jamais être masqué par une continuité graphique artificielle.

## 10. Privacy et minimisation

ANL privilégie l'agrégation. Les événements/projections personnels ne sont consommés que si une métrique enregistrée les exige et si purpose/CNS/retention l'autorisent.

Interdits :
- ingestion « au cas où » de tous les événements ;
- dataset nominatif permanent pour simple commodité analytique ;
- contournement d'une révocation via snapshot historique opérationnel ;
- ré-identification à partir d'agrégats ;
- exposition de petits segments sensibles sans politique validée.

Les seuils numériques de confidentialité/agrégation restent `TBD-LEGAL/PREPROD`.

## 11. Corrections, suppressions et révocations

Le contrat source détermine l'événement/projection autoritative.

ANL doit supporter selon le contrat :
- correction/version supérieure ;
- DELETE ;
- WITHDRAW/EXPIRE ;
- REVOKE/privacy restriction ;
- reclassification.

Une ancienne version ne ressuscite jamais une donnée retirée par une version plus récente.

Une révocation Privacy peut exiger suppression, anonymisation, exclusion de futurs calculs ou conservation restreinte selon la politique gouvernée applicable ; ANL n'invente pas la règle juridique.

## 12. Fraîcheur

États :
- `FRESH`
- `STALE-ACCEPTABLE`
- `EXPIRED`
- `UNKNOWN`.

Une métrique ne peut être FRESH si une source obligatoire a un watermark inconnu ou incompatible.

Les seuils temporels sont propres aux familles de métriques et restent `TBD-PREPROD` jusqu'à validation.

## 13. Reconstruction

ANL-001 doit supporter :
- `FULL_REBUILD` ;
- `PARTIAL_REBUILD` par dataset/période/territoire lorsque sûr ;
- `CATCH_UP` depuis checkpoints.

Le rebuild part des contrats sources enregistrés, jamais d'une autre projection analytique présentée comme vérité de secours.

Pendant rebuild, DELETE/REVOKE/corrections ont priorité sémantique sur les anciens UPSERT.

## 14. Consommateurs

ANL-002/003, INT-001 et DPR-001 peuvent consommer `YD-CTR-ANL-SNAPSHOT-v1`.

Ils ne doivent pas :
- réinterpréter une métrique sous le même ID ;
- supprimer methodology/source version ;
- présenter un snapshot stale comme actuel ;
- transformer une corrélation analytique en fait causal ou décision individuelle sans politique distincte.

## 15. IA

Une IA peut assister à expliquer, explorer ou proposer une analyse, mais :
- ne crée pas seule une MetricDefinition ACTIVE ;
- ne remplace pas les sources autoritatives ;
- ne fabrique pas une valeur absente ;
- toute métrique publiée reste reproductible par méthodologie et sources versionnées.

## 16. Gates

Avant `REBUILDABLE` :
- catalogue de métriques enregistré ;
- contrats sources concrets ;
- Privacy/purpose validés ;
- snapshot/replay/watermarks prouvés ;
- FULL_REBUILD exécuté ;
- corrections/delete/revoke testés ;
- convergence mesurée ;
- SLO/freshness/RTO validés.

Statut : `ANALYTICS-SEMANTICS-CLOSED / METRIC-INSTANCES-AND-REBUILD-EVIDENCE-PENDING`.
