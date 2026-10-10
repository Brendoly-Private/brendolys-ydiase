---
document_id: "YD-DOC-DOM-ORIENTATION-RECOMMENDATION-FRONTIERES-ET-DEPENDANCES"
title: "Frontières et dépendances — Orientation et recommandation"
document_type: "domain-knowledge"
document_role: "Documente la connaissance métier et les frontières applicables au domaine concerné."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "domain"
---

# Frontières et dépendances — Orientation et recommandation

Statut : `DOMAIN-REVIEW-CANDIDATE`

## ASM-001 — Assessment

Possède :
- AssessmentDefinition ;
- AssessmentSession ;
- AssessmentResponse ;
- AssessmentResult ;
- validité, confiance et version méthodologique associées.

Consomme Identity/Profile refs, CNS, CFG et SKL-001 lorsque la méthodologie référence une taxonomie.

Un AssessmentResult est une mesure produite selon une méthode. Il ne devient pas automatiquement UserSkill ; SKL-002 décide de son intégration selon sa politique de dérivation.

## ORI-001 — Orientation

Possède :
- OrientationCase ;
- OrientationObjective ;
- OrientationConstraintSet ;
- OrientationDecisionRecord.

Il orchestre les données autorisées provenant de PRF, EDU, SKL, ASM, CAR, LAB et REC sans en reprendre l'ownership.

## ORI-002 — Comparison & Decision Support

Responsabilité logique hébergée dans YD-MS-ORI-001 :
- ComparisonCase ;
- ComparisonSet ;
- DecisionCriterion ;
- DecisionScorecard.

Les critères spécifiques au dossier appartiennent à Orientation. Les préférences générales restent PRF-001.

Decision Support compare et documente ; il ne crée pas un ranking REC concurrent.

## REC-001 — Recommendation

Frontière physique distincte. Produit RecommendationRun/Set/Item/Explanation/EvidenceSnapshot. Son ranking sera gouverné par une politique séparée.

## Flux structurants

| Producteur | Consommateur | Objet | Règle |
|---|---|---|---|
| ASM-001 | ORI/REC/SKL-002 | AssessmentResultRef/projection minimale | ASM reste autorité |
| SKL-002 | ORI/REC | état de compétence minimisé | pas d'écriture retour |
| CAR | ORI/REC | métiers, paths/transitions | refs/version |
| EDU | ORI/REC | institutions/programmes/qualifications | refs/version |
| LAB | ORI/REC | signaux/intelligence datés | jamais certitude |
| REC-001 | ORI-001 | RecommendationResultRef/version | ORI ne recalcule pas le ranking REC |
| ORI-001 | REC-001 | job/request contextualisé | asynchrone/contrat, pas boucle synchrone |

## Fusion ORI-001 + ORI-002

Maintenue. Extraction uniquement si Decision Support acquiert durablement une consommation transverse, datastore, équipe, SLO, cycle de déploiement ou ownership propre.

## Interdictions

- ASM déclarant une compétence acquise ;
- ORI modifiant PRF/SKL/EDU/CAR/LAB ;
- ORI recopiant le moteur de ranking REC ;
- REC décidant à la place du sujet et écrivant OrientationDecisionRecord ;
- boucle synchrone ORI ↔ REC ;
- résultat ancien présenté comme actuel sans date/version ;
- IA inventant une justification ou une mesure ;
- support interne accédant aux dossiers sans autorisation/audit.

## Récupération

ASM et ORI ont chacun leur chaîne de backup/restore C1. Les services consommés ne sont jamais leurs backups. Après restore, les références externes sont réconciliées sans transfert d'ownership.

Statut : `BOUNDARIES-STABLE-CANDIDATE`.
