# YD-MS-LRN-001 — K3 Contract Baseline

Statut : `K3-CONTRACT-BASELINE / IMPLEMENTATION-PENDING`
Nature : `MIXED`

## 1. Portée

LRN-001 est l'autorité sur les ressources learning propres à YDIASE et sur les résultats spécialisés de découverte learning. Il référence les programmes EDU, les compétences SKL et les offres MKT sans reprendre leur autorité.

K3 fixe les contrats logiques. Aucun protocole, datastore, broker ou format physique n'est imposé.

## 2. Objets possédés

- `LearningResource`
- `LearningOfferingRef`
- `LearningRecommendationSet`

Les `Program` académiques restent EDU. Les compétences et niveaux individuels restent SKL. Les prix, vendeurs, commandes et disponibilités commerciales restent MKT.

## 3. Contrats entrants

LRN peut consommer des références versionnées provenant notamment de EDU, SKL, MKT, REC, CFG et des décisions Privacy applicables.

Une entrée minimale conserve selon son type :
- `source_domain`
- `source_ref`
- `source_version`
- statut et validité
- fraîcheur
- provenance et qualité
- territoire/langue/modalité lorsque pertinent
- droits d'usage lorsque pertinent
- finalité/Privacy lorsque personnalisation

Un gap SKL/CAR/ORI est une entrée. LRN ne crée pas le gap.

Une donnée critique inconnue reste `UNKNOWN`. Une donnée périmée ou incompatible ne reçoit aucune valeur inventée.

## 4. Contrats sortants

### LearningResource

Expose une ressource avec ID/version, type, source/provider, outcomes déclarés, mappings versionnés, prérequis, langue, modalité, provenance, qualité, droits, fraîcheur et statut.

### LearningOfferingRef

Expose uniquement une référence datée vers une offre EDU/MKT. La projection locale ne devient jamais autoritative.

### LearningRecommendationSet

Expose les options learning spécialisées, critères organiques, prérequis, gaps ciblés, inconnues, fraîcheur, policy version et evidence snapshot applicable.

LRN peut fournir candidats/signaux à REC-001 sans devenir un second moteur générique de recommandation.

## 5. Contrat de données

### LearningResource

États minimaux : `DRAFT`, `ACTIVE`, `LIMITED`, `STALE`, `WITHDRAWN`, `RETIRED`.

### LearningOfferingRef

Conserve domaine source, objet/version, watermark de disponibilité/fraîcheur et projection minimale nécessaire.

### Mapping gap-learning

Conserve gap/skill ref/version, target outcome, resource/program ref/version, type/force/confiance du mapping, état des prérequis, provenance et inconnues.

### LearningRecommendationSet

Conserve versions minimisées des gaps/profils/skills, ressources/programmes/offres, mappings, contexte, finalité, policy et états de fraîcheur/qualité.

## 6. Invariants

- Ressource learning, programme EDU, offre MKT et compétence acquise restent distincts.
- Consulter, acheter ou terminer une ressource ne prouve jamais automatiquement une compétence.
- `UNKNOWN` n'est jamais `FAILED`.
- LRN ne contourne aucune exigence EDU ou restriction fournisseur.
- Coût, durée, bourse, place ou session ne sont actuels que si source/version/fraîcheur le permettent.
- Paiement, commission, sponsoring ou relation partenaire ne modifient jamais le rang organique learning.
- Une correction ne réécrit jamais silencieusement un ancien résultat.
- Aucun `LRN-002` physique n'est créé sans autorité et cycle autonome démontrés.

## 7. Exigences traçables

| ID | Exigence |
|---|---|
| LRN-REQ-001 | Préserver les frontières d'autorité EDU, SKL, MKT et REC. |
| LRN-REQ-002 | Versionner ressources, mappings et références externes. |
| LRN-REQ-003 | Conserver provenance, qualité, droits d'usage et fraîcheur applicables. |
| LRN-REQ-004 | Ne jamais convertir UNKNOWN en échec ou valeur inventée. |
| LRN-REQ-005 | Distinguer découverte learning et preuve d'acquisition d'une compétence. |
| LRN-REQ-006 | Conserver les prérequis selon leur classe normative. |
| LRN-REQ-007 | Isoler ranking organique et influence commerciale. |
| LRN-REQ-008 | Conserver un evidence snapshot pour tout résultat personnalisé persistant. |
| LRN-REQ-009 | Invalider ou dater les anciens résultats après correction des sources. |
| LRN-REQ-010 | Déclencher une revue de frontière avant toute autorité LMS/progression/assessment autonome. |

## 8. Versionnement

- Les IDs logiques restent stables pendant la vie de l'objet.
- Toute mutation sémantique significative crée une nouvelle version.
- Un changement incompatible du contrat crée une nouvelle version majeure.
- Les versions de ressources, mappings, policies et sources externes restent distinctes.
- Tout consommateur doit pouvoir identifier les versions qu'il utilise.

## 9. Compatibilité et dépréciation

- Une version consommée n'est pas retirée sans règle de migration.
- Une valeur ou un type inconnu n'est pas interprété silencieusement.
- Une offre devenue invérifiable est masquée comme achetable sans supprimer une ressource encore valide.
- Les anciens RecommendationSet restent historisés avec fraîcheur/statut.
- La durée physique de coexistence reste `TBD-PREPROD`.

## 10. ADR

Les décisions structurelles sont enregistrées dans `ADR-LRN-001-DISCOVERY-AUTHORITY-BOUNDARY.md`.

## 11. Limites

K3 ne ferme pas les mappings réels, droits d'usage opérationnels, fairness, IAM/IDOR, rétention physique, SLO/RPO/RTO, restore, observabilité, contrats physiques ou infrastructure.
