---
document_id: "YD-DOC-POL-PRF-002-PRF002-CONTINUITY"
title: "PRF002_CONTINUITY_POLICY — Continuité et mode dégradé"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de prf002 continuity pour YD-MS-PRF-002."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: false
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "policy"
---

# PRF002_CONTINUITY_POLICY — Continuité et mode dégradé

> **Rôle du document**
> Établit les règles normatives de prf002 continuity pour YD-MS-PRF-002.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `PREPROD-CANDIDATE`
Service : `YD-MS-PRF-002 — Education & Experience Profile`
Nature : `AUTH`
Criticité : `C1`
Référence : `ADR-PRF002-RPO-RTO.md`

## 1. Objet

Cette politique définit le comportement de PRF-002 lorsqu'une panne, une restauration, une corruption, une indisponibilité de dépendance ou une opération DR empêche son fonctionnement nominal.

Le principe prioritaire est de préserver l'autorité et l'intégrité de l'historique individuel. Le mode dégradé ne doit jamais fabriquer une continuité apparente en acceptant des mutations dont la cohérence, la finalité ou l'autorisation ne peuvent pas être établies.

## 2. Principes normatifs

- PRF-002 reste l'unique autorité YDIASE de ses agrégats pendant une reprise.
- aucune projection, cache, index, export ou service consommateur ne prend son autorité pendant l'incident.
- PRF-001 ne devient jamais propriétaire de l'historique PRF-002.
- une donnée incertaine n'est pas publiée comme état confirmé.
- les opérations de lecture et d'écriture sont traitées séparément.
- une dépendance indisponible ne bloque PRF-002 que si elle est nécessaire à la sécurité, à la légalité ou à la validité de l'opération demandée.
- les opérations pouvant attendre utilisent un mécanisme explicite de reprise ou sont refusées. Aucun buffer implicite non gouverné n'est autorisé.
- une décision Privacy obligatoire impossible à vérifier entraîne `fail-closed` pour la mutation concernée.
- les modes dégradés sont observables, auditables et réversibles.

## 3. États opérationnels

PRF-002 utilise au minimum les états suivants :

| État | Sens | Écritures | Lectures |
|---|---|---|---|
| `NORMAL` | autorité saine et dépendances requises disponibles | autorisées | autorisées |
| `DEGRADED-READ` | autorité lisible mais certaines dépendances indisponibles | limitées selon matrice | autorisées avec indicateur de fraîcheur/contexte si nécessaire |
| `READ-ONLY` | autorité jugée saine mais mutations suspendues | interdites | autorisées |
| `RECOVERY` | restauration ou réconciliation en cours | interdites par défaut | interdites ou limitées à une copie explicitement qualifiée |
| `QUARANTINE` | corruption ou compromission suspectée | interdites | interdites par défaut |
| `RECONCILIATION` | autorité restaurée, consommateurs/projections en rattrapage | contrôlées selon runbook | autorisées depuis l'autorité restaurée |
| `NORMAL-RESTORED` | contrôles de reprise terminés | autorisées | autorisées |

Le passage entre états produit un événement d'exploitation/audit et possède un responsable opérationnel identifiable.

## 4. Mode dégradé minimal

Le MBCO de PRF-002 consiste à :

1. protéger le dernier état autoritatif reconnu sain
2. maintenir les lectures de cet état lorsque leur sécurité et leur cohérence sont établies
3. suspendre les mutations dont les préconditions ne peuvent pas être vérifiées
4. permettre au reste de YDIASE de continuer sans PRF-002 lorsqu'il n'en dépend pas
5. exposer un statut explicite aux consommateurs afin qu'ils sachent si PRF-002 est normal, en lecture seule, en reprise ou indisponible
6. conserver les demandes différables uniquement via un mécanisme durable, idempotent et gouverné lorsqu'un contrat l'autorise
7. empêcher une projection aval de devenir l'autorité de secours

## 5. Opérations autorisées par état

| Opération | DEGRADED-READ | READ-ONLY | RECOVERY | QUARANTINE | RECONCILIATION |
|---|---|---|---|---|---|
| lire son historique sain | oui | oui | non par défaut | non | oui |
| lire une projection minimale déjà publiée | consommateur selon fraîcheur | consommateur selon fraîcheur | consommateur selon politique | non si intégrité suspecte | oui avec fraîcheur |
| ajouter EducationRecord | conditionnel | non | non | non | conditionnel |
| ajouter ExperienceRecord | conditionnel | non | non | non | conditionnel |
| corriger un historique | conditionnel | non | non | non | conditionnel |
| ajouter/détacher une preuve | conditionnel | non | non | non | conditionnel |
| modifier un état de vérification | conditionnel strict | non | non | non | conditionnel strict |
| export utilisateur | oui si données et autorisations fiables | oui si fiable | non | non | oui après contrôle |
| suppression/rectification Privacy | priorité selon instruction CNS | enregistrer/traiter selon runbook | réappliquer avant retour normal | conserver instruction hors zone compromise | priorité avant normalisation |
| publication d'événements métier | uniquement mutations validées | non | non | non | replay/republication contrôlés |

`Conditionnel` signifie que toutes les dépendances nécessaires à l'opération sont disponibles et que le datastore PRF-002 est reconnu sain. À défaut, l'opération est refusée ou différée selon le contrat.

## 6. Dépendances et caractère bloquant

### 6.1 BRENDOLYS Identity

Rôle : authentifier le sujet, l'opérateur ou le workload.

- bloquant pour toute nouvelle opération authentifiée si aucun contexte d'identité valide ne peut être établi
- une session/token déjà validé peut être accepté uniquement selon les règles IAM et sa validité cryptographique
- aucune authentification locale de secours n'est créée dans PRF-002
- une panne IAM ne justifie jamais de contourner l'autorisation

### 6.2 CNS-001 — Consent / Privacy

Rôle : finalités, restrictions, demandes Privacy et instructions applicables.

- bloquant pour toute mutation nécessitant une décision Privacy non disponible
- `fail-closed` lorsque la décision est obligatoire
- une décision CNS déjà matérialisée localement ne peut être utilisée que si son contrat autorise cette projection, sa fraîcheur et sa portée
- les instructions d'effacement ou restriction reçues pendant la reprise doivent être réappliquées avant retour à `NORMAL`

### 6.3 EDU

Rôle : institutions, programmes, qualifications et autres références éducatives autoritatives.

- non bloquant pour lire un historique déjà enregistré
- non bloquant pour restaurer PRF-002
- bloquant pour créer ou confirmer une nouvelle relation qui exige la validation d'une référence EDU et pour laquelle aucune projection autorisée suffisamment fraîche n'existe
- une panne EDU ne provoque jamais la suppression ou l'invalidation automatique d'un historique existant

### 6.4 SKL

Rôle : taxonomies et références de compétences nécessaires à certains usages.

- non bloquant pour restaurer ou lire l'historique PRF-002
- bloquant uniquement pour une opération qui exige une référence SKL actuelle et ne dispose pas d'une projection autorisée valide
- PRF-002 ne crée pas de compétence autoritative en remplacement de SKL

### 6.5 DAT-003 / provenance

Rôle : références de provenance selon les contrats définis.

- non bloquant pour la restauration physique de l'autorité PRF-002 si les références de provenance déjà enregistrées restent intactes
- potentiellement bloquant pour accepter une nouvelle preuve ou une nouvelle source lorsqu'une provenance gouvernée est obligatoire
- une indisponibilité DAT ne permet pas de supprimer la provenance requise d'une nouvelle mutation

### 6.6 PRF-001

Rôle : profil courant.

- non bloquant pour backup, restore et autorité PRF-002
- non bloquant pour lire l'historique par son propriétaire si l'identité et l'autorisation sont établies autrement selon les contrats
- bloquant uniquement pour une opération dont le contrat exige explicitement une donnée courante PRF-001
- aucune lecture directe de sa base n'est autorisée pendant un incident

### 6.7 Edge/API management

- une panne edge peut rendre PRF-002 inaccessible aux utilisateurs sans rendre son datastore indisponible
- les opérations internes de DR restent possibles via les canaux opérationnels autorisés
- aucun endpoint temporaire non gouverné n'est exposé pour contourner l'edge

## 7. Matrice des dépendances bloquantes

| Dépendance | Lecture historique existant | Nouvelle déclaration | Correction | Vérification | Restore | Retour NORMAL |
|---|---|---|---|---|---|---|
| BRENDOLYS Identity | oui pour accès utilisateur | oui | oui | oui | non pour restauration technique | oui pour service utilisateur |
| CNS-001 | selon finalité | oui si décision requise | oui si décision requise | oui si décision requise | non pour restauration technique | oui pour réapplication Privacy |
| EDU | non | conditionnel | conditionnel | conditionnel | non | non si références conservées |
| SKL | non | conditionnel | conditionnel | conditionnel | non | non |
| DAT/provenance | non si provenance locale intacte | conditionnel | conditionnel | conditionnel | non | non, sauf réconciliation requise |
| PRF-001 | non | conditionnel selon contrat | conditionnel | non par défaut | non | non |
| datastore PRF-002 sain | oui | oui | oui | oui | cible du restore | oui |

## 8. Politique des écritures pendant reprise

En `RECOVERY` et `QUARANTINE`, les écritures métier sont interdites par défaut.

Une file d'attente de commandes n'est autorisée que si le Contract Registry définit :

- identifiant idempotent
- durée maximale de conservation
- identité du demandeur
- finalité et autorisation conservées de manière vérifiable
- comportement si la commande devient invalide avant replay
- ordre requis
- déduplication
- politique Privacy
- dead-letter ou traitement manuel

Sans ce contrat, l'appel reçoit une réponse explicite d'indisponibilité et le client doit réessayer selon la politique publiée.

## 9. Lectures et fraîcheur

Une lecture pendant `DEGRADED-READ` ou `READ-ONLY` doit indiquer au consommateur, directement ou par métadonnée contractuelle :

- état opérationnel du service
- version ou timestamp de l'état retourné lorsque nécessaire
- niveau de fraîcheur si une projection est utilisée
- interdiction de considérer une projection comme nouvelle autorité

Une lecture est interdite si l'intégrité de l'état est suspecte.

## 10. Corruption et compromission

En cas de corruption ou compromission suspectée, PRF-002 passe en `QUARANTINE`.

La priorité devient :

1. stopper les mutations
2. isoler le périmètre
3. préserver les preuves techniques nécessaires
4. identifier le dernier état sain
5. restaurer dans un environnement contrôlé
6. vérifier intégrité, temporalité et provenance
7. réappliquer les décisions Privacy
8. réconcilier les consommateurs
9. rouvrir progressivement

Le RTO ne justifie jamais une remise en service d'un état dont l'intégrité n'est pas établie.

## 11. Reconciliation après restauration

Après restore, PRF-002 entre en `RECONCILIATION`.

Avant `NORMAL-RESTORED` :

- les agrégats restaurés sont contrôlés
- les projections aval sont comparées à l'autorité restaurée
- les consommateurs obsolètes sont resynchronisés
- les événements nécessaires sont rejoués ou republiés de façon idempotente
- aucune projection aval n'écrase PRF-002
- les décisions Privacy reçues depuis le point restauré sont réappliquées
- les commandes différées sont revalidées avant exécution
- les anomalies disposent d'un owner et d'un traitement

## 12. Continuité du reste de YDIASE

Les consommateurs de PRF-002 doivent documenter leur propre comportement lorsque PRF-002 est indisponible.

Ils ne doivent pas transformer une dépendance fonctionnelle en dépendance de disponibilité globale. Une fonctionnalité qui n'a pas besoin de l'historique personnel continue à fonctionner.

Les recommandations, matching ou autres fonctions qui nécessitent PRF-002 doivent soit :

- utiliser une projection explicitement autorisée avec fraîcheur connue
- produire un résultat limité clairement identifié si le contrat le permet
- suspendre la fonction

Elles ne doivent pas inventer ou compléter silencieusement l'historique manquant par une IA.

## 13. Communications opérationnelles

Le runbook doit définir :

- qui déclare l'incident
- qui autorise le passage en `READ-ONLY`, `RECOVERY` ou `QUARANTINE`
- qui autorise le retour à `NORMAL`
- comment les consommateurs sont informés
- comment l'état est exposé aux systèmes dépendants
- quelles informations peuvent être communiquées aux utilisateurs sans exposer de données sensibles ou de détails de sécurité

Les personnes nominatives restent `TBD-PREPROD`. Les responsabilités fonctionnelles doivent être attribuées avant production.

## 14. Critères de sortie du mode dégradé

Le retour à `NORMAL` exige :

- datastore autoritatif déclaré sain
- intégrité des agrégats vérifiée
- dépendances bloquantes disponibles ou projections contractuellement valides
- décisions Privacy réappliquées
- replay/réconciliation terminés au seuil défini
- absence d'anomalie C1 non traitée
- health/readiness conformes
- validation opérationnelle enregistrée
- preuves de reprise archivées

## 15. Tests obligatoires

Avant production, le plan DR doit tester au minimum :

- passage NORMAL → READ-ONLY
- panne EDU avec lecture historique maintenue
- panne CNS avec mutation sensible refusée
- panne IAM sans contournement local
- perte complète du datastore et passage RECOVERY
- corruption simulée et QUARANTINE
- restauration avec PRF-001 indisponible
- restauration avec EDU ou SKL indisponible
- réconciliation de projections
- replay idempotent
- commande différée devenue invalide
- réapplication d'une instruction Privacy après restore
- retour contrôlé à NORMAL

## 16. Gates ouverts

Avant `ready-for-production` :

- confirmer MTPD, MDL et MBCO dans `PRF002_BIA.md`
- finaliser les contrats de projections utilisables en mode dégradé
- définir les commandes différables ou décider qu'aucune ne l'est
- attribuer les responsabilités opérationnelles
- définir les seuils de fraîcheur par projection
- exécuter `PRF002_DR_TEST_PLAN.md`
- démontrer les RPO/RTO de `ADR-PRF002-RPO-RTO.md`

Statut de continuité : `TBD-PREPROD — POLICY DEFINED, PROOF REQUIRED`.