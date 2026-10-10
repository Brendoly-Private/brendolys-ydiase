---
document_id: "YD-DOC-TRU-CNS-001-REVOCATION-RETENTION-RECOVERY-POLICY"
title: "YD-MS-CNS-001 — Revocation, Retention & Recovery Policy"
document_type: "trust-policy"
document_role: "Établit une règle ou baseline normative de gouvernance, confidentialité ou sécurité."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "trust"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-CNS-001 — Revocation, Retention & Recovery Policy

> **Rôle du document**
> Établit une règle ou baseline normative de gouvernance, confidentialité ou sécurité.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `NORMATIVE-C1-BASELINE / PREPROD-PROOF-PENDING`

## Invariant principal

Une restauration CNS ne peut jamais faire redevenir actif un grant, consentement ou droit qui était révoqué, expiré, restreint ou superseded avant l'incident.

La récupération de disponibilité n'autorise jamais une régression de l'état Privacy.

## Ordre autoritatif

Les agrégats CNS portent version monotone et effective_at. Les événements/projections consommateurs rejettent toute version plus ancienne que la dernière version appliquée.

Une réconciliation post-restore compare les watermarks/versions connus afin de détecter toute projection consommateur plus récente que le point restauré.

## Backup et restore

CNS possède sa chaîne de backup/restore chiffrée et indépendante. Aucun cache consommateur, PRF ou autre service ne constitue un backup de CNS.

Avant promotion du service restauré :
1. isoler les écritures ;
2. restaurer depuis une génération saine ;
3. vérifier intégrité et chronologie ;
4. établir le point de restauration ;
5. comparer journal durable/événements/revocation ledger disponibles ;
6. réappliquer toute révocation/restriction postérieure au snapshot si la chaîne autoritative le permet ;
7. invalider/réconcilier les caches consommateurs ;
8. vérifier qu'aucun état ancien n'a repris priorité ;
9. seulement ensuite autoriser NORMAL-RESTORED.

Si l'ordre récent des révocations ne peut pas être prouvé, les décisions concernées sont `NOT-DETERMINABLE` et fail-closed jusqu'à résolution.

## Ledger de révocation

L'implémentation doit disposer d'un mécanisme durable permettant de démontrer l'ordre des révocations/restrictions au-delà d'un simple cache applicatif. La technologie exacte reste à décider.

Ce ledger ne devient pas une seconde autorité métier indépendante : il fait partie de la chaîne de récupération CNS.

## Consommateurs

Chaque consommateur de PrivacyDecision/ConsentChanged doit :
- stocker decision/version watermark minimal nécessaire ;
- rejeter événement ancien ;
- invalider cache à révocation ;
- ne pas prolonger un TTL expiré en cas de panne CNS ;
- fournir un mécanisme de réconciliation ciblée.

## Effacement et backups

L'effacement actif est exécuté par le domaine propriétaire. Pour les backups immuables, la donnée ne doit pas être réintroduite dans l'état actif après restore ; les suppressions/restrictions applicables sont rejouées avant réouverture normale.

Les durées physiques de backup et mécanismes cryptographiques éventuels restent à valider selon obligations pays et architecture.

## Tests obligatoires préproduction

- restauration après grant puis révocation ;
- restauration depuis snapshot antérieur à une révocation ;
- événements de révocation reçus hors ordre ;
- cache consommateur plus ancien ;
- cache consommateur plus récent que snapshot CNS restauré ;
- perte temporaire CNS avec TTL expiré ;
- rétention/effacement avant backup puis restore ;
- effacement après backup puis restore ;
- correction de grant ;
- replay idempotent des événements ;
- CNS indisponible pendant traitement personnalisé REC/ORI/SKL ;
- intégrité des PrivacyRequest en cours.

Tout scénario qui réactive un traitement interdit est `RELEASE-BLOCKING`.

Statut final : `REVOCATION-RECOVERY-INVARIANTS-DEFINED / IMPLEMENTATION-AND-DR-EVIDENCE-PENDING`.
