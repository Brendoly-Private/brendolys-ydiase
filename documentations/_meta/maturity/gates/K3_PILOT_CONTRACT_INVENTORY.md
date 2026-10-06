# Inventaire K3 — pilote transversal

Statut : `EVIDENCE-INVENTORY / GAPS-EXPLICIT`

## YD-MS-SKL-001

### Preuves existantes
- `13-architecture/services/YD-SVC-SKL-001/SERVICE_DEFINITION.md` — agrégats, autorité, données consommées et incohérences.
- `13-architecture/microservices/YD-MS-SKL-001/PHASE_CLOSURE.md` — invariants, dépendances, provenance/version et gates différés.
- `13-architecture/EVENT_MAP.md` — événements Education consommables.
- `04-competences-connaissances/FRONTIERES_ET_DEPENDANCES.md` — frontières métier.

### État K3
- invariants : PASS
- API/événements : PARTIAL → UNKNOWN pour le gate, car les contrats physiques/versionnés propres à SKL restent à fermer.
- dataContracts : UNKNOWN
- requirements : UNKNOWN
- ADR structurels : UNKNOWN
- versioningRules : UNKNOWN
- compatibilityRules : UNKNOWN

## YD-MS-REC-001

### Preuves existantes
- `13-architecture/microservices/YD-MS-REC-001/RECOMMENDATION_RANKING_POLICY.md` — pipeline normatif et règles de ranking.
- `FAIRNESS_EVALUATION_POLICY.md` — métriques et exigences d'équité.
- `PHASE_CLOSURE.md` — ownership, invariants C1, séparation sponsoring/organique et préconditions ACTIVE.
- `13-architecture/EVENT_MAP.md` et `DEPENDENCY_MAP.md` — relations et événements transversaux.

### État K3
- invariants : PASS
- requirements : PARTIAL → UNKNOWN pour le gate tant qu'elles ne sont pas reliées à des IDs d'exigences stables.
- API/événements : UNKNOWN
- dataContracts : UNKNOWN
- ADR structurels : UNKNOWN
- versioningRules : PARTIAL → UNKNOWN
- compatibilityRules : UNKNOWN

## YD-MS-KNW-001

### Preuves existantes
- `KNOWLEDGE_GRAPH_PROJECTION_POLICY.md` — sémantique des projections, provenance et reconstruction.
- `KNW_TO_SEARCH_PROJECTION_CONTRACT.md` — contrat logique candidat `YD-CTR-KNW-SRH-SEARCH-ENRICHMENT-v1`, payload, usages, interdictions, fraîcheur et rebuild.
- `PHASE_CLOSURE.md` — invariants et gates de reconstruction.
- `DERIVED_RECOVERY_REGISTER.md` — état de reconstruction.

### État K3
- invariants : PASS
- API/événements : PARTIAL → le contrat KNW→SRH est réel au niveau logique mais reste candidat et son contrat physique est explicitement en attente.
- dataContracts : PARTIAL → UNKNOWN pour le gate, car le contrat de projection ne couvre pas encore toutes les entrées/sorties KNW.
- requirements : PARTIAL → UNKNOWN
- ADR structurels : UNKNOWN
- versioningRules : PARTIAL → UNKNOWN
- compatibilityRules : UNKNOWN

## YD-MS-LRN-001

### Preuves existantes
- `LEARNING_DISCOVERY_POLICY.md` — politique normative.
- `PHASE_CLOSURE.md` — frontières, invariants, boucle métier et préconditions ACTIVE.
- `13-architecture/EVENT_MAP.md` — interactions événementielles existantes.
- `YD-MS-SRH-001/SOURCE_PROJECTION_BASELINE.md` — famille de projection `LRN-SEARCHABLE` côté Search.

### État K3
- invariants : PASS
- API/événements : PARTIAL → UNKNOWN pour le gate.
- dataContracts : UNKNOWN
- requirements : PARTIAL → UNKNOWN
- ADR structurels : UNKNOWN
- versioningRules : UNKNOWN
- compatibilityRules : UNKNOWN

## Conclusion

Aucun des quatre microservices ne doit être promu artificiellement à K3 aujourd'hui. Le dépôt possède déjà une part importante de la sémantique contractuelle, mais il manque encore des contrats complets, des exigences à identifiants stables, des règles de version/compatibilité et des ADR reliés.

Le prochain lot doit créer ces artefacts en priorité pour `YD-MS-KNW-001`, qui possède déjà le contrat logique le plus avancé, puis appliquer le même patron à SKL, REC et LRN.
