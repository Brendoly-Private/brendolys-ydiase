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
