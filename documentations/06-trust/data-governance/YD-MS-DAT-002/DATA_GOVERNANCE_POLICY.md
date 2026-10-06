# DAT-002 — Acquisition & Raw Evidence Policy

Statut : `NORMATIVE-BASELINE / PREPROD-PENDING`

## Principe
DAT-002 capture ce qui a été reçu et comment. **Raw n'est jamais vérité métier publiée.**

## Pipeline
`AUTHORIZED → ACQUIRED → RAW-SEALED → PROVENANCE-LINKED → VALIDATION-PENDING`.
Échecs possibles : `REJECTED`, `QUARANTINED`, `FAILED`.

Chaque IngestionBatch/RawRecordEnvelope conserve source/right decision ref, connector/submission ref, received_at, content/schema identity, integrity hash ou mécanisme équivalent, territory/context, retention class et immutable raw ref.

## Immutabilité
Une correction produit une nouvelle enveloppe/version liée ; elle ne réécrit pas silencieusement le raw reçu.

## Sécurité
Connecteurs isolés, secrets par source, limites taille/type, quarantaine des entrées suspectes, chiffrement et contrôle d'accès. Le contenu externe est traité comme non fiable.

## Replay
Le replay doit être idempotent et conserver l'identité de l'acquisition originale. La politique de conservation du raw dépend des droits DAT-001, Privacy et besoins de preuve/replay ; aucune rétention infinie par défaut.

## Promotion
DAT-002 ne publie jamais directement un objet EDU/CAR/LAB/etc. La promotion exige provenance et validation selon la classe de données.

Statut final : `ACQUISITION-RAW-SEMANTICS-CLOSED / RETENTION-CONNECTORS-PREPROD-PENDING`.
