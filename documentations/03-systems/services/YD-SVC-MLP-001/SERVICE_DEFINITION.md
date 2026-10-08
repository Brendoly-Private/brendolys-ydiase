---
document_id: "YD-DOC-SVC-MLP-001-DEF"
title: "YD-SVC-MLP-001 — Model Lifecycle & Registry Service"
document_type: "service-definition"
document_role: "Définit le service logique YD-SVC-MLP-001, son périmètre, ses responsabilités et ses dépendances documentées."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "service"
created_at: "2026-10-04"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-SVC-MLP-001 — Model Lifecycle & Registry Service

> **Rôle du document**
> Définit le service logique YD-SVC-MLP-001, son périmètre, ses responsabilités et ses dépendances documentées.
> **Usage développement :** référence obligatoire pour cadrer ce service logique avant toute traduction en composant physique.

`domain: ai` · `documentation: D2` · `status: candidate` · `implementation: not-started`

## Mission
Gouverner le catalogue des modèles utilisables par YDIASE et leur cycle de vie sans confondre cette responsabilité avec l’exécution des requêtes IA.

## Agrégats possédés
`ModelDefinition`, `ModelVersion`, `ModelEndpoint`, `ModelEvaluation`, `ModelApproval`, `ModelDeploymentState`, `ModelRetirement`.

## Source autoritative
YD-SVC-MLP-001 est l’unique source autoritative interne pour les modèles enregistrés, versions, endpoints approuvés, évaluations, états de promotion et retrait.

## Données consommées
AI policies depuis AI-001, métriques d’exécution et qualité depuis AI/ANL, exigences de sécurité et conformité, configuration d’infrastructure autorisée, audit depuis AUD-001.

## Frontières
- AI-001 décide si une requête IA peut être exécutée et selon quelle politique.
- AI-004 orchestre les tâches IA.
- MLP-001 décide quels modèles/versions/endpoints sont enregistrés et approuvés pour un usage donné.
- MLP-001 ne possède aucune vérité métier produite par les modèles.

## Condition d’activation
Le service peut rester documenté et non déployé tant qu’un registre simple suffit. Son activation autonome devient nécessaire lorsque plusieurs modèles, versions, endpoints, évaluations ou cycles de promotion doivent être gouvernés indépendamment.

## Incohérences
Aucune incohérence D2 ouverte. Les contrats d’évaluation, promotion, rollback et sélection seront spécifiés en D3.
