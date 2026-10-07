---
document_id: "YD-DOC-POL-PRF-002-PRF002-BACKUP-RESTORE"
title: "PRF002_BACKUP_RESTORE_POLICY — Sauvegarde et restauration autoritatives"
document_type: "microservice-policy"
document_role: "Établit les règles normatives de prf002 backup restore pour YD-MS-PRF-002."
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

# PRF002_BACKUP_RESTORE_POLICY — Sauvegarde et restauration autoritatives

> **Rôle du document**
> Établit les règles normatives de prf002 backup restore pour YD-MS-PRF-002.
> **Usage développement :** référence normative obligatoire pour les implémentations concernées.

Statut : `PREPROD-CANDIDATE`
Service : `YD-MS-PRF-002 — Education & Experience Profile`
Nature : `AUTH`
Criticité : `C1`
Références : `ADR-PRF002-RPO-RTO.md`, `PRF002_CONTINUITY_POLICY.md`

## 1. Objet

Cette politique traduit les objectifs de continuité de PRF-002 en exigences de sauvegarde, réplication, restauration temporelle, rétention, intégrité et isolement.

PRF-002 possède des données autoritatives qui ne sont pas entièrement reconstructibles depuis d'autres services. Sa récupération doit donc reposer sur ses propres mécanismes de protection.

## 2. Invariant d'indépendance de reprise

`PRF-001`, `EDU` et `SKL` ne sont jamais des dépendances de restauration de l'autorité PRF-002.

La procédure DR doit pouvoir restaurer et qualifier le datastore autoritatif avec ces trois services simultanément indisponibles.

Sont interdits pendant la récupération de l'autorité :

- reconstruction depuis la base PRF-001
- reconstruction depuis EDU
- reconstruction depuis SKL
- obligation de lire leurs API pour rendre le datastore restauré autoritatif
- promotion d'une de leurs projections comme source de vérité PRF-002

Ils peuvent intervenir après restauration pour la réconciliation fonctionnelle. Cette réconciliation n'est pas une condition de récupération de l'autorité.

## 3. Objectifs normatifs

| Objectif | Seuil |
|---|---:|
| RPO nominal | `≤ 15 minutes` |
| RTO incident courant | `≤ 1 heure` |
| RTO perte complète datastore | `≤ 4 heures` |
| RTO sinistre majeur | `≤ 8 heures` |
| corruption logique | restauration temporelle obligatoire |

Ces seuils restent soumis à confirmation BIA et à des tests mesurés avant production.

## 4. Protection en couches

La stratégie doit combiner plusieurs mécanismes indépendants :

1. disponibilité ou réplication pour les pannes courantes
2. mécanisme permettant le RPO ≤ 15 min
3. sauvegardes indépendantes du datastore actif
4. restauration temporelle
5. au moins une copie isolée du blast radius principal
6. contrôles d'intégrité
7. tests réels de restauration

Aucun mécanisme unique ne constitue la stratégie DR complète.

## 5. Réplication

La réplication sert la disponibilité et la réduction du temps de reprise. Elle ne remplace pas les sauvegardes.

Exigences :

- mesurer le retard de réplication
- empêcher deux autorités concurrentes non contrôlées
- auditer toute promotion de replica
- vérifier la cohérence avant promotion
- conserver une récupération indépendante si une suppression ou corruption se propage aux replicas
- respecter les contraintes de localisation et transfert applicables

Une réplication synchrone n'est pas imposée. Son adoption exige une décision technique justifiée.

## 6. Respect du RPO ≤ 15 minutes

La chaîne de protection doit récupérer un état dont la perte de mutations confirmées ne dépasse pas 15 minutes lors d'une perte complète du datastore actif.

Selon l'ADR technique, elle peut combiner snapshots cohérents, sauvegardes incrémentales, journal transactionnel archivé, point-in-time recovery, réplication ou mécanisme équivalent.

La fréquence d'un backup complet n'est pas le RPO.

Le RPO mesuré correspond à l'écart entre la dernière mutation confirmée avant l'incident et la dernière mutation effectivement récupérée.

Un écart supérieur à 15 minutes échoue le test nominal.

## 7. Restauration temporelle

PRF-002 doit pouvoir revenir à un état antérieur sain après corruption logique, suppression accidentelle ou erreur humaine.

Le mécanisme doit permettre :

- d'identifier un point antérieur à l'incident
- de restaurer ce point dans un environnement isolé
- de préserver les identifiants durables
- de préserver temporalité, versions, états de vérification et provenance
- de comparer l'état restauré à l'état courant lorsque possible
- de récupérer ou rejouer les mutations valides postérieures lorsque cela reste sûr
- d'exclure la mutation identifiée comme corrompue

La restauration ne réécrit pas silencieusement l'histoire métier.

## 8. Sauvegardes indépendantes

Les sauvegardes doivent réduire le blast radius du datastore actif.

Au minimum :

- credentials distincts des credentials applicatifs
- droits minimaux dédiés backup/restore
- stockage non monté comme stockage applicatif ordinaire
- identité applicative incapable de supprimer les sauvegardes
- protection contre suppression accidentelle ou malveillante
- chiffrement
- journalisation des accès et opérations
- contrôle d'intégrité avant utilisation

Une copie sur le même volume avec les mêmes droits de suppression que la base active n'est pas une sauvegarde indépendante.

## 9. Copie isolée

Au moins une copie de récupération possède un blast radius distinct du datastore actif et de sa réplication principale.

L'isolement couvre selon l'analyse de menace :

- rôle ou identité de gestion distinct
- contrôle de suppression distinct
- périmètre de défaillance distinct
- séparation documentée des secrets et clés
- accès réseau limité

L'ADR d'infrastructure décide de la topologie exacte sans lier cette politique à un fournisseur.

## 10. Chiffrement et clés

Les sauvegardes sont chiffrées au repos et protégées en transit.

Exigences :

- aucun secret ou clé dans Git
- rotation documentée
- accès minimal aux clés
- test réel de récupération des clés pendant un exercice restore
- stratégie empêchant qu'une rotation rende toutes les générations requises irrécupérables
- procédure de révocation en cas de compromission

Une sauvegarde dont la clé requise est irrécupérable est considérée inutilisable.

## 11. Intégrité

Toute génération utilisée pour une reprise doit être contrôlable.

Les contrôles couvrent :

- lisibilité
- format
- déchiffrement
- schéma attendu
- présence et cohérence des agrégats autoritatifs
- identifiants durables
- relations métier nécessaires
- temporalité
- provenance

Checksums ou mécanismes équivalents complètent les tests mais ne remplacent pas une restauration métier.

## 12. Rétention

Les durées de rétention doivent découler de la BIA, de la fenêtre de restauration temporelle, du risque de détection tardive, des obligations applicables, des instructions Privacy, des exigences probatoires autorisées et du coût de récupération.

Avant production, il faut définir :

- fenêtre de restauration temporelle
- rétention opérationnelle
- rétention des copies isolées
- conditions de purge
- destruction de fin de vie
- exceptions documentées

Les durées restent `TBD-PREPROD` jusqu'à validation BIA et conformité.

## 13. Privacy et données supprimées

Une sauvegarde peut contenir une donnée supprimée du datastore actif.

Après restauration :

1. restaurer techniquement un état cohérent
2. retrouver les décisions Privacy applicables depuis le point restauré
3. les réappliquer avant retour normal
4. enregistrer cette réapplication

Une restauration ne doit pas réactiver durablement une donnée dont la suppression ou restriction est applicable.

PRF-002 ne décide pas seul d'une exception de conservation.

## 14. Migrations

Une migration de datastore, format, version majeure ou technologie ne doit pas invalider silencieusement la capacité de reprise.

Avant une migration structurante :

- créer et vérifier une sauvegarde de référence
- tester la restauration vers la cible
- vérifier la compatibilité des historiques
- documenter rollback ou compensation
- conserver un chemin de restauration des générations encore requises

## 15. Procédure de restauration

Toute restauration C1 suit au minimum :

1. déclarer l'incident et l'état opérationnel
2. stopper ou isoler les mutations si nécessaire
3. qualifier l'incident
4. déterminer le dernier état sain
5. sélectionner une source vérifiée
6. restaurer dans un environnement isolé
7. contrôler schéma, agrégats, identifiants, temporalité et provenance
8. confirmer que PRF-001, EDU et SKL n'ont pas été requis pour récupérer l'autorité
9. mesurer le RPO
10. réappliquer les décisions Privacy nécessaires
11. empêcher toute autorité concurrente
12. promouvoir l'autorité restaurée
13. réconcilier ensuite les projections et dépendances fonctionnelles
14. rejouer les événements nécessaires de manière idempotente
15. mesurer le RTO
16. documenter les écarts
17. archiver les preuves

## 16. Critères de promotion

Un datastore restauré ne devient autoritatif que si :

- son intégrité technique est validée
- ses agrégats requis sont cohérents
- les identifiants durables sont préservés
- temporalité et provenance restent interprétables
- le point de restauration est connu
- les pertes sont quantifiées
- les obligations Privacy nécessaires sont traitées
- aucune autorité concurrente n'existe
- l'opérateur autorisé approuve la promotion
- la récupération n'a pas dépendu de PRF-001, EDU ou SKL

## 17. Tests obligatoires

Avant production :

- restauration complète depuis backup
- restauration temporelle avant corruption simulée
- backup récent volontairement inutilisable puis génération saine précédente
- restauration de la copie isolée
- récupération réelle des clés
- restauration avec PRF-001, EDU et SKL simultanément indisponibles
- mesure du RPO
- mesure des RTO applicables
- réconciliation postérieure des projections
- replay idempotent
- réapplication d'une décision Privacy postérieure au point restauré

## 18. Surveillance

Suivre au minimum :

- âge de la dernière sauvegarde exploitable
- retard du mécanisme contribuant au RPO
- succès et échecs des jobs
- intégrité des générations
- capacité de stockage
- erreurs de chiffrement et accès aux clés
- retard et échecs de réplication
- date du dernier restore réussi
- durée des restores
- RPO/RTO mesurés

Une protection trop ancienne pour respecter le RPO déclenche une alerte C1 selon la politique d'exploitation.

## 19. Séparation des pouvoirs

Avant production, attribuer :

- owner métier PRF-002
- owner opérationnel
- responsable backup
- responsable restore/DR
- responsable sécurité
- responsable Privacy/conformité
- suppléants

La même identité technique ne cumule pas sans justification les droits applicatifs complets, suppression de la base active, suppression des sauvegardes et gestion des clés.

## 20. Interdictions

Sont interdits :

- réplication comme seule sauvegarde
- seule copie sur le volume actif
- credentials applicatifs capables de supprimer les sauvegardes
- RPO déclaré depuis la seule fréquence planifiée d'un job
- RTO déclaré sans test chronométré
- restauration directement promue sans contrôle lorsqu'un environnement isolé est disponible
- PRF-001, EDU, SKL ou une projection aval comme autorité de secours
- reconstruction autoritative depuis PRF-001, EDU ou SKL
- réactivation silencieuse de données supprimées
- sauvegarde utilisée sans intégrité établie

## 21. Gates préproduction

Avant `ready-for-production` :

- `PRF002_BIA.md` validé
- topologie de sauvegarde décidée
- mécanisme démontrant RPO ≤ 15 min
- rétention validée
- restauration temporelle opérationnelle
- copie isolée opérationnelle
- chiffrement et récupération des clés testés
- contrôle d'intégrité validé
- surveillance et alertes définies
- responsabilités attribuées
- `PRF002_DR_TEST_PLAN.md` exécuté
- restauration réussie avec PRF-001, EDU et SKL indisponibles
- RPO et RTO mesurés conformes
- traitement Privacy après restore validé

Statut backup/restore : `TBD-PREPROD — POLICY DEFINED, IMPLEMENTATION AND PROOF REQUIRED`.