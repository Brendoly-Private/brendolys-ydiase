# DAT-003 — Provenance & Lineage Policy

Statut : `NORMATIVE-BASELINE / PREPROD-PENDING`

## Principe
Toute assertion importante doit pouvoir répondre : **d'où vient-elle, de quelle version, par quelles transformations et avec quelles preuves ?**

## Autorité
DAT-003 possède ProvenanceRecord, AssertionLineage, EvidenceRecord et TransformationLineage. Il possède la preuve de provenance, jamais la vérité métier de l'assertion.

## Lineage
Un lineage relie source/raw/input refs → transformations versionnées → validation refs → publication/domain object ref. Les étapes conservent acteur/workload, timestamps, code/rule/model version lorsque pertinent et relations parent/enfant.

## Histoire
Append/versioned : une correction ou invalidation ajoute un nouvel état lié. Aucune altération silencieuse d'une preuve historique.

## Provenance manquante
Lorsqu'une classe exige une provenance obligatoire, absence/incohérence bloque promotion. `UNKNOWN` reste explicite.

## IA et dérivations
Une sortie AI/ML ne devient pas source primaire. Son lineage référence modèle/policy, grounding/input refs et verification applicable.

## Confidentialité
Les contrats aval exposent la provenance minimale nécessaire ; preuves contractuelles, PII ou secrets restent protégés.

## Recovery
DAT-003 est C1 AUTH : projections aval ne sont jamais son backup. Restore doit préserver graph/chaîne, versions et liens publication-preuve.

Statut final : `PROVENANCE-LINEAGE-SEMANTICS-CLOSED / DR-EVIDENCE-PENDING`.
