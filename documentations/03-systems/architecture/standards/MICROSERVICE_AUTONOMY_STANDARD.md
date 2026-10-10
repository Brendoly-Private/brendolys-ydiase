---
document_id: "YD-DOC-SYS-MICROSERVICE-AUTONOMY-STANDARD"
title: "Microservice Autonomy Standard — BRENDOLYS YDIASE"
document_type: "architecture-standard"
document_role: "Définit une règle normative d’autonomie des microservices YDIASE."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "systems"
---

# Microservice Autonomy Standard — BRENDOLYS YDIASE

Statut : `D3-normative-candidate`

## 1. Objet

Ce standard définit l’autonomie obligatoire des frontières physiques YDIASE. Il s’applique aux 47 `YD-MS-*` confirmés et, avec adaptations explicites, aux 4 `YD-PLT-*`.

## 2. Règles non négociables

Chaque frontière possède un identifiant stable, repository, owners, artefact et CI/CD propres, runtime/configuration, datastore possédé si nécessaire, migrations privées, politique de reprise adaptée à AUTH/MIXED/DERIVED, RPO/RTO/SLO, contrats, identité machine, IAM, secrets/certificats, réseau deny-by-default, chiffrement, observabilité, health/readiness, scaling, rollback, mode dégradé, runbook, DR testé, rétention/suppression, decommission, SBOM et contrôles de sécurité.

## 3. Données

Chaque microservice est seul propriétaire en écriture de ses agrégats. Aucun autre service ne lit directement son stockage interne. `Database per service` signifie propriété exclusive du schéma, migrations, credentials et cycle de reprise, sans imposer un serveur physique par service.

## 4. Classification de reprise

### AUTH
Les données autoritatives exigent backup et restauration indépendants testés.

### MIXED
La partie autoritative suit AUTH. Les projections reconstruisibles suivent DERIVED. Le profil sépare les deux catégories.

### DERIVED — règle normative

`DERIVED` signifie que l’état persistant n’est jamais la seule copie d’un fait nécessaire au métier et peut être reconstruit intégralement depuis des sources gouvernées.

#### Éligibilité
Une frontière n’est DERIVED que si : aucun agrégat autoritatif n’y réside; aucune donnée irremplaçable n’existe uniquement localement; chaque donnée a une chaîne de sources identifiables et versionnées; suppressions, corrections, expirations et révocations sont reproductibles; une perte totale est récupérable sans ressaisie humaine de faits; la fenêtre de replay est prouvable. Toute donnée locale non reconstructible impose `MIXED` ou `AUTH`.

#### Sources de reconstruction
Pour chaque projection, le profil liste producteurs/sources, contrat/version, partition ou identifiant source, rétention, accès replay/snapshot, règles de suppression/révocation et owner source. « événements des domaines » ne suffit pas au gate production.

#### Checkpoint et watermark
Chaque pipeline maintient un checkpoint ou watermark durable comparable à une position source : offset/partition, séquence, version d’agrégat, timestamp métier protégé contre les trous, snapshot version ou équivalent. Il permet de détecter retard, trou, replay incomplet, source jamais traitée et divergence. Un timestamp local seul est insuffisant. Le checkpoint doit survivre ou être recalculable après perte du datastore dérivé.

#### Replay
Le replay est automatisable, borné et reproductible. Il définit point de départ, ordre, parallélisme, doublons, idempotence, événements hors ordre, corrections, tombstones, révocations privacy, erreurs permanentes, quarantaine/DLQ et reprise après interruption. Un doublon ne doit pas modifier le résultat final. La rétention des sources couvre la fenêtre maximale de replay; sinon snapshot gouverné ou mécanisme équivalent obligatoire.

#### Reconstruction
Trois opérations sont obligatoires : `FULL_REBUILD` depuis état vide, `PARTIAL_REBUILD` d’un sous-ensemble déterministe et `CATCH_UP` depuis checkpoint valide. Un backup local peut accélérer la reprise mais ne remplace jamais la preuve de reconstructibilité.

#### États de reconstructibilité
- `REBUILDABLE` : sources, replay et FULL_REBUILD testés et conformes
- `REBUILD-DEGRADED` : reconstruction possible mais RTO ou fraîcheur cible non respecté
- `REBUILD-BLOCKED` : une dépendance requise empêche la reconstruction
- `REBUILD-UNVERIFIED` : procédure théorique non encore prouvée

Seul `REBUILDABLE` permet `ready-for-production`.

#### Fraîcheur
Chaque projection expose `FRESH`, `STALE-ACCEPTABLE`, `EXPIRED` ou `UNKNOWN`. Les seuils numériques sont propres au service et fixés par SLO/ADR. `EXPIRED` et `UNKNOWN` ne sont jamais présentés comme actuels. La fraîcheur est exposée au consommateur lorsqu’elle influence sa décision.

#### Intégrité et convergence
Après replay/rebuild, des contrôles déterministes vérifient selon le service : comptages, checksums, versions, cardinalités, trous, doublons, références orphelines, tombstones et comparaison avec snapshots gouvernés. La reprise se termine uniquement après convergence vérifiée.

#### Schéma
Tout changement incompatible prévoit rebuild complet, migration déterministe, double projection/version ou remplacement atomique. Aucun consommateur ne doit migrer simultanément par obligation technique.

#### RPO/RTO
Le RPO DERIVED dépend de la fenêtre reconstructible des sources, pas de la seule sauvegarde locale. Le RTO inclut runtime, reconstruction jusqu’à état exploitable, catch-up, contrôle d’intégrité et fraîcheur minimale.

#### Tests
Avant production puis selon la cadence liée à la criticité, un test contrôlé isole ou supprime l’état dérivé et exécute un FULL_REBUILD. Le rapport mesure durée, volume, positions source, fraîcheur finale, doublons, trous, événements hors ordre, suppressions/révocations, erreurs, convergence, ressources et respect du RTO. Le profil conserve date, résultat, durée, fraîcheur, versions et anomalies. Un échec place le service en `REBUILD-BLOCKED` ou `REBUILD-DEGRADED` et bloque le gate production.

#### Reclassification
Tout fait non reconstructible, décision autoritative, état transactionnel unique ou rétention source insuffisante non compensée déclenche une ADR `DERIVED → MIXED/AUTH` et la mise à jour des exigences de reprise, sécurité et ownership.

## 5. BRENDOLYS Identity

BRENDOLYS Identity est l’IAM externe. Realms : `brendolys-internal`, `brendolys-networks`, `brendolys-customers`. Issuer OIDC : `https://sso.godinfradsby.xyz/realms/{realm}/protocol/openid-connect`. Chaque profil déclare realms, audience, clients, scopes, rôles, claims, règles tenant/organisation et comportement IAM indisponible.

## 6. Réseau et service-to-service

Identité workload dédiée. Deny-by-default. Chaque relation déclare caller, callee, audience, scopes machine, protocole, timeout, retry et comportement de panne. Aucun datastore n’est public.

## 7. Sécurité et observabilité

Secrets isolés, rotation/révocation, TLS pour données non publiques, chiffrement au repos selon classification, threat model, SAST/SCA/image et tests d’autorisation. Logs, métriques, traces, correlation IDs et alertes sont requis. DERIVED expose en plus lag, watermark, freshness state, rebuild state et progression de replay.

## 8. Health, résilience et scaling

Liveness et readiness sont séparés. Pour DERIVED, readiness distingue runtime disponible et projection suffisamment fraîche. Timeout sur dépendances distantes, retries sûrs/idempotents, backpressure et circuit breakers selon besoin. Le rebuild/catch-up dispose d’un budget de capacité propre.

## 9. CI/CD et rollback

Build, test, promotion et rollback indépendants. Les changements de projection DERIVED incluent un test de rebuild de la version cible.

## 10. Audit

Les faits sensibles sont transmis à `YD-PLT-AUD-001`. Le producteur reste responsable du fait audité.

## 11. Mode dégradé

Chaque profil définit fail-closed, stale borné, queue, réponse partielle ou indisponibilité contrôlée. Privacy et sécurité ne passent pas fail-open par défaut. DERIVED ne présente jamais `EXPIRED` ou `UNKNOWN` comme actuel.

## 12. DR

Les scénarios couvrent perte de serveur/zone, corruption, suppression, compromission, perte datastore et dépendance externe. Pour DERIVED, destruction contrôlée de l’état suivie d’un FULL_REBUILD fait partie du test DR.

## 13. Template obligatoire

Chaque profil contient : Boundary ID, services logiques, owners, repository, artefact, runtime, datastores, migrations, classification, reprise, dernier test, RPO/RTO/SLO/criticité, APIs/events/projections, DNS, IAM, workload identity, secrets/certificats, réseau, chiffrement, audit, observabilité, health, quotas, scaling, déploiement/rollback, dépendances/interdictions, mode dégradé, runbook, DR, rétention/suppression, decommission et ADR ouverts.

DERIVED ajoute obligatoirement : sources et versions, rétention source, checkpoint/watermark, replay/idempotence, FULL_REBUILD/PARTIAL_REBUILD/CATCH_UP, état REBUILD-*, politique FRESH/STALE-ACCEPTABLE/EXPIRED/UNKNOWN, contrôle d’intégrité, dernier test, durée mesurée, fraîcheur obtenue et anomalies.

## 14. Gates

Aucun service ne passe `ready-for-production` avec un champ obligatoire inconnu sans ADR ou dérogation datée. DERIVED exige `REBUILDABLE`, FULL_REBUILD réussi, fenêtre source compatible, watermark vérifiable, replay idempotent, suppressions/révocations prouvées, intégrité réussie et seuils de fraîcheur fixés.

## 15. Application

Le standard s’applique aux 47 microservices métier et aux 4 composants plateforme. Les frontières différées n’obtiennent pas de ressources dédiées avant ADR d’extraction.
