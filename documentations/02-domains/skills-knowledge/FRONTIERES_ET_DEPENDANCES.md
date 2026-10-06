# Frontières et dépendances — Compétences et connaissances

Statut : `DOMAIN-REVIEW-CANDIDATE`

## SKL-001 — Skills Knowledge

Possède :
- Skill ;
- KnowledgeConcept ;
- SkillRelation ;
- SkillTaxonomyMapping ;
- versions taxonomiques et relations sémantiques gouvernées.

Consomme DAT-005, provenance DAT-003 et evidence structurée provenant notamment de EDU-003 et CAR-001.

Ne possède jamais UserSkill, SkillEvidence individuel ou résultat Assessment.

## SKL-002 — User Skills Profile

Possède :
- UserSkill ;
- SkillEvidence ;
- SkillAssessmentState ;
- SkillHistory ;
- versions de l'état individuel.

Consomme :
- IdentityRef ;
- ProfileRef ;
- SkillRef/taxonomy version de SKL-001 ;
- AssessmentResultRef de ASM-001 ;
- Education/Experience evidence refs de PRF-002 ;
- décisions CNS-001.

SKL-002 peut produire un état individuel à partir de preuves autorisées, mais ne devient pas owner des preuves sources.

## Contrats structurants

| Producteur | Consommateur | Objet | Règle |
|---|---|---|---|
| SKL-001 | SKL-002 | SkillRef + taxonomy version | SKL-002 ne crée pas de Skill canonique |
| EDU-003 | SKL-001 | CurriculumSkillEvidence | evidence, pas commande d'ownership |
| CAR-001 | SKL-001 | OccupationSkillEvidence | evidence, pas commande d'ownership |
| PRF-002 | SKL-002 | Education/Experience evidence refs | PRF-002 reste autorité historique |
| ASM-001 | SKL-002 | AssessmentResultRef/dimensions autorisées | ASM reste autorité résultat |
| CNS-001 | SKL-002 | PurposeGrant/restrictions | fail-closed pour traitement non autorisable |
| SKL-002 | ORI/REC/OPP/CAR | UserSkillProjection minimisée | consommateurs ne réécrivent pas UserSkill |

## Boucles sémantiques

EDU/CAR peuvent fournir des assertions de couverture/demande à SKL-001. SKL-001 peut ensuite être consommé par EDU/CAR. Cette boucle est maîtrisée si :
- les assertions sources sont attribuées ;
- les changements taxonomiques suivent un workflow propre à SKL-001 ;
- aucune evidence entrante ne modifie automatiquement la taxonomie ;
- les versions sont explicites ;
- aucune commande circulaire transactionnelle n'est introduite.

## Récupération

SKL-001 et SKL-002 ont des chaînes de backup/restore séparées.

SKL-002 ne peut pas reconstruire son autorité depuis PRF-002, ASM-001 ou SKL-001 : ces services fournissent des références/preuves sources, pas une copie de secours de UserSkill/SkillHistory.

Après restore, certaines preuves externes peuvent être temporairement non résolues jusqu'à réconciliation.

## Interdictions

- datastore partagé SKL-001/SKL-002 ;
- accès DB croisé ;
- taxonomie contenant les profils individuels ;
- SKL-002 réécrivant un AssessmentResult ;
- SKL-002 réécrivant EducationRecord/ExperienceRecord ;
- EDU/CAR publiant directement un Skill canonique ;
- IA publiant seule Skill/SkillRelation ou UserSkill autoritatif ;
- moteur Recommendation/Orientation modifiant UserSkill directement ;
- exposition d'un profil de compétences complet lorsqu'une projection minimisée suffit.

Statut : `BOUNDARIES-STABLE-CANDIDATE`.
