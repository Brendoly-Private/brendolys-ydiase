# DAT-005 — Reference & Taxonomy Governance Policy

Statut : `NORMATIVE-BASELINE / REFERENCE-CONTENT-PENDING`

## Principe
DAT-005 possède les **référentiels transversaux YDIASE**, pas les taxonomies spécialisées déjà possédées par un domaine.

## Frontières
DAT-005 peut posséder classifications génériques, mappings inter-référentiels et versions de datasets de référence.
Il ne possède pas :
- Skill/Knowledge taxonomy spécialisée : SKL-001 ;
- Occupation graph : CAR-001 ;
- Qualification framework métier : EDU-004 ;
- CountryConfiguration : CFG-001.

Un référentiel officiel externe conserve son attribution ; DAT-005 publie sa représentation/version gouvernée lorsque nécessaire.

## Versionnement
ReferenceVersion conserve dataset/taxonomy ref, semantic version ou identifiant équivalent, effective dates, provenance, compatibility state et status.

États : `DRAFT`, `ACTIVE`, `DEPRECATED`, `SUPERSEDED`, `RETIRED`.

## Mapping
ReferenceMapping conserve source ref/version, target ref/version, relation type, confidence/validation state, provenance et effective dates.
Un mapping n'est jamais une équivalence parfaite par défaut.

## Compatibilité
Breaking change exige nouvelle version, impact analysis et migration explicite. Les objets historiques gardent la référence/version utilisée lors de leur création.

## Panne
Dernière version valide peut rester lisible. Mutation/publication nécessitant une source ou validation courante absente est bloquée.

Statut final : `REFERENCE-TAXONOMY-SEMANTICS-CLOSED / CONTENT-AND-PREPROD-EVIDENCE-PENDING`.
