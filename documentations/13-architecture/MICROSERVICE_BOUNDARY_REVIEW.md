# Microservice Boundary Review — BRENDOLYS YDIASE

Statut : `D3-boundary-target`

## Objet

Cette revue fixe les critères de fusion et la liste cible des frontières physiques de BRENDOLYS YDIASE. Elle s’appuie sur l’ownership D2, la Dependency Map D3, l’Event Map D3 et les ADR ultérieurs. Elle ne choisit pas encore le runtime, le moteur de base, le broker ou l’orchestrateur.

## Principe cardinal

Un service logique n’est pas automatiquement un microservice. Une fusion ne sert jamais à réduire artificiellement le nombre de déploiements. Une séparation ne sert jamais à afficher une architecture distribuée. La frontière retenue doit protéger le métier, les données, la sécurité, l’exploitation et l’évolution indépendante.

## Statuts de frontière

- `INDEPENDENT` : microservice physique cible confirmé.
- `MERGE` : responsabilité logique conservée comme module/agrégat dans un microservice cible.
- `LOGICAL_ONLY` : capacité interne sans datastore ni déploiement métier propre.
- `PLATFORM_COMPONENT` : déploiement autonome transverse, hors comptage des microservices métier.
- `DEFERRED` : microservice cible conditionnel, documentation conservée, extraction déclenchée par seuil explicite.
- `EXTERNAL_PLATFORM` : responsabilité fournie hors YDIASE.
- `SUPERSEDED` : identifiant retiré et interdit pour une nouvelle implémentation.

# 1. Critères normatifs de fusion

Une fusion exige cohérence transactionnelle, ownership sans ambiguïté, cycles de vie compatibles, profils de charge compatibles, criticité compatible, sécurité compatible, données compatibles, responsabilité opérationnelle compatible, dépendances D3 simplifiées et autonomie future conservée.

Une fusion est refusée lorsqu’elle impose notamment des owners incompatibles, restauration commune injustifiée, règles de confidentialité/rétention incompatibles, scaling indépendant nécessaire, blast radius inacceptable, datastore partagé entre domaines, mélange autoritatif/dérivé, dépendance circulaire ou simple économie de serveurs.

Après passage des bloqueurs, le score secondaire de fusion reste : `16–20` fusion forte candidate, `11–15` ADR obligatoire, `0–10` séparation par défaut. Le score n’annule jamais un bloqueur.

# 2. Critères d’extraction d’un service DEFERRED

Un service `DEFERRED` devient `INDEPENDENT` lorsqu’un ADR valide au moins un déclencheur fort : scaling indépendant, sécurité/données divergentes, équipe distincte, cadence indépendante, SLO/RTO/RPO incompatibles, technologie spécialisée, workload perturbateur, blast radius à réduire, produit/contrat externe propre ou contrainte réglementaire/territoriale propre.

# 3. Décisions de frontière réconciliées

| Service logique | Décision | Frontière physique | Motif principal |
|---|---|---|---|
| PRF-001 Profile | INDEPENDENT | `YD-MS-PRF-001 Profile` | profil courant, préférences, objectifs et contraintes |
| PRF-002 Education & Experience Profile | INDEPENDENT | `YD-MS-PRF-002 Education & Experience Profile` | temporalité longue, preuves/provenance, rétention et blast radius distincts; ADR accepté |
| CAR-003 Career Transition | MERGE | `YD-MS-CAR-002 Career Path` | même famille de trajectoires et même charge fonctionnelle |
| ORI-002 Comparison & Decision Support | MERGE | `YD-MS-ORI-001 Orientation` | comparaison intrinsèque au dossier de décision |
| RSH-001 Academic Research Topic | LOGICAL_ONLY | `YD-MS-REC-001 Recommendation` | moteur spécialisé sans autorité propre justifiant un datastore |
| EMP-003 Employer Workspace | LOGICAL_ONLY | Edge/BFF employeur | façade d’expérience sans agrégat métier autoritatif |
| INS-001 Institution Workspace | LOGICAL_ONLY | Edge/BFF institution | façade, EDU reste autoritatif |
| ADM-001 Administration | LOGICAL_ONLY | Admin plane | commandes vers les owners, aucune DB métier autoritative |

Référence normative pour PRF : `ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY.md`. L’ancienne fusion PRF est `SUPERSEDED`.

# 4. Responsabilités hors microservices métier YDIASE

| Responsabilité | Statut | Décision |
|---|---|---|
| IDN-001 Identity & Access | EXTERNAL_PLATFORM | BRENDOLYS Identity fournit l’IAM, YDIASE ne stocke aucun mot de passe utilisateur |
| REC-002 Application historique | SUPERSEDED | remplacé par APP-001 |

BRENDOLYS Identity utilise `brendolys-internal`, `brendolys-networks`, `brendolys-customers`.

Issuer OIDC : `https://sso.godinfradsby.xyz/realms/{realm}/protocol/openid-connect`.

# 5. Liste cible — microservices métier confirmés

| # | Microservice physique cible | Services logiques contenus | Domaine |
|---:|---|---|---|
| 1 | `YD-MS-PRF-001 Profile` | PRF-001 | Identité-profils |
| 2 | `YD-MS-PRF-002 Education & Experience Profile` | PRF-002 | Identité-profils |
| 3 | `YD-MS-EDU-001 Institution Catalog` | EDU-001 | Éducation |
| 4 | `YD-MS-EDU-002 Program Catalog` | EDU-002 | Éducation |
| 5 | `YD-MS-EDU-003 Curriculum & Module` | EDU-003 | Éducation |
| 6 | `YD-MS-EDU-004 Qualification Framework` | EDU-004 | Éducation |
| 7 | `YD-MS-SKL-001 Skills Knowledge` | SKL-001 | Compétences |
| 8 | `YD-MS-SKL-002 User Skills Profile` | SKL-002 | Compétences |
| 9 | `YD-MS-CAR-001 Occupation & Career Graph` | CAR-001 | Métiers-carrières |
| 10 | `YD-MS-CAR-002 Career Path & Transition` | CAR-002 + CAR-003 | Métiers-carrières |
| 11 | `YD-MS-ASM-001 Assessment` | ASM-001 | Orientation |
| 12 | `YD-MS-ORI-001 Orientation & Decision Support` | ORI-001 + ORI-002 | Orientation |
| 13 | `YD-MS-REC-001 Recommendation` | REC-001 + RSH-001 logical module | Orientation |
| 14 | `YD-MS-SRH-001 Search & Discovery` | SRH-001 | Plateforme produit |
| 15 | `YD-MS-LAB-001 Labor Signals` | LAB-001 | Marché du travail |
| 16 | `YD-MS-LAB-002 Labor Market Intelligence` | LAB-002 | Marché du travail |
| 17 | `YD-MS-OPP-001 Opportunity` | OPP-001 | Opportunités |
| 18 | `YD-MS-OPP-002 Opportunity Matching` | OPP-002 | Opportunités |
| 19 | `YD-MS-APP-001 Application` | APP-001 | Recrutement |
| 20 | `YD-MS-EMP-001 Employer` | EMP-001 | Recrutement |
| 21 | `YD-MS-EMP-002 Talent & Recruitment` | EMP-002 | Recrutement |
| 22 | `YD-MS-CNT-001 Content` | CNT-001 | Contenu |
| 23 | `YD-MS-CNT-002 Feed` | CNT-002 | Contenu |
| 24 | `YD-MS-COM-001 Community` | COM-001 | Communauté |
| 25 | `YD-MS-LRN-001 Learning Discovery` | LRN-001 | Learning |
| 26 | `YD-MS-NTF-001 Notification` | NTF-001 | Plateforme produit |
| 27 | `YD-MS-PRT-001 Partner` | PRT-001 | Écosystème |
| 28 | `YD-MS-AMB-001 Ambassador Network` | AMB-001 | Écosystème |
| 29 | `YD-MS-DAT-001 Data Source Registry` | DAT-001 | Data |
| 30 | `YD-MS-DAT-002 Data Acquisition` | DAT-002 | Data |
| 31 | `YD-MS-DAT-003 Data Provenance` | DAT-003 | Data |
| 32 | `YD-MS-DAT-004 Data Quality & Validation` | DAT-004 | Data |
| 33 | `YD-MS-DAT-005 Reference & Taxonomy` | DAT-005 | Data |
| 34 | `YD-MS-KNW-001 Knowledge Graph` | KNW-001 | Knowledge |
| 35 | `YD-MS-ANL-001 Analytics` | ANL-001 | Analytics |
| 36 | `YD-MS-ANL-002 Institution Intelligence` | ANL-002 | Analytics produit |
| 37 | `YD-MS-ANL-003 Employer Intelligence` | ANL-003 | Analytics produit |
| 38 | `YD-MS-AI-002 Retrieval & Grounding` | AI-002 | AI |
| 39 | `YD-MS-AI-003 AI Verification` | AI-003 | AI |
| 40 | `YD-MS-BIL-001 Subscription & Entitlement` | BIL-001 | Économie |
| 41 | `YD-MS-BIL-002 Billing` | BIL-002 | Économie |
| 42 | `YD-MS-MKT-001 Learning Marketplace` | MKT-001 | Économie |
| 43 | `YD-MS-SPN-001 Sponsored Placement` | SPN-001 | Économie |
| 44 | `YD-MS-DPR-001 Data Product` | DPR-001 | Produits Data |
| 45 | `YD-MS-INT-001 Intelligence Product` | INT-001 | Produits Intelligence |
| 46 | `YD-MS-MOD-001 Moderation` | MOD-001 | Gouvernance |
| 47 | `YD-MS-CFG-001 Country Configuration` | CFG-001 | Gouvernance multi-pays |
| 48 | `YD-MS-CNS-001 Consent & Privacy` | CNS-001 | Privacy |

**Cible confirmée actuelle : 48 microservices métier physiques.**

# 6. Composants de plateforme autonomes confirmés

| # | Composant autonome | Responsabilité |
|---:|---|---|
| P1 | `YD-PLT-AI-001 AI Gateway` | contrôle d’accès, policy gate et entrée des usages IA |
| P2 | `YD-PLT-MLP-001 Model Lifecycle & Registry` | modèles, versions, évaluations, approbations, déploiements et retraits |
| P3 | `YD-PLT-API-001 External API Management` | exposition API externe, clients et quotas techniques |
| P4 | `YD-PLT-AUD-001 Audit & Trace` | trail transverse et preuves d’audit |

**Total autonome cible actuel : 52 = 48 microservices métier + 4 composants plateforme.** BRENDOLYS Identity reste externe à ce total.

# 7. Frontières différées

| Future frontière | Hôte initial / relation | Déclencheur d’extraction |
|---|---|---|
| `YD-MS-CAR-004 Career Simulation` | capacité rattachée initialement à CAR-002 | calcul lourd, modèles propres, SLO ou scaling distinct |
| `YD-MS-LAB-003 Labor Forecasting` | capacité exploitant LAB-002/Analytics | forecasting industrialisé, modèles/versioning/SLO propres |
| `YD-PLT-AI-004 AI Orchestration` | orchestration initiale minimale autour du Gateway et des services AI | workflows multiples, état durable ou scaling propre |

Si les trois frontières sont extraites, la cible passerait à **55 déploiements autonomes** : 50 microservices métier et 5 composants plateforme.

# 8. Frontières explicitement protégées contre fusion

- `PRF-001 / PRF-002` : profil courant contre historique long, preuves et temporalité
- `EDU-001 / EDU-002 / EDU-003 / EDU-004` : cycles, versions et responsabilités distincts
- `SKL-001 / SKL-002` : référentiel global contre données individuelles sensibles
- `CAR-001 / CAR-002` : catalogue autoritatif contre calcul de trajectoire
- `ORI-001 / REC-001` : dossier métier contre moteur de recommandation
- `LAB-001 / LAB-002` : observations contre intelligence dérivée
- `OPP-001 / OPP-002` : opportunité autoritative contre matching dérivé
- `APP-001 / EMP-002` : candidature contre décision/campagne recruteur
- `CNT-001 / CNT-002` : contenu autoritatif contre feed dérivé
- `DAT-002 / DAT-003 / DAT-004` : acquisition, preuve et validation séparées
- `ANL-001 / domaines transactionnels` : Analytics ne devient jamais source transactionnelle
- `AI-002 / AI-003` : grounding et vérification indépendants
- `BIL-001 / BIL-002` : entitlement commercial contre état financier
- `SPN-001 / REC-001 / OPP-002` : sponsoring isolé de tout score organique
- `MOD-001 / CNT-001 / COM-001` : contrôle indépendant des objets contrôlés
- `CNS-001 / services consommateurs` : consentement et finalités restent autoritatifs et séparés
- `AUD-001 / producteurs audités` : le trail ne partage pas leur datastore

# 9. Règles de comptage

1. Un `YD-MS-*` `INDEPENDENT` compte comme microservice métier physique cible.
2. Un `YD-PLT-*` compte comme déploiement autonome de plateforme.
3. Un `MERGE` ou `LOGICAL_ONLY` ne compte pas séparément.
4. Un `DEFERRED` ne compte qu’après ADR d’extraction.
5. `EXTERNAL_PLATFORM` n’entre pas dans le déploiement YDIASE.
6. `SUPERSEDED` n’entre jamais dans le comptage.
7. Web, mobile, desktop et BFF ne sont pas comptés comme microservices métier sans décision explicite.

# 10. Gates avant changement de frontière

Toute future fusion, séparation ou extraction exige un ADR qui documente problème, métriques, ownership, agrégats, contrats touchés, migration des données, migration événementielle/API, IAM, backup/restore, RTO/RPO, blast radius, coût d’exploitation, rollback et date de réévaluation.

# 11. Réconciliation post-ADR PRF

`YD-MS-PRF-002` doit être présent dans les registres d’autonomie, la closure D3, les profils individuels et les futurs contrats. Les Dependency/Event Maps historiques peuvent conserver les identifiants logiques PRF-001/PRF-002, mais toute matérialisation physique doit respecter les deux frontières autonomes.