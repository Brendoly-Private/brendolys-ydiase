# Inventaire K3 — pilote transversal

Statut : `EVIDENCE-INVENTORY / K3-CLOSED / IMPLEMENTATION-PENDING`

## Objet

Cet inventaire reflète l'état courant du pilote K3 après création des baselines contractuelles canoniques. Il ne constitue pas une seconde autorité contractuelle : les contrats et baselines sous `04-contracts/` restent les sources canoniques.

K3 signifie ici que la connaissance nécessaire à l'implémentation est contractualisée. Il ne signifie ni schéma physique final, ni code, ni déploiement, ni preuve runtime.

## YD-MS-KNW-001

### Preuves K3
- `04-contracts/baselines/YD-MS-KNW-001/K3_CONTRACT_BASELINE.md` — entrées/sorties, data contracts, invariants, exigences KNW-REQ-001..010, versionnement et compatibilité.
- `YD-CTR-KNW-SRH-SEARCH-ENRICHMENT-v1` dans le Contract Registry — contrat logique KNW → Search.
- `KNOWLEDGE_GRAPH_PROJECTION_POLICY.md` — sémantique des projections, provenance et reconstruction.
- `ADR-KNW-001-DERIVED-KNOWLEDGE-GRAPH.md` — décisions structurelles.

### État K3
- API/événements applicables : PASS
- dataContracts : PASS
- invariants : PASS
- requirements : PASS
- ADR structurels : PASS
- versioningRules : PASS
- compatibilityRules : PASS

**Verdict : K3 PASS.**

## YD-MS-SKL-001

### Preuves K3
- `04-contracts/baselines/YD-MS-SKL-001/K3_CONTRACT_BASELINE.md` — objets autoritatifs, contrats entrants/sortants, data contracts, invariants, exigences SKL-REQ-001..010, versionnement et compatibilité.
- familles SKL du Contract Registry, notamment `YD-CTR-SKL-TAXONOMY-v1` et projections associées.
- `ADR-SKL-001-AUTHORITATIVE-SKILLS-KNOWLEDGE.md` — autorité et décisions structurelles.
- frontières métier Skills/Knowledge et profil d'autonomie associés.

### État K3
- API/événements applicables : PASS
- dataContracts : PASS
- invariants : PASS
- requirements : PASS
- ADR structurels : PASS
- versioningRules : PASS
- compatibilityRules : PASS

**Verdict : K3 PASS.**

## YD-MS-REC-001

### Preuves K3
- `04-contracts/baselines/YD-MS-REC-001/K3_CONTRACT_BASELINE.md` — contrats entrants/sortants, objets REC, invariants, exigences REC-REQ-001..010, versionnement et compatibilité.
- familles REC du Contract Registry, notamment request/result ORI↔REC et projections/analytics associées.
- `RECOMMENDATION_RANKING_POLICY.md` et politiques associées — règles normatives de recommandation.
- `ADR-REC-001-ORGANIC-RANKING-SEPARATION.md` — séparation structurelle du ranking organique.

### État K3
- API/événements applicables : PASS
- dataContracts : PASS
- invariants : PASS
- requirements : PASS
- ADR structurels : PASS
- versioningRules : PASS
- compatibilityRules : PASS

**Verdict : K3 PASS.**

## YD-MS-LRN-001

### Preuves K3
- `04-contracts/baselines/YD-MS-LRN-001/K3_CONTRACT_BASELINE.md` — objets, entrées/sorties, data contracts, invariants, exigences LRN-REQ-001..010, versionnement et compatibilité.
- familles LRN du Contract Registry, notamment `YD-CTR-LRN-RESOURCE-v1`, Search/Analytics associés.
- `LEARNING_DISCOVERY_POLICY.md` — politique normative de découverte learning.
- `ADR-LRN-001-DISCOVERY-AUTHORITY-BOUNDARY.md` — frontière d'autorité et décisions structurelles.

### État K3
- API/événements applicables : PASS
- dataContracts : PASS
- invariants : PASS
- requirements : PASS
- ADR structurels : PASS
- versioningRules : PASS
- compatibilityRules : PASS

**Verdict : K3 PASS.**

## Limites communes

La fermeture K3 ne transforme aucun de ces contrats en `PHYSICAL-READY`. Restent notamment hors K3, selon le composant : schémas physiques finaux, protocoles, broker/datastore, IAM physique, valeurs SLO/RTO/RPO, rétention physique, contract tests exécutés, tests de reconstruction/restore et preuves runtime.

Ces éléments sont traités par K4/K5, les gates PREPROD et l'implémentation lorsqu'ils deviennent applicables.

## Conclusion

Le pilote transversal K3 est **fermé pour YD-MS-KNW-001, YD-MS-SKL-001, YD-MS-REC-001 et YD-MS-LRN-001** au niveau de connaissance contractuelle.

Le prochain travail n'est plus de recréer les contrats K3 de ces quatre composants. Il consiste à :
- maintenir leurs baselines K3 et le Contract Registry synchronisés ;
- fermer/maintenir K4 pour les composants concernés ;
- produire les validations et preuves K5 sans confondre maturité documentaire et état de déploiement.

Toute régression d'une preuve ou contradiction avec une source canonique doit faire recalculer le verdict au lieu de conserver artificiellement K3.
