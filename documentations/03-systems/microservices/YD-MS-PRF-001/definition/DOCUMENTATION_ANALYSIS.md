---
document_id: "YD-DOC-MS-PRF-001-ANA"
title: "YD-MS-PRF-001 — Analyse documentaire individualisée"
document_type: "microservice-documentation-analysis"
document_role: "Analyse individuellement la cohérence documentaire, les dépendances, invariants et inconnues de YD-MS-PRF-001."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "microservice"
---

# YD-MS-PRF-001 — Analyse documentaire individualisée

> **Rôle du document**
> Analyse individuellement la cohérence documentaire, les dépendances, invariants et inconnues de YD-MS-PRF-001.
> **Usage développement :** analyse de support ; les sources canoniques et politiques applicables prévalent.

Statut : ANALYSIS-COMPLETE / K3-K4-RECONCILIATION-REQUIRED
Nature : AUTH
Criticité : C1

## Identité
PRF-001 est l'autorité du profil courant individuel : Profile Core, préférences, objectifs, contraintes déclarées et vues sémantiques autoritatives du profil courant.

Il ne possède pas les historiques PRF-002, l'identité IAM, les référentiels EDU/SKL ni les décisions Privacy CNS.

## Frontières
PRF-001 et PRF-002 ont des datastores privés distincts. Aucun accès DB croisé. PRF-002 fournit seulement des projections minimales lorsque nécessaires. IDN fournit IdentityRef. CNS gouverne les décisions Privacy. CFG fournit les règles pays applicables.

## Données et Privacy
Le profil courant est personnel et potentiellement très sensible selon les attributs. Minimisation forte, aucune donnée profil dans les tokens, contrôle self par sujet, accès support séparé et audité, export complet interdit sans finalité, décision Privacy obligatoire en fail-closed.

## Invariants
- PRF-001 reste AUTH du profil courant.
- PRF-002 reste AUTH de l'historique éducatif et professionnel.
- aucune base partagée ou lecture DB croisée.
- aucune reconstruction locale de PRF-002 par commodité.
- une panne PRF-002 ne bloque pas les opérations indépendantes du profil courant.
- CNS reste autorité Privacy.
- un scope universel profile:* est interdit.
- une projection ou un cache aval ne devient jamais autorité de secours.
- PRF-001 restaure son autorité depuis sa propre chaîne de recovery.

## K3
Le Contract Registry contient YD-CTR-PRF-CURRENT-PROFILE-v1 et les dépendances IDN/CNS/CFG. Les responsabilités et invariants sont définis. Une baseline K3 propre à PRF-001 doit maintenant les réconcilier avec le gate actuel.

Verdict : K3-RECONCILIATION-REQUIRED.

## K4
IAM logique, sécurité, Privacy, criticité C1 et principes backup/restore sont définis. RPO/RTO/SLO, rétention, observabilité physique, owners nommés et preuve de restore restent ouverts.

Verdict : K4-ASSESSMENT-REQUIRED.

## K5
Les preuves devront couvrir invariants, contrats, self/IDOR, accès support, Privacy fail-closed, backup/restore indépendant, intégrité, non-réactivation de données supprimées ou restreintes, replay/réconciliation et résilience applicable.

Verdict : K5-NOT-YET-PASS.

## Choix ouverts
RPO/RTO/SLO, datastore/runtime physiques, rétention, clients OIDC, step-up, network policies, observabilité, scaling, rollback, mécanisme backup/restore, portabilité et règles mineurs.

## Verdict global
ANALYSIS-COMPLETE / RECONCILE-EXISTING-DOCS-BEFORE-READINESS.

PRF-001 ne reçoit pas automatiquement les contrôles détaillés de PRF-002 : sa donnée est le profil courant, non l'historique longitudinal avec preuves. La méthode est commune ; les exigences restent propres à sa frontière.
