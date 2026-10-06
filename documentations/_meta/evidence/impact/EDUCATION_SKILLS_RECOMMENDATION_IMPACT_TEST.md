# Test d'impact transverse — Curriculum → Skills → Recommendation → Knowledge → Learning

Statut : `K2-CROSS-DOMAIN-PROOF / DRAFT`

## Changement testé

`CurriculumVersion V3` était publiée. EDU-003 la remplace par V4 et invalide V3.

## Propagation attendue

1. EDU-003 conserve l'autorité sur Curriculum et publie `YD-EVT-EDU-006`.
2. EDU-002 cesse de considérer V3 comme curriculum publié actif après convergence.
3. SKL-001 réévalue les preuves de compétence issues de V3. Il ne modifie jamais Curriculum.
4. KNW-001 réévalue les relations sémantiques dérivées de V3. Il reste DERIVED.
5. REC-001 ne doit plus utiliser V3 pour un nouveau calcul exigeant un curriculum actif. Les recommandations historiques conservent leur `RecommendationEvidenceSnapshot` et la version V3 utilisée au moment du calcul.
6. LRN-001 réévalue les rattachements ou recommandations learning dérivés de V3 sans modifier Education ou Skills.

## Analyse d'autorité

| Élément | Autorité |
|---|---|
| Curriculum | YD-MS-EDU-003 |
| Skill / KnowledgeConcept | YD-MS-SKL-001 |
| Graphe sémantique | YD-MS-KNW-001, DERIVED |
| État de recommandation conservé | YD-MS-REC-001 |
| Ressource learning propre YDIASE | YD-MS-LRN-001 pour sa partie AUTH |

## Propriétés vérifiées

- pas de réécriture cross-domain de la source Curriculum
- propagation versionnée
- conservation de provenance
- conservation des résultats historiques
- séparation AUTH / MIXED / DERIVED
- possibilité d'identifier les consommateurs depuis un changement Curriculum

## Résultat

`PASS-K2-CROSS-DOMAIN`

Le graphe peut désormais suivre un changement Education vers Skills, Knowledge, Recommendation et Learning avec des frontières d'autorité explicites.

## Gate suivant

Avant généralisation aux autres frontières physiques :

1. ajouter une validation automatique de tous les identifiants du catalogue
2. détecter références orphelines et types de relations non autorisés
3. générer automatiquement une première vue d'impact depuis les YAML
4. comparer la vue générée avec DEPENDENCY_MAP, EVENT_MAP et DATA_OWNERSHIP_MATRIX
5. généraliser seulement après absence d'écart non expliqué