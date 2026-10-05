# R1 — Inventaire documentaire gouverné — BRENDOLYS YDIASE

Statut : `R1-IN-PROGRESS / STRUCTURAL-INVENTORY-ESTABLISHED / AUTHORITY-TYPING-ESTABLISHED / LOGICAL-PHYSICAL-MAPPING-ESTABLISHED / EXHAUSTIVE-TREE-PENDING`

## 1. Objet

Ce registre constitue l'inventaire gouverné de restructuration du corpus YDIASE.

Il ne décide pas encore quelle information est canonique lorsqu'une analyse de contenu est nécessaire. Cette responsabilité appartient à `R2 — Canonicality Map`.

R1 répond d'abord à :
- qu'est-ce qui existe ?
- de quelle nature est chaque famille documentaire ?
- quel niveau de connaissance représente-t-elle ?
- son emplacement actuel est-il structurellement viable ?
- quelle disposition de migration est probable ?
- quelles vérifications restent nécessaires avant déplacement ?

## 2. Règles de classification

Dispositions :
- `KEEP`
- `MOVE`
- `GROUP`
- `SPLIT`
- `MERGE`
- `REFERENCE`
- `SUPERSEDE`
- `ARCHIVE`
- `REVIEW`

Confiance :
- `HIGH` : nature et destination conceptuelle déterminables sans ambiguïté ;
- `MEDIUM` : famille claire, destination exacte à confirmer ;
- `LOW` : contenu/canonicalité à lire avant toute décision.

Aucun `MERGE`, `SUPERSEDE` ou `ARCHIVE` définitif n'est autorisé par R1 seul.



## 2A. Registres R1 normatifs associés

- `DOCUMENT_TYPE_AUTHORITY_MODEL.md` définit les types documentaires, la normativité, les couches de réalité et les règles de priorité.
- `LOGICAL_TO_PHYSICAL_BOUNDARY_REGISTER.md` définit la navigation entre services logiques, microservices, composants plateforme, capacités LOGICAL_ONLY, plateformes externes, éléments superseded et deferred.
- `DOCUMENTATION_INFORMATION_ARCHITECTURE_REVIEW.md` définit l'architecture d'information cible et les phases R0–R10.

R1 ne doit pas recopier leurs détails : il les référence.

## 3. Vue structurelle actuelle

| Zone actuelle | Nature | Diagnostic R1 | Disposition probable |
|---|---|---|---|
| racine `documentations/` | entrée + registre | utile mais navigation insuffisante à l'échelle actuelle | GROUP/REFERENCE |
| `00-gouvernance-documentaire/` | constitution, politiques, registres, templates | bonne autorité mais trop plat à terme | GROUP |
| `01-fondations-produit/` | vision et fondations produit | cohérent, peut recevoir sous-groupes à mesure qu'il croît | KEEP/GROUP |
| `02-identite-profils/` | domaine métier | domaine le plus développé ; structure plate commence à saturer | GROUP |
| `03-education-institutions/` | domaine métier | structure légère | KEEP puis enrichir |
| `04-competences-connaissances/` | domaine métier | structure légère | KEEP puis enrichir |
| `05-metiers-carrieres/` | domaine métier | structure légère | KEEP puis enrichir |
| `06-marche-travail/` | domaine métier | README minimal confirmé ; profondeur à inventorier | KEEP/REVIEW |
| `07-opportunites-recrutement/` | domaine métier | README minimal confirmé ; profondeur à inventorier | KEEP/REVIEW |
| `08-orientation-recommandation/` | domaine métier | structure légère | KEEP puis enrichir |
| `09-contenu-communaute-learning/` | domaine métier | README minimal confirmé ; profondeur à inventorier | KEEP/REVIEW |
| `10-partenaires-ecosysteme/` | domaine métier | README minimal confirmé ; profondeur à inventorier | KEEP/REVIEW |
| `11-economie-produit/` | domaine métier | README minimal confirmé ; profondeur à inventorier | KEEP/REVIEW |
| `12-data-knowledge-analytics-ai/` | capacités transversales dérivées | README absent au chemin attendu ; principes présents | GROUP/REVIEW |
| `13-architecture/` | système, DDD, services, frontières, contrats, ADR, validations | surcharge structurelle majeure | SPLIT/GROUP/MOVE |
| `14-securite-conformite/` | transverse sécurité/conformité | baseline trop seule pour cible | KEEP/GROUP |
| `15-exploitation-resilience/` | transverse opérations/résilience | baseline trop seule pour cible | KEEP/GROUP |
| `16-country-frameworks/` | adaptation pays | README + Burkina confirmés | KEEP/GROUP |
| `17-roadmap-phases/` | delivery/activation | cohérent mais devra se relier aux gates | MOVE/GROUP |
| `implementation-artifacts/` | artefacts de réalisation | nature différente du corpus normatif | MOVE/REVIEW |

## 4. Gouvernance documentaire — inventaire de familles

### 4.1 Constitution / doctrine
- `CHARTE_DOCUMENTAIRE.md`
- `NIVEAUX_AUTORITE.md`
- `CONVENTION_IDENTIFIANTS.md`
- `CYCLE_VIE_DOCUMENTAIRE.md`

Disposition : `GROUP → governance/constitution|conventions` — confiance HIGH.

### 4.2 Politiques
- `POLITIQUE_CHANGEMENT_IMPACT.md`
- `POLITIQUE_CONTRADICTIONS.md`
- `POLITIQUE_REVUE_APPROBATION.md`

Disposition : `GROUP → governance/policies` — HIGH.

### 4.3 Registres
- `AUTORITATIVE_SOURCE_REGISTRY.md`
- `REFERENTIEL_EXIGENCES.md`
- `REGISTRES.md`
- `REGISTRE_DECISIONS.md`
- `REGISTRE_HYPOTHESES.md`
- `REGISTRE_RISQUES.md`
- `REGISTRE_SOURCES.md`
- `MATRICE_TRACABILITE.md`

Disposition : `GROUP → governance/registries` — HIGH.
R2 doit vérifier le chevauchement exact entre `REGISTRES.md` et les registres spécialisés avant tout MERGE.

### 4.4 Templates
Le sous-dossier `templates/` est structurellement correct.
Disposition : KEEP, avec future séparation par type seulement si le volume le justifie.

## 5. Fondations produit

Familles observées :
- vision : `VISION_PRODUIT`, `VISION_PANAFRICAINE`, `CHARTE_FONDATRICE` ;
- problèmes/valeur : `PROBLEMES_ET_BESOINS`, `PROPOSITION_VALEUR` ;
- acteurs : `SEGMENTS_UTILISATEURS`, `PARTIES_PRENANTES` ;
- structure produit : `CARTE_DOMAINES`, `CAPACITES_PRODUIT`, `PERIMETRE_PRODUIT` ;
- stratégie : `MODELE_ECONOMIQUE`, `CRITERES_SUCCES`, `HORIZONS_PRODUIT`, `PILOTE_BURKINA` ;
- doctrine : `PRINCIPES_PRODUIT`, `DOCTRINE_PERENNITE` ;
- incertitude : `HYPOTHESES_ET_INCONNUES`.

Disposition : KEEP à court terme ; GROUP par sous-familles lors de la migration.
Aucun contenu n'est candidat à MERGE sur le titre seul.

## 6. Domaines métier

Les dix domaines de `CARTE_DOMAINES.md` restent les unités fonctionnelles de premier niveau :
1. Identity
2. Education
3. Skills
4. Careers
5. Labor
6. Opportunities
7. Guidance
8. Content
9. Partners
10. Economy

R1 ne renumérote pas ces domaines et ne les remplace pas par les microservices.

### Structure domaine cible minimale

```text
<domain>/
├── README.md
├── language/
├── model/
├── rules/
├── capabilities/
├── authority/
├── interactions/
└── validation/
```

Les sous-dossiers ne sont créés que lorsqu'un contenu réel existe.

### Cas Identity
Les fichiers actuels se répartissent déjà naturellement :
- model : `MODELE_DOMAINE`, `CYCLE_VIE_PERSONNE`, `PROFIL_ET_TEMPORALITE`, `IDENTITE_DURABLE` ;
- rules : `REGLES_METIER`, `VISIBILITE_ET_PARTAGE`, `PREUVES_ET_PROVENANCE` ;
- interactions : `FRONTIERES_ET_DEPENDANCES` ;
- capabilities : `CAPACITES_ET_TRACABILITE` ;
- validation : `GATES_ET_INCONNUES`.

Disposition : GROUP — HIGH.

### Domaines encore légers
Education, Skills, Careers, Labor, Opportunities, Guidance, Content, Partners et Economy doivent conserver leur existence même si certains README sont encore minimaux. La faible profondeur n'autorise ni fusion de domaines ni création artificielle de documents.

## 7. Architecture — décomposition R1

`13-architecture/` est le principal candidat à restructuration.

### 7.1 Vue système
- `ARCHITECTURE_CIBLE.md`
- `ARCHITECTURE_LOGIQUE.md`
- `README.md`

Destination conceptuelle : `system-architecture/overview`.
Disposition : MOVE/GROUP — HIGH.

### 7.2 DDD et frontières
- `DDD_REVIEW.md`
- `MICROSERVICE_BOUNDARY_REVIEW.md`
- `SENSITIVE_MERGER_REVIEW.md`
- `TRANSVERSAL_ARCHITECTURE_REVIEW_48.md`

Destination : `system-architecture/ddd|reviews`.
Disposition : MOVE/GROUP — HIGH.
R2 doit déterminer quelles revues restent normatives et lesquelles deviennent historical review.

### 7.3 Services logiques
`services/YD-SVC-*/SERVICE_DEFINITION.md`

Nature : service logique / responsabilité cible.
Destination : `system-architecture/logical-services/`.
Disposition : MOVE — HIGH.

Important : ces fiches ne doivent jamais être fusionnées automatiquement avec `YD-MS-*`.

### 7.4 Frontières physiques
`microservices/YD-MS-*/`

Nature : frontière autonome physique.
Destination : `system-architecture/physical-boundaries/`.
Disposition : MOVE + GROUP interne selon volume — HIGH.

### 7.5 Composants plateforme
`platform-components/YD-PLT-*/`

Nature : frontières autonomes non métier.
Destination : `system-architecture/platform-components/`.
Disposition : MOVE — HIGH.

### 7.6 Ownership et dépendances
- `DATA_OWNERSHIP_MATRIX.md`
- `DEPENDENCY_MAP.md`
- `AUTONOMY_PROFILE_REGISTER.md`
- `AUTONOMY_CLOSURE_MATRIX.md`
- `MICROSERVICE_AUTONOMY_STANDARD.md`

Destination : system-architecture/data-ownership, dependencies, physical-boundaries/governance.
Disposition : GROUP/MOVE — HIGH.

### 7.7 Contrats et événements
- `CONTRACT_REGISTRY.md`
- `CONTRACT_V1_VALIDATION_MATRIX.md`
- `EVENT_MAP.md`

Destination conceptuelle : zone indépendante `contracts/`.
Disposition : MOVE — HIGH.

Le registre reste canonique ; les futurs schémas physiques ne doivent pas être incorporés dans le même fichier.

### 7.8 Derived systems / recovery
- `DERIVED_RECOVERY_REGISTER.md`
- politiques de projection/rebuild locales SRH/CNT/KNW/ANL/AI.

Destination : vue transverse `data-knowledge-analytics-ai/derived-recovery` + documents locaux par frontière.
Disposition : REFERENCE/GROUP — MEDIUM.
R2 doit éviter la duplication entre politique locale et registre transverse.

### 7.9 Décisions
- `ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY.md`
- `ADR-PRF002-RPO-RTO.md`
- `D3_BLOCKING_CLOSURE_DECISIONS.md`

Destination : `decisions/architecture/`.
Disposition : MOVE — HIGH.

`D2_INCONSISTENCIES.md`, `D2_STATUS.md` et documents similaires doivent être évalués en R2 comme status historique, review ou norme encore active.

## 8. Structure interne des microservices — inventaire de types

Les dossiers `YD-MS-*` contiennent actuellement plusieurs types documentaires.

### A — Governance de frontière
- `AUTONOMY_PROFILE.md`
- `PHASE_CLOSURE.md`

Destination locale : `governance/`.

### B — Domain/business policies
Exemples :
- `APPLICATION_LIFECYCLE_POLICY.md`
- `ASSESSMENT_RESULT_POLICY.md`
- `CAREER_GAP_TRANSITION_POLICY.md`
- `OPPORTUNITY_LIFECYCLE_POLICY.md`
- `RECOMMENDATION_RANKING_POLICY.md`
- `LEARNING_DISCOVERY_POLICY.md`

Destination locale : `policies/`.

### C — Data/projection/source policies
Exemples :
- `DATA_GOVERNANCE_POLICY.md`
- `KNOWLEDGE_GRAPH_PROJECTION_POLICY.md`
- `SOURCE_PROJECTION_BASELINE.md`
- `ANALYTICS_SOURCE_CONTRACT_REGISTER.md`

Destination : authority/contracts/policies selon responsabilité exacte.
R2 nécessaire pour les cas hybrides.

### D — Security/privacy
Exemples :
- `PRIVACY_DECISION_POLICY.md`
- `REVOCATION_RETENTION_RECOVERY_POLICY.md`
- `COUNTRY_CHANGE_SAFETY_POLICY.md`

La règle spécifique reste locale ; la doctrine transverse est référencée depuis Security/Privacy.

### E — Resilience / DR
PRF-002 :
- `PRF002_BIA.md`
- `PRF002_BIA_ASSUMPTION_REGISTER.md`
- `PRF002_CONTINUITY_POLICY.md`
- `PRF002_BACKUP_RESTORE_POLICY.md`
- `PRF002_DR_RUNBOOK.md`

Destination locale : `resilience/` ou `operations/`.

### F — Validation / evidence
PRF-002 :
- `PRF002_DR_TEST_PLAN.md`
- `PRF002_DR_EVIDENCE_MATRIX.md`
- `PRF002_SENSITIVE_ROLE_PRACTICAL_QUALIFICATION.md`

Destination : `validation/`, avec preuves d'exécution réelles référencées depuis `evidence/`.

### G — Organisation/nomination
- `PRF002_NOMINATION_MATRIX.md`
- `PRF002_NOMINATION_REGISTER.md`

Classification : REVIEW en R2. Ces documents peuvent relever de gouvernance opérationnelle plutôt que de la frontière métier elle-même.

## 9. Data / Knowledge / Analytics / AI

Le dossier `12-data-knowledge-analytics-ai/` doit devenir une vraie porte d'entrée transverse.

R1 observe au moins `PRINCIPES.md`, mais aucun `README.md` au chemin attendu.

Disposition :
- créer ultérieurement un README canonique de navigation ;
- séparer Data, Knowledge, Analytics, AI et Derived Recovery ;
- référencer les frontières DAT/KNW/ANL/AI sans recopier leurs politiques locales.

Aucune création de nouveau « domaine Data » n'est décidée : `CARTE_DOMAINES.md` les qualifie comme capacités transversales.

## 10. Security / Privacy / Compliance

`14-securite-conformite/SECURITE_BASELINE.md` est une baseline transverse.

La cible documentaire devra distinguer :
- security architecture ;
- privacy ;
- audit/trace ;
- threat models ;
- compliance contexts ;
- policies transverses.

Les politiques spécifiques d'un microservice restent locales avec lien vers la baseline.

Disposition : KEEP puis GROUP — HIGH.

## 11. Operations / Resilience

`15-exploitation-resilience/RESILIENCE_BASELINE.md` est la baseline transverse.

La cible distinguera :
- reliability ;
- observability ;
- continuity ;
- DR ;
- runbooks ;
- incidents.

Les BIA/runbooks propres à une frontière restent locaux ; les preuves d'exécution sont indexées dans Evidence.

Disposition : KEEP puis GROUP — HIGH.

## 12. Country Frameworks

README et `BURKINA_FASO.md` sont confirmés.

Disposition : KEEP/GROUP.

Principe R1 :
- pas de fork complet de la documentation par pays ;
- Country Framework référence les différences ;
- CFG-001 porte la configuration runtime correspondante ;
- Burkina n'est jamais l'héritage implicite de l'Afrique.

## 13. Delivery / Roadmap

`17-roadmap-phases/` contient la roadmap et son entrée documentaire.

Destination conceptuelle : `delivery/roadmap`, puis activation/releases/gates lorsque ces artefacts existent.
Disposition : MOVE/GROUP — HIGH.

## 14. Experiences / surfaces — gap structurel confirmé

Aucune zone documentaire de premier niveau dédiée aux expériences/surfaces n'est encore établie dans la structure observée.

Cela ne signifie pas que les surfaces n'ont pas été prévues : `SERVICE_MAP`, capacités et roadmap en contiennent déjà des éléments.

R1 enregistre donc un **knowledge-structure gap**, pas un product gap.

Disposition future :
- créer `experiences/catalog` ;
- dériver les surfaces des acteurs, journeys, capacités, contextes d'accès et décisions existantes ;
- établir des IDs avant multiplication des fiches ;
- ne pas déduire le catalogue du seul nombre d'interfaces cité dans une conversation.

## 15. Implementation artifacts

`implementation-artifacts/spec-foundation-documentaire-ydiase.md` n'a pas la même autorité qu'une politique ou une décision canonique.

R2 doit déterminer s'il s'agit :
- d'une spécification historique ;
- d'un artefact de livraison ;
- d'une source de migration encore active.

Disposition : REVIEW — MEDIUM.

## 16. Gaps R1 à fermer

Avant de déclarer R1 complet :
1. obtenir une liste repository-tree exhaustive plutôt qu'un inventaire fondé uniquement sur code search ;
2. confirmer le nombre exact de fichiers par dossier ;
3. inventorier tous les fichiers non Markdown ;
4. confirmer les 61 dossiers `YD-SVC-*` et les 48 `YD-MS-*` contre les registres canoniques ;
5. confirmer les 4 `YD-PLT-*` ;
6. inventorier intégralement les dossiers 06, 07, 09, 10, 11, 12, 14, 15, 16, 17 ;
7. détecter liens cassés et chemins relatifs entrants ;
8. détecter documents sans statut/autorité ;
9. détecter fichiers qui mélangent plusieurs types d'autorité ;
10. produire la table fichier → type → disposition → destination candidate.

## 17. Gate de sortie R1

R1 passe `COMPLETE` uniquement si :
- inventaire physique exhaustif obtenu ;
- chaque fichier a une classification ;
- chaque incertitude est explicitement REVIEW ;
- aucun fichier n'est supprimé ;
- aucune canonicalité n'est inventée ;
- la migration peut être planifiée sans perte de connaissance.

## 18. Suite

Après fermeture R1 :
`R2 — CANONICALITY_MAP`

R2 devra notamment résoudre :
- document canonique versus vue/résumé ;
- documents historiques encore présentés comme actifs ;
- contradictions ;
- duplications réelles ;
- relations SVC ↔ MS/PLT/BFF/LOGICAL_ONLY/SUPERSEDED ;
- politiques transverses versus politiques locales ;
- statut des documents de validation et preuves.

Aucun déplacement massif n'est exécuté avant ce gate.


## 19. État R1 après normalisation d'autorité

Établi :
- architecture d'information cible ;
- classification structurelle des grandes zones ;
- modèle de type/autorité documentaire ;
- distinction normative/descriptive/evidence ;
- distinction vision/target/design/implementation/deployment/activation/evidence ;
- relation canonique service logique ↔ frontière physique ;
- règle de traitement des surfaces/experiences ;
- catégories de migration ;
- gates empêchant les déplacements prématurés.

Encore bloquant pour `R1-COMPLETE` :
- tree physique exhaustif du repository ;
- table exhaustive fichier par fichier ;
- liens entrants/sortants ;
- documents non Markdown ;
- détection systématique des documents orphelins ;
- canonicality de contenu, qui appartient ensuite à R2.

Verdict courant :
`R1-STRUCTURAL-BASELINE-STRONG / NO-MASS-MIGRATION-YET`.
