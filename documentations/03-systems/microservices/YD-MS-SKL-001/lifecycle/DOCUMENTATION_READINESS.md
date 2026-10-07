# YD-MS-SKL-001 — Documentation Readiness

Statut : `DOCUMENTATION-READY / K5-EXECUTION-BLOCKED-BY-IMPLEMENTATION`

## État

SKL-001 est suffisamment défini pour commencer son implémentation sans réinventer son autorité métier.

K3 : PASS.  
K4 : PASS.  
K5 : NOT-YET-PASS.  
K6 : NOT-APPLICABLE-YET.

## Invariants à ne pas réinventer

- SKL est `AUTH` sur Skill, KnowledgeConcept, SkillRelation et SkillTaxonomyMapping ;
- UserSkill, profils individuels et curricula EDU restent hors ownership SKL ;
- EDU/CAR/DAT fournissent des evidence, jamais une mutation canonique directe ;
- une IA peut proposer, jamais publier seule ;
- toute mutation canonique est versionnée et traçable ;
- provenance obligatoire pour mappings/relations concernés ;
- le store autoritatif est indépendant des caches/projections ;
- aucune projection consommateur ne peut reconstruire l'autorité SKL ;
- la dernière taxonomie valide peut soutenir un mode dégradé gouverné.

## Choix laissés à l'implémentation

Datastore, protocole/broker, schéma physique, langage/framework, IAM physique, mécanisme de workflow, stratégie de backup, observabilité technique et valeurs RPO/RTO/SLO restent ouverts jusqu'aux décisions correspondantes.

## K5

La matrice de preuves et le protocole de restore définissent les vérifications à exécuter lorsque l'implémentation testable existe.

Verdict : `DOCUMENTATION-READY / K4-PASS / K5-NOT-YET-PASS`.

Aucun document supplémentaire ne doit simuler une preuve d'exécution absente.
