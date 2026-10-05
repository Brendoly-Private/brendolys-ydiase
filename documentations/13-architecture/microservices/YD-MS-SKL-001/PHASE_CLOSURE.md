# YD-MS-SKL-001 — Skills Knowledge — Fermeture de phase documentaire

Statut : `DOCUMENTATION-BASELINE-CLOSED / IMPLEMENTATION-PENDING`
Nature : `AUTH`
Criticité : `C2`

## Autorité
SKL-001 possède Skill, KnowledgeConcept, SkillRelation, SkillTaxonomyMapping et leurs versions gouvernées.

## Invariants
- aucun UserSkill ou profil individuel ;
- evidence EDU/CAR n'entraîne jamais une mutation canonique automatique ;
- provenance et version obligatoires ;
- IA peut proposer mais jamais publier seule ;
- IDs durables et compatibilité/versionnement nécessaires ;
- datastore et recovery propres.

## Dépendances
DAT-005, DAT-003, EDU-003 et CAR-001 selon contrats. Les boucles sémantiques sont asynchrones/evidence-driven, sans transaction distribuée.

## Récupération
Backup/restore indépendant C2. EDU, CAR et DAT ne sont pas des sources de reconstruction de l'autorité SKL-001.

## Gates différés
Gouvernance taxonomique, workflow validation, RPO/RTO/SLO, rétention/versioning, IAM physique, restore test et contrats physiques restent à fermer avant production.

Statut final : `CLOSED-FOR-NOW — RETURN AT IMPLEMENTATION/PREPROD`.
