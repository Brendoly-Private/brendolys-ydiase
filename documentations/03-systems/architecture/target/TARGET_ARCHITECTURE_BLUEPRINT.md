---
document_id: "YD-DOC-SYS-ARC-TGT-008"
title: "BRENDOLYS YDIASE — Architecture cible complète"
document_type: "target-architecture-blueprint"
document_role: "Définit la blueprint complète de la cible YDIASE, conçue intégralement avant activation et dimensionnée pour l’hyperscale."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "architecture"
---

# BRENDOLYS YDIASE — Architecture cible complète

> **Rôle du document**
> Définit la blueprint complète de la cible YDIASE, conçue intégralement avant activation et dimensionnée pour l’hyperscale.
> **Usage développement :** référence obligatoire pour la conception et l’implémentation de la frontière concernée.

Statut : TARGET-ARCHITECTURE / NORMATIVE-BASELINE
Portée : cible complète, indépendamment de l'ordre d'activation

## 1. Doctrine

YDIASE est conçu intégralement maintenant puis activé progressivement.

Chaîne canonique :
Vision → Domaines → Capacités → Bounded Contexts → Microservices → Contrats/Événements → Plateformes Data/IA → Architecture physique → Implémentation → Déploiement → Activation → Vérification.

La cible architecturale est dimensionnée pour 5 à 15 millions d'utilisateurs simultanément actifs à l'échelle de la plateforme. Chaque microservice possède cependant son propre profil de charge ; aucun service n'est supposé recevoir à lui seul 15 millions de requêtes simultanées.

## 2. Domaines cibles

### Identité, profils et Privacy
Identités, sessions, profil courant, historique éducatif/professionnel, consentements, finalités, droits et préférences de confidentialité.

### Éducation
Institutions, campus, programmes, curricula, modules, qualifications, admissions, coûts, prérequis et cadres nationaux.

### Compétences et connaissances
Taxonomie de compétences, niveaux, acquis, preuves, équivalences et compétences transférables.

### Métiers et carrières
Métiers, familles, activités, trajectoires, transitions, reconversion et simulations de carrière.

### Orientation et recommandation
Assessment, dossiers d'orientation, comparaison, décision, recommandation explicable et scénarios éducatifs, professionnels, entrepreneuriaux et hybrides.

### Marché du travail et intelligence économique
Signaux de demande/offre, secteurs, territoires, activité formelle/informelle qualifiée, indicateurs, tendances et prévisions.

### Opportunités, candidatures et recrutement
Stages, emplois, missions, programmes, candidatures, matching, employeurs, talents et campagnes.

### Entrepreneuriat
Projet entrepreneurial, opportunités économiques, hypothèses de marché, progression, écosystème d'accompagnement, financement/opportunités, complémentarités de fondateurs et passage entrepreneur → employeur.

### Contenu, communauté et apprentissage
Contenus, feed, communauté, learning discovery, ressources de progression et sujets académiques/professionnels.

### Partenaires et écosystème
Institutions, employeurs, ambassadeurs, partenaires, contributeurs, vérificateurs et workspaces.

### Data, Knowledge et Analytics
Sources, acquisition, provenance, qualité, référentiels, Knowledge Graph, analytics, forecasting et produits dérivés gouvernés.

### Intelligence artificielle
Gateway IA, grounding/retrieval, orchestration, vérification, modèles, évaluation, safety et usages contextualisés.

### Économie produit
Abonnements, entitlements, billing, marketplace, sponsoring, API, produits Data et Intelligence.

### Plateforme et gouvernance
Search, notifications, administration, modération, audit, configuration pays, sécurité, observabilité et capacités d'exploitation.

## 3. Frontières fonctionnelles

Une frontière possède une responsabilité métier, un owner de données et des invariants propres. Aucun microservice ne lit directement la base d'un autre. Les échanges passent par contrats gouvernés.

AUTH : source de vérité métier.
DERIVED : projection reconstruisible.
MIXED : état propre + données dérivées explicitement séparées.
PLATFORM : capacité technique transverse sans appropriation de vérité métier externe.

Search, Analytics, Knowledge Graph, IA, lakehouse, caches et index ne deviennent jamais autorités des domaines sources.

## 4. Microservices cibles

La Service Map existante reste la base des frontières déjà identifiées. La cible ajoute une famille Entrepreneuriat à soumettre à revue DDD :

- YD-SVC-ENT-001 — Venture Profile Service : projet entrepreneurial, stade, objectifs, hypothèses et progression.
- YD-SVC-ENT-002 — Entrepreneurial Opportunity Intelligence Service : opportunités économiques territoriales et sectorielles fondées sur signaux/provenance.
- YD-SVC-ENT-003 — Entrepreneurship Support Ecosystem Service : incubateurs, accélérateurs, mentors, programmes et structures d'appui.
- YD-SVC-ENT-004 — Funding Opportunity Service : dispositifs, appels, subventions, concours et financements avec règles d'éligibilité sourcées.
- YD-SVC-ENT-005 — Founder & Team Matching Service : complémentarités de compétences et mise en relation gouvernée.
- YD-SVC-ENT-006 — Venture Progression Service : jalons, écarts, actions, résultats observés et transition vers le rôle employeur.

Ces IDs définissent des frontières logiques cibles. Leur maintien comme microservices physiques indépendants doit être confirmé par DDD/ADR ; aucune responsabilité n'est absorbée silencieusement par ORI, REC, LAB ou EMP.

## 5. Plateforme Data cible

Le plan Data comprend :
1. registre des sources et droits ;
2. ingestion batch, streaming, fichiers, partenaires et connecteurs ;
3. provenance de bout en bout ;
4. qualité, validation, corroboration et quarantaine ;
5. event backbone logique et contrats versionnés ;
6. stockage opérationnel privé par service ;
7. lakehouse/stockage analytique pour historique et analyses ;
8. traitements batch/stream ;
9. projections Search ;
10. Knowledge Graph dérivé ;
11. Analytics/BI et forecasting ;
12. feature/data serving gouverné pour ML/IA ;
13. catalogage, lineage, classification, rétention et suppression ;
14. observabilité des pipelines, lag, qualité, coûts et capacité.

Le choix de Kafka/Pulsar, Flink/Spark, lakehouse, moteurs de recherche, bases et orchestrateurs relève d'ADR après Capacity Profiles et benchmarks.

## 6. Plateforme IA cible

La plateforme IA sépare :
- AI Gateway : contrôle d'accès, politiques, quotas et routage ;
- Retrieval & Grounding : récupération de connaissances autorisées avec provenance ;
- AI Orchestration : composition de modèles/tâches/outils autorisés ;
- AI Verification : validation de sorties, sources, contraintes et confiance ;
- model serving et lifecycle : versions, registry, déploiement et rollback ;
- evaluation : qualité, robustesse, biais/équité selon usage, sécurité et régression ;
- feature/data access : données minimisées, finalité et lineage ;
- observabilité : latence, coût, erreurs, dérive et qualité.

L'IA n'est jamais l'autorité d'un fait métier. Elle ne crée pas une preuve absente. Pour l'entrepreneuriat, elle distingue faits, signaux, hypothèses, inconnues, fraîcheur et confiance ; elle ne garantit ni succès, financement, revenu ni conformité.

## 7. Flux structurants

Flux transactionnel : client → edge/API → service autoritatif → datastore privé → résultat.

Flux événementiel : service autoritatif → événement versionné → consommateurs/projections → Search/Knowledge/Analytics/IA selon contrat.

Flux Data : sources gouvernées → acquisition → provenance → qualité/validation → domaine autoritatif ou zone analytique selon nature → lakehouse/analytics.

Flux IA : demande autorisée → AI Gateway → retrieval/grounding → orchestration/model → verification → réponse avec provenance/limites.

Flux Orientation : PRF/SKL/ASM/EDU/CAR/LAB/ENT → ORI/REC → scénarios comparables → décision explicite du sujet/acteur autorisé.

Flux Entrepreneuriat : profil/compétences + signaux économiques + territoire + écosystème + financement → intelligence/opportunités → ORI/REC → projet/progression. Aucun signal économique n'est transformé en certitude.

## 8. Dépendances

Les dépendances synchrones sont réservées aux décisions nécessitant une réponse immédiate. Les propagations, projections et calculs non bloquants privilégient l'asynchronisme.

Interdictions :
- shared database entre bounded contexts ;
- chaîne synchrone longue pour une fonctionnalité critique ;
- boucle synchrone ORI ↔ REC ou IA ↔ domaine ;
- Analytics/Knowledge/Search/IA écrivant une vérité source ;
- pipeline analytique bloquant une transaction métier ;
- sponsoring influençant le ranking organique ;
- contournement CNS/IAM pour performance ;
- dépendance obligatoire à une capacité inactive sans mode de repli documenté.

## 9. Architecture hyperscale

La cible 15M impose horizontal scaling, partitionnement, caches lorsque compatibles, edge/CDN, backpressure, admission control, rate limiting, bulkheads, circuit breaking, files bornées, traitements async, isolation OLTP/OLAP/IA, réplication, observabilité de saturation et dégradation contrôlée.

Chaque microservice doit produire un Capacity Profile : concurrence, RPS/QPS, débit événements, payloads, volumes, croissance, latence, cacheabilité, partitionnement, ressources, autoscaling, limites, recovery et coûts.

La capacité est validée par paliers via load, stress, endurance, failover et recovery tests. 15M reste TARGET tant qu'une preuve représentative n'existe pas.

## 10. Déploiement et activation

Conçu ≠ implémenté ≠ déployé ≠ activé ≠ vérifié.

Une fonctionnalité peut être totalement conçue et rester inactive. L'activation utilise des mécanismes gouvernés et observables sans modifier l'ownership ni contourner sécurité/Privacy.

## 11. Gate TARGET-DESIGN-COMPLETE

La cible n'est COMPLETE que lorsque chaque domaine a ses capacités, chaque capacité son ownership, chaque microservice ses modules/fonctionnalités/use cases, ses données/contrats, ses NFR/Capacity Profile, son architecture technique, sa sécurité/résilience, ses tests et son plan d'implémentation.

La présence dans cette architecture ne confère aucun statut K5/K6 ni aucune preuve de performance.
