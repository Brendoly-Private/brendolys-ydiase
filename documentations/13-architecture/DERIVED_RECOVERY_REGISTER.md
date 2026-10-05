# DERIVED Recovery Register — BRENDOLYS YDIASE

Statut : `D3-derived-control`

## Inventaire

| Boundary | Criticité | État rebuild | Contrats sources candidats | Gate préproduction principal |
|---|---:|---|---|---|
| YD-MS-SRH-001 Search & Discovery | C2 | REBUILD-UNVERIFIED | EDU-SEARCHABLE, CAR-SEARCHABLE, OPP-SEARCHABLE, CNT-SEARCHABLE, LRN-SEARCHABLE | FULL_REBUILD + rétention compatible |
| YD-MS-CNT-002 Feed | C3 | REBUILD-UNVERIFIED | CNT-FEEDABLE, COM-FEED-SIGNALS, MOD-CONTENT-DECISION, SPN-PLACEMENT | FULL_REBUILD + retraits MOD |
| YD-MS-KNW-001 Knowledge Graph | C2 | REBUILD-UNVERIFIED | EDU/SKL/CAR/LAB-KNOWLEDGE, DAT-PROVENANCE | FULL_REBUILD + provenance |
| YD-MS-ANL-001 Analytics | C2 | REBUILD-UNVERIFIED | familles DOMAIN-ANALYTICS enregistrées par métrique | catalogue métriques + FULL_REBUILD |
| YD-MS-AI-002 Retrieval & Grounding | C2 | REBUILD-UNVERIFIED | SRH-RETRIEVAL, KNW-GROUNDING, CNS-CORPUS-AUTHORIZATION + sources directes autorisées | droits corpus + FULL_REBUILD |

Total : 5 DERIVED purs.

## Contrats candidats v1

Les IDs normatifs complets sont définis dans `D3_BLOCKING_CLOSURE_DECISIONS.md` sous forme `YD-CTR-...-v1`. Ils identifient des contrats logiques et ne préjugent ni topic, ni broker, ni protocole physique.

Chaque contrat source doit porter ou permettre de déterminer : identifiant de message/projection, version, owner source, identifiant objet/agrégat, version source, opération UPSERT/DELETE/REVOKE ou équivalent, temps effectif, provenance minimale et position de replay.

## Rétention et reconstruction

Le gate D3 « contrats/versions/rétention sources » est fermé pour la construction du Contract Registry : les familles et obligations sont définies.

La valeur numérique de rétention reste `TBD-PREPROD`. Avant production, chaque source doit prouver l’une des options :

1. fenêtre de replay suffisante pour le besoin de reconstruction du consommateur
2. snapshot/version autoritatif permettant FULL_REBUILD puis CATCH_UP

Si aucune option n’est prouvée, le consommateur passe `REBUILD-BLOCKED`.

## Contrôle de conformité

| Exigence | SRH | Feed | KNW | ANL | AI-002 |
|---|---|---|---|---|---|
| aucune autorité primaire | OK | OK | OK | OK | OK |
| familles sources définies | OK | OK | OK | OK | OK |
| version contractuelle candidate | v1 | v1 | v1 | v1 | v1 |
| obligation replay/snapshot | OK | OK | OK | OK | OK |
| watermark exigé | OK | OK | OK | OK | OK |
| replay idempotent | OK | OK | OK | OK | OK |
| suppressions/révocations | OK | OK | OK | OK | OK |
| FULL/PARTIAL/CATCH_UP | OK | OK | OK | OK | OK |
| fraîcheur 4 états | OK | OK | OK | OK | OK |
| FULL_REBUILD testé | NON | NON | NON | NON | NON |
| état | REBUILD-UNVERIFIED | REBUILD-UNVERIFIED | REBUILD-UNVERIFIED | REBUILD-UNVERIFIED | REBUILD-UNVERIFIED |

## Passage à REBUILDABLE

Exige : contrats enregistrés, compatibilité rétention/snapshot prouvée, watermark observable, replay idempotent testé, suppressions/révocations testées, FULL_REBUILD réussi, convergence, seuils de fraîcheur, RTO mesuré et rapport de test.

## Verdict

`DERIVED-SOURCE-CONTRACTS` n’est plus `TBD-BLOCKING` pour D3. Les cinq services restent interdits de production en état `REBUILD-UNVERIFIED`. Les preuves de reconstruction restent des gates préproduction.