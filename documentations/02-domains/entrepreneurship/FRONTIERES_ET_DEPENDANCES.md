---
document_id: "YD-DOC-DOM-ENTREPRENEURSHIP-FRONTIERES-ET-DEPENDANCES"
title: "Frontières et dépendances — Entrepreneurship"
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

# Frontières et dépendances — Entrepreneurship

Statut : DOMAIN-BASELINE / TARGET-BOUNDARIES-CANDIDATE

## ENT-001 — Venture Profile
Possède Venture, VentureObjective, VentureStage, VentureConstraint, VentureTeamRef et snapshots de contexte propres au projet. PRF reste owner de la personne.

## ENT-002 — Entrepreneurial Opportunity Intelligence
Possède EntrepreneurialOpportunityHypothesis, OpportunityEvidenceSet et OpportunityAssessmentSnapshot. Consomme signaux LAB/DAT/KNW. Une hypothèse ne devient jamais une certitude de demande ou rentabilité.

## ENT-003 — Entrepreneurship Support Ecosystem
Possède le catalogue fonctionnel SupportOrganization, IncubatorProgram, MentorOffering, EntrepreneurshipResource et règles d'éligibilité publiées. PRT reste owner de la relation partenaire.

## ENT-004 — Funding Opportunity
Possède FundingOpportunity, FundingProgram et EligibilitySnapshot. Ne possède ni compte bancaire ni décision du financeur.

## ENT-005 — Founder & Team Matching
Possède FounderMatchRun, TeamNeed, ComplementarityAssessment et MatchExplanation. Consentement/visibilité gouvernés ; aucune modification PRF/SKL.

## ENT-006 — Venture Progression
Possède VenturePlan, Milestone, Experiment, Assumption, ValidationResult et ProgressSnapshot. Suit le projet sans devenir comptabilité autoritative.

## Dépendances
PRF → ENT : objectifs/contexte autorisés.
SKL → ENT : compétences minimisées.
ASM → ENT/ORI : résultats versionnés.
LAB → ENT-002 : signaux économiques datés.
CFG → ENT : pays/territoire.
DAT/KNW → ENT-002 : provenance/relations.
PRT → ENT-003/004 : partenaires.
EDU/LRN → ENT : apprentissage.
ENT → ORI/REC : options/evidence/progression.
ENT → EMP/OPP : transition vers employeur/opportunités.

## Interdictions
Aucun ENT n'écrit PRF/SKL/LAB. REC ne crée pas de Venture. IA ne crée pas silencieusement une vérité de marché. Funding n'est pas un système bancaire. Founder Matching n'expose pas de profil sans autorisation. Aucun datastore partagé entre frontières ENT.

## Scale
Chaque ENT reçoit son Capacity Profile. ENT-002/005 peuvent utiliser calcul distribué asynchrone ; ENT-001/006 privilégient cohérence des agrégats ; ENT-003/004 sont fortement cacheables selon fraîcheur.


## Consolidation K2 — ownership, interfaces et décisions ouvertes (2026-10-10)

Cette section complète la baseline de domaine sans déclarer K3, K4 ou K5 acquis. Les six frontières sont des **candidats autonomes** : leurs profils individuels restent `DRAFT`. Les règles d'ownership ci-dessus priment sur les raccourcis de description des consommateurs.

### Invariants transversaux

1. Toute référence externe porte l'identifiant stable de son owner, et, pour les données évolutives, sa version ou son horodatage de validité ; une copie ENT n'acquiert jamais l'autorité source.
2. Une hypothèse entrepreneuriale, une estimation d'éligibilité et une suggestion de cofondateur sont des **résultats explicables et révocables**, jamais une promesse de marché, de financement ou d'association.
3. Les finalités, consentements, permissions de visibilité, droits de source et restrictions territoriales sont vérifiés à chaque diffusion pertinente ; un cache ou une projection ne contourne pas une révocation.
4. Aucun appel synchrone en chaîne n'est nécessaire au fonctionnement de base de ENT-001. Les calculs ENT-002 et ENT-005 peuvent être asynchrones ; l'indisponibilité d'un dérivé ne corrompt pas les owners.
5. Les transitions interservices reposent sur des commandes/événements/projections contractés ; aucune écriture directe dans les datastores PRF, SKL, PRT, LAB, ORI, REC, EMP ou OPP.

### Interfaces logiques candidates — non assimilées à des contrats physiques

| Frontière | Entrées minimales | Sorties candidates | Condition critique |
|---|---|---|---|
| ENT-001 | contexte PRF autorisé, CFG, CNS | VentureRef, état/version du Venture, événements de cycle de vie | contrôle d'accès par venture ; ownership indépendant du profil |
| ENT-002 | snapshots LAB/DAT/KNW sourcés, CFG | OpportunityHypothesis et EvidenceSet versionnés | fraîcheur, provenance, incertitude, retrait source |
| ENT-003 | références PRT, CFG et sources publiables | catalogue programmes/ressources versionné | distinguer organisation projetée et partenariat autoritatif |
| ENT-004 | programmes externes sourcés, règles territoriales | FundingOpportunity et EligibilitySnapshot expirables | aucune garantie d'éligibilité ni décision du financeur |
| ENT-005 | TeamNeed, VentureRef, PRF/SKL minimisés, CNS | MatchRun, explication et consentement traçable | refus, révocation, anti-exposition et minimisation |
| ENT-006 | VentureRef, apprentissage/compétences autorisés | plan, jalons, expériences, résultats versionnés | pas de modification de l'identité du Venture |

### Décisions à fermer avant contractualisation K3

- **ENT-002 :** classifier précisément les agrégats `DERIVED` versus l'état `MIXED` conservé ; définir les sources reconstructibles et l'état non reconstructible, s'il existe.
- **ENT-003 :** arbitrer l'ownership du `SupportOrganization` fonctionnel face à `SupportOrganizationProjection` : la projection ne doit pas être décrite comme une autorité primaire sur la relation PRT.
- **ENT-004 :** distinguer l'autorité sur les entrées de catalogue et règles locales de la projection d'une décision externe ; fixer le traitement des règles `AUTH/MIXED`.
- **ENT-005 :** séparer les `TeamNeed` persistants des résultats de matching dérivés et définir les obligations de retrait/révocation et reconstruction.
- **ENT-001/006 :** définir les commandes et événements de création, changement d'état, suppression/retrait et progression, avec concurrence/idempotence, sans fusionner leurs datastores.
- **Transversal :** arrêter classifications Privacy, contrats logiques, politiques de rétention, gouvernance pays, droits de source et dépendances de reconstruction ; les formats physiques et métriques de charge restent des gates ultérieurs.

**Verdict documentaire :** frontières et dépendances consolidées au niveau cible K2 ; `K3-NOT-ASSESSED`, `K4-NOT-ASSESSED`, `K5-NOT-EXECUTED`. Ce verdict ne modifie pas les statuts des profils individuels.


## Consolidation de la frontière K2 — 2026-10-10

La cible compte six frontières candidates distinctes ; leurs profils d'autonomie restent DRAFT. Ce complément n'atteste ni K3, ni K4, ni K5.

| Frontière | Contrat logique à détailler | Point de décision |
|---|---|---|
| ENT-001 | VentureRef, changements d'état, accès par VentureId | cohérence locale, idempotence, cycle de vie |
| ENT-002 | hypothèses, jeux de preuves, versions de sources, retrait | état DERIVED versus MIXED et reconstructibilité |
| ENT-003 | catalogue d'accompagnement, projection organisation | ne pas confondre SupportOrganizationProjection et autorité PRT |
| ENT-004 | programmes, règles d'éligibilité, snapshots expirables | distinguer AUTH et MIXED ; aucune décision du financeur |
| ENT-005 | besoin d'équipe, consentement, matching, révocation | distinguer TeamNeed persistant et scores dérivés |
| ENT-006 | VentureRef, jalons, expériences, résultats | historique autonome sans posséder l'identité Venture |

Les contrats physiques, IAM, droits de source, politiques pays, capacité chiffrée, preuves de restauration/reconstruction et tests ne sont pas établis par cette consolidation. Les échanges passent exclusivement par interfaces gouvernées ; aucun datastore interservices partagé.

**Verdict :** `K2-BOUNDARIES-CONSOLIDATED / K3-K4-NOT-ATTESTED / K5-NOT-EXECUTED`.
