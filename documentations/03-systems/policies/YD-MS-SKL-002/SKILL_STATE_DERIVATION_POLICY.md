---
document_id: "YD-DOC-POL-SKL-002-SKILL-STATE-DERIVATION"
title: "YD-MS-SKL-002 — Skill State Derivation Policy"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de skill state derivation pour YD-MS-SKL-002."
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
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-SKL-002 — Skill State Derivation Policy

> **Rôle du document**
> Établit les règles normatives de skill state derivation pour YD-MS-SKL-002.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `DECISION-BASELINE / IMPLEMENTATION-PENDING`
Nature : politique normative de dérivation de l'état individuel de compétence

## 1. Principe

SKL-002 ne stocke pas un simple couple `skill + score`.

Pour chaque sujet et SkillRef, il maintient un `UserSkillState` versionné, explicable et dérivé de `SkillEvidence` immuables/versionnées.

Une preuve ne fixe jamais directement le niveau courant. Elle produit une assertion normalisée ; le moteur de dérivation versionné décide de l'état courant selon les règles applicables.

## 2. Séparation des dimensions

Un état de compétence contient au minimum :

- `skill_ref` ;
- `taxonomy_version` ;
- `proficiency_level_ref` ;
- `proficiency_scale_version` ;
- `confidence_band` ;
- `freshness_state` ;
- `evidence_state` ;
- `derivation_method_version` ;
- `effective_at` ;
- `computed_at` ;
- `state_version`.

Le niveau, la confiance et la fraîcheur sont trois dimensions distinctes. Un niveau élevé avec preuve ancienne n'est pas équivalent à un niveau faible très récent.

## 3. Niveau / proficiency

SKL-002 utilise une échelle canonique versionnée par référence, jamais un nombre sans sémantique.

La baseline logique prévoit les rangs ordonnés :
`L0-UNDETERMINED`, `L1-AWARE`, `L2-BASIC`, `L3-OPERATIONAL`, `L4-ADVANCED`, `L5-EXPERT`.

Ces labels sont une échelle YDIASE interne et ne prétendent pas remplacer un cadre officiel. Les mappings vers des cadres externes sont versionnés et gouvernés séparément.

`L0-UNDETERMINED` signifie absence de preuve suffisante, jamais absence certaine de compétence.

Le moteur ne compare des niveaux que dans une version d'échelle compatible.

## 4. SkillEvidence

Toute preuve normalisée conserve au minimum :
- `evidence_id` durable ;
- `subject_ref` ;
- `skill_ref` ;
- `source_type` ;
- `source_ref` et version ;
- `asserted_level` ou assertion observable si disponible ;
- `observed_at` / période ;
- `received_at` ;
- `provenance_ref` ;
- `verification_state` ;
- `validity_state` ;
- `evidence_strength_class` ;
- `purpose_ref` lorsque requis ;
- version de normalisation.

Classes logiques de source :
- `ASSESSMENT` — résultat autoritatif ASM référencé ;
- `EDUCATION` — élément éducatif PRF-002 relié à une compétence via mapping gouverné ;
- `EXPERIENCE` — expérience PRF-002 avec evidence/mapping gouverné ;
- `CREDENTIAL` — preuve vérifiée admissible ;
- `OBSERVATION` — observation structurée autorisée ;
- `SELF_DECLARED` — déclaration du sujet ;
- `INFERRED` — inférence explicitement identifiée.

Une classe ne reçoit pas ici un poids numérique universel. Les poids/seuils appartiennent à une `DerivationPolicyVersion` testée et gouvernée.

## 5. Effets des preuves

Une preuve peut :
- créer un état si le minimum de preuve est satisfait ;
- renforcer la confiance ;
- soutenir une hausse de niveau ;
- soutenir une baisse/révision ;
- maintenir l'état ;
- devenir stale/expired ;
- être révoquée/infirmée ;
- déclencher un recalcul.

Aucune preuve unique n'augmente ou ne diminue automatiquement un niveau sauf règle explicite de la politique versionnée.

L'absence de nouvelle preuve ne constitue jamais à elle seule une preuve de baisse de compétence.

## 6. Confiance

`confidence_band` est catégoriel et explicable :
- `INSUFFICIENT` ;
- `LOW` ;
- `MEDIUM` ;
- `HIGH`.

La confiance exprime la solidité de l'estimation, pas le niveau.

Elle dépend notamment de la qualité, vérification, diversité, cohérence et fraîcheur des preuves selon la `DerivationPolicyVersion`.

Les consommateurs ne doivent pas convertir arbitrairement cette bande en certitude.

## 7. Fraîcheur et expiration

Chaque type de preuve utilise une `FreshnessPolicyVersion`.

États :
- `CURRENT` ;
- `AGING` ;
- `STALE` ;
- `EXPIRED` ;
- `NOT-APPLICABLE`.

Aucune durée universelle n'est codée en dur pour toutes les compétences. La vitesse d'obsolescence peut dépendre de la famille de compétence, du type de preuve et du contexte.

L'expiration d'une preuve retire sa contribution future au calcul selon la politique ; elle ne supprime jamais son existence historique.

Un état peut conserver son niveau avec confiance réduite, devenir `UNDETERMINED`, ou nécessiter réévaluation selon politique. Il ne baisse pas silencieusement par convention.

## 8. Contradictions

Lorsque des preuves valides se contredisent :
1. elles restent toutes traçables ;
2. la politique évalue vérification, temporalité, portée et comparabilité ;
3. l'état peut être marqué `CONFLICTED` si le conflit matériel ne peut être résolu automatiquement ;
4. un workflow de revue peut être déclenché ;
5. aucun LLM ne tranche seul un conflit autoritatif.

`evidence_state` minimal :
`INSUFFICIENT`, `SUPPORTED`, `CONFLICTED`, `STALE`, `UNDER-REVIEW`.

## 9. Correction, révocation et invalidation

Les événements sources ne sont jamais réécrits dans SKL-002.

Si PRF-002, ASM-001 ou une autre source corrige/révoque une donnée :
- l'ancienne `SkillEvidence` est conservée avec son état historique ;
- une nouvelle version/lien de correction est enregistré ;
- la preuve précédente devient `SUPERSEDED`, `REVOKED` ou `INVALIDATED` selon le contrat ;
- un recalcul produit une nouvelle `UserSkillState.state_version` ;
- `SkillHistory` conserve avant/après, cause, source, méthode et horodatage ;
- un nouvel événement `user-skill.changed` est émis si l'état publié change.

Il est interdit d'écraser silencieusement le niveau antérieur.

## 10. Historique

`SkillHistory` est append-only au niveau logique.

Chaque transition conserve :
- version précédente et nouvelle ;
- cause ;
- evidence refs ajoutées/retirées/révoquées ;
- version de politique ;
- acteur ou workload responsable ;
- correlation/causation refs ;
- timestamps.

Une correction technique d'une donnée erronée suit une procédure auditée ; elle ne transforme pas l'historique métier en état mutable opaque.

## 11. Inférence et IA

Une inférence est `INFERRED`, jamais équivalente par défaut à une preuve vérifiée.

Une IA peut :
- proposer un mapping ;
- suggérer une compétence candidate ;
- expliquer un état déjà calculé ;
- détecter une contradiction pour revue.

Elle ne peut pas seule :
- créer une Skill canonique ;
- attribuer définitivement un niveau individuel ;
- augmenter/diminuer silencieusement un niveau ;
- résoudre une contradiction autoritative ;
- convertir une absence de donnée en absence de compétence.

Les règles déterminant quand une inférence peut contribuer au calcul sont versionnées et auditables.

## 12. Recalcul et reproductibilité

Un état publié doit être reproductible à partir :
- des evidence versions applicables ;
- de la taxonomy/proficiency scale version ;
- de la DerivationPolicyVersion ;
- de la FreshnessPolicyVersion ;
- des décisions de validation applicables.

Un changement de politique ne réécrit pas les anciennes versions. Il déclenche, si nécessaire, un nouveau calcul avec une nouvelle state_version.

## 13. Publication aux consommateurs

La projection minimale vers ORI/REC/OPP/CAR contient uniquement les champs nécessaires à la finalité, typiquement :
`subject_ref`, `skill_ref`, `proficiency_level_ref`, `confidence_band`, `freshness_state`, `evidence_state`, `skill_state_version`.

Les preuves détaillées ne sont pas propagées par défaut.

## 14. Gates désormais fermés

Sont désormais `DEFINED` :
- modèle logique de proficiency ;
- séparation niveau/confiance/fraîcheur ;
- modèle logique de preuve ;
- comportement création/hausse/baisse/révision ;
- expiration ;
- contradiction ;
- correction/révocation ;
- historique non destructif ;
- politique d'inférence ;
- reproductibilité.

Restent à l'implémentation/préproduction :
- coefficients/seuils réels de chaque DerivationPolicyVersion ;
- durées Freshness par famille/type ;
- mappings externes ;
- validation métier/psychométrique lorsque applicable ;
- Privacy/rétention ;
- BIA/RPO/RTO/restore ;
- tests de biais, accès, reproductibilité et réconciliation.

Statut final : `SEMANTIC-DERIVATION-BASELINE-CLOSED / NUMERIC-POLICIES-REQUIRE-VALIDATION`.
