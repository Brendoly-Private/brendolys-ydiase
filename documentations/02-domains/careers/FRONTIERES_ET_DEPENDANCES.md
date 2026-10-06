# Frontières et dépendances — Métiers et carrières

Statut : `DOMAIN-REVIEW-CANDIDATE`

## CAR-001 — Occupation & Career Graph

Possède :
- Occupation ;
- OccupationVersion ;
- OccupationSkillRequirement ;
- OccupationRelation ;
- CareerTransitionEdge.

Consomme SKL-001, EDU-004, CFG, DAT-005/DAT-003 et signaux LAB selon contrats.

CAR-001 possède l'assertion « ce métier requiert/référence telle compétence » mais SKL-001 reste owner de la Skill canonique.

## CAR-002 — Career Path

Responsabilité logique :
- CareerPath ;
- CareerPathStep ;
- PathScenario ;
- PathComparisonState.

Consomme CAR-001, PRF/SKL-002, EDU-002 et LAB-002. Les entrées sont référencées/versionnées ; elles ne sont pas recopiées comme nouvelle vérité.

## CAR-003 — Career Transition

Responsabilité logique actuellement hébergée dans YD-MS-CAR-002 :
- TransitionCase ;
- TransitionGap ;
- TransitionPlan ;
- TransitionOption.

Consomme métiers source/cible CAR-001, UserSkill SKL-002, options d'apprentissage LRN/EDU et intelligence marché LAB.

CAR-003 reste un module/contrat logique distinct pour permettre son extraction future sans casser la sémantique.

## CAR-004 — Career Simulation

Service logique :
- CareerSimulation ;
- SimulationScenario ;
- SimulationAssumption ;
- SimulationResult.

Une simulation possède son résultat et ses hypothèses, jamais les faits source. Elle doit conserver les versions des entrées et signaler explicitement l'incertitude.

Aucune décision n'est prise ici de créer `YD-MS-CAR-004`.

## Dépendances structurantes

| Producteur | Consommateur | Objet | Règle |
|---|---|---|---|
| SKL-001 | CAR-001 | SkillRef/taxonomy version | CAR ne crée pas de Skill |
| EDU-004 | CAR-001 | QualificationRef | EDU reste autorité |
| LAB | CAR-001 | signaux marché | evidence, jamais mutation automatique |
| CAR-001 | CAR-002/003/004 | métiers/exigences/edges | inputs versionnés |
| SKL-002 | CAR-002/003/004 | projection UserSkill minimisée | pas d'écriture retour directe |
| PRF | CAR-002/004 | objectifs/contraintes autorisés | finalité/minimisation |
| EDU/LRN | CAR-002/003/004 | options éducatives | références versionnées |
| LAB-002 | CAR-002/003/004 | intelligence/forecast | signal daté, jamais certitude |

## Invariants

- faits observés, assertions de référence, inférences et simulations restent distingués ;
- toute trajectoire/transition persistée conserve ses input versions ;
- absence de donnée n'est pas interprétée comme impossibilité de carrière ;
- une transition suggérée n'est jamais une garantie d'emploi ;
- les résultats personnalisés ne modifient pas CAR-001 ;
- pas de transaction distribuée entre CAR et SKL/EDU/LAB/PRF ;
- projections aval ne deviennent pas autorité.

## Gate d'extraction CAR-003

CAR-003 doit faire l'objet d'un ADR d'extraction si au moins un axe devient durablement distinct :
- dataset/stockage ;
- modèle de calcul ;
- SLO/criticité ;
- cadence/charge ;
- équipe/ownership ;
- rétention/Privacy ;
- cycle de déploiement.

Jusque-là, fusion physique CAR-002 + CAR-003 maintenue.

## Récupération

CAR-001 restaure son autorité depuis sa propre chaîne.

YD-MS-CAR-002 restaure ses trajectoires/transitions persistées depuis sa propre chaîne. PRF, SKL, EDU, LAB et CAR-001 ne sont pas ses backups. Après restore, certaines références peuvent nécessiter réconciliation.

Statut : `BOUNDARIES-STABLE-CANDIDATE`.
