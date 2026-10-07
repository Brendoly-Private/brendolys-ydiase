# Service Map cible de BRENDOLYS YDIASE

Ce catalogue décrit les **services logiques candidats de l’architecture cible**. Il ne fixe pas le nombre final de microservices physiques. Un service peut être fusionné, scindé ou retiré après validation DDD et ADR. Chaque service retenu dans la cible doit recevoir une fiche documentaire minimale, même s’il n’est ni développé, ni déployé, ni activé.

## Principes

- Domaine métier ≠ capacité ≠ service logique ≠ microservice physique ≠ infrastructure.
- Le pilote Burkina n’est qu’un sous-ensemble activé de la cible.
- La cible est conçue pour 5 à 15 millions d'utilisateurs simultanément actifs à l'échelle plateforme ; chaque service reçoit son Capacity Profile propre.
- Les phases indiquent l’ordre de maturation fonctionnelle, pas une obligation de déploiement indépendant.
- Data, Knowledge, Analytics et AI restent séparés.
- Une base de données, Kafka, Flink, Kubernetes, un LLM ou tout autre produit technique n’est jamais un service métier YDIASE par nature.
- Les données personnelles ne constituent pas un produit commercial.

## Inventaire fonctionnel ayant conduit au catalogue

La cible couvre au minimum : identité et profils ; établissements, campus, programmes, curricula, modules et qualifications ; connaissances et compétences ; métiers, trajectoires et reconversion ; évaluations ; orientation et comparaison ; recherche ; recommandations ; marché du travail et intelligence économique ; entrepreneuriat, projet venture, accompagnement, financement et équipe fondatrice ; opportunités, candidatures et recrutement ; employeurs ; contenu, feed, communauté et learning ; notifications ; partenaires et ambassadeurs ; collecte, provenance, qualité et gouvernance Data ; Knowledge Graph ; analytics et forecasting ; IA ; produits Data/API/Intelligence ; abonnements, facturation, marketplace et sponsoring ; administration, modération, audit ; configuration pays et expansion panafricaine.

## Catalogue cible — services métier et produit

| ID | Service logique candidat | Responsabilité principale | Domaine | Phase cible | Doc | Implémentation |
|---|---|---|---|---|---|---|
| YD-SVC-IDN-001 | Identity & Access Service | Identités, authentification, sessions et accès applicatifs | Identité | P1 | D1 | not-started |
| YD-SVC-PRF-001 | Profile Service | Profil utilisateur, préférences, objectifs et contexte individuel | Identité-profils | P1 | D0 | not-started |
| YD-SVC-PRF-002 | Education & Experience Profile Service | Historique éducatif, expériences et acquis déclarés | Identité-profils | P2 | D0 | not-started |
| YD-SVC-EDU-001 | Institution Catalog Service | Établissements, campus, types, statut et informations validées | Éducation-institutions | P1 | D1 | not-started |
| YD-SVC-EDU-002 | Program Catalog Service | Filières, formations et versions de programmes | Éducation-institutions | P1 | D1 | not-started |
| YD-SVC-EDU-003 | Curriculum & Module Service | Curricula, modules, unités d’enseignement et historique | Éducation-institutions | P1 | D0 | not-started |
| YD-SVC-EDU-004 | Qualification Framework Service | Diplômes, niveaux, prérequis, équivalences et cadres nationaux | Éducation-institutions | P2 | D0 | not-started |
| YD-SVC-SKL-001 | Skills Knowledge Service | Référentiel de compétences et connaissances | Compétences-connaissances | P1 | D1 | not-started |
| YD-SVC-SKL-002 | User Skills Profile Service | Compétences détenues, niveaux, preuves et historique | Compétences-connaissances | P2 | D0 | not-started |
| YD-SVC-CAR-001 | Occupation & Career Graph Service | Métiers, professions, relations et trajectoires professionnelles | Métiers-carrières | P2 | D1 | not-started |
| YD-SVC-CAR-002 | Career Path Service | Construction et comparaison de trajectoires professionnelles | Métiers-carrières | P3 | D0 | not-started |
| YD-SVC-CAR-003 | Career Transition Service | Reconversion, passerelles et écarts entre situations professionnelles | Métiers-carrières | P3 | D0 | not-started |
| YD-SVC-ASM-001 | Assessment Service | Évaluations d’intérêts, aptitudes, préférences et critères | Orientation-recommandation | P2 | D0 | not-started |
| YD-SVC-ORI-001 | Orientation Service | Cas d’orientation éducative et professionnelle | Orientation-recommandation | P2 | D0 | not-started |
| YD-SVC-REC-001 | Recommendation Service | Classement et recommandations explicables | Orientation-recommandation | P2 | D1 | not-started |
| YD-SVC-ORI-002 | Comparison & Decision Support Service | Comparaison formations, métiers, options et scénarios | Orientation-recommandation | P2 | D0 | not-started |
| YD-SVC-CAR-004 | Career Simulation Service | Simulation de trajectoires, scénarios et écarts de compétences | Métiers-carrières | P3 | D0 | not-started |
| YD-SVC-SRH-001 | Search & Discovery Service | Recherche transverse établissements, formations, métiers et opportunités | Plateforme | P1 | D0 | not-started |
| YD-SVC-LAB-001 | Labor Signals Service | Collecte logique et représentation des signaux du marché | Marché-travail | P3 | D1 | not-started |
| YD-SVC-LAB-002 | Labor Market Intelligence Service | Analyse demande, tension, évolution, secteurs et territoires | Marché-travail | P4 | D0 | not-started |
| YD-SVC-LAB-003 | Labor Forecasting Service | Prévisions, scénarios et tendances du marché du travail | Marché-travail | P7 | D0 | not-started |
| YD-SVC-OPP-001 | Opportunity Service | Stages, emplois, programmes et autres opportunités | Opportunités-recrutement | P4 | D0 | not-started |
| YD-SVC-OPP-002 | Opportunity Matching Service | Matching profil-compétences-opportunités | Opportunités-recrutement | P4 | D0 | not-started |
| YD-SVC-REC-002 | Application Service | SUPERSEDED — remplacé par YD-SVC-APP-001 | Opportunités-recrutement | P4 | D2 | SUPERSEDED |
| YD-SVC-EMP-001 | Employer Service | Organisations employeuses, profils et présence employeur | Opportunités-recrutement | P4 | D0 | not-started |
| YD-SVC-EMP-002 | Talent & Recruitment Service | Recherche de talents, viviers et campagnes de recrutement | Opportunités-recrutement | P5 | D0 | not-started |
| YD-SVC-CNT-001 | Content Service | Articles, vidéos, ressources et contenus éditoriaux | Contenu-communauté-learning | P5 | D0 | not-started |
| YD-SVC-CNT-002 | Feed Service | Fil personnalisé éducatif et professionnel | Contenu-communauté-learning | P5 | D0 | not-started |
| YD-SVC-COM-001 | Community Service | Interactions communautaires autorisées, abonnements et échanges | Contenu-communauté-learning | P5 | D0 | not-started |
| YD-SVC-LRN-001 | Learning Discovery Service | Ressources et formations complémentaires liées aux écarts de compétences | Contenu-communauté-learning | P5 | D0 | not-started |
| YD-SVC-RSH-001 | Academic Research Topic Service | Sujets académiques reliés aux domaines, compétences et trajectoires | Contenu-communauté-learning | P5 | D0 | not-started |
| YD-SVC-NTF-001 | Notification Service | Notifications multicanales, préférences et événements utilisateur | Plateforme | P2 | D0 | not-started |
| YD-SVC-PRT-001 | Partner Service | Partenaires, conventions, rôles et relations d’écosystème | Partenaires-écosystème | P3 | D0 | not-started |
| YD-SVC-AMB-001 | Ambassador Network Service | Ambassadeurs, mandats, rattachements, renouvellements et contributions | Partenaires-écosystème | P1 | D0 | not-started |
| YD-SVC-INS-001 | Institution Workspace Service | Espace établissement, validation et maintenance de ses informations | Partenaires-écosystème | P5 | D0 | not-started |
| YD-SVC-EMP-003 | Employer Workspace Service | Espace employeur, opportunités, campagnes et intelligence associée | Partenaires-écosystème | P5 | D0 | not-started |



## Extension cible — Entrepreneurship

L'entrepreneuriat est désormais un domaine de premier rang. Les frontières logiques candidates suivantes sont intégrées à la cible et devront suivre la même revue DDD, autonomie, contrats, K3/K4, Capacity Profile et Development Readiness que les autres services.

| ID | Service logique candidat | Responsabilité principale | Domaine | Activation | Doc | Implémentation |
|---|---|---|---|---|---|---|
| YD-SVC-ENT-001 | Venture Profile Service | Projet entrepreneurial, stade, objectifs, contraintes et contexte du projet | Entrepreneurship | progressive | D0 | not-started |
| YD-SVC-ENT-002 | Entrepreneurial Opportunity Intelligence Service | Hypothèses/opportunités économiques sourcées, territoriales et sectorielles | Entrepreneurship | progressive | D0 | not-started |
| YD-SVC-ENT-003 | Entrepreneurship Support Ecosystem Service | Incubateurs, mentors, programmes et ressources d'accompagnement | Entrepreneurship | progressive | D0 | not-started |
| YD-SVC-ENT-004 | Funding Opportunity Service | Financements, subventions, concours, dispositifs et éligibilité | Entrepreneurship | progressive | D0 | not-started |
| YD-SVC-ENT-005 | Founder & Team Matching Service | Besoins d'équipe, complémentarités et matching sous consentement | Entrepreneurship | progressive | D0 | not-started |
| YD-SVC-ENT-006 | Venture Progression Service | Plans, hypothèses, expérimentations, jalons et progression | Entrepreneurship | progressive | D0 | not-started |

Ces frontières ne dupliquent pas PRF, SKL, LAB, ORI, REC, PRT, EMP ou OPP. Leur ownership détaillé est défini dans `02-domains/entrepreneurship/FRONTIERES_ET_DEPENDANCES.md`.

## Catalogue cible — Data, Knowledge, Analytics et AI

| ID | Service logique candidat | Responsabilité principale | Domaine | Phase cible | Doc | Implémentation |
|---|---|---|---|---|---|---|
| YD-SVC-DAT-001 | Data Source Registry Service | Registre des sources, droits, territoires et conditions d’usage | Data | P0.1 | D0 | not-started |
| YD-SVC-DAT-002 | Data Acquisition Service | Ingestion manuelle, fichiers, partenaires, agents et connecteurs autorisés | Data | P1 | D0 | not-started |
| YD-SVC-DAT-003 | Data Provenance Service | Traçabilité des assertions, origine, preuve et chaîne de transformation | Data | P1 | D0 | not-started |
| YD-SVC-DAT-004 | Data Quality & Validation Service | Contrôle, corroboration, confiance, validation et anomalies | Data | P1 | D0 | not-started |
| YD-SVC-DAT-005 | Reference & Taxonomy Service | Taxonomies, classifications, correspondances et référentiels partagés | Data | P1 | D0 | not-started |
| YD-SVC-KNW-001 | Knowledge Graph Service | Relations sémantiques entre éducation, compétences, métiers et marché | Knowledge | P2 | D0 | not-started |
| YD-SVC-ANL-001 | Analytics Service | Agrégations, indicateurs et analyses internes gouvernées | Analytics | P3 | D0 | not-started |
| YD-SVC-ANL-002 | Institution Intelligence Service | Indicateurs et analyses destinés aux établissements | Analytics | P6 | D0 | not-started |
| YD-SVC-ANL-003 | Employer Intelligence Service | Indicateurs compétences, recrutement et disponibilité des profils | Analytics | P6 | D0 | not-started |
| YD-SVC-AI-001 | AI Gateway Service | Point de contrôle des usages de modèles IA | AI | P2 | D1 | not-started |
| YD-SVC-AI-002 | Retrieval & Grounding Service | Récupération de connaissances vérifiées pour les usages IA | AI | P2 | D0 | not-started |
| YD-SVC-AI-003 | AI Verification Service | Contrôle des réponses, preuves, règles et niveaux de confiance | AI | P2 | D0 | not-started |
| YD-SVC-AI-004 | AI Orchestration Service | Orchestration des modèles et tâches IA autorisées | AI | P6 | D0 | not-started |

## Catalogue cible — économie, exposition et gouvernance opérationnelle

| ID | Service logique candidat | Responsabilité principale | Domaine | Phase cible | Doc | Implémentation |
|---|---|---|---|---|---|---|
| YD-SVC-BIL-001 | Subscription & Entitlement Service | Plans, droits fonctionnels, quotas et accès commerciaux | Économie-produit | P5 | D0 | not-started |
| YD-SVC-BIL-002 | Billing Service | Facturation, transactions et états de paiement | Économie-produit | P5 | D0 | not-started |
| YD-SVC-MKT-001 | Learning Marketplace Service | Catalogue commercial de formations et attribution des conversions | Économie-produit | P6 | D0 | not-started |
| YD-SVC-SPN-001 | Sponsored Placement Service | Visibilité sponsorisée séparée des scores d’orientation | Économie-produit | P6 | D0 | not-started |
| YD-SVC-API-001 | External API Management Service | Produits API, clients, quotas et politiques d’exposition | Économie-produit | P7 | D0 | not-started |
| YD-SVC-DPR-001 | Data Product Service | Produits de données agrégées et gouvernées | Économie-produit | P7 | D0 | not-started |
| YD-SVC-INT-001 | Intelligence Product Service | Produits d’intelligence et observatoires destinés aux organisations | Économie-produit | P7 | D0 | not-started |
| YD-SVC-ADM-001 | Administration Service | Administration fonctionnelle de la plateforme | Plateforme-gouvernance | P1 | D0 | not-started |
| YD-SVC-MOD-001 | Moderation Service | Modération des contenus et interactions selon les politiques actives | Plateforme-gouvernance | P5 | D0 | not-started |
| YD-SVC-AUD-001 | Audit & Trace Service | Traces fonctionnelles, actions sensibles et preuves d’audit | Plateforme-gouvernance | P1 | D0 | not-started |
| YD-SVC-CFG-001 | Country Configuration Service | Paramètres pays, cadres éducatifs, territoires, langues et classifications locales | Plateforme-gouvernance | P1 | D0 | not-started |
| YD-SVC-CNS-001 | Consent & Privacy Service | Consentements, finalités, préférences de confidentialité et droits applicables | Plateforme-gouvernance | P1 | D0 | not-started |

## Applications et portails — hors comptage des services métier

Ces surfaces ne sont pas automatiquement des microservices :

- application Web BRENDOLYS YDIASE
- application mobile
- application desktop si sa valeur est confirmée
- portail élève/étudiant
- portail professionnel et reconversion
- portail établissement
- portail employeur/recruteur
- portail ambassadeur et collecte terrain
- portail administration
- portail Data/Intelligence
- interfaces partenaires et API

## Moteurs logiques à tracer vers les services

Les moteurs suivants sont des capacités ou assemblages de services, pas automatiquement des microservices indépendants :

- Orientation Engine
- Recommendation Engine
- Skill Matching Engine
- Career Path Engine
- Career Transition Engine
- Labor Market Engine
- Opportunity Matching Engine
- Feed Recommendation Engine
- Academic Research Topic Engine
- Institution Intelligence Engine
- Employer Intelligence Engine
- Forecasting Engine
- Search Engine
- Knowledge Engine
- Assessment Engine
- Career Simulation Engine

## Rattachement aux moteurs économiques

Le catalogue doit permettre l’activation progressive des moteurs économiques déjà retenus : Free, Premium, Institutions, Employers, Recruitment, Intelligence, Data, API, Marketplace, Sponsored et Studies. `Studies` reste principalement une offre de service de BRENDOLYS INTELLIGENCE appuyée par YDIASE et ne justifie pas automatiquement un microservice dédié.

## Règle de validation

Cette carte est un **inventaire cible candidat**, pas une décision définitive de découpage physique. La prochaine revue DDD doit, pour chaque ligne :

1. confirmer le bounded context et l’owner métier
2. confirmer ou corriger les données possédées
3. identifier les dépendances interdites et autorisées
4. décider si le service reste autonome, fusionne ou se scinde
5. créer ou compléter sa `SERVICE_DEFINITION.md`
6. rattacher capacités, exigences, événements candidats et critères de vérification
7. conserver les services non activés dans la documentation cible avec leur statut explicite
