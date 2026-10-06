# ADR-SKL-001 — Authoritative Skills Knowledge

Statut : `ACCEPTED / DOCUMENTARY-BASELINE`

## Contexte

YDIASE reçoit des signaux Education, Career et Data susceptibles d'enrichir la connaissance des compétences. Sans frontière d'autorité, une evidence externe ou une inférence IA pourrait modifier silencieusement le référentiel canonique.

## Décision

`YD-MS-SKL-001` reste l'autorité exclusive de `Skill`, `KnowledgeConcept`, `SkillRelation` et `SkillTaxonomyMapping`.

Les autres domaines fournissent des evidence et références versionnées. Toute mutation canonique passe par la gouvernance SKL. Une IA peut produire une proposition mais ne peut jamais publier seule une mutation canonique.

Les échanges inter-domaines sont découplés et evidence-driven. SKL conserve son datastore autoritatif et son mécanisme de recovery indépendants.

## Conséquences

- ownership sans ambiguïté
- provenance obligatoire
- workflow de validation requis avant production
- absence de transaction distribuée EDU/CAR/DAT ↔ SKL
- caches et projections reconstruisibles séparés du store autoritatif
- versionnement des taxonomies, mappings et contrats requis

## Alternatives rejetées

1. Autoriser Education ou Career à créer directement des Skills canoniques : rejeté pour éviter l'autorité multiple.
2. Autoriser l'IA à publier automatiquement : rejeté faute de contrôle de gouvernance.
3. Utiliser une base partagée multi-domaines comme autorité : rejeté car elle brouille ownership et recovery.

## Preuves documentaires

- `PHASE_CLOSURE.md`
- `AUTONOMY_PROFILE.md`
- `K3_CONTRACT_BASELINE.md`
