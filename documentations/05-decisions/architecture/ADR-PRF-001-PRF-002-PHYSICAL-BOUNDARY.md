---
document_id: "YD-DOC-ADR-ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY"
title: "ADR — Séparation physique PRF-001 / PRF-002"
document_type: "architecture-decision-record"
document_role: "Consigne une décision d’architecture et ses conséquences applicables."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "decisions"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# ADR — Séparation physique PRF-001 / PRF-002

> **Rôle du document**
> Consigne une décision d’architecture et ses conséquences applicables.
> **Usage développement :** référence obligatoire pour les choix d’architecture concernés.

Statut : `ACCEPTED`
Date : 2026-10-05
Portée : domaine `02-identite-profils`

## Contexte

Deux décisions D3 se contredisaient : `DDD_REVIEW.md` classait PRF-002 `REVIEW-SPLIT`, tandis que `SENSITIVE_MERGER_REVIEW.md` validait la fusion PRF-001 + PRF-002 sous contrôle renforcé.

La baseline métier du domaine 02 confirme deux responsabilités distinctes :

- PRF-001 : profil courant, préférences, objectifs et contraintes déclarées
- PRF-002 : historique éducatif/professionnel, réalisations et liens de preuve

## Décision

La cible physique sépare PRF-001 et PRF-002 en deux microservices autonomes :

- `YD-MS-PRF-001 Profile`
- `YD-MS-PRF-002 Education & Experience Profile`

La séparation logique et physique devient la cible de référence. Une future fusion reste possible uniquement par nouvel ADR si les faits d'exploitation démontrent qu'elle respecte encore les critères normatifs de frontière.

## Motifs

1. Les cycles de vie divergent : profil courant contre historique long et temporel.
2. Les règles de preuve et provenance sont plus fortes pour PRF-002.
3. Les politiques de rétention peuvent diverger selon finalité et catégorie de donnée.
4. Les permissions minimales ne sont pas identiques : de nombreux consommateurs ont besoin du profil courant sans avoir besoin de l'historique complet.
5. La restauration, migration et portabilité de l'historique doivent pouvoir évoluer indépendamment.
6. La concentration des deux responsabilités augmente le rayon d'impact d'une compromission.
7. La doctrine de pérennité favorise une frontière extractible lorsque sémantique, temporalité et contraintes de preuve divergent durablement.

## Coûts acceptés

- un déploiement autonome supplémentaire
- contrats interservices explicites
- observabilité, sauvegarde et restauration propres à PRF-002
- cohérence éventuelle pour certaines vues combinées
- complexité opérationnelle supérieure à une fusion locale

Ces coûts sont acceptés car la décision cible l'architecture de long terme et non une économie de serveurs au pilote.

## Invariants

- PRF-001 ne possède pas les historiques détaillés PRF-002.
- PRF-002 ne possède pas les institutions, formations, qualifications ou compétences de référence.
- aucune base de données n'est partagée entre PRF-001 et PRF-002.
- les échanges passent par contrats gouvernés.
- un consommateur reçoit uniquement les données minimales nécessaires.
- les références de preuve et provenance restent interprétables après migration.
- la suppression ou restriction d'une donnée respecte CNS-001 et les règles de conformité applicables.

## Conséquences D3

- `MICROSERVICE_BOUNDARY_REVIEW.md` doit passer PRF-002 de `MERGE` à `INDEPENDENT`.
- la cible passe de 47 à 48 microservices métier physiques.
- avec 4 composants plateforme, la cible autonome passe de 51 à 52 frontières.
- `SENSITIVE_MERGER_REVIEW.md` doit marquer l'ancienne fusion PRF comme `SUPERSEDED`.
- PRF-002 doit recevoir son propre `AUTONOMY_PROFILE.md` avant toute implémentation.
- Dependency Map, Event Map, contrats et profils d'autonomie devront représenter la frontière physique lorsqu'ils seront réconciliés après les revues métier.

## Réversibilité

Cette décision n'est pas éternelle. Une future architecture peut fusionner, redistribuer ou remplacer ces déploiements si elle préserve les responsabilités métier, la temporalité, la provenance, les droits, l'historique et les capacités de migration définies par le domaine 02.
