---
document_id: "YD-DOC-POL-LRN-001-LEARNING-DISCOVERY"
title: "YD-MS-LRN-001 — Learning Discovery Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de learning discovery pour YD-MS-LRN-001."
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
---

# YD-MS-LRN-001 — Learning Discovery Policy

> **Rôle du document**
> Établit les règles normatives de learning discovery pour YD-MS-LRN-001.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-BASELINE / IMPLEMENTATION-PENDING`
Nature : `MIXED`
Criticité : `C2`

## 1. Mission et autorité

LRN-001 permet de découvrir et relier des options d'apprentissage à un besoin explicite.

Il possède :
- `LearningResource` pour le catalogue complémentaire propre à YDIASE ;
- `LearningOfferingRef` comme référence vers une offre détenue ailleurs ;
- `LearningRecommendationSet` pour un résultat spécialisé de découverte learning.

Il ne possède ni `Program` académique EDU, ni `Skill`/niveau individuel SKL, ni listing/commande Marketplace MKT.

## 2. Ressource ≠ programme ≠ offre commerciale ≠ compétence acquise

Une ressource learning décrit un contenu ou moyen d'apprentissage.

Un programme académique reste EDU-002/003/004 selon son objet.

Une offre commerciale (prix, disponibilité à l'achat, vendeur, commande) reste MKT-001.

Le fait de consulter, terminer ou acheter une ressource ne crée jamais automatiquement une compétence SKL-002. Une preuve/évaluation gouvernée est nécessaire selon les règles SKL/ASM.

## 3. LearningResource

Une ressource propre conserve au minimum :
- resource_ref/version ;
- title/type/provider/source ;
- learning outcomes déclarés ;
- skill/knowledge mappings versionnés ;
- prerequisites ;
- language ;
- modality ;
- territory/accessibility lorsque pertinent ;
- duration/workload si connu ;
- provenance/quality ;
- rights/usage constraints ;
- freshness/status.

États minimaux : `DRAFT`, `ACTIVE`, `LIMITED`, `STALE`, `WITHDRAWN`, `RETIRED`.

## 4. LearningOfferingRef

LRN peut référencer une formation EDU ou un listing MKT sans copier son autorité.

La référence conserve source domain, object/version, availability/freshness watermark et les projections strictement nécessaires à la découverte.

Si l'offre commerciale n'est plus vérifiable/disponible, elle est masquée comme offre achetable ; la ressource pédagogique sous-jacente peut rester découvrable si son autorité la maintient valide.

## 5. Skill gap → option d'apprentissage

Un gap SKL/CAR/ORI est une entrée, jamais une vérité créée par LRN.

La correspondance conserve :
- gap/skill ref/version ;
- target outcome ;
- resource/program ref/version ;
- mapping type et force/confiance ;
- prerequisite state ;
- evidence/provenance ;
- unknowns.

Un mapping "couvre cette compétence" ne garantit pas que l'utilisateur acquerra la compétence.

## 6. Prérequis et éligibilité

Les prérequis sont séparés en `HARD`, `REQUIRED`, `PREFERRED`, `INFORMATIONAL` selon la source/policy applicable.

`UNKNOWN` n'est jamais `FAILED`. Une donnée critique inconnue entraîne statut conditionnel ou abstention selon policy.

LRN ne contourne pas une exigence EDU officielle ou une restriction fournisseur.

## 7. Durée, coût et disponibilité

Une durée, un coût, une bourse, une place disponible ou une date de session n'est affiché comme actuel que si sa source/version/fraîcheur le permet.

Si aucune source fiable n'existe : `UNKNOWN`. LRN n'invente pas un prix moyen, une durée ou une disponibilité.

Les coûts commerciaux restent MKT ; LRN peut en consommer une projection datée.

## 8. Découverte et recommandation learning

Un `LearningRecommendationSet` spécialisé peut ordonner des options selon adéquation au gap, prérequis, qualité, langue, modalité, contraintes utilisateur, disponibilité et autres critères organiques gouvernés.

Si REC-001 orchestre une recommandation cross-domain, LRN fournit candidats/signaux/résultats spécialisés ; LRN ne devient pas un second moteur générique REC.

Paiement, commission, sponsoring ou relation partenaire ne modifie jamais le rang organique learning. Tout placement commercial est séparé et explicitement étiqueté.

## 9. Evidence Snapshot et explicabilité

Tout résultat personnalisé persistant référence :
- gap/profile/skill versions minimisées ;
- resource/program/offering versions ;
- mappings ;
- CFG/context ;
- CNS purpose/decision si applicable ;
- policy version ;
- freshness/quality.

L'explication expose pourquoi l'option correspond, quels gaps elle vise, prérequis, limites/inconnues, provenance majeure et fraîcheur.

## 10. Progression et achèvement

LRN-001 n'est pas, par cette baseline, l'autorité d'un LMS complet.

Si YDIASE doit posséder inscriptions pédagogiques, progression détaillée, devoirs, sessions, évaluations, complétion/certification ou learning records autoritatifs, cela déclenche une revue de frontière et potentiellement un microservice distinct.

Aucun `LRN-002` physique n'est créé sans cette autorité/cycle autonome démontré.

## 11. Correction

Correction d'un mapping, programme, ressource, prix ou disponibilité ne réécrit pas silencieusement un ancien RecommendationSet. Il est daté/stale/invalidated et un nouveau calcul utilise les nouvelles versions.

## 12. Privacy et mineurs

La personnalisation utilise uniquement les données nécessaires et une finalité autorisée. Les règles spécifiques aux mineurs, contenus restreints ou territoires restent gouvernées par CNS/CFG et policies applicables.

## 13. Gates

`DEFINED` : frontières EDU/SKL/MKT/REC, modèle ressource, mappings gap-learning, prérequis, UNKNOWN, coût/durée/disponibilité, ranking organique, evidence snapshot, limite LMS/LRN-002.

`TBD-PREPROD` : taxonomie réelle des ressources, règles de mapping/seuils, droits d'usage, freshness MKT/EDU, fairness si ranking personnalisé, IAM/IDOR, rétention, SLO/RPO/RTO, restore et contrats physiques.

Statut final : `LEARNING-DISCOVERY-SEMANTICS-CLOSED / MAPPINGS-AND-PREPROD-EVIDENCE-PENDING`.
