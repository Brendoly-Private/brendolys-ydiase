# YD-MS-REC-001 — K3 Contract Baseline

Statut : `K3-CONTRACT-BASELINE / IMPLEMENTATION-PENDING`
Nature : `MIXED`

## 1. Portée

REC-001 possède les résultats de recommandation et leurs preuves de calcul. Il ne possède aucune donnée source utilisée pour calculer ces résultats. K3 fixe les contrats logiques sans choisir protocole, format physique, modèle IA ou infrastructure.

## 2. Objets possédés

- `RecommendationRun`
- `RecommendationSet`
- `RecommendationItem`
- `RecommendationExplanation`
- `RecommendationEvidenceSnapshot`

Les données EDU, SKL, CAR, LAB, OPP, LRN, KNW, PRF et Privacy restent sous l'autorité de leurs propriétaires respectifs.

## 3. Contrats entrants

Un run peut consommer uniquement des données autorisées et versionnées nécessaires à sa finalité. Une entrée minimale conserve selon le type :
- `source_ref` et `source_version` ;
- `purpose_ref` lorsque personnalisation ;
- contexte pays/territoire ;
- état de publication/validité ;
- fraîcheur et qualité ;
- contraintes HARD/REQUIRED/SOFT/INFORMATIONAL applicables ;
- provenance ou evidence refs ;
- décision Privacy applicable.

Une donnée critique `UNKNOWN` n'est jamais transformée en `FAILED`. Une donnée critique périmée, conflictuelle ou non autorisée déclenche abstention, dégradation explicite ou exclusion selon policy.

## 4. Contrats sortants

Chaque `RecommendationRun` expose au minimum :
- `run_id` ;
- `recommendation_type` ;
- `policy_version` ;
- `model_version` si applicable ;
- `candidate_generation_version` ;
- `evidence_snapshot_ref` ;
- contexte ;
- timestamps ;
- fraîcheur/qualité ;
- état d'abstention.

Chaque item expose selon applicabilité : éligibilité, `organic_score`, `organic_rank`, composantes, contraintes, incertitude et explication structurée.

Un consommateur ne doit jamais interpréter une recommandation comme vérité sur une source métier.

## 5. Contrat de données

### RecommendationRun

Un calcul immuable dans son contexte de versions. Une correction de source crée un nouveau run ou invalide le précédent, sans réécriture silencieuse.

### RecommendationEvidenceSnapshot

Référence les versions nécessaires à la reproductibilité en minimisant les copies de données personnelles ou preuves brutes.

### RecommendationItem

Conserve candidat, état d'éligibilité, score/rang organique applicables, incertitude et références d'explication.

### RecommendationExplanation

Explication structurée issue des critères réellement utilisés. Un LLM peut reformuler, jamais inventer une justification.

## 6. Invariants

- Un échec HARD n'est jamais compensé par un score élevé.
- `UNKNOWN` n'est jamais `FAILED`.
- REC ne fabrique pas de ranking pour éviter une réponse vide.
- Le score organique n'utilise aucun paiement, enchère, commission ou statut partenaire.
- SPN-001 ne modifie jamais score, rang, pondération, exclusion ou explication organique.
- Un ancien run conserve date, versions et état de fraîcheur.
- Les projections consommées ne deviennent jamais autorités.
- Une décision Privacy requise non vérifiable entraîne fail-closed ou mode explicitement autorisé.

## 7. Exigences traçables

| ID | Exigence |
|---|---|
| REC-REQ-001 | Séparer eligibility, scoring organique, ranking organique et présentation. |
| REC-REQ-002 | Versionner policy, modèle et génération de candidats applicables. |
| REC-REQ-003 | Conserver un evidence snapshot permettant audit et reproductibilité. |
| REC-REQ-004 | Gérer abstention et données critiques inconnues sans fabriquer de résultat. |
| REC-REQ-005 | Produire une explication structurée fondée sur les données réellement utilisées. |
| REC-REQ-006 | Maintenir l'incertitude distincte du score. |
| REC-REQ-007 | Interdire toute influence commerciale sur le ranking organique. |
| REC-REQ-008 | Préserver l'historique lors d'une correction de source. |
| REC-REQ-009 | Respecter finalité, minimisation et décisions Privacy. |
| REC-REQ-010 | Permettre évaluation et rollback d'une policy personnalisée avant activation. |

## 8. Versionnement

- Tout run conserve `policy_version` et les versions de calcul applicables.
- Un changement de policy ou modèle produit un nouveau run.
- Un changement incompatible du contrat crée une nouvelle version majeure.
- Les ajouts compatibles restent explicitement versionnés.
- Les versions de données sources restent distinctes de la version REC.

## 9. Compatibilité et dépréciation

- Un consommateur doit pouvoir identifier la version du contrat et de la policy.
- Une valeur ou un type inconnu ne reçoit pas une sémantique inventée.
- Une policy retirée reste identifiable dans les runs historiques.
- Les migrations ne réécrivent pas silencieusement l'historique.
- La durée de coexistence physique des versions reste `TBD-PREPROD`.

## 10. ADR

Les décisions structurelles sont enregistrées dans `ADR-REC-001-ORGANIC-RANKING-SEPARATION.md`.

## 11. Limites

K3 ne ferme pas coefficients numériques, seuils d'équité, datasets représentatifs, tests de dérive, règles mineurs, IAM/IDOR, rétention physique, BIA/RPO/RTO/SLO, runtime, observabilité ou protocole physique.
