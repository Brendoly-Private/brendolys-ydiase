# KNW-001 → SRH-001 — Search Enrichment Contract Baseline

Statut : `DEPENDENCY-BASELINE / SRH-SEMANTIC-CLOSURE-COMPLETE`

## 1. Principe

SRH-001 peut consommer KNW pour **enrichir la découverte**, mais KNW n'est pas requis pour indexer la vérité de base publiée par EDU/CAR/OPP/CNT/LRN.

Cela évite qu'une panne/reconstruction KNW rende toute recherche impossible.

## 2. Contrat logique

Contrat candidat : `YD-CTR-KNW-SRH-SEARCH-ENRICHMENT-v1`.

Payload/projection minimal :
- graph_version ;
- source_watermarks ;
- subject source_ref/source_version ;
- relation_type/class ;
- related source_ref/source_version ;
- provenance summary ref ;
- confidence/quality si applicable ;
- territory/temporal scope ;
- freshness ;
- operation UPSERT/DELETE/REVOKE.

## 3. Usages autorisés dans Search

- expansion sémantique de requête ;
- navigation "lié à" ;
- filtres/facettes dérivés explicitement marqués ;
- synonymie/mapping gouverné ;
- candidate enrichment avant ranking Search.

Le document de recherche primaire conserve toujours son source_domain/source_ref/source_version.

## 4. Interdictions

SRH ne doit pas :
- créer un document métier uniquement à partir d'une inférence KNW si aucune source publiable ne l'autorise ;
- transformer `INFERRED` en fait certain ;
- maintenir un résultat après DELETE/REVOKE source ;
- utiliser un edge personnel sans décision Privacy applicable ;
- dépendre synchroniquement de KNW pour chaque requête.

## 5. Fraîcheur

SRH conserve séparément :
- `source_document_watermark` ;
- `knowledge_enrichment_watermark`.

Un enrichment KNW stale peut être désactivé sans retirer un document source encore valide.

## 6. Rebuild

FULL_REBUILD SRH doit pouvoir fonctionner sans KNW enrichment puis effectuer un enrichissement incrémental lorsque KNW redevient disponible.

FULL_REBUILD KNW ne commande jamais directement un rebuild SRH ; il publie GraphVersion/watermarks et SRH décide son rattrapage.

## 7. Préconditions SRH

Avant fermeture SRH-001, enregistrer :
- familles `EDU-SEARCHABLE`, `CAR-SEARCHABLE`, `OPP-SEARCHABLE`, `CNT-SEARCHABLE`, `LRN-SEARCHABLE` ;
- suppression/retrait prioritaire ;
- publication/visibility state ;
- language/territory fields ;
- source version + replay position ;
- Privacy/access labels pour documents non publics ;
- KNW enrichment comme dépendance optionnelle, versionnée et reconstructible.

Statut : `SRH-DEPENDENCIES-DEFINED / PHYSICAL-CONTRACT-AND-REBUILD-EVIDENCE-PENDING`.
