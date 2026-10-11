---
document_id: "YD-DOC-ADR-ENT-DERIVED-MIXED"
title: "ADR candidat — ownership DERIVED/MIXED Entrepreneurship"
document_type: "architecture-decision"
document_role: "Documente les propositions et vérifications restantes sans modifier les sources canoniques existantes."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
created_at: "2026-10-11"
last_reviewed_at: "2026-10-11"
---

# ADR candidat — ownership DERIVED/MIXED Entrepreneurship

Statut : **PROPOSED / NOT-APPROVED**. Ne remplace pas les classifications DDD cibles existantes.

## Question
Comment distinguer les états métier persistants et les calculs reconstructibles dans ENT-002, ENT-004 et ENT-005, sans dupliquer les autorités LAB/PRT/PRF/SKL ?

## Contexte et forces
Les profils DDD classent ENT-002 et ENT-005 DERIVED/MIXED, ENT-004 AUTH/MIXED. Le référentiel `YD-REQ-DER-001` interdit à une frontière purement DERIVED de détenir un fait irremplaçable. La confidentialité et la révocation imposent de séparer sources, autorisations et calculs.

## Décision proposée
- **ENT-002** : hypothèses, jeux de preuves et assessments calculés sont reconstructibles à partir de snapshots autorisés et versionnés ; tout enrichissement humain irréconstructible doit être identifié comme état AUTH distinct, sinon ne pas prétendre que le service est purement DERIVED.
- **ENT-004** : les fiches et règles publiées/validées dans YDIASE sont l'état de catalogue propre au service ; les évaluations personnalisées sont des snapshots expirables, jamais des décisions de prêteur.
- **ENT-005** : TeamNeed, visibilité et modifications explicites sont persistants et autoritatifs dans ENT-005 ; scores, runs et explications sont dérivés, reconstructibles ou invalidables selon les sources et autorisations disponibles.
- Chaque état persistant non reconstructible exige sauvegarde/restauration indépendante ; chaque état DERIVED exige FULL_REBUILD, replay, watermark et convergence avant production.

## Alternatives considérées
1. Tout déclarer DERIVED : rejet proposé, car TeamNeed et certaines validations de catalogue seraient irréconstructibles.
2. Tout déclarer AUTH : rejet proposé, car le matching et les estimations dépendent de sources extérieures.
3. Fusionner les services avec leurs sources : rejet proposé, contredit les frontières DDD conservées.

## Conséquences et coûts
Séparation des stockages logiques et responsabilités de reprise ; nécessité de versionner les sources et d'assurer l'invalidation. Aucun broker, moteur de calcul ou datastore n'est imposé.

## Sécurité, conformité et données
CNS gouverne la décision Privacy ; un retrait ou une révocation interdit la réexposition d'un snapshot ancien. Les données de personnes sont minimisées ; aucun ENT n'écrit dans PRF/SKL/LAB/PRT.

## Réversibilité et migration
Si une revue prouve que ENT-002 détient un état non reconstructible, documenter son owner et ses procédures de restauration ; modifier la qualification après analyse d'impact, pas silencieusement.

## Vérifications et preuves attendues
Inventaire des états par agrégat, source et méthode de reconstruction ; matrice de retrait ; tests de rebuild/restore ; revue des contrats et Privacy. **Aucune preuve runtime actuellement attestée.**

## Approbation et date de revue
Approbation humaine **en attente**. La création de ce document ne constitue pas une approbation d'ADR ni K3 PASS.


## Inventaire des états et conditions de décision — version candidate finalisée

| Service | Agrégat / état | Owner de vérité | Classification proposée | Reconstruction / reprise |
|---|---|---|---|---|
| ENT-002 | OpportunityEvidenceSet sourcé | LAB/DAT/KNW pour les faits ; ENT-002 pour la composition | DERIVED si sources et sélection reproductibles | Replay des sources versionnées + watermark ; vérifier licence et rétractation |
| ENT-002 | EntrepreneurialOpportunityHypothesis calculée | ENT-002 pour l'interprétation, pas les faits sources | DERIVED sous condition | Recalcul déterministe ou version de méthode et provenance |
| ENT-002 | Annotation éditoriale irréconstructible, si introduite | ENT-002 explicitement | AUTH, **non encore démontré nécessaire** | Backup/restore ; décision spécifique avant introduction |
| ENT-004 | FundingOpportunity/FundingProgram publiés par YDIASE | ENT-004 pour fiche publiée ; source externe pour conditions du financeur | AUTH pour publication | Backup/restore + expiration des sources |
| ENT-004 | EligibilityRuleSet gouverné localement | ENT-004 pour la règle publiée | AUTH | Historique versionné, validation et restauration |
| ENT-004 | EligibilitySnapshot personnalisé | ENT-004 pour résultat indicatif | DERIVED | Recalcul sous version de règle et décision CNS valable |
| ENT-005 | TeamNeed, visibilité | ENT-005 | AUTH | Backup/restore, version et révocation |
| ENT-005 | FounderMatchRun/ComplementarityAssessment/MatchExplanation | ENT-005 pour résultat calculé ; PRF/SKL/CNS pour entrées | DERIVED | Recalcul conditionné par versions et droits actuels ; ne pas rejouer une divulgation |
| ENT-006 | VenturePlan/Milestone/ValidationResult | ENT-006 | AUTH | Backup/restore et historique ; VentureRef externe ENT-001 |

### Décisions structurelles explicitement conservées

- Aucun service DERIVED ne peut devenir autorité de PRF, SKL, LAB, DAT, KNW ou PRT.
- Les événements en retard ne rétablissent pas un état révoqué ; les tombstones et versions sont nécessaires.
- Une impossibilité de reconstruire ENT-002 ou les matches ENT-005 doit être traitée comme une lacune, pas masquée par le mot DERIVED.
- Le transport, les datastores et le partitionnement physiques restent hors de cet ADR logique et requièrent des décisions séparées si non triviaux.

### Validation restant nécessaire

L'inventaire ci-dessus constitue la **proposition d'arbitrage technique complète**, mais pas une approbation. Avant changement de statut : signature de l'autorité d'architecture, revue des owners ENT/LAB/DAT/KNW/PRT/PRF/SKL/CNS concernés, analyse d'impact, critères de reconstruction et références de preuves. Les tests FULL_REBUILD et restore restent préproduction.

**Verdict : READY-FOR-ARCHITECTURE-APPROVAL / NOT-APPROVED / K3-NOT-PASS.**
