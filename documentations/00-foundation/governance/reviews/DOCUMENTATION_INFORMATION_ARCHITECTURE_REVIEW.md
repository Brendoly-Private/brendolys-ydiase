---
document_id: "YD-DOC-FND-REV-001"
title: "Revue d'architecture de l'information documentaire — BRENDOLYS YDIASE"
document_type: "documentation-architecture-review"
document_role: "Consigne la revue d’architecture de l’information ayant motivé la restructuration du corpus et ses critères de migration."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
owners:
  - "Documentation Governance"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "foundation"
  - "documentation-migration"
---

# Revue d'architecture de l'information documentaire — BRENDOLYS YDIASE

> **Rôle du document**
> Consigne la revue d’architecture de l’information ayant motivé la restructuration du corpus et ses critères de migration.
> **Usage développement :** support de migration et de traçabilité ; les sources canoniques actives restent autoritatives.

Statut : `BASELINE-CANDIDATE / RESTRUCTURING-AUTHORIZED`

## 1. Décision

La documentation YDIASE doit être traitée comme un **système de connaissance gouverné**, et non comme une collection croissante de fichiers Markdown.

La présente revue autorise une restructuration progressive du corpus sans modifier silencieusement les décisions métier ou architecturales existantes.

La restructuration doit préserver :
- les identifiants stables ;
- l'autorité documentaire ;
- l'historique et les statuts ;
- la séparation domaine / capacité / service logique / frontière physique / plateforme / infrastructure ;
- la traçabilité vers contrats, vérifications et preuves ;
- les liens de supersession ;
- la distinction cible / implémentation / déploiement / activation.

Aucun déplacement de fichier ne vaut changement sémantique.

## 2. Problème constaté

Le corpus a atteint une taille où la structure initiale n'est plus suffisante.

Le dossier Architecture concentre désormais des documents de natures très différentes : vues système, DDD, services logiques, frontières physiques, composants plateforme, contrats, événements, ownership, dépendances, ADR, recovery, validations et revues transverses.

Les dossiers `services/YD-SVC-*` et `microservices/YD-MS-*` sont légitimes mais représentent deux niveaux différents. Sans navigation explicite, ils peuvent être interprétés comme deux sources concurrentes.

Plusieurs domaines produit restent beaucoup moins détaillés que l'architecture physique.

Les surfaces produit sont prévues dans la cible mais ne disposent pas encore d'une architecture documentaire propre suffisamment structurée. La restructuration ne doit pas réduire ces surfaces aux interfaces déjà évoquées lors d'une conversation : leur catalogue canonique doit être dérivé des décisions produit, capacités, acteurs et phases.

Enfin, les microservices les plus documentés accumulent progressivement des politiques, profils, plans, matrices et documents de clôture au même niveau.

## 3. Objectifs de long terme

Le système documentaire doit rester exploitable même si :
- le nombre de frontières évolue fortement ;
- YDIASE couvre de nombreux pays ;
- les technologies actuelles disparaissent ;
- plusieurs générations d'équipes se succèdent ;
- les interfaces et canaux changent ;
- certains microservices fusionnent ou sont scindés ;
- plusieurs IA spécialisées assistent architecture, développement, tests, sécurité et exploitation.

La pérennité ne signifie pas figer l'arborescence pendant des siècles. Elle signifie rendre **les concepts, identités, décisions, provenance et relations migrables sans perte de sens**.

## 4. Principes structurants

### P1 — Une information, une autorité canonique
Une règle normative ne doit pas être copiée dans plusieurs dossiers. Les autres vues la référencent.

### P2 — Plusieurs chemins de lecture, une seule vérité
La même connaissance doit être accessible par domaine, frontière, contrat, surface, phase ou tâche sans duplication normative.

### P3 — README comme porte d'entrée
Tout dossier significatif possède un `README.md` qui explique : rôle, autorité, contenu, ordre de lecture, dépendances, documents canoniques et éléments non applicables.

### P4 — Localité de connaissance
La connaissance spécifique à une frontière reste proche de cette frontière. La connaissance transverse reste dans un registre/politique transverse et est référencée localement.

### P5 — Progressive disclosure
Un lecteur commence par une carte concise puis descend vers le détail. Il ne doit pas lire 100 fichiers pour comprendre un microservice.

### P6 — Navigation humaine et IA
Les chemins, métadonnées, identifiants et index doivent permettre un retrieval déterministe et borné.

### P7 — Séparer intention et réalisation
Produit, domaine, architecture logique, architecture physique, contrats, implémentation, déploiement et exploitation restent séparés.

### P8 — Les surfaces ne possèdent pas implicitement le métier
Une application, un portail, un BFF ou une interface compose des capacités ; elle ne devient pas owner des agrégats métier par commodité.

### P9 — Pas de structure dépendante d'une technologie
Kafka, Kubernetes, PostgreSQL, un framework Web ou un modèle IA peuvent changer sans obliger à réécrire la taxonomie fondamentale.

### P10 — Country context explicite
Les variantes pays se rattachent au Country Framework et aux objets concernés. Aucun pays n'est implicite.

## 5. Architecture documentaire cible

La numérotation finale sera décidée lors de la migration. Les noms ci-dessous expriment les **zones de connaissance**, pas encore les chemins physiques définitifs.

```text
documentations/
├── governance/
│   ├── constitution/
│   ├── policies/
│   ├── registries/
│   ├── conventions/
│   └── templates/
│
├── product/
│   ├── vision/
│   ├── problems-needs/
│   ├── actors-segments/
│   ├── capabilities/
│   ├── value-economics/
│   ├── success/
│   └── horizons/
│
├── domains/
│   └── <domain>/
│       ├── README.md
│       ├── language/
│       ├── model/
│       ├── rules/
│       ├── capabilities/
│       ├── authority/
│       ├── interactions/
│       └── validation/
│
├── system-architecture/
│   ├── overview/
│   ├── ddd/
│   ├── logical-services/
│   ├── physical-boundaries/
│   ├── platform-components/
│   ├── dependencies/
│   ├── data-ownership/
│   ├── derived-systems/
│   └── reviews/
│
├── contracts/
│   ├── registry/
│   ├── api/
│   ├── events/
│   ├── projections/
│   ├── jobs/
│   ├── schemas/
│   ├── compatibility/
│   └── validation/
│
├── experiences/
│   ├── catalog/
│   ├── journeys/
│   ├── surfaces/
│   ├── composition/
│   ├── access-contexts/
│   └── experience-contracts/
│
├── data-knowledge-analytics-ai/
│   ├── data/
│   ├── knowledge/
│   ├── analytics/
│   ├── ai/
│   ├── provenance-quality/
│   └── derived-recovery/
│
├── security-privacy-compliance/
│   ├── security/
│   ├── privacy/
│   ├── audit/
│   ├── threat-models/
│   └── compliance-contexts/
│
├── engineering/
│   ├── standards/
│   ├── implementation-guides/
│   ├── testing/
│   ├── migrations/
│   └── developer-workflows/
│
├── operations/
│   ├── reliability/
│   ├── observability/
│   ├── continuity/
│   ├── disaster-recovery/
│   ├── runbooks/
│   └── incidents/
│
├── country-frameworks/
│   ├── core/
│   └── countries/
│
├── delivery/
│   ├── roadmap/
│   ├── activation/
│   ├── releases/
│   └── gates/
│
├── decisions/
│   ├── architecture/
│   ├── product/
│   ├── data/
│   └── retired/
│
├── evidence/
│   ├── contract-tests/
│   ├── rebuild/
│   ├── resilience/
│   ├── security/
│   └── acceptance/
│
└── knowledge-index/
    ├── START_HERE.md
    ├── KNOWLEDGE_MAP.md
    ├── DOMAIN_CATALOG.md
    ├── CAPABILITY_CATALOG.md
    ├── SERVICE_CATALOG.md
    ├── BOUNDARY_CATALOG.md
    ├── CONTRACT_CATALOG.md
    ├── EXPERIENCE_CATALOG.md
    ├── DECISION_CATALOG.md
    ├── EVIDENCE_CATALOG.md
    └── AI_RETRIEVAL_GUIDE.md
```

Cette structure est conceptuelle : elle sera confrontée à chaque fichier existant avant migration physique.

## 6. Structure canonique d'une frontière autonome

Un microservice ne reçoit pas mécaniquement tous les sous-dossiers. Ils sont créés lorsque du contenu réel existe.

```text
YD-MS-XXX-001/
├── README.md
├── domain/
│   ├── responsibility.md
│   ├── invariants.md
│   └── lifecycle.md
├── authority/
│   ├── owned-data.md
│   └── consumed-data.md
├── contracts/
│   ├── inbound.md
│   └── outbound.md
├── policies/
├── security/
├── resilience/
├── operations/
├── validation/
│   ├── test-plan.md
│   └── evidence.md
└── governance/
    ├── autonomy-profile.md
    └── phase-closure.md
```

Le `README.md` de frontière doit fournir en moins d'une lecture :
- mission ;
- owner métier / domaine ;
- type AUTH / DERIVED / MIXED ;
- criticité ;
- données possédées ;
- dépendances principales ;
- contrats principaux ;
- invariants critiques ;
- privacy/security class ;
- état documentation / implémentation / déploiement / activation ;
- état recovery ;
- ordre de lecture ciblé.

## 7. Services logiques versus frontières physiques

Les deux vues sont conservées mais leur relation devient explicite.

### Service logique `YD-SVC-*`
Répond à : **quelle responsabilité/capacité logique existe dans la cible ?**

Il documente :
- mission logique ;
- capacités ;
- bounded context ;
- acteurs ;
- règles de haut niveau ;
- données conceptuelles ;
- phase cible.

### Frontière physique `YD-MS-*`
Répond à : **où cette autorité/responsabilité est-elle isolée opérationnellement ?**

Elle documente :
- ownership physique ;
- datastore authority ;
- contrats runtime ;
- isolation ;
- recovery ;
- sécurité opérationnelle ;
- observabilité ;
- preuves.

Une table canonique `YD-SVC → YD-MS/YD-PLT/LOGICAL_ONLY/BFF/SUPERSEDED` doit permettre la navigation bidirectionnelle.

## 8. Architecture documentaire des expériences et surfaces

La couche `experiences/` ne part pas d'un nombre d'interfaces prédéterminé.

Elle part de :
1. acteurs et segments ;
2. journeys et jobs-to-be-done validés ;
3. capacités produit ;
4. contextes d'accès ;
5. contraintes de terminal/connectivité/accessibilité ;
6. droits et entitlements ;
7. compositions de services.

Le catalogue peut contenir, selon les décisions actives : applications, portails, workspaces, interfaces internes, expériences terrain, API ou autres canaux futurs.

Chaque surface documentée doit préciser :
- `Experience/Surface ID` stable ;
- acteurs autorisés ;
- jobs/journeys servis ;
- capacités exposées ;
- données affichées ou saisies ;
- services/BFF/API consommés ;
- contraintes offline/connectivité ;
- privacy et entitlement ;
- limites d'autorité ;
- état cible / implémentation / déploiement / activation.

**Une surface n'est jamais créée dans la documentation uniquement parce qu'un écran est imaginé.**

## 9. Architecture des contrats

Le `CONTRACT_REGISTRY` reste le catalogue canonique des relations inter-frontières. Les schémas physiques seront séparés du registre.

Un contrat doit être retrouvable :
- depuis son producer ;
- depuis chaque consumer ;
- depuis le domaine ;
- depuis une surface si elle en dépend ;
- depuis ses tests ;
- depuis ses décisions/ADR ;
- depuis ses preuves de compatibilité/replay.

La hiérarchie ne doit jamais devenir la seule relation : les IDs stables restent la clé durable.

## 10. Architecture de la preuve

Les documents normatifs et les preuves d'exécution sont séparés.

Exemple :
- politique de rebuild : normative ;
- plan de test : vérifiable ;
- résultat d'un FULL_REBUILD daté : evidence ;
- incident de rebuild : operational record.

Cela évite de transformer un ancien résultat de test en règle d'architecture.

## 11. Knowledge Graph documentaire

À long terme, la documentation doit être interprétable comme un graphe de connaissance.

Nœuds durables :
- DOC
- DOMAIN
- CAPABILITY
- REQUIREMENT
- RULE
- SERVICE
- BOUNDARY
- DATA
- CONTRACT
- EVENT
- EXPERIENCE
- COUNTRY-FRAMEWORK
- DECISION
- TEST
- EVIDENCE
- RISK
- SOURCE

Relations minimales :
- `BELONGS_TO`
- `OWNS`
- `CONSUMES`
- `PRODUCES`
- `EXPOSES`
- `IMPLEMENTS`
- `DEPENDS_ON`
- `GOVERNS`
- `VALIDATED_BY`
- `EVIDENCED_BY`
- `SUPERSEDES`
- `APPLIES_IN`
- `ACTIVATED_IN`

Le Markdown reste lisible par l'humain ; les métadonnées structurées rendent le corpus indexable par machine.

## 12. Métadonnées minimales futures

Tout document normatif nouveau ou migré devra progressivement pouvoir exprimer :

```yaml
id: YD-DOC-XXXX
title: ...
status: ...
authority: ...
scope: ...
owners: []
applies_to: []
supersedes: []
superseded_by: []
related:
  domains: []
  capabilities: []
  services: []
  boundaries: []
  contracts: []
  experiences: []
  countries: []
validation:
  tests: []
  evidence: []
review:
  triggers: []
```

Les champs sans décision ne sont pas inventés.

## 13. Retrieval IA

Une IA ne doit pas recevoir tout le corpus par défaut.

Ordre de retrieval recommandé :
1. `START_HERE` / Knowledge Map ;
2. index de l'objet demandé ;
3. README du domaine/frontière/surface ;
4. documents canoniques liés ;
5. contrats/règles pertinents ;
6. décisions applicables ;
7. tests/evidence seulement si la tâche l'exige.

Exemples :
- développement d'un microservice : frontière → domaine → contrats → sécurité → tests ;
- changement d'un contrat : Contract Registry → producer/consumers → compatibility → tests ;
- changement d'une surface : Experience → journeys/capabilities → composition → contracts ;
- incident : runbook → frontière → dépendances → contrats → evidence historique.

Une IA doit pouvoir distinguer `normative`, `descriptive`, `decision`, `test-plan`, `evidence`, `historical`.

## 14. Anti-patterns interdits

- dossier contenant des dizaines de documents hétérogènes sans index ;
- copie locale d'une règle transverse ;
- README purement décoratif ;
- fichier `MISC.md`, `NOTES.md` ou `OTHER.md` utilisé comme dépôt permanent ;
- création automatique de sous-dossiers vides ;
- duplication des contrats dans chaque consumer ;
- architecture par écran ;
- architecture par technologie ;
- country fork complet du corpus ;
- déplacement massif sans table de migration ;
- suppression d'un ancien chemin sans redirect/supersession documentaire ;
- génération IA de décisions manquantes pour « compléter » la structure.

## 15. Classification de migration

Chaque fichier existant recevra exactement une disposition principale :

- `KEEP` : emplacement et rôle corrects ;
- `MOVE` : contenu correct, emplacement à changer ;
- `GROUP` : contenu correct, sous-groupe nécessaire ;
- `SPLIT` : plusieurs autorités/natures dans un fichier ;
- `MERGE` : doublon réel à consolider ;
- `REFERENCE` : doit devenir une vue/index vers une autorité ailleurs ;
- `SUPERSEDE` : remplacé mais conservé historiquement ;
- `ARCHIVE` : preuve/historique non normatif ;
- `REVIEW` : décision humaine/ADR nécessaire.

Aucun `MERGE` ne sera décidé sur la seule similarité de titre.

## 16. Phases de restructuration

### R0 — Freeze structurel
Continuer les corrections critiques, mais suspendre l'expansion documentaire non urgente des domaines suivants tant que leur emplacement cible n'est pas fixé.

### R1 — Inventaire exhaustif
Recenser tous les fichiers, leur type, statut, autorité, IDs, liens entrants/sortants et domaine.

### R2 — Canonicality map
Déterminer pour chaque connaissance son document canonique et détecter contradictions/duplications.

### R3 — Taxonomie et indexes
Créer Knowledge Map, catalogues et relation SVC↔MS avant les déplacements.

### R4 — Experiences
Formaliser le catalogue des expériences/surfaces prévu par la vision, sans imposer un nombre arbitraire d'interfaces.

### R5 — Migration Architecture
Séparer vues système, DDD, frontières, contrats, décisions et preuves.

### R6 — Migration domaines
Normaliser les dossiers domaine sans perdre leur langage métier.

### R7 — Microservices
Appliquer la structure locale uniquement aux frontières ayant assez de contenu pour la justifier.

### R8 — Data/Knowledge/Analytics/AI + Security + Operations
Reclasser les préoccupations transverses et supprimer les ambiguïtés d'autorité.

### R9 — AI retrieval
Ajouter métadonnées, index machine-friendly, guides de contexte et contrôles de liens.

### R10 — Validation
Tester navigation humaine, retrieval IA, liens, canonicalité et absence de perte documentaire.

## 17. Gates de migration

Un fichier ne change de chemin que si :
1. son identité est connue ;
2. son autorité est connue ou marquée REVIEW ;
3. sa destination est déterminée ;
4. ses références entrantes principales sont identifiées ;
5. les index concernés sont mis à jour ;
6. aucun changement sémantique n'est caché dans le déplacement ;
7. le rollback est possible.

## 18. Critères de réussite

La restructuration est réussie lorsqu'un nouveau développeur ou une IA peut répondre rapidement à :
- qu'est-ce que YDIASE ?
- quels domaines existent ?
- quelle capacité répond à quel besoin ?
- quel service logique porte la responsabilité ?
- quelle frontière physique est autoritative ?
- qui possède cette donnée ?
- quel contrat transporte cette information ?
- quelles surfaces utilisent cette capacité ?
- quelles règles privacy/security s'appliquent ?
- quelles décisions expliquent cette architecture ?
- comment la frontière est-elle testée et restaurée ?
- quelles preuves existent réellement ?
- qu'est-ce qui est cible, implémenté, déployé et actif ?

sans interpréter la position d'un fichier comme seule preuve d'autorité.

## 19. Décision immédiate

La prochaine étape n'est pas ANL-002.

La prochaine étape est `R1 — inventaire exhaustif`, suivie de `R2 — canonicality map`.

Aucun déplacement massif n'est autorisé avant ces deux étapes.
