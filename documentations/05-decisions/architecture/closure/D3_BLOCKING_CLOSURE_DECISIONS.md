---
document_id: "YD-DOC-ADR-D3-BLOCKING-CLOSURE-DECISIONS"
title: "D3 Blocking Closure Decisions — BRENDOLYS YDIASE"
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

# D3 Blocking Closure Decisions — BRENDOLYS YDIASE

> **Rôle du document**
> Consigne une décision d’architecture et ses conséquences applicables.
> **Usage développement :** référence obligatoire pour les choix d’architecture concernés.

Statut : `D3-normative`

## 1. Objet

Ce document ferme les six familles `TBD-BLOCKING` identifiées par `AUTONOMY_CLOSURE_MATRIX.md`. Il fixe les règles sémantiques nécessaires au futur Contract Registry sans choisir prématurément runtime, datastore, broker, gateway, secrets manager ou autres technologies physiques.

Les valeurs purement opérationnelles qui nécessitent mesure ou ADR restent `TBD-PREPROD` ou `ADR-REQUIRED` et ne bloquent plus la construction du Contract Registry candidat.

## 2. PRF-IAM — CLOSED

### Audience

Audience logique obligatoire : `ydiase-profile`.

### Realms

- `brendolys-customers` : accès du sujet à son propre profil et aux fonctions utilisateur autorisées.
- `brendolys-internal` : support, conformité ou opérations explicitement autorisés. Aucun accès global implicite.
- `brendolys-networks` : refusé par défaut. Toute future délégation exige un cas d'usage, une finalité et un scope dédiés.
- M2M : identité workload dédiée, audience `ydiase-profile`, scopes minimaux par consommateur.

### Scopes candidats normatifs

- `profile:read:self`
- `profile:write:self`
- `profile:education:read:self`
- `profile:education:write:self`
- `profile:experience:read:self`
- `profile:experience:write:self`
- `profile:goals:read:self`
- `profile:goals:write:self`
- `profile:read:support` — interne, usage contrôlé et audité
- `profile:projection:read` — M2M, projection minimale seulement

Un scope `profile:*` universel est interdit pour les clients ordinaires.

### Claims minimaux

`sub`, `iss`, `aud`, expiration/temps standard du token et scopes. `org_id`/tenant uniquement lorsque le cas d'usage l'exige. Les données de profil, objectifs, études et expériences ne sont pas copiées dans les tokens.

### Autorisation

Le service PRF contrôle l'autorisation objet. `sub` doit correspondre au sujet demandé pour les scopes `:self`. Les accès support exigent rôle interne autorisé, finalité opérationnelle et audit. Une décision CNS requise et indisponible entraîne fail-closed.

**Résultat :** le modèle IAM est assez défini pour enregistrer les contrats. Les noms de clients OIDC physiques, durées de token et règles de step-up restent préproduction/ADR.

## 3. DPR-LICENSING — CLOSED

Chaque `DataProductRelease` possède un `LicenseManifest` versionné et immuable pour la release. Le manifest contient au minimum :

- `license_id` et `license_version`
- `data_product_id` et `release_id`
- owner commercial
- catégories de consommateurs autorisés
- finalités autorisées et interdites
- territoires/pays autorisés
- durée/expiration si applicable
- droits de consultation, export, redistribution et dérivation
- restrictions de sous-licence
- référence à l'entitlement BIL requis
- référence à la décision privacy/distribution CNS
- obligations de suppression/retrait
- provenance et références aux sources
- statut `DRAFT`, `APPROVED`, `SUSPENDED`, `REVOKED`, `EXPIRED`

Une release ne devient `PUBLISHED` que si licence, entitlement model et décision privacy sont compatibles. Une licence révoquée bloque les nouveaux accès. Les effets sur copies déjà distribuées suivent les obligations du manifest et sont auditables.

Aucune licence DPR ne peut accorder un droit que la source, la réglementation ou CNS n'autorise pas.

## 4. DPR-PRIVACY-AGGREGATION — CLOSED

DPR ne décide jamais seul qu'un dataset est distribuable. CNS reste autorité sur finalité, restrictions privacy et décision de distribution.

### Classes de sortie

- `PUBLIC-NONPERSONAL` : données publiques/non personnelles dont les droits permettent la distribution.
- `AGGREGATED` : agrégats dont le risque de réidentification a été évalué et accepté.
- `ANONYMIZED` : transformation validée comme non personnelle selon le cadre juridique/pays applicable et la méthode documentée.
- `RESTRICTED-DERIVED` : résultat dérivé distribuable uniquement à des consommateurs/finalités déterminés.
- `NOT-DISTRIBUTABLE` : données personnelles, sensibles, insuffisamment agrégées, sans droits suffisants ou refusées par CNS.

### Privacy Manifest obligatoire

Chaque release référence un `PrivacyDistributionDecision` contenant : finalité, catégories de données sources, pays/territoires, méthode de transformation, variables de quasi-identification examinées, règles de suppression/generalisation, tests de réidentification applicables, restrictions, durée de validité, décision CNS et version.

Aucun seuil universel d'anonymisation n'est inventé à D3. Les seuils numériques dépendent du dataset, du risque et du Country Framework. Ils deviennent obligatoires avant publication de la release concernée.

Les données personnelles brutes, identifiants directs et secrets sont `NOT-DISTRIBUTABLE` par défaut. L'agrégation ne change pas automatiquement le statut privacy.

**Résultat :** le schéma de décision et l'autorité sont fixés pour le Contract Registry. Les paramètres statistiques propres à chaque produit restent un gate de release, pas un blocage D3 global.

## 5. DERIVED-SOURCE-CONTRACTS — CLOSED FOR REGISTRY

Les cinq DERIVED purs utilisent des familles de contrats sources candidates stables. Les identifiants ci-dessous sont des IDs documentaires/contractuels, pas des noms de topics physiques.

### Search & Discovery

Sources requises :
- `YD-CTR-EDU-SEARCHABLE-v1` — institutions/programmes/modules publiables
- `YD-CTR-CAR-SEARCHABLE-v1` — métiers/carrières publiables
- `YD-CTR-OPP-SEARCHABLE-v1` — opportunités et état de publication
- `YD-CTR-CNT-SEARCHABLE-v1` — contenus publiés/retraits
- `YD-CTR-LRN-SEARCHABLE-v1` — ressources learning publiables

### Feed

Sources requises :
- `YD-CTR-CNT-FEEDABLE-v1`
- `YD-CTR-COM-FEED-SIGNALS-v1`
- `YD-CTR-MOD-CONTENT-DECISION-v1`
- `YD-CTR-SPN-PLACEMENT-v1` — canal sponsorisé explicitement séparé

### Knowledge Graph

Sources requises :
- `YD-CTR-EDU-KNOWLEDGE-v1`
- `YD-CTR-SKL-KNOWLEDGE-v1`
- `YD-CTR-CAR-KNOWLEDGE-v1`
- `YD-CTR-LAB-KNOWLEDGE-v1`
- `YD-CTR-DAT-PROVENANCE-v1`

### Analytics

Analytics n'accepte pas un flux générique « tous événements ». Chaque métrique enregistrée référence une ou plusieurs familles `YD-CTR-<DOMAIN>-ANALYTICS-v1` explicitement autorisées, sa méthodologie, son grain, sa finalité et son owner. Une métrique sans sources enregistrées reste `DRAFT` et ne peut être publiée.

### Retrieval & Grounding

Sources requises :
- `YD-CTR-SRH-RETRIEVAL-v1`
- `YD-CTR-KNW-GROUNDING-v1`
- `YD-CTR-CNS-CORPUS-AUTHORIZATION-v1`
- plus toute source documentaire directe explicitement autorisée avec provenance et droits.

### Obligations communes des contrats DERIVED

Chaque contrat source v1 doit porter ou permettre de déterminer : `event/projection id`, version, source owner, object/aggregate id, source version, operation (`UPSERT`, `DELETE`, `REVOKE` ou équivalent), occurred/effective time, provenance minimale et position de replay.

La source doit fournir soit :

1. une fenêtre de replay couvrant le besoin de reconstruction du consommateur, soit
2. un snapshot/version autoritatif permettant un FULL_REBUILD, complété par un catch-up.

L'absence de durée numérique n'empêche plus l'enregistrement du contrat. Avant production, la compatibilité `source retention/snapshot >= consumer recovery requirement` doit être prouvée et enregistrée. Si elle ne l'est pas, le service DERIVED reste `REBUILD-BLOCKED`.

Les suppressions, retraits et révocations doivent être représentables. Les consommateurs gardent leur watermark par source/partition logique. Le transport physique et la forme exacte du checkpoint restent ADR-REQUIRED.

**Résultat :** les familles, responsabilités et obligations de replay sont assez définies pour construire le Contract Registry. Les FULL_REBUILD réels restent gates préproduction.

## 6. PLT-AI-IAM — CLOSED

Audience logique : `ydiase-ai-gateway`.

### Realms

- `brendolys-customers` : fonctions AI exposées aux utilisateurs/organisations clientes selon produit et entitlement.
- `brendolys-networks` : uniquement cas d'usage explicitement autorisés pour ambassadeurs/réseaux. Aucun accès général.
- `brendolys-internal` : administration, diagnostic, évaluation et usages internes autorisés.
- M2M : appels des services YDIASE avec identité workload dédiée.

### Scopes

- `ai:invoke` — invocation d'un cas d'usage autorisé
- `ai:grounded:invoke` — invocation exigeant grounding
- `ai:verify:invoke` — invocation exigeant vérification
- `ai:usage:read:self` — lecture de l'usage propre lorsque exposé
- `ai:policy:read` — interne contrôlé
- `ai:policy:manage` — interne privilégié, audit obligatoire
- `ai:model:route` — M2M/interne, jamais client ordinaire

L'autorisation finale est l'intersection de : realm + scope + use-case policy + purpose CNS + entitlement si applicable + modèle approuvé MLP + contraintes tenant/pays.

Le token ne contient ni prompt complet ni données métier. Les politiques sensibles ne sont pas déléguées au client. Si CNS, entitlement ou approbation modèle obligatoire n'est pas vérifiable, fail-closed.

Les clients OIDC physiques et règles de step-up restent préproduction/ADR.

## 7. PLT-API-IAM — CLOSED

Audience logique : `ydiase-external-api`.

### Principes clients

Chaque client API possède une identité distincte. Les credentials partagés entre organisations sont interdits. Les accès machine utilisent client/workload identity; les appels agissant au nom d'un utilisateur conservent la délégation utilisateur selon le contrat concerné.

### Realms

- `brendolys-customers` : organisations clientes et utilisateurs clients lorsque l'API le prévoit.
- `brendolys-internal` : administration/support API contrôlés.
- `brendolys-networks` : aucune API générale; uniquement contrat explicitement destiné au réseau.

### Scopes

Aucun scope global `api:*` ne donne accès aux backends. Les scopes sont attachés à un produit/contrat, par exemple `api:<contract-id>:read` ou `api:<contract-id>:write`. L'External API Management vérifie le scope technique et l'entitlement BIL; le backend reste responsable de l'autorisation métier et objet.

### Onboarding minimal

Chaque client enregistré possède : client owner, organisation/tenant, contrats autorisés, scopes, entitlement, quotas, territoires si applicables, méthode d'authentification, dates de création/expiration, statut, contact sécurité et audit trail.

Statuts : `PENDING`, `ACTIVE`, `SUSPENDED`, `REVOKED`, `EXPIRED`.

Une suspension/revocation prend effet avant routage vers le backend. L'indisponibilité d'Identity ou de l'entitlement requis entraîne fail-closed pour les nouveaux appels protégés.

La méthode physique d'authentification M2M, mTLS éventuel, durées credentials et rotation relèvent d'ADR/préproduction.

## 8. Verdict

Les six familles précédemment `TBD-BLOCKING` passent à `DEFINED-FOR-CONTRACT-REGISTRY` :

1. PRF-IAM — fermé
2. DPR-LICENSING — fermé
3. DPR-PRIVACY-AGGREGATION — fermé
4. DERIVED-SOURCE-CONTRACTS — fermé pour construction du registre; preuves de rebuild restent préproduction
5. PLT-AI-IAM — fermé
6. PLT-API-IAM — fermé

Le Contract Registry canonique est désormais matérialisé dans `CONTRACT_REGISTRY.md`. Il ne reste aucun `TBD-BLOCKING` connu sur l'identification des familles contractuelles; les schémas physiques, SLO et preuves préproduction restent actifs. Cette fermeture ne vaut pas autorisation de production : les `TBD-PREPROD` et `ADR-REQUIRED` restent actifs.