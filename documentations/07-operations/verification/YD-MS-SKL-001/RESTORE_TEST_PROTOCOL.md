# YD-MS-SKL-001 — Authoritative Restore Test Protocol

Statut : `TEST-PROTOCOL-DEFINED / NOT-EXECUTED`

## Objectif

Vérifier que le store autoritatif SKL peut être restauré sans reconstruire sa vérité depuis EDU, CAR, DAT, caches ou projections consommateurs.

## Préconditions

Identifier commit/version, schéma, backup, taxonomie/version, métadonnées de gouvernance, environnement, configuration, watermarks sortants et reviewer.

## Procédure

1. capturer l'état canonique de référence ;
2. créer ou sélectionner un backup versionné gouverné ;
3. simuler la perte contrôlée du store cible de test ;
4. restaurer le store et ses métadonnées de gouvernance ;
5. vérifier IDs, versions, statuts, provenance, relations et mappings ;
6. vérifier que l'historique gouverné requis est cohérent ;
7. comparer à l'état attendu ;
8. réconcilier les projections/publications sortantes ;
9. vérifier qu'aucun consommateur n'a été utilisé comme source d'autorité ;
10. enregistrer durée, erreurs, écarts et verdict.

## Scénarios obligatoires

- Skill et KnowledgeConcept versionnés ;
- SkillRelation avec provenance ;
- SkillTaxonomyMapping versionné ;
- relation retirée/invalide ;
- proposition externe non publiée ;
- tentative de publication autonome IA refusée ;
- conflit de version ;
- reprise avec dernière taxonomie valide lorsque la nouvelle version est invalide.

## PASS

PASS exige intégrité de l'autorité restaurée, provenance/versionnement cohérents, absence de reconstruction depuis un consommateur et réconciliation sortante contrôlée.

RPO/RTO ne peuvent être déclarés conformes que si les seuils PREPROD correspondants ont été fixés avant le test.

Le protocole seul ne constitue pas une preuve K5.
