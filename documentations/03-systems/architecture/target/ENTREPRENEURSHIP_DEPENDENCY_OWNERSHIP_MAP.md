---
document_id: "YD-DOC-SYS-ENTREPRENEURSHIP-DEPENDENCY-OWNERSHIP-MAP"
title: "Entrepreneurship — Ownership & Dependency Map"
document_type: "target-architecture"
document_role: "Définit une référence canonique de l’architecture cible YDIASE."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "systems"
---

# Entrepreneurship — Ownership & Dependency Map

Statut : TARGET-OWNERSHIP-BASELINE / DDD-RECONCILED

| Owner | Agrégats principaux | Consomme | Ne possède jamais |
|---|---|---|---|
| ENT-001 | Venture, VentureObjective, VentureStage, VentureConstraint, VentureTeamRef | PRF, SKL, CNS, CFG | UserProfile, UserSkill, LaborSignal |
| ENT-002 | EntrepreneurialOpportunityHypothesis, OpportunityEvidenceSet, OpportunityAssessmentSnapshot | LAB, DAT, KNW, CFG | LaborSignal, MarketIndicator, Venture |
| ENT-003 | SupportOrganizationProjection, IncubatorProgram, MentorOffering, EntrepreneurshipResource | PRT, CFG, DAT | PartnerAgreement, UserProfile |
| ENT-004 | FundingOpportunity, FundingProgram, EligibilityRuleSet, EligibilitySnapshot | PRT, CFG, DAT, CNS si personnalisation | bank account, payment, lender decision |
| ENT-005 | TeamNeed, FounderMatchRun, ComplementarityAssessment, MatchExplanation | ENT-001, PRF, SKL, CNS | UserProfile, UserSkill, Venture |
| ENT-006 | VenturePlan, Milestone, Experiment, Assumption, ValidationResult, ProgressSnapshot | ENT-001, SKL, EDU/LRN, ORI | Venture identity, UserProfile, LearningResource |

## Sens des dépendances
ENT-001 est utilisable sans ENT-002..006.
ENT-006 dépend d'une VentureRef ENT-001 mais ENT-001 ne dépend pas synchroniquement d'ENT-006.
ENT-002 ne dépend pas d'un Venture pour produire de l'intelligence générique ; une personnalisation référence ensuite un contexte autorisé.
ENT-003/004 sont catalogues indépendants et peuvent fonctionner sans profil utilisateur.
ENT-005 ne doit pas rendre ENT-001 indisponible lorsqu'un calcul de matching est en panne.

## Cohérence
Forte locale dans chaque agrégat owner. Entre frontières : éventuelle par défaut, sauf commande métier explicitement contractée. Les snapshots dérivés portent source/version/fraîcheur.

## Cycles évités
ORI/REC consomment ENT mais n'écrivent pas ses agrégats.
LAB alimente ENT-002 ; ENT-002 ne réécrit pas LAB.
PRT alimente ENT-003/004 ; ceux-ci ne modifient pas Agreement.
EMP/OPP peuvent consommer une transition entrepreneur-employeur ; ils ne deviennent pas owners du Venture.
