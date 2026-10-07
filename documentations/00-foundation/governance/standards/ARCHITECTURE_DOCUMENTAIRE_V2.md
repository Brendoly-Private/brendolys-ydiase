# Architecture documentaire V2 — BRENDOLYS YDIASE

**Statut :** APPROUVÉ — BASELINE DE MIGRATION  
**Principe directeur :** une information canonique = une source ; ailleurs = référence ; les vues calculables sont générées.

## 1. Décision

La documentation YDIASE doit évoluer vers une source documentaire unique. Le dossier `_knowledge/` ne constitue pas une seconde documentation pérenne : ses mécanismes utiles seront intégrés à la documentation canonique ou déplacés vers `_meta/`, puis `_knowledge/` sera supprimé après migration et validation.

La migration ne doit supprimer aucune connaissance utile ni confondre connaissance métier, architecture logique, implémentation et déploiement.

## 2. Structure cible

```text
documentations/
├── README.md
├── 00-foundation/
│   ├── vision/
│   ├── principles/
│   ├── vocabulary/
│   └── governance/
├── 01-product/
│   ├── product-model/
│   ├── journeys/
│   ├── capabilities/
│   ├── economics/
│   └── roadmap/
├── 02-domains/
│   ├── identity-profile/
│   ├── education/
│   ├── skills-knowledge/
│   ├── careers/
│   ├── labor-market/
│   ├── opportunities-recruitment/
│   ├── orientation-recommendation/
│   ├── content-community-learning/
│   ├── partners-ecosystem/
│   └── data-intelligence-ai/
├── 03-systems/
│   ├── services/
│   ├── microservices/
│   ├── data/
│   ├── interfaces/
│   └── infrastructure/
├── 04-contracts/
│   ├── api/
│   ├── events/
│   ├── data/
│   └── integrations/
├── 05-decisions/
│   ├── architecture/
│   ├── product/
│   ├── data/
│   ├── security/
│   └── operations/
├── 06-trust/
│   ├── security/
│   ├── privacy/
│   ├── compliance/
│   ├── data-governance/
│   └── ai-governance/
├── 07-operations/
│   ├── observability/
│   ├── reliability/
│   ├── backup-recovery/
│   ├── incident-management/
│   └── runbooks/
├── 08-countries/
└── _meta/
    ├── schemas/
    ├── ontology/
    ├── maturity/
    ├── indexes/
    └── validation/
```

## 3. Sémantique des espaces

- **00-foundation** : identité durable, vision, principes, vocabulaire et gouvernance documentaire.
- **01-product** : modèle produit, capacités, parcours, économie et évolution produit.
- **02-domains** : connaissance métier indépendante de l'architecture technique courante.
- **03-systems** : composants logiques et techniques qui réalisent le produit.
- **04-contracts** : contrats de communication et d'intégration, objets de première classe.
- **05-decisions** : décisions durables et ADR, référencées par ID.
- **06-trust** : sécurité, vie privée, conformité, gouvernance data et IA.
- **07-operations** : exploitation, fiabilité, observabilité, reprise et procédures.
- **08-countries** : cadres pays et variantes territoriales.
- **_meta** : métamodèle et mécanique documentaire ; ce n'est pas une seconde documentation métier ou technique.

## 4. Règles de durabilité

1. Une information normative possède un emplacement canonique unique.
2. Une autre page référence son ID ou son URI documentaire ; elle ne la recopie pas.
3. Les domaines métier ne dépendent pas de la topologie microservices actuelle.
4. Un microservice possède un dossier canonique unique sous `03-systems/microservices/`.
5. Les contrats sont indépendants des fiches microservices et sont référencés par ID.
6. Les décisions sont indépendantes des composants qu'elles affectent.
7. Catalogues, registres calculables, matrices d'impact, graphes et index doivent être générés lorsque les sources permettent de les calculer.
8. Les niveaux K0–K6 et E0–E4 mesurent la connaissance et la preuve ; ils ne créent pas une documentation parallèle.
9. Architecture, implémentation et déploiement restent des dimensions distinctes.
10. Aucun composant futur ou non activé n'est présenté comme déployé.
11. Aucune donnée ou décision n'est inventée pour satisfaire un schéma.
12. Les suppressions physiques n'interviennent qu'après preuve de migration, contrôle des références et validation du Knowledge Gate.

## 5. Modèle Source / Reference / View / Evidence

- **SOURCE** : emplacement canonique d'une information.
- **REFERENCE** : lien stable vers une source par identifiant.
- **VIEW** : représentation dérivée et régénérable (catalogue, registre, matrice, graphe).
- **EVIDENCE** : preuve traçable soutenant une affirmation ou un niveau de maturité.

Une VIEW ne doit jamais devenir une deuxième source de vérité.

## 6. Sort de _knowledge

Le contenu actuel de `documentations/_knowledge/` est classé avant migration :

- `SOURCE` : connaissance normative à fusionner dans son emplacement canonique ;
- `MOVE` : contenu unique à déplacer sans duplication ;
- `MERGE` : contenu à fusionner avec une source existante ;
- `GENERATED` : vue qui devra être produite automatiquement ;
- `HISTORICAL` : artefact conservé uniquement pour traçabilité historique ;
- `DELETE-CANDIDATE` : contenu redondant supprimable après validation.

Cibles privilégiées :
- schemas → `_meta/schemas/`
- ontology → `_meta/ontology/`
- maturité et gates → `_meta/maturity/`
- validation → `_meta/validation/`
- catalogues/relations/impact → générés dès que possible à partir des sources canoniques.

## 7. Migration

La migration se fait sans big-bang :

1. inventaire exhaustif ;
2. classification de chaque fichier ;
3. carte ancien chemin → chemin canonique ;
4. définition des métadonnées minimales communes ;
5. migration par famille ;
6. adaptation du validateur et du CI ;
7. génération des vues ;
8. contrôle des références et contradictions ;
9. validation de parité documentaire ;
10. suppression de `_knowledge/` et des duplications seulement après réussite des contrôles.

## 8. Interdiction de progression prématurée

Tant que cette migration n'est pas stabilisée, les promotions K4/K5/K6 ne doivent pas créer de nouvelles duplications dans l'ancienne architecture.

Cette baseline remplace l'idée de maintenir durablement une documentation classique et un Knowledge Catalog documentaire parallèle.


## 9. Métadonnées officielles obligatoires

Le standard `YD-STD-DOC-META-001` dans `OFFICIAL_DOCUMENT_METADATA_STANDARD.md` gouverne désormais l'identification et la personnalisation des documents.

Tout nouveau document canonique doit :
- posséder un `document_id` stable ;
- expliquer sa fonction avec `document_role` ;
- référencer `BRENDOLYS YDIASE` et l'identité institutionnelle canonique ;
- déclarer son niveau d'autorité et son usage pour le développement ;
- relier les domaines, capacités, services, microservices, contrats ou décisions concernés lorsque applicable ;
- séparer statut documentaire, implémentation, déploiement et activation ;
- inclure un bloc humain « Rôle du document » lorsqu'il est substantiel.

Les fichiers historiques sont migrés progressivement. Leur absence de métadonnées signifie `LEGACY-METADATA-PENDING`, sans annuler leur contenu existant.

La readiness de développement doit prendre en compte les documents `mandatory-reference` applicables. Une contradiction non résolue entre références obligatoires bloque la readiness du périmètre concerné.
