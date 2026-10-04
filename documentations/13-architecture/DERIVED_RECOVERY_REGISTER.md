# DERIVED Recovery Register — BRENDOLYS YDIASE

Statut : `D3-derived-control`

## Objet

Ce registre recense toutes les frontières actuellement classées `DERIVED` dans `AUTONOMY_PROFILE_REGISTER.md` et contrôle leur conformité à la règle normative de `MICROSERVICE_AUTONOMY_STANDARD.md`.

## Inventaire exact

| Boundary | Criticité | État rebuild actuel | Sources principales | Gate principal |
|---|---:|---|---|---|
| YD-MS-SRH-001 Search & Discovery | C2 | REBUILD-UNVERIFIED | EDU, CAR, OPP, CNT, LRN | contrats/versions/rétention, watermark, FULL_REBUILD |
| YD-MS-CNT-002 Feed | C3 | REBUILD-UNVERIFIED | CNT, COM, MOD, SPN séparé | watermark multi-source, retraits MOD, FULL_REBUILD |
| YD-MS-KNW-001 Knowledge Graph | C2 | REBUILD-UNVERIFIED | EDU, SKL, CAR, LAB, DAT provenance | provenance, watermarks, FULL_REBUILD |
| YD-MS-ANL-001 Analytics | C2 | REBUILD-UNVERIFIED | événements/projections métier autorisés | catalogue métriques, sources explicites, FULL_REBUILD |
| YD-MS-AI-002 Retrieval & Grounding | C2 | REBUILD-UNVERIFIED | SRH, KNW, sources autorisées | droits corpus, provenance, watermark, FULL_REBUILD |

**Total : 5 frontières DERIVED pures.**

Les frontières `MIXED` ne figurent pas dans ce total. Leur partie dérivée devra suivre la même règle, mais leur partie autoritative reste soumise aux exigences AUTH.

## Contrôle de conformité de conception

| Exigence | SRH | Feed | KNW | ANL | AI-002 |
|---|---|---|---|---|---|
| aucune autorité métier primaire | OK | OK | OK | OK | OK |
| sources identifiées au niveau domaine | OK | OK | OK | OK, à détailler par métrique | OK |
| contrats/versions exacts | GATE | GATE | GATE | GATE | GATE |
| rétention source compatible replay | GATE | GATE | GATE | GATE | GATE |
| checkpoint/watermark exigé | OK | OK | OK | OK | OK |
| replay idempotent exigé | OK | OK | OK | OK | OK |
| suppressions/révocations couvertes | OK | OK | OK | OK | OK |
| FULL_REBUILD défini | OK | OK | OK | OK | OK |
| PARTIAL_REBUILD défini | OK | OK | OK | OK | OK |
| CATCH_UP défini | OK | OK | OK | OK | OK |
| fraîcheur à quatre états | OK | OK | OK | OK | OK |
| contrôle d’intégrité défini | OK | OK | OK | OK | OK |
| FULL_REBUILD réellement testé | NON — préproduction | NON — préproduction | NON — préproduction | NON — préproduction | NON — préproduction |
| état actuel | REBUILD-UNVERIFIED | REBUILD-UNVERIFIED | REBUILD-UNVERIFIED | REBUILD-UNVERIFIED | REBUILD-UNVERIFIED |

## Règles de passage

Aucune de ces cinq frontières ne peut passer `ready-for-production` tant que son état reste `REBUILD-UNVERIFIED`.

Le passage à `REBUILDABLE` exige simultanément :

1. contrats et versions sources enregistrés
2. fenêtre de rétention/replay prouvée
3. checkpoint/watermark implémenté et observable
4. replay idempotent testé
5. suppressions, corrections et révocations testées
6. FULL_REBUILD depuis état vide réussi
7. contrôles d’intégrité convergents
8. seuils FRESH/STALE-ACCEPTABLE/EXPIRED fixés
9. RTO de reconstruction mesuré et accepté
10. rapport de test enregistré avec versions et anomalies

## Cohérence

Aucune des cinq frontières ne contient actuellement, dans sa définition documentaire, un agrégat métier autoritatif imposant une reclassification immédiate. La classification `DERIVED` reste donc cohérente à D3.

Points à surveiller :

- Search : ne jamais stocker une correction métier uniquement dans l’index.
- Feed : ne jamais transformer un score/ranking ou une interaction temporaire en vérité métier sans owner dédié.
- Knowledge Graph : les relations dérivées gardent leur provenance; un fait édité manuellement et irremplaçable imposerait MIXED/AUTH.
- Analytics : toute métrique ou annotation manuelle durable non reconstructible doit être séparée de la projection analytique.
- Retrieval & Grounding : les corpus, chunks et embeddings restent dérivés; les droits d’usage, décisions privacy et faits sources restent chez leurs owners.

## Prochaine revue

Rejouer ce registre après le Contract Registry, car les contrats et versions exacts permettront de fermer les gates `sources/versions/rétention`. Rejouer également avant toute mise en production après les tests FULL_REBUILD.