---
document_id: "YD-DOC-POL-CAR-002-CAREER-GAP-TRANSITION"
title: "YD-MS-CAR-002 — Career Gap & Transition Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de career gap transition pour YD-MS-CAR-002."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "policy"
---

# YD-MS-CAR-002 — Career Gap & Transition Policy

> **Rôle du document**
> Établit les règles normatives de career gap transition pour YD-MS-CAR-002.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `DECISION-BASELINE / IMPLEMENTATION-PENDING`
Portée logique : `CAR-002 Career Path + CAR-003 Career Transition`

## 1. Principe

YDIASE ne réduit pas une transition professionnelle à un score de similarité.

Une transition compare un `CurrentStateSnapshot` à un `TargetStateSnapshot`, identifie des gaps multidimensionnels, construit des options d'action, puis produit un ou plusieurs scénarios versionnés et explicables.

Une trajectoire ou transition est une aide à la décision contextualisée. Elle n'est ni une promesse d'emploi, ni une prédiction certaine, ni une vérité sur la personne.

## 2. Entrées versionnées

Tout calcul conserve au minimum les références/versions applicables :
- occupation source et cible CAR-001 ;
- exigences métier CAR-001 ;
- UserSkill SKL-002 ;
- profil/objectifs/contraintes PRF autorisés ;
- qualifications/formation EDU ;
- options d'apprentissage LRN/EDU ;
- signaux/intelligence marché LAB ;
- contexte pays CFG ;
- policy/model version du calcul ;
- timestamp et fenêtre temporelle des signaux.

Une entrée indisponible n'est jamais inventée.

## 3. CurrentStateSnapshot

Le snapshot courant représente uniquement ce qui est nécessaire à la finalité :
- compétences/niveaux/confiance/fraîcheur autorisés ;
- qualifications pertinentes ;
- expérience pertinente par références autorisées ;
- occupation/situation courante si connue ;
- objectifs et contraintes explicitement utilisables ;
- contexte géographique/réglementaire nécessaire.

Le snapshot n'est pas une copie autoritative de PRF/SKL/EDU. Il sert à reproduire/expliquer le calcul selon politique de rétention.

## 4. TargetStateSnapshot

La cible contient :
- occupation/version cible ;
- exigences obligatoires ;
- exigences préférées ;
- compétences/niveaux attendus ;
- qualifications/licences/prérequis applicables ;
- contraintes pays/secteur lorsque gouvernées ;
- signaux marché datés utilisés ;
- provenance et version.

Les exigences légales/réglementaires doivent être distinguées des préférences employeur ou tendances statistiques.

## 5. TransitionGap

Un gap est typé. Types minimaux :
- `SKILL` ;
- `QUALIFICATION` ;
- `EXPERIENCE` ;
- `REGULATORY` ;
- `LEARNING` ;
- `CONSTRAINT` ;
- `MARKET` ;
- `INFORMATION`.

Chaque gap conserve :
- `gap_id` ;
- type ;
- source requirement ref/version ;
- current evidence ref/version ;
- état ;
- sévérité/importance selon politique ;
- caractère `BLOCKING`, `REQUIRED`, `PREFERRED` ou `INFORMATIONAL` ;
- confidence ;
- provenance ;
- reason/explanation code ;
- policy version.

États minimaux :
`SATISFIED`, `PARTIAL`, `MISSING`, `UNKNOWN`, `CONFLICTED`, `NOT-APPLICABLE`.

`UNKNOWN` n'est jamais traité comme `MISSING`.

## 6. Gap de compétence

Le gap Skill compare une exigence CAR-001 à un UserSkill SKL-002 compatible en SkillRef/taxonomy/proficiency scale.

Le moteur tient compte séparément :
- du niveau ;
- de la confiance ;
- de la fraîcheur ;
- de l'état de preuve.

Un niveau insuffisant avec forte confiance est différent d'un niveau inconnu faute de preuve.

Aucune conversion entre échelles incompatibles n'est implicite.

## 7. Gaps non-Skill

Une transition ne peut pas être déclarée faisable uniquement parce que les Skills correspondent.

Les qualifications, licences/règles réglementaires, expérience requise, contraintes déclarées et informations manquantes restent des dimensions indépendantes.

Un prérequis réglementaire `BLOCKING` ne peut jamais être compensé par un bon score Skill.

## 8. Construction d'une TransitionOption

Une option est une séquence ordonnée d'actions permettant de traiter tout ou partie des gaps :
- formation/programme/module ;
- évaluation ou collecte de preuve ;
- acquisition d'expérience ;
- qualification/certification applicable ;
- étape métier intermédiaire ;
- action administrative/réglementaire gouvernée ;
- révision d'une hypothèse ou information manquante.

Chaque action conserve la source qui justifie son inclusion.

Une option qui ne ferme pas tous les gaps bloquants est marquée explicitement `PARTIAL` ou `NOT-YET-FEASIBLE`.

## 9. TransitionPlan

Le plan regroupe une ou plusieurs options comparables.

Il peut contenir, lorsque les données existent :
- ordre/dépendances ;
- durée estimée ;
- coût estimé ;
- disponibilité géographique ;
- effort ;
- risques ;
- opportunités marché ;
- prérequis.

Une valeur inconnue reste `UNKNOWN`; elle n'est pas remplacée par une moyenne inventée.

Coûts et durées sont toujours associés à leur source, date, contexte et niveau de confiance.

## 10. Faisabilité

Statuts minimaux :
- `FEASIBLE` ;
- `FEASIBLE-WITH-GAPS` ;
- `CONDITIONAL` ;
- `NOT-YET-FEASIBLE` ;
- `INSUFFICIENT-DATA`.

`NOT-YET-FEASIBLE` signifie que les conditions connues ne sont pas actuellement satisfaites ; cela ne signifie jamais impossibilité permanente.

## 11. Incertitude

L'incertitude n'est pas un score décoratif. Elle est produite par dimensions :
- qualité/fraîcheur du profil ;
- couverture des exigences métier ;
- stabilité/version du référentiel ;
- qualité des données formation ;
- fraîcheur/couverture des signaux marché ;
- hypothèses nécessaires au scénario.

Bande synthétique possible :
`LOW-UNCERTAINTY`, `MEDIUM-UNCERTAINTY`, `HIGH-UNCERTAINTY`, `NOT-ASSESSABLE`.

Une forte incertitude ne doit pas être masquée par un classement élevé.

## 12. Explicabilité

Tout résultat publié doit permettre de répondre :
1. pourquoi cette cible/étape apparaît ;
2. quelles exigences sont satisfaites ;
3. quels gaps existent ;
4. lesquels sont bloquants ;
5. quelles preuves ont été utilisées ;
6. quelles données manquent ;
7. quelles hypothèses ont été faites ;
8. quelles actions pourraient réduire les gaps ;
9. quels signaux marché ont influencé le résultat ;
10. quelle version de politique/modèle a produit le résultat.

L'explication est fondée sur les données/règles du calcul. Un LLM peut reformuler l'explication mais ne doit pas inventer une justification absente du moteur.

## 13. Classement et score global

Un score global peut exister pour comparer des options sous une `TransitionPolicyVersion`, mais :
- il n'est jamais l'autorité métier ;
- ses composantes restent accessibles ;
- un gap `BLOCKING` reste bloquant quel que soit le score ;
- les pondérations sont versionnées et validées ;
- aucune pondération continentale universelle n'est supposée ;
- les préférences utilisateur ne sont appliquées que si autorisées et explicites.

Les coefficients numériques restent `TBD-VALIDATION`.

## 14. Career Path

CAR-002 construit une trajectoire comme une séquence de `CareerPathStep` reliés à des occupations/états versionnés.

Chaque étape conserve :
- justification ;
- préconditions ;
- gaps pertinents ;
- transition option utilisée ;
- input versions ;
- incertitude.

Le moteur peut proposer plusieurs scénarios au lieu de prétendre qu'il existe un chemin unique optimal.

## 15. Correction et recalcul

Si CAR-001, SKL-002, PRF, EDU/LRN ou LAB corrige une entrée :
- le résultat historique n'est pas écrasé ;
- la source/version antérieure reste associée au résultat historique ;
- un nouveau calcul produit une nouvelle version si nécessaire ;
- la cause du recalcul est tracée ;
- les consommateurs reçoivent l'événement versionné approprié.

## 16. IA et prédiction

L'IA peut aider à :
- générer des candidats à évaluer ;
- expliquer des résultats structurés ;
- détecter des alternatives ;
- signaler des données manquantes.

Elle ne peut pas seule :
- déclarer un métier accessible/inaccessible ;
- inventer une exigence ;
- contourner un prérequis bloquant ;
- transformer une corrélation marché en certitude ;
- créer une garantie d'emploi/salaire/durée ;
- masquer l'incertitude.

## 17. Reproductibilité

Une transition persistée doit être reproductible ou, au minimum, auditée à partir de :
- input refs/versions ;
- snapshots nécessaires ;
- TransitionPolicyVersion ;
- règles/pondérations applicables ;
- contexte ;
- timestamp.

Un changement de politique produit une nouvelle version, jamais une réécriture silencieuse.

## 18. Gates fermés

Désormais `DEFINED` :
- modèle multidimensionnel de gap ;
- distinction obligatoire/préféré/bloquant ;
- distinction UNKNOWN/MISSING ;
- construction logique des TransitionOption/Plan ;
- statuts de faisabilité ;
- incertitude ;
- explicabilité ;
- traitement des corrections ;
- rôle de l'IA ;
- reproductibilité.

Restent `TBD-VALIDATION/PREPROD` :
- coefficients/pondérations ;
- seuils de classement ;
- durées/coûts et sources physiques ;
- règles pays/réglementaires physiques ;
- validation métier des modèles ;
- Privacy/rétention ;
- tests de biais/équité ;
- contrats/runtime/RPO/RTO/restore.

Statut final : `CAREER-TRANSITION-SEMANTICS-CLOSED / NUMERIC-AND-PREPROD-VALIDATION-PENDING`.
