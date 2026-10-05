# YD-MS-SRH-001 — Search & Discovery Policy

Statut : `NORMATIVE-BASELINE / REBUILD-EVIDENCE-PENDING`
Classification : `DERIVED`
Criticité : `C2`

## 1. Mission et autorité

SRH-001 fournit recherche, découverte, facettes et ranking de pertinence sur des projections publiables.

Il possède `SearchIndexDefinition`, `SearchDocumentProjection` et, si persistée, `SearchQuerySession`. Il n'est jamais autorité sur Institution, Program, Occupation, Opportunity, Content ou LearningResource.

## 2. Sources primaires

Familles candidates :
- `YD-CTR-EDU-SEARCHABLE-v1`
- `YD-CTR-CAR-SEARCHABLE-v1`
- `YD-CTR-OPP-SEARCHABLE-v1`
- `YD-CTR-CNT-SEARCHABLE-v1`
- `YD-CTR-LRN-SEARCHABLE-v1`

KNW intervient uniquement via `YD-CTR-KNW-SRH-SEARCH-ENRICHMENT-v1`, comme enrichment optionnel.

## 3. SearchDocumentProjection

Chaque document indexé conserve au minimum :
- source_domain/source_ref/source_version ;
- document_type ;
- publication/visibility state ;
- language(s) ;
- territory/country scope si applicable ;
- searchable text/fields minimisés ;
- filter/facet fields ;
- effective/validity dates si applicables ;
- source watermark/replay position ;
- indexed_at ;
- freshness state ;
- access/privacy labels si non public.

L'index ne crée jamais un nouvel identifiant métier canonique.

## 4. Publication et suppression

Seuls les objets publiables/visibles selon leur owner sont découvrables.

`DELETE`, `WITHDRAW`, `REVOKE`, expiration OPP, dépublication CNT ou restriction Privacy ont priorité sur l'amélioration de ranking.

Un résultat devenu non publiable doit disparaître selon un SLO de retrait à définir avant production. Une panne d'enrichissement KNW ne retarde jamais ce retrait.

## 5. Ranking Search

Le ranking Search répond à : **quels documents correspondent le mieux à cette requête et à ses filtres autorisés ?**

Il peut utiliser pertinence textuelle/sémantique, langue, territoire, fraîcheur, qualité/publication et signaux de découverte explicitement autorisés.

Les coefficients/algorithmes sont versionnés et évalués.

Le ranking Search n'est pas :
- le ranking personnalisé REC-001 ;
- le score de matching OPP-002 ;
- une décision ORI ;
- une décision de recrutement.

## 6. Commercial

Paiement, commission, sponsoring, budget ou statut partenaire ne modifient jamais le ranking organique Search.

Tout placement sponsorisé éventuel est une surface séparée, étiquetée, et ne remplace pas les résultats organiques.

## 7. KNW enrichment

KNW peut fournir synonymes, relations, expansion sémantique, navigation et facettes dérivées.

`INFERRED` reste identifié comme tel. Une inférence KNW ne peut rendre découvrable un objet dont la source n'est pas publiable.

SRH conserve séparément `source_document_watermark` et `knowledge_enrichment_watermark`.

## 8. Langue et territoire

La requête conserve langue détectée/déclarée et contexte territorial autorisé. Les mappings/translations utilisés sont versionnés.

Absence de traduction n'autorise pas l'invention d'un équivalent. Une recherche panafricaine ne suppose pas que mêmes termes, qualifications ou métiers ont la même sémantique dans tous les pays.

CFG et taxonomies gouvernées fournissent le contexte ; SRH ne crée pas une vérité pays parallèle.

## 9. Privacy et accès

Les documents publics sont séparés des projections restreintes.

Une requête authentifiée ne donne pas automatiquement accès à tout l'index. Les résultats restreints exigent scopes/tenant/finalité/Privacy applicables.

Les champs non nécessaires, secrets, credentials et PII inutile ne sont pas indexés.

Une SearchQuerySession persistée est minimisée, soumise à rétention et ne devient pas un profil comportemental implicite.

## 10. Fraîcheur

États : `FRESH`, `STALE-ACCEPTABLE`, `EXPIRED`, `UNKNOWN`.

Un document `EXPIRED` ou `UNKNOWN` n'est pas présenté comme actuel lorsque l'actualité est requise. Les seuils numériques sont définis par classe avant ACTIVE.

## 11. Rebuild

Modes : `FULL_REBUILD`, `PARTIAL_REBUILD`, `CATCH_UP`.

Le FULL_REBUILD part des snapshots/projections autoritatives puis rattrape les flux depuis watermarks compatibles.

Le rebuild doit fonctionner sans KNW, puis appliquer l'enrichment de façon incrémentale.

Replay idempotent obligatoire : doublons, out-of-order, delete/revoke et réindexation doivent converger vers l'état logique source.

## 12. Panne

SRH peut fournir recherche partielle si les sources concernées restent dans leurs seuils de fraîcheur et si l'UI/API expose la dégradation pertinente.

Aucun index stale ne devient source de secours pour valider une candidature, une opportunité, un programme ou une autre commande sensible.

## 13. Explicabilité et observabilité

Pour diagnostic, chaque résultat permet de retrouver document source/version, index version et facteurs de ranking non sensibles.

Les métriques incluent au minimum index lag, source watermark lag, retrait lag, rebuild duration, documents orphelins, erreurs d'autorisation et qualité de recherche.

## 14. Gates

`DEFINED` : authority boundary, source contracts, document projection, publication/retrait, ranking boundary, commercial isolation, KNW enrichment, langue/territoire, Privacy, freshness, rebuild, panne.

`TBD-PREPROD` : schémas physiques, analyzers/tokenizers multilingues, ranking coefficients, quality metrics, freshness/removal SLO, access model détaillé, query retention, FULL_REBUILD mesuré, RTO/SLO et tests de sécurité.

Statut final : `SEARCH-DISCOVERY-SEMANTICS-CLOSED / FULL-REBUILD-AND-PREPROD-EVIDENCE-PENDING`.
