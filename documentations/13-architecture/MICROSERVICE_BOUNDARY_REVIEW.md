# Microservice Boundary Review — BRENDOLYS YDIASE

Statut : `D3-boundary-target`

## Objet

Cette revue fixe les critères de fusion et la liste cible des frontières physiques de BRENDOLYS YDIASE. Elle s’appuie sur l’ownership D2, la Dependency Map D3 et l’Event Map D3. Elle ne choisit pas encore le runtime, le moteur de base, le broker ou l’orchestrateur.

## Principe cardinal

Un service logique n’est pas automatiquement un microservice. Une fusion ne sert jamais à réduire artificiellement le nombre de déploiements. Une séparation ne sert jamais à afficher une architecture distribuée. La frontière retenue doit protéger le métier, les données, la sécurité, l’exploitation et l’évolution indépendante.

## Statuts de frontière

- `INDEPENDENT` : microservice physique cible confirmé.
- `MERGE` : responsabilité logique conservée comme module/agrégat dans un microservice cible.
- `LOGICAL_ONLY` : capacité interne sans datastore ni déploiement métier propre.
- `PLATFORM_COMPONENT` : déploiement autonome transverse, hors comptage des microservices métier.
- `DEFERRED` : microservice cible conditionnel; documentation conservée, extraction déclenchée par seuil explicite.
- `EXTERNAL_PLATFORM` : responsabilité fournie hors YDIASE.
- `SUPERSEDED` : identifiant retiré et interdit pour une nouvelle implémentation.

# 1. Critères normatifs de fusion

## 1.1 Une fusion est autorisée seulement si tous les critères bloquants passent

### F1 — Cohérence transactionnelle
Les agrégats concernés peuvent vivre dans la même frontière sans transaction distribuée et leurs invariants métier nécessitent fréquemment une coordination locale.

### F2 — Ownership sans ambiguïté
La fusion ne crée pas deux équipes ou deux domaines concurrents propriétaires du même agrégat. Chaque agrégat garde un owner métier explicite, même à l’intérieur du même déploiement.

### F3 — Cycle de vie compatible
Les responsabilités fusionnées évoluent à une cadence comparable. Une capacité qui doit pouvoir être livrée, restaurée ou retirée indépendamment ne doit pas être fusionnée par défaut.

### F4 — Profil de charge compatible
Les patterns CPU, mémoire, I/O, stockage et latence sont suffisamment proches. Une charge massive ou très différente constitue un argument de séparation.

### F5 — Criticité compatible
Une panne de la capacité B ne doit pas rendre indisponible une capacité A qui devrait continuer seule. Si les blast radii doivent être différents, la fusion est refusée.

### F6 — Sécurité compatible
Les deux responsabilités ont des niveaux de sensibilité, politiques d’accès, realms IAM, règles de rétention et exigences d’audit compatibles. Une frontière de sécurité forte bloque la fusion.

### F7 — Données compatibles
Les données peuvent partager un datastore possédé par le même microservice sans créer d’accès croisé illégitime. Les schémas restent internes et aucun autre service n’y accède directement.

### F8 — Équipe et responsabilité opérationnelle compatibles
Une même équipe peut raisonnablement posséder code, incidents, SLO, backup, restauration et astreinte de la frontière.

### F9 — Dépendances D3 simplifiées
La fusion supprime un couplage artificiel ou un échange interne très bavard sans introduire un nouveau cycle, une dépendance cachée ou un service fourre-tout.

### F10 — Autonomie future conservée
La responsabilité fusionnée reste structurée en module interne avec contrats et ownership documentés afin de permettre une extraction future sans réécriture complète du domaine.

## 1.2 Bloqueurs absolus de fusion

Une seule condition ci-dessous suffit à refuser la fusion :

1. owners métier incompatibles
2. nécessité de restaurer une capacité sans restaurer l’autre
3. exigences de confidentialité ou de rétention incompatibles
4. besoin démontré de scaling indépendant très différent
5. cadence de livraison indépendante nécessaire
6. blast radius inacceptable
7. risque de créer une base partagée entre domaines distincts
8. mélange entre source autoritative et projection dérivée
9. mélange entre contrôle et système contrôlé lorsque l’indépendance protège l’intégrité, par exemple AI Verification face à génération
10. mélange entre contenu organique et mécanisme sponsorisé
11. mélange entre données transactionnelles et Analytics/Knowledge/Search dérivés
12. création d’un cycle synchrone interne qui réapparaîtrait lors d’une future extraction
13. fusion motivée uniquement par économie de serveurs ou facilité initiale

## 1.3 Score de décision secondaire

Après passage des bloqueurs, chaque paire reçoit une note de `0` à `2` sur : cohésion métier, besoin transactionnel local, similarité de charge, similarité sécurité, similarité cycle de vie, même équipe, même criticité, réduction de chatter, facilité de restauration commune, facilité d’extraction future.

- `16–20` : fusion forte candidate
- `11–15` : revue ADR obligatoire
- `0–10` : séparation par défaut

Le score ne peut jamais annuler un bloqueur absolu.

# 2. Critères d’extraction d’un service DEFERRED

Un service `DEFERRED` devient `INDEPENDENT` lorsqu’au moins un déclencheur fort est validé par ADR :

- scaling indépendant mesuré
- modèle de sécurité ou de données devenu différent
- équipe propriétaire distincte
- cadence de livraison indépendante nécessaire
- SLO/RTO/RPO incompatibles avec le service hôte
- technologie spécialisée justifiée
- volume ou coût du workload perturbe le service hôte
- blast radius à réduire
- produit ou contrat externe propre
- contraintes réglementaires ou territoriales propres

# 3. Décisions de fusion validées

| Service logique | Décision | Hôte physique | Motif principal |
|---|---|---|---|
| PRF-002 Education & Experience Profile | MERGE | `YD-MS-PRF-001 Profile` | même sujet, confidentialité, ownership et cohérence de profil |
| CAR-003 Career Transition | MERGE | `YD-MS-CAR-002 Career Path` | même famille de trajectoires et même charge fonctionnelle |
| ORI-002 Comparison & Decision Support | MERGE | `YD-MS-ORI-001 Orientation` | comparaison intrinsèque au dossier de décision |
| RSH-001 Academic Research Topic | LOGICAL_ONLY | `YD-MS-REC-001 Recommendation` | moteur spécialisé de recommandation, sans autorité propre justifiant un datastore |
| EMP-003 Employer Workspace | LOGICAL_ONLY | Edge/BFF employeur | façade d’expérience sans agrégat métier autoritatif |
| INS-001 Institution Workspace | LOGICAL_ONLY | Edge/BFF institution | workflow/façade; EDU reste autoritatif |
| ADM-001 Administration | LOGICAL_ONLY | Admin plane | commandes administratives vers les owners, aucune DB métier autoritative |

# 4. Responsabilités hors microservices métier YDIASE

| Responsabilité | Statut | Décision |
|---|---|---|
| IDN-001 Identity & Access | EXTERNAL_PLATFORM | BRENDOLYS Identity fournit l’IAM; YDIASE ne stocke aucun mot de passe utilisateur |
| REC-002 Application historique | SUPERSEDED | remplacé par APP-001 |

BRENDOLYS Identity utilise trois realms : `brendolys-internal`, `brendolys-networks`, `brendolys-customers`.

Issuer OIDC : `https://sso.godinfradsby.xyz/realms/{realm}/protocol/openid-connect`.

# 5. Liste cible — microservices métier confirmés

Les identifiants physiques `YD-MS-*` deviennent les identifiants de frontières de déploiement. Les anciens `YD-SVC-*` restent les identifiants des services logiques et responsabilités documentaires.

| # | Microservice physique cible | Services logiques contenus | Domaine |
|---:|---|---|---|
| 1 | `YD-MS-PRF-001 Profile` | PRF-001 + PRF-002 | Identité-profils |
| 2 | `YD-MS-EDU-001 Institution Catalog` | EDU-001 | Éducation |
| 3 | `YD-MS-EDU-002 Program Catalog` | EDU-002 | Éducation |
| 4 | `YD-MS-EDU-003 Curriculum & Module` | EDU-003 | Éducation |
| 5 | `YD-MS-EDU-004 Qualification Framework` | EDU-004 | Éducation |
| 6 | `YD-MS-SKL-001 Skills Knowledge` | SKL-001 | Compétences |
| 7 | `YD-MS-SKL-002 User Skills Profile` | SKL-002 | Compétences |
| 8 | `YD-MS-CAR-001 Occupation & Career Graph` | CAR-001 | Métiers-carrières |
| 9 | `YD-MS-CAR-002 Career Path & Transition` | CAR-002 + CAR-003 | Métiers-carrières |
| 10 | `YD-MS-ASM-001 Assessment` | ASM-001 | Orientation |
| 11 | `YD-MS-ORI-001 Orientation & Decision Support` | ORI-001 + ORI-002 | Orientation |
| 12 | `YD-MS-REC-001 Recommendation` | REC-001 + RSH-001 logical module | Orientation |
| 13 | `YD-MS-SRH-001 Search & Discovery` | SRH-001 | Plateforme produit |
| 14 | `YD-MS-LAB-001 Labor Signals` | LAB-001 | Marché du travail |
| 15 | `YD-MS-LAB-002 Labor Market Intelligence` | LAB-002 | Marché du travail |
| 16 | `YD-MS-OPP-001 Opportunity` | OPP-001 | Opportunités |
| 17 | `YD-MS-OPP-002 Opportunity Matching` | OPP-002 | Opportunités |
| 18 | `YD-MS-APP-001 Application` | APP-001 | Recrutement |
| 19 | `YD-MS-EMP-001 Employer` | EMP-001 | Recrutement |
| 20 | `YD-MS-EMP-002 Talent & Recruitment` | EMP-002 | Recrutement |
| 21 | `YD-MS-CNT-001 Content` | CNT-001 | Contenu |
| 22 | `YD-MS-CNT-002 Feed` | CNT-002 | Contenu |
| 23 | `YD-MS-COM-001 Community` | COM-001 | Communauté |
| 24 | `YD-MS-LRN-001 Learning Discovery` | LRN-001 | Learning |
| 25 | `YD-MS-NTF-001 Notification` | NTF-001 | Plateforme produit |
| 26 | `YD-MS-PRT-001 Partner` | PRT-001 | Écosystème |
| 27 | `YD-MS-AMB-001 Ambassador Network` | AMB-001 | Écosystème |
| 28 | `YD-MS-DAT-001 Data Source Registry` | DAT-001 | Data |
| 29 | `YD-MS-DAT-002 Data Acquisition` | DAT-002 | Data |
| 30 | `YD-MS-DAT-003 Data Provenance` | DAT-003 | Data |
| 31 | `YD-MS-DAT-004 Data Quality & Validation` | DAT-004 | Data |
| 32 | `YD-MS-DAT-005 Reference & Taxonomy` | DAT-005 | Data |
| 33 | `YD-MS-KNW-001 Knowledge Graph` | KNW-001 | Knowledge |
| 34 | `YD-MS-ANL-001 Analytics` | ANL-001 | Analytics |
| 35 | `YD-MS-ANL-002 Institution Intelligence` | ANL-002 | Analytics produit |
| 36 | `YD-MS-ANL-003 Employer Intelligence` | ANL-003 | Analytics produit |
| 37 | `YD-MS-AI-002 Retrieval & Grounding` | AI-002 | AI |
| 38 | `YD-MS-AI-003 AI Verification` | AI-003 | AI |
| 39 | `YD-MS-BIL-001 Subscription & Entitlement` | BIL-001 | Économie |
| 40 | `YD-MS-BIL-002 Billing` | BIL-002 | Économie |
| 41 | `YD-MS-MKT-001 Learning Marketplace` | MKT-001 | Économie |
| 42 | `YD-MS-SPN-001 Sponsored Placement` | SPN-001 | Économie |
| 43 | `YD-MS-DPR-001 Data Product` | DPR-001 | Produits Data |
| 44 | `YD-MS-INT-001 Intelligence Product` | INT-001 | Produits Intelligence |
| 45 | `YD-MS-MOD-001 Moderation` | MOD-001 | Gouvernance |
| 46 | `YD-MS-CFG-001 Country Configuration` | CFG-001 | Gouvernance multi-pays |
| 47 | `YD-MS-CNS-001 Consent & Privacy` | CNS-001 | Privacy |

**Cible confirmée actuelle : 47 microservices métier physiques.**

# 6. Composants de plateforme autonomes confirmés

Ils suivent le même standard d’autonomie opérationnelle qu’un microservice, mais ne sont pas comptés dans les 47 microservices métier.

| # | Composant autonome | Responsabilité |
|---:|---|---|
| P1 | `YD-PLT-AI-001 AI Gateway` | contrôle d’accès, policy gate et entrée des usages IA |
| P2 | `YD-PLT-MLP-001 Model Lifecycle & Registry` | modèles, versions, évaluations, approbations, déploiements et retraits |
| P3 | `YD-PLT-API-001 External API Management` | exposition API externe, clients et quotas techniques |
| P4 | `YD-PLT-AUD-001 Audit & Trace` | trail transverse et preuves d’audit |

**Total des déploiements autonomes confirmés à ce stade : 51 = 47 microservices métier + 4 composants de plateforme.** BRENDOLYS Identity reste externe à ce total.

# 7. Frontières différées

| Future frontière | Hôte initial / relation | Déclencheur d’extraction |
|---|---|---|
| `YD-MS-CAR-004 Career Simulation` | capacité rattachée initialement à CAR-002 | calcul lourd, modèles propres, SLO ou scaling distinct |
| `YD-MS-LAB-003 Labor Forecasting` | capacité exploitant LAB-002/Analytics | forecasting industrialisé, modèles/versioning/SLO propres |
| `YD-PLT-AI-004 AI Orchestration` | orchestration initiale minimale autour du Gateway et des services AI | plusieurs workflows/modèles/outils, état de workflow durable ou scaling propre |

Si les trois frontières sont extraites, la cible passerait à **53 déploiements autonomes** : 49 microservices métier et 4 composants de plateforme, en considérant Career Simulation et Labor Forecasting comme métier et AI Orchestration comme plateforme.

# 8. Frontières explicitement protégées contre fusion

Les couples suivants restent séparés même si une implémentation commune semblerait moins coûteuse :

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

1. Un `YD-MS-*` `INDEPENDENT` compte comme un microservice métier physique cible.
2. Un `YD-PLT-*` compte comme déploiement autonome de plateforme, pas comme microservice métier.
3. Un `MERGE` ou `LOGICAL_ONLY` ne compte pas séparément.
4. Un `DEFERRED` ne compte qu’après ADR d’extraction.
5. `EXTERNAL_PLATFORM` n’entre pas dans le déploiement YDIASE.
6. `SUPERSEDED` n’entre jamais dans le comptage.
7. Les Web/mobile/desktop/BFF ne sont pas comptés comme microservices métier sauf décision future explicite.

# 10. Gates avant changement de frontière

Toute future fusion, séparation ou extraction exige un ADR qui documente : problème, métriques, ownership, agrégats, contrats touchés, migration des données, migration événementielle/API, IAM, backup/restore, RTO/RPO, blast radius, coût d’exploitation, rollback et date de réévaluation.

# 11. Prochaine étape

La liste cible est maintenant suffisamment précise pour créer `MICROSERVICE_AUTONOMY_STANDARD.md`. Ce standard définira ce que signifie concrètement « autonome » pour chacun des 47 microservices métier et des 4 composants de plateforme : repository, datastore, backup/restore, API, DNS, IAM, identité machine, secrets, certificats, réseau, chiffrement, audit, logs, métriques, traces, health/readiness, quotas, rate limiting, CI/CD, déploiement, rollback, scaling, SLO, RTO/RPO, runbook, DR et retrait.
