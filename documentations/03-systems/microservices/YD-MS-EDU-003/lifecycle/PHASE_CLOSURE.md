---
document_id: "YD-DOC-MS-EDU-003-CLS"
title: "YD-MS-EDU-003 — Curriculum & Module — Fermeture de phase documentaire"
document_type: "microservice-phase-closure"
document_role: "Consigne la fermeture documentaire EDU-003 et les gates Privacy, rétention, IAM et recovery restant à prouver."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "evidence"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "microservice"
---

# YD-MS-EDU-003 — Curriculum & Module — Fermeture de phase documentaire

> **Rôle du document**
> Consigne la fermeture documentaire EDU-003 et les gates Privacy, rétention, IAM et recovery restant à prouver.
> **Usage développement :** preuve de maturité ou de fermeture ; le profil canonique et les politiques référencées restent autoritatifs.

Statut : `DOCUMENTATION-BASELINE-CLOSED / IMPLEMENTATION-PENDING`
Nature : `AUTH`
Criticité : `C2`

## Décision

La baseline documentaire de YD-MS-EDU-003 est suffisante pour poursuivre l'architecture globale de BRENDOLYS YDIASE. Cette fermeture ne signifie ni `VERIFIED`, ni `PRODUCTION-READY`.

## Autorité

YD-MS-EDU-003 est l'autorité de : Curriculum, CurriculumVersion, Module, TeachingUnit, ModuleSequence et mappings pédagogiques.

Dépendances structurantes : EDU-002, SKL-001 et provenance/qualité.

## Invariants

- ne possède ni Program ni Skill canonique.
- publication exige un Program valide.
- Skill inconnue ne devient jamais canonique ici.
- CurriculumPublished est versionné et réconciliable.
- datastore, migrations, secrets, workload identity et pipeline sont propres au service ;
- aucun accès DB croisé ;
- les projections/caches/consommateurs aval ne deviennent jamais autorité.

## Récupération C2

Le service possède une chaîne de backup/restore indépendante. Il doit pouvoir restaurer son autorité sans reconstruire ses agrégats depuis la base d'un autre microservice.

Après restauration, les références externes peuvent rester temporairement non résolues jusqu'à réconciliation. Cela ne transfère jamais l'ownership.

Les cibles RPO/RTO/SLO et les preuves de restore restent `TBD-PREPROD` et seront fixées à partir des besoins réels C2.

## IAM et exposition

La baseline logique de `AUTONOMY_PROFILE.md` reste canonique. Les clients OIDC, scopes détaillés, workload identities physiques, secrets/certificats et network policies sont fermés avant production.

Les lectures publiques/client passent par l'edge lorsque prévues ; les mutations de gestion/intégration restent contrôlées.

## Contrats

Les contrats physiques restent à lier à l'implémentation. Les événements D3 existants conservent leurs producteurs autoritatifs et leur versionnement. Aucun contrat n'autorise un consommateur à modifier directement les agrégats de YD-MS-EDU-003.

## Travaux différés

- owner et suppléant ;
- repository final (candidat : `brendolys-ydiase-curriculum-module`) ;
- datastore/runtime physiques ;
- RPO/RTO/SLO ;
- rétention/versioning détaillés ;
- IAM physique ;
- réseau/DNS ;
- observabilité/health/readiness ;
- quotas/scaling/rollback ;
- commandes backup/restore ;
- restore test ;
- contrats API/events/projections physiques ;
- workflows de validation applicables ;
- confrontation avec les domaines consommateurs/producteurs avant activation.

## Réouverture

Réouvrir si l'implémentation démarre, si une dépendance modifie la frontière, si un ADR transversal fixe les choix physiques, ou si la préproduction devient disponible.

Statut final : `CLOSED-FOR-NOW — RETURN AT IMPLEMENTATION/PREPROD`.
