# Microservice Boundary Review — BRENDOLYS YDIASE

Statut : `D3-boundary-decision`

## Objet

Cette revue transforme les services logiques candidats en frontières physiques candidates. Elle s’appuie sur l’ownership D2, la Dependency Map D3 et l’Event Map D3. Elle ne choisit pas encore le runtime, la base, le broker ou l’orchestrateur.

## Règle de décision

- `INDEPENDENT` : frontière physique autonome retenue dans la cible.
- `MERGE` : responsabilité logique conservée, mais hébergée dans le microservice cible indiqué.
- `SPLIT` : le service logique doit produire plusieurs frontières physiques.
- `LOGICAL_ONLY` : capacité interne d’un autre microservice, sans déploiement propre.
- `PLATFORM_COMPONENT` : composant autonome de plateforme, compté séparément des microservices métier.
- `DEFERRED` : frontière cible conservée mais décision physique reportée jusqu’au seuil d’activation.
- `EXTERNAL_PLATFORM` : responsabilité fournie par une plateforme Brendolys externe à YDIASE.
- `SUPERSEDED` : identifiant retiré, non implémentable.

## Critères utilisés

Chaque décision tient compte de : ownership d’agrégats, invariants transactionnels, couplage, dépendances D3, événements, sécurité, criticité, profil de charge, fréquence de changement, autonomie de déploiement, autonomie de restauration, données possédées, besoin d’isolation et risque de cycle.

## Décisions

| Service logique | Décision physique | Frontière cible / justification |
|---|---|---|
| IDN-001 Identity & Access | EXTERNAL_PLATFORM | L’authentification est fournie par BRENDOLYS Identity. YDIASE ne doit pas créer un second IAM. Les profils et objets métier gardent seulement les `subject_id` externes et leurs autorisations applicatives. |
| PRF-001 Profile | INDEPENDENT | Profil individuel, préférences et objectifs ont leur propre cycle de vie et données personnelles. |
| PRF-002 Education & Experience Profile | MERGE → PRF-001 | Même sujet, même frontière de confidentialité et fort besoin de cohérence avec le profil. Garder les agrégats séparés dans le même microservice. Revue de split uniquement si charge ou équipe diverge fortement. |
| EDU-001 Institution Catalog | INDEPENDENT | Référentiel établissement autonome et partagé. |
| EDU-002 Program Catalog | INDEPENDENT | Programme possède son cycle de version et ses règles propres. |
| EDU-003 Curriculum & Module | INDEPENDENT | Historique/versionnement curriculum distinct et volume potentiellement élevé. |
| EDU-004 Qualification Framework | INDEPENDENT | Cadres nationaux, équivalences et règles multi-pays exigent une frontière dédiée. |
| SKL-001 Skills Knowledge | INDEPENDENT | Référentiel transversal fortement réutilisé. |
| SKL-002 User Skills Profile | INDEPENDENT | Données individuelles sensibles, charge et rétention différentes du référentiel Skills. |
| CAR-001 Occupation & Career Graph | INDEPENDENT | Source métier des occupations et relations professionnelles. |
| CAR-002 Career Path | INDEPENDENT | Calcul et persistance des trajectoires peuvent évoluer/scaler séparément du catalogue métier. |
| CAR-003 Career Transition | MERGE → CAR-002 | Même famille d’agrégats dérivés et même profil de charge. Conserver module/agrégats séparés dans Career Path. |
| CAR-004 Career Simulation | DEFERRED | Candidat à extraction depuis CAR-002 lorsque simulation lourde, modèles spécifiques ou scaling indépendant apparaissent. Pas de microservice séparé au pilote. |
| ASM-001 Assessment | INDEPENDENT | Données personnelles sensibles, sessions et règles d’évaluation propres. |
| ORI-001 Orientation | INDEPENDENT | Owner du dossier d’orientation et orchestration métier. |
| ORI-002 Comparison & Decision Support | MERGE → ORI-001 | Fonction directement liée au dossier d’orientation, sans owner externe nécessitant une frontière physique. |
| REC-001 Recommendation | INDEPENDENT | Calcul, versionnement, explicabilité et scaling distincts. |
| RSH-001 Academic Research Topic | LOGICAL_ONLY → REC-001 | Capacité spécialisée de recommandation. Extraction future possible si elle devient un produit autonome. |
| SRH-001 Search & Discovery | INDEPENDENT | Index reconstruisible, charge lecture spécifique et scaling indépendant. |
| LAB-001 Labor Signals | INDEPENDENT | Source autoritative des signaux normalisés. |
| LAB-002 Labor Market Intelligence | INDEPENDENT | Produits analytiques du marché séparés des observations brutes. |
| LAB-003 Labor Forecasting | DEFERRED | Frontière cible probable, activée lorsque forecasting industrialisé et évalué. |
| OPP-001 Opportunity | INDEPENDENT | Owner transactionnel des opportunités. |
| OPP-002 Opportunity Matching | INDEPENDENT | Charge de calcul et logique de matching indépendantes; ne doit pas être absorbé par Recommendation générale. |
| REC-002 Application historique | SUPERSEDED | Remplacé par APP-001. |
| APP-001 Application | INDEPENDENT | Owner des candidatures et transitions d’état. |
| EMP-001 Employer | INDEPENDENT | Référentiel employeur. |
| EMP-002 Talent & Recruitment | INDEPENDENT | Campagnes, viviers et décisions de recrutement ont leurs invariants propres. |
| EMP-003 Employer Workspace | LOGICAL_ONLY | BFF/experience layer. À implémenter comme façade stateless ou module d’edge, sans base métier propriétaire. |
| CNT-001 Content | INDEPENDENT | Publication/versionnement de contenu. |
| CNT-002 Feed | INDEPENDENT | Ranking/feed et charge lecture très différents du Content Service. |
| COM-001 Community | INDEPENDENT | Interactions, commentaires et relations sociales ont leur propre charge et modération. |
| LRN-001 Learning Discovery | INDEPENDENT | Agrège des ressources de formation sans devenir owner des programmes; peut évoluer comme produit propre. |
| NTF-001 Notification | INDEPENDENT | Effets externes, retries, canaux et idempotence exigent une isolation forte. |
| PRT-001 Partner | INDEPENDENT | Conventions, rôles et droits partenaires. |
| AMB-001 Ambassador Network | INDEPENDENT | Mandats, renouvellements et contributions distincts du Partner générique. |
| INS-001 Institution Workspace | LOGICAL_ONLY | BFF/workflow d’expérience. Les soumissions restent dans ce module mais aucune donnée EDU autoritative n’y réside. Extraction seulement si workflow institutionnel devient complexe. |
| DAT-001 Data Source Registry | INDEPENDENT | Droits d’usage et registre des sources sont une frontière de gouvernance forte. |
| DAT-002 Data Acquisition | INDEPENDENT | Connecteurs, batches, raw envelopes et scaling ingestion propres. |
| DAT-003 Data Provenance | INDEPENDENT | Lineage et preuve doivent survivre indépendamment des pipelines. |
| DAT-004 Data Quality & Validation | INDEPENDENT | Moteur de validation/corroboration et décisions qualité séparés de l’ingestion. |
| DAT-005 Reference & Taxonomy | INDEPENDENT | Référentiels transversaux versionnés. |
| KNW-001 Knowledge Graph | INDEPENDENT | Stockage/charge/reconstruction propres et aucune autorité sur les entités sources. |
| ANL-001 Analytics | INDEPENDENT | Agrégations et datasets analytiques isolés des transactions. |
| ANL-002 Institution Intelligence | INDEPENDENT | Produit B2B, droits, métriques et évolution propres. Peut partager infrastructure analytique, pas la base transactionnelle. |
| ANL-003 Employer Intelligence | INDEPENDENT | Produit B2B distinct avec données et contrats d’accès propres. |
| AI-001 AI Gateway | PLATFORM_COMPONENT | Policy gate central des usages IA. Autonome mais classé plateforme plutôt que métier. |
| AI-002 Retrieval & Grounding | INDEPENDENT | Index/corpus et profil de charge propres. |
| AI-003 AI Verification | INDEPENDENT | Frontière de contrôle indépendante de la génération; évite l’auto-validation. |
| AI-004 AI Orchestration | DEFERRED | À extraire lorsque plusieurs workflows/modèles/outils exigent orchestration indépendante. |
| MLP-001 Model Lifecycle & Registry | PLATFORM_COMPONENT | Frontière MLOps autonome : versions, évaluations, approbations, déploiements et retraits de modèles. |
| BIL-001 Subscription & Entitlement | INDEPENDENT | Autorité commerciale des plans, produits, droits et quotas. |
| BIL-002 Billing | INDEPENDENT | Transactions financières, factures et intégrations de paiement isolées. |
| MKT-001 Learning Marketplace | INDEPENDENT | Orders/listings et modèle économique propre. |
| SPN-001 Sponsored Placement | INDEPENDENT | Isolation obligatoire vis-à-vis des scores organiques. |
| API-001 External API Management | PLATFORM_COMPONENT | Exposition, clients API, quotas techniques et usage; ne possède pas les données exposées. |
| DPR-001 Data Product | INDEPENDENT | Releases de datasets gouvernés, licences et livraisons propres. |
| INT-001 Intelligence Product | INDEPENDENT | Éditions, briefs et produits d’intelligence ont leur cycle produit propre. |
| ADM-001 Administration | LOGICAL_ONLY | Admin plane/BFF sans ownership métier. Commande les domaines via contrats. |
| MOD-001 Moderation | INDEPENDENT | Policy et décisions de modération doivent rester séparées des contenus modérés. |
| AUD-001 Audit & Trace | PLATFORM_COMPONENT | Trail transverse, append-only et sécurité propres. |
| CFG-001 Country Configuration | INDEPENDENT | Configuration multi-pays partagée par tous les domaines. |
| CNS-001 Consent & Privacy | INDEPENDENT | Autorité privacy/consentement, données très sensibles et fail-closed. |

## Résultat cible

La revue ne valide plus l’hypothèse `1 service logique = 1 microservice`.

- `EXTERNAL_PLATFORM` : 1 responsabilité — Identity & Access, fournie par BRENDOLYS Identity.
- `SUPERSEDED` : 1 ancien identifiant — REC-002.
- `MERGE` : PRF-002, CAR-003, ORI-002.
- `LOGICAL_ONLY` : RSH-001, EMP-003, INS-001, ADM-001.
- `DEFERRED` : CAR-004, LAB-003, AI-004.
- `PLATFORM_COMPONENT` : AI-001, MLP-001, API-001, AUD-001.
- Toutes les autres frontières listées `INDEPENDENT` deviennent des microservices physiques cibles candidats.

Le comptage physique doit être recalculé depuis ce fichier lors de la mise à jour du Service Map. Les éléments `DEFERRED` ne sont pas comptés comme microservices actifs tant que leur seuil d’extraction n’est pas atteint. Les `PLATFORM_COMPONENT` sont des déploiements autonomes mais restent distingués des microservices métier.

## BRENDOLYS Identity — contrainte externe

YDIASE utilise BRENDOLYS Identity comme IAM. Les trois realms imposés sont :

- `brendolys-internal` : employés et équipe interne Brendolys
- `brendolys-networks` : ambassadeurs et autres membres externes des réseaux
- `brendolys-customers` : élèves, étudiants, professionnels, organisations clientes et utilisateurs clients

Issuer OIDC client : `https://sso.godinfradsby.xyz/realms/{realm}/protocol/openid-connect`.

Aucun microservice YDIASE ne stocke de mot de passe utilisateur. Les contrats futurs doivent définir les audiences, clients, scopes, rôles, claims minimaux et règles de service-to-service. Le simple fait qu’un token soit valide ne donne aucun droit métier.

## Règles d’autonomie physique après confirmation

Une frontière `INDEPENDENT` ou `PLATFORM_COMPONENT` devra ensuite recevoir : dépôt Git propre, ownership d’équipe, API/événements propres, datastore possédé, migrations, sauvegarde et restauration indépendantes, secrets propres, identité machine, politiques réseau, chiffrement, audit, observabilité, health/readiness, quotas, déploiement/rollback, scaling, DR, runbook, DNS si exposition réseau nécessaire et procédure de retrait.

Une base dédiée signifie propriété exclusive du schéma et du cycle de sauvegarde; elle n’impose pas nécessairement un serveur physique de base de données par service. La décision d’isolation physique du moteur de base dépendra de criticité, sécurité, charge et coût.

## Gates avant implémentation

Une frontière ne devient microservice implémentable que si :

1. ses agrégats ont un owner unique
2. ses dépendances D3 sont acycliques au niveau synchrone
3. ses contrats entrants/sortants sont enregistrés
4. son modèle IAM et ses realms autorisés sont définis
5. son datastore et sa politique backup/restore sont définis
6. ses SLO, RTO et RPO sont définis selon criticité
7. son runbook minimal existe
8. son mode dégradé est défini
9. ses données sensibles et finalités sont classifiées
10. son autonomie de déploiement et de rollback est démontrable

## Étape suivante

Mettre à jour `SERVICE_MAP.md` et `DDD_REVIEW.md` avec ces décisions, puis créer `MICROSERVICE_AUTONOMY_STANDARD.md`. Le Contract Registry vient après ce standard afin que chaque contrat soit rattaché à une frontière physique et à une politique IAM explicites.
