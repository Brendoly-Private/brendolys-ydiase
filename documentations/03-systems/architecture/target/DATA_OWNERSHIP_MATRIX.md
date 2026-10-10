---
document_id: "YD-DOC-SYS-DATA-OWNERSHIP-MATRIX"
title: "Matrice D2 — Agrégats, sources autoritatives et données consommées"
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

# Matrice D2 — Agrégats, sources autoritatives et données consommées

Cette matrice définit la propriété logique des données pour les 61 services candidats de BRENDOLYS YDIASE. `Autoritatif` signifie que le service est l’unique référence interne pour l’agrégat indiqué. Une projection, un index de recherche, un cache, un feature store ou un data mart ne devient jamais autoritatif par copie.

## Règles DDD de propriété

1. Un agrégat mutable possède un seul owner autoritatif.
2. Un service consommateur référence l’identifiant stable de l’agrégat et reçoit les données par contrat, événement ou projection gouvernée.
3. Data Provenance porte la preuve de provenance, pas la vérité métier de l’objet observé.
4. Data Quality porte évaluations et anomalies, pas l’objet métier évalué.
5. Analytics, Recommendation et AI produisent des résultats dérivés et ne réécrivent jamais les sources métier.
6. Les données externes restent attribuées à leur source externe jusqu’à validation et publication dans un domaine YDIASE.
7. Les agrégats indiqués ici sont candidats D2. Leur structure interne et leurs invariants seront fixés en D3.

## Identité et profils

| Service | Agrégats possédés | Source autoritative | Données consommées |
|---|---|---|---|
| YD-SVC-IDN-001 Identity & Access | `Identity`, `CredentialBinding`, `Account`, `Session`, `AccessPrincipal` | IDN-001 pour identité technique et comptes | Consent status (CNS), country policy (CFG), audit policy (AUD) |
| YD-SVC-PRF-001 Profile | `UserProfile`, `Preference`, `Goal`, `DeclaredConstraint` | PRF-001 | IdentityRef (IDN), consent/privacy (CNS), country configuration (CFG) |
| YD-SVC-PRF-002 Education & Experience Profile | `EducationRecord`, `ExperienceRecord`, `AchievementClaim`, `ProfileEvidenceLink` | PRF-002 pour historique individuel déclaré/vérifié | ProfileRef (PRF-001), institutions/programs/qualifications (EDU), skills taxonomy (SKL-001), evidence/provenance (DAT-003) |

## Éducation et qualifications

| Service | Agrégats possédés | Source autoritative | Données consommées |
|---|---|---|---|
| YD-SVC-EDU-001 Institution Catalog | `Institution`, `Campus`, `InstitutionStatus`, `InstitutionPresence` | EDU-001 après validation/publication YDIASE | source records (DAT-002/003), taxonomies (DAT-005), country/territory (CFG), partner/institution claims (PRT/INS) |
| YD-SVC-EDU-002 Program Catalog | `Program`, `ProgramVersion`, `ProgramOffering`, `AdmissionRuleSet` | EDU-002 | Institution/Campus (EDU-001), qualification refs (EDU-004), curriculum refs (EDU-003), provenance/quality (DAT-003/004), country config (CFG) |
| YD-SVC-EDU-003 Curriculum & Module | `Curriculum`, `CurriculumVersion`, `Module`, `TeachingUnit`, `ModuleSequence` | EDU-003 | ProgramRef (EDU-002), Skill/Knowledge refs (SKL-001), provenance/quality (DAT-003/004) |
| YD-SVC-EDU-004 Qualification Framework | `Qualification`, `QualificationLevel`, `QualificationFramework`, `EquivalenceRule`, `PrerequisiteRule` | EDU-004 pour représentation YDIASE validée du cadre applicable | country framework (CFG), reference taxonomy (DAT-005), official-source assertions (DAT-002/003) |

## Compétences et carrières

| Service | Agrégats possédés | Source autoritative | Données consommées |
|---|---|---|---|
| YD-SVC-SKL-001 Skills Knowledge | `Skill`, `KnowledgeConcept`, `SkillRelation`, `SkillTaxonomyMapping` | SKL-001 | reference taxonomies (DAT-005), curricula/modules (EDU-003), occupations (CAR-001), provenance (DAT-003) |
| YD-SVC-SKL-002 User Skills Profile | `UserSkill`, `SkillEvidence`, `SkillAssessmentState`, `SkillHistory` | SKL-002 pour état individuel de compétence | ProfileRef (PRF), SkillRef (SKL-001), assessments (ASM), education/experience evidence (PRF-002), consent (CNS) |
| YD-SVC-CAR-001 Occupation & Career Graph | `Occupation`, `OccupationVersion`, `OccupationSkillRequirement`, `OccupationRelation`, `CareerTransitionEdge` | CAR-001 | skills (SKL-001), qualifications (EDU-004), labor signals (LAB-001), taxonomies (DAT-005), provenance (DAT-003) |
| YD-SVC-CAR-002 Career Path | `CareerPath`, `CareerPathStep`, `PathScenario`, `PathComparisonState` | CAR-002 pour trajectoires construites | occupations/edges (CAR-001), user profile/skills (PRF/SKL-002), programs (EDU-002), labor intelligence (LAB-002) |
| YD-SVC-CAR-003 Career Transition | `TransitionCase`, `TransitionGap`, `TransitionPlan`, `TransitionOption` | CAR-003 | current/target occupation (CAR-001), user skills (SKL-002), learning options (LRN/EDU), labor intelligence (LAB-002) |
| YD-SVC-CAR-004 Career Simulation | `CareerSimulation`, `SimulationScenario`, `SimulationAssumption`, `SimulationResult` | CAR-004 pour résultats de simulation, jamais pour faits source | career paths (CAR-002), transition data (CAR-003), labor intelligence/forecast (LAB), user state (PRF/SKL), education (EDU) |

## Orientation, évaluation, recommandation et recherche

| Service | Agrégats possédés | Source autoritative | Données consommées |
|---|---|---|---|
| YD-SVC-ASM-001 Assessment | `AssessmentDefinition`, `AssessmentSession`, `AssessmentResponse`, `AssessmentResult` | ASM-001 | Identity/Profile refs, consent (CNS), skills taxonomy (SKL-001), country rules (CFG) |
| YD-SVC-ORI-001 Orientation | `OrientationCase`, `OrientationObjective`, `OrientationConstraintSet`, `OrientationDecisionRecord` | ORI-001 pour dossier d’orientation | profile/education/skills, assessments, programs, occupations, labor intelligence, recommendation outputs, consent |
| YD-SVC-REC-001 Recommendation | `RecommendationRun`, `RecommendationSet`, `RecommendationItem`, `RecommendationExplanation`, `RecommendationEvidenceSnapshot` | REC-001 pour résultat calculé et explication | profile, skills, assessments, programs, occupations, labor signals/intelligence, opportunities, knowledge graph, policy/config |
| YD-SVC-ORI-002 Comparison & Decision Support | `ComparisonCase`, `ComparisonSet`, `DecisionCriterion`, `DecisionScorecard` | ORI-002 pour comparaison sauvegardée | programs, occupations, recommendations, labor intelligence, user preferences |
| YD-SVC-SRH-001 Search & Discovery | `SearchIndexDefinition`, `SearchDocumentProjection`, `SearchQuerySession` si persistée | Sources métier restent autoritatives; SRH-001 n’est autoritatif que pour configuration/index de recherche | institutions, programs, modules, occupations, opportunities, content, learning, partner/publication states |

## Marché du travail, opportunités et recrutement

| Service | Agrégats possédés | Source autoritative | Données consommées |
|---|---|---|---|
| YD-SVC-LAB-001 Labor Signals | `LaborSignal`, `ObservedDemandSignal`, `DeclaredNeedSignal`, `InstitutionalSignal`, `EconomicSignal`, `SignalObservation` | LAB-001 pour signaux normalisés YDIASE; source externe conservée dans provenance | raw acquisitions (DAT-002), provenance/quality, occupation/skill refs, employer refs, territory/config |
| YD-SVC-LAB-002 Labor Market Intelligence | `LaborMarketIndicator`, `LaborMarketSnapshot`, `DemandSupplyMeasure`, `TensionMeasure`, `SectorTerritoryAnalysis` | LAB-002 pour indicateurs dérivés publiés | labor signals, occupations, skills, opportunities, analytics aggregates, territory/reference data |
| YD-SVC-LAB-003 Labor Forecasting | `LaborForecast`, `ForecastScenario`, `ForecastModelRun`, `ForecastAssumption`, `ForecastEvaluation` | LAB-003 pour prévisions et évaluations | historical labor intelligence/signals, economic signals, occupation/skill refs, analytics datasets |
| YD-SVC-OPP-001 Opportunity | `Opportunity`, `OpportunityVersion`, `OpportunityRequirement`, `OpportunityPublication` | OPP-001 | employer (EMP-001), occupation/skills, location/config, provenance/quality, partner feeds |
| YD-SVC-OPP-002 Opportunity Matching | `OpportunityMatchRun`, `OpportunityMatch`, `MatchExplanation` | OPP-002 pour résultat de matching | opportunities, profile/skills/experience, occupations, consent, recommendation policies |
| YD-SVC-APP-001 Application | `Application`, `ApplicationStatusHistory`, `ApplicationSubmission`, `CandidateResponse` | APP-001 | OpportunityRef, candidate Identity/Profile refs, employer refs, consent/privacy |
| YD-SVC-EMP-001 Employer | `Employer`, `EmployerPresence`, `EmployerVerification`, `EmployerProfile` | EMP-001 | identity/account refs, partner data, country/territory, provenance/quality |
| YD-SVC-EMP-002 Talent & Recruitment | `TalentPool`, `RecruitmentCampaign`, `CandidateSelection`, `RecruitmentPipeline` | EMP-002 | employer, opportunities/applications, permitted profile/skill projections, matching results, consent |

## Contenu, communauté et learning

| Service | Agrégats possédés | Source autoritative | Données consommées |
|---|---|---|---|
| YD-SVC-CNT-001 Content | `ContentItem`, `ContentVersion`, `Publication`, `ContentAssetRef` | CNT-001 | author/profile refs, taxonomy, moderation state, provenance where external |
| YD-SVC-CNT-002 Feed | `FeedDefinition`, `FeedCandidateSet`, `FeedRankingRun`, `UserFeedState` | CNT-002 pour état/ranking du feed | content, user preferences, community relations, learning/opportunities, recommendation signals, moderation |
| YD-SVC-COM-001 Community | `CommunityRelation`, `Follow`, `Reaction`, `Comment`, `CommunityThread` | COM-001 | Identity/Profile refs, content refs, moderation, privacy settings |
| YD-SVC-LRN-001 Learning Discovery | `LearningResource`, `LearningOfferingRef`, `LearningRecommendationSet` | LRN-001 pour catalogue complémentaire propre à YDIASE; fournisseur externe reste source de ses faits | skill gaps, programs/modules, skills, marketplace items, provenance/quality |
| YD-SVC-RSH-001 Academic Research Topic | `ResearchTopic`, `ResearchTopicVersion`, `TopicRecommendation` | RSH-001 pour sujets édités/générés puis validés | programs/modules, skills/knowledge, occupations, labor intelligence, content, AI outputs vérifiés |
| YD-SVC-NTF-001 Notification | `Notification`, `DeliveryAttempt`, `NotificationPreferenceProjection`, `NotificationTemplate` | NTF-001 pour notification/livraison; préférences maîtres restent PRF/CNS selon type | identity/contact route, user preferences/consent, événements des domaines producteurs |

## Partenaires et espaces institutionnels

| Service | Agrégats possédés | Source autoritative | Données consommées |
|---|---|---|---|
| YD-SVC-PRT-001 Partner | `Partner`, `Partnership`, `Agreement`, `PartnerRole`, `PartnerAccessScope` | PRT-001 | organization refs, identity/access, country config, audit |
| YD-SVC-AMB-001 Ambassador Network | `AmbassadorMandate`, `AmbassadorAssignment`, `AmbassadorTerm`, `AmbassadorContribution` | AMB-001 | person identity/profile, partner/institution refs, collected submission refs, audit |
| YD-SVC-INS-001 Institution Workspace | `InstitutionWorkspace`, `InstitutionMembership`, `InstitutionSubmission`, `ValidationWorkflow` | INS-001 pour workspace/workflow; EDU reste autoritatif après publication | institution catalog, identity/access, partner agreement, data submissions, audit |
| YD-SVC-EMP-003 Employer Workspace | `EmployerWorkspace`, `EmployerMembership`, `EmployerWorkspacePreference` | EMP-003 pour expérience workspace; EMP/OPP/REC restent autoritatifs sur objets métier | employer, opportunities, campaigns, applications, intelligence products, access/entitlements |

## Data, Knowledge, Analytics et AI

| Service | Agrégats possédés | Source autoritative | Données consommées |
|---|---|---|---|
| YD-SVC-DAT-001 Data Source Registry | `DataSource`, `SourceContract`, `UsageRight`, `SourceTerritoryScope`, `SourceAccessPolicy` | DAT-001 | partner agreements, country/legal constraints, audit |
| YD-SVC-DAT-002 Data Acquisition | `AcquisitionJob`, `IngestionBatch`, `RawRecordEnvelope`, `ConnectorConfiguration`, `SubmissionBatch` | DAT-002 pour état d’acquisition et enveloppe brute immuable; jamais vérité métier publiée | source registry, partner/ambassador submissions, connector inputs, country config |
| YD-SVC-DAT-003 Data Provenance | `ProvenanceRecord`, `AssertionLineage`, `EvidenceRecord`, `TransformationLineage` | DAT-003 | raw records, domain publication identifiers, validation decisions, source registry |
| YD-SVC-DAT-004 Data Quality & Validation | `QualityAssessment`, `ValidationCase`, `Anomaly`, `CorroborationCase`, `ValidationDecision` | DAT-004 pour qualité/décisions de validation; pas pour objet métier | raw/domain records, provenance, validation rules, reference taxonomies |
| YD-SVC-DAT-005 Reference & Taxonomy | `ReferenceDataset`, `Taxonomy`, `Classification`, `ReferenceMapping`, `ReferenceVersion` | DAT-005 pour référentiels transversaux YDIASE; référentiels officiels externes gardent leur attribution | country framework, official/reference sources, provenance/quality |
| YD-SVC-KNW-001 Knowledge Graph | `KnowledgeNodeProjection`, `KnowledgeEdge`, `SemanticAssertion`, `GraphVersion` | KNW-001 pour relations sémantiques propres au graphe; domaines restent autoritatifs sur leurs entités | education, skills, careers, labor, opportunities, taxonomies, provenance/quality |
| YD-SVC-ANL-001 Analytics | `MetricDefinition`, `AnalyticalDataset`, `AggregateSnapshot`, `AnalysisRun` | ANL-001 pour métriques/datasets dérivés | projections gouvernées de tous domaines autorisés, provenance/quality, country/reference data |
| YD-SVC-ANL-002 Institution Intelligence | `InstitutionInsight`, `InstitutionBenchmark`, `InstitutionReportSnapshot` | ANL-002 pour produit analytique institutionnel | institution/program/curriculum data, labor intelligence, analytics aggregates, entitlements |
| YD-SVC-ANL-003 Employer Intelligence | `EmployerInsight`, `TalentMarketSnapshot`, `RecruitmentInsight` | ANL-003 pour produit analytique employeur | employer/recruitment data, labor intelligence, skills/occupation aggregates, analytics, entitlements |
| YD-SVC-AI-001 AI Gateway | `AIRequest`, `AIExecutionPolicy`, `ModelEndpointRegistration`, `AIUsageRecord` | AI-001 pour contrôle/exécution IA | identity/access, consent, entitlements, approved model registry/config, audit policies |
| YD-SVC-AI-002 Retrieval & Grounding | `RetrievalCorpusDefinition`, `GroundingIndex`, `RetrievalRun`, `GroundingBundle` | AI-002 pour index/bundles; sources métier restent autoritatives | knowledge graph, search projections, validated domain data, provenance/quality, access policy |
| YD-SVC-AI-003 AI Verification | `AIVerificationCase`, `ClaimCheck`, `AIConfidenceAssessment`, `VerificationDecision` | AI-003 pour résultat de vérification | AI outputs, grounding bundles, provenance, domain truths, policy rules |
| YD-SVC-AI-004 AI Orchestration | `AIWorkflow`, `AITask`, `AIWorkflowRun`, `AIExecutionPlan` | AI-004 pour orchestration | AI Gateway, retrieval, verification, domain tool contracts, access/consent |

## Économie et produits

| Service | Agrégats possédés | Source autoritative | Données consommées |
|---|---|---|---|
| YD-SVC-BIL-001 Subscription & Entitlement | `Plan`, `Subscription`, `Entitlement`, `Quota`, `EntitlementGrant` | BIL-001 | account/organization refs, product catalog refs, billing status, country config |
| YD-SVC-BIL-002 Billing | `BillingAccount`, `Invoice`, `PaymentRecord`, `Transaction`, `CreditNote` | BIL-002 pour comptabilité applicative YDIASE; prestataire de paiement reste source externe de son opération | subscription, customer refs, payment-provider events, country/currency config |
| YD-SVC-MKT-001 Learning Marketplace | `MarketplaceListing`, `MarketplaceOffer`, `ConversionAttribution`, `MarketplaceOrder` | MKT-001 | learning resources, partner/provider, billing, entitlements, profile consented context |
| YD-SVC-SPN-001 Sponsored Placement | `SponsoredCampaign`, `SponsoredPlacement`, `SponsorshipBudget`, `PlacementDelivery` | SPN-001 | advertiser/partner, eligible inventory, billing, moderation; aucune écriture dans scores REC/ORI |
| YD-SVC-API-001 External API Management | `APIProduct`, `APIClient`, `APISubscription`, `APIQuotaPolicy`, `APIUsageRecord` | API-001 | entitlements, identity/access, exposed domain contracts, billing, audit |
| YD-SVC-DPR-001 Data Product | `DataProduct`, `DataProductVersion`, `DatasetRelease`, `DataLicense`, `DataProductDelivery` | DPR-001 pour produit publié; données sources restent leurs domaines | approved aggregated datasets, analytics, provenance/quality, privacy policy, entitlements |
| YD-SVC-INT-001 Intelligence Product | `IntelligenceProduct`, `IntelligenceEdition`, `Observation`, `IntelligenceBrief`, `IntelligenceDelivery` | INT-001 pour publication d’intelligence | labor/education/employer analytics, data products, verified sources, entitlements |

## Gouvernance de plateforme

| Service | Agrégats possédés | Source autoritative | Données consommées |
|---|---|---|---|
| YD-SVC-ADM-001 Administration | `AdminCase`, `AdministrativeActionRequest`, `OperationalOverride` | ADM-001 pour workflow administratif; ne devient jamais owner des objets administrés | domain admin contracts, identity/access, audit, moderation, configuration |
| YD-SVC-MOD-001 Moderation | `ModerationCase`, `ModerationDecision`, `PolicyViolation`, `Appeal` | MOD-001 | content/community/marketplace/sponsored objects, identity refs, moderation policy, audit |
| YD-SVC-AUD-001 Audit & Trace | `AuditEvent`, `AuditTrail`, `SensitiveActionRecord`, `AuditExport` | AUD-001 | événements/actions des services; identity refs; security context |
| YD-SVC-CFG-001 Country Configuration | `CountryConfiguration`, `Territory`, `LanguageConfiguration`, `CurrencyConfiguration`, `CountryFrameworkBinding`, `LocalPolicyParameter` | CFG-001 pour configuration opérationnelle YDIASE; textes/règles officiels externes restent attribués | reference datasets, official country sources, legal/compliance decisions, provenance |
| YD-SVC-CNS-001 Consent & Privacy | `ConsentRecord`, `PurposeGrant`, `PrivacyPreference`, `DataSubjectRequest`, `RetentionInstruction` | CNS-001 | IdentityRef, country/legal configuration, data-processing purpose registry, audit |

## Contrôles anti-conflit

Les frontières suivantes sont obligatoires :

- `Identity` appartient à IDN-001; `UserProfile` à PRF-001.
- `Institution` appartient à EDU-001; INS-001 ne possède que son workspace et ses soumissions.
- `Program` appartient à EDU-002; `Curriculum` et `Module` à EDU-003.
- `Skill` appartient à SKL-001; `UserSkill` à SKL-002.
- `Occupation` appartient à CAR-001; chemins, transitions et simulations possèdent leurs résultats dérivés uniquement.
- `LaborSignal` appartient à LAB-001; indicateurs à LAB-002; prévisions à LAB-003.
- `Opportunity` appartient à OPP-001; `Application` à REC-002.
- `Employer` appartient à EMP-001; workspaces et campagnes ne dupliquent pas cette propriété.
- Les services Data portent acquisition, provenance, qualité et référentiels; ils ne prennent pas la propriété des objets métier publiés.
- KNW-001 possède les relations sémantiques du graphe, pas les entités métier sources.
- ANL, REC et AI possèdent leurs exécutions et résultats dérivés, jamais les faits sources.
- SPN-001 reste isolé des scores et classements ORI/REC.
- DPR-001 ne publie que des produits dont droits, agrégation, confidentialité et finalité sont validés.

## Condition de passage D2

Un `SERVICE_DEFINITION.md` peut passer à D2 lorsque ses agrégats ci-dessus sont confirmés, que les consommateurs ne revendiquent aucune propriété concurrente, que les données personnelles ont leur finalité et contrôle CNS identifiés, et que les dépendances nécessaires figurent dans la Dependency Map. La présente matrice sert de référence de travail pour cette validation; elle ne remplace pas les contrats D3.

## Extension D2 — Entrepreneurship

| Service | Agrégats possédés | Source autoritative | Données consommées |
|---|---|---|---|
| YD-SVC-ENT-001 | Venture, VentureObjective, VentureStage, VentureConstraint, VentureTeamRef | ENT-001 pour état du projet | PRF/SKL projections autorisées, CNS, CFG |
| YD-SVC-ENT-002 | EntrepreneurialOpportunityHypothesis, OpportunityEvidenceSet, OpportunityAssessmentSnapshot | ENT-002 pour interprétation entrepreneuriale dérivée | LAB, DAT, KNW, CFG |
| YD-SVC-ENT-003 | SupportOrganizationProjection, IncubatorProgram, MentorOffering, EntrepreneurshipResource | ENT-003 pour catalogue d'accompagnement | PRT, DAT, CFG |
| YD-SVC-ENT-004 | FundingOpportunity, FundingProgram, EligibilityRuleSet, EligibilitySnapshot | ENT-004 pour catalogue/éligibilité YDIASE | PRT, DAT, CFG, CNS si personnalisation |
| YD-SVC-ENT-005 | TeamNeed, FounderMatchRun, ComplementarityAssessment, MatchExplanation | ENT-005 pour résultat de matching | ENT-001, PRF, SKL, CNS |
| YD-SVC-ENT-006 | VenturePlan, Milestone, Experiment, Assumption, ValidationResult, ProgressSnapshot | ENT-006 pour progression | ENT-001, SKL, EDU/LRN, ORI |

Cette extension est réconciliée par `ENTREPRENEURSHIP_DEPENDENCY_OWNERSHIP_MAP.md`. Elle ne modifie aucun ownership PRF/SKL/LAB/PRT/ORI/REC/EMP/OPP existant.
