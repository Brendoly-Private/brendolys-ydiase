---
document_id: "YD-DOC-OPS-PRF-002-PRF002-SENSITIVE-ROLE-PRACTICAL-QUALIFICATION"
title: "PRF002_SENSITIVE_ROLE_PRACTICAL_QUALIFICATION"
document_type: "operations-reference"
document_role: "Documente la qualification pratique des rôles sensibles du périmètre PRF-002."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "operations"
---

# PRF002_SENSITIVE_ROLE_PRACTICAL_QUALIFICATION

> **Rôle du document**
> Documente la qualification pratique des rôles sensibles du périmètre PRF-002.
> **Usage développement :** référence de support pour la préparation opérationnelle.

Statut : PREPROD-CANDIDATE / QUALIFICATION-REQUIRED
Service : YD-MS-PRF-002 — Education & Experience Profile
Criticité : C1
Références : PRF002_NOMINATION_MATRIX.md, PRF002_NOMINATION_REGISTER.md, PRF002_CONTINUITY_POLICY.md, PRF002_BACKUP_RESTORE_POLICY.md

## 1. Objet

Ce document définit la qualification pratique obligatoire avant qu'un titulaire ou suppléant des rôles DR, Operations, Backup, Security ou Infrastructure puisse assurer seul une astreinte PRF-002.

Une nomination administrative ne vaut pas qualification opérationnelle.

## 2. Règle d'habilitation

Pour chacun des cinq rôles sensibles, la personne doit :
1. être nominativement désignée ;
2. satisfaire les compétences documentées ;
3. exécuter ou conduire l'exercice minimal de son rôle ;
4. être observée par une personne habilitée distincte ;
5. satisfaire tous les critères bloquants ;
6. disposer d'un rapport et des preuves ;
7. recevoir une validation de qualification.

Avant cela, son statut ne peut dépasser NOMINATED. Après réussite : QUALIFIED. Le passage ACTIVE exige en plus des habilitations techniques cohérentes.

## 3. Exercices obligatoires

| Rôle | Exercice pratique minimal | Observateur/validateur indépendant | Critères PASS bloquants |
|---|---|---|---|
| OWN-PRF2-DR | Restaurer PRF-002 dans un environnement isolé à partir d'une sauvegarde autorisée, mesurer RPO/RTO, contrôler l'intégrité et conduire jusqu'à l'état de reprise prévu | Operations ou autre responsable DR qualifié ; Owner métier pour intégrité métier | runbook respecté ; autorité unique ; intégrité contrôlée ; RPO/RTO calculés ; aucune reconstruction depuis PRF-001/EDU/SKL ; preuves complètes |
| OWN-PRF2-OPS | Gérer une panne applicative simulée : détection, qualification, changement d'état, communication, rollback/recovery et readiness | DR ou responsable Operations qualifié distinct | incident détecté ; état correct ; aucune écriture interdite ; restauration du service ; readiness valide ; chronologie et décisions tracées |
| OWN-PRF2-BKP | Identifier une génération de backup, vérifier son état, déclencher un restore de test et démontrer que les données restaurées sont exploitables | DR ou Operations qualifié distinct | backup identifiable ; intégrité vérifiée ; restore réussi ; dernière mutation récupérée mesurable ; aucune simple réussite de job acceptée comme preuve |
| OWN-SEC | Traiter une suspicion de compromission simulée : passage QUARANTINE, confinement, préservation des preuves, contrôle des accès et critères de réouverture | autre responsable Security habilité ou contrôle indépendant désigné ; DR pour reprise | mutations stoppées ; périmètre isolé ; preuves préservées ; accès privilégiés tracés ; aucun état non qualifié promu ; décision de réouverture documentée |
| OWN-INFRA | Simuler l'indisponibilité du périmètre principal et rendre disponible l'infrastructure de reprise/copie isolée sans dépendance au même blast radius | Security + DR | chemin de reprise disponible ; accès distincts ; copie isolée exploitable ; dépendances critiques identifiées ; absence de dépendance cachée au périmètre déclaré perdu |

## 4. Scénario renforcé DR obligatoire

Le candidat DR doit réussir au moins un exercice où PRF-001, EDU et SKL sont simultanément indisponibles pendant toute la restauration de l'autorité PRF-002.

PASS exige :
- aucune lecture de leurs bases ;
- aucune API requise pour reconstruire PRF-002 ;
- aucune projection aval utilisée comme nouvelle autorité ;
- restauration de l'autorité PRF-002 depuis sa propre chaîne de recovery ;
- références externes pouvant rester non résolues jusqu'à RECONCILIATION ;
- preuve RPO/RTO et intégrité conservée.

## 5. Preuves à conserver

Chaque exercice produit :
- ID d'exercice ;
- rôle et personne évaluée ;
- date et environnement ;
- version du runbook ;
- scénario injecté ;
- heures de début/fin ;
- mesures RPO/RTO si applicables ;
- logs et contrôles d'intégrité pertinents ;
- actions effectuées ;
- écarts observés ;
- résultat PASS ou FAIL ;
- identité de l'observateur ;
- approbations requises ;
- actions correctives ;
- référence du rapport.

Les preuves sensibles ne sont pas publiées dans une documentation publique. Le registre conserve uniquement les références nécessaires.

## 6. Registre prêt à remplir

| Rôle | Titulaire/suppléant évalué | Exercice ID | Date | Observateur | Résultat | Rapport/preuve | Qualification |
|---|---|---|---|---|---|---|---|
| OWN-PRF2-DR | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | PENDING | À RENSEIGNER | NOT-QUALIFIED |
| OWN-PRF2-OPS | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | PENDING | À RENSEIGNER | NOT-QUALIFIED |
| OWN-PRF2-BKP | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | PENDING | À RENSEIGNER | NOT-QUALIFIED |
| OWN-SEC | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | PENDING | À RENSEIGNER | NOT-QUALIFIED |
| OWN-INFRA | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | PENDING | À RENSEIGNER | NOT-QUALIFIED |

Chaque suppléant est évalué séparément : la réussite du titulaire ne qualifie pas automatiquement son suppléant.

## 7. Echec et requalification

FAIL interdit QUALIFIED. Les écarts bloquants sont corrigés puis l'exercice concerné est rejoué.

Une requalification est requise après une modification majeure du mécanisme de backup/restore, de l'infrastructure DR, du modèle IAM/sécurité ou du runbook affectant directement le rôle, ainsi qu'après un incident C1 démontrant que la compétence précédemment validée n'est plus suffisante.

## 8. Gate VERIFIED

VERIFIED est bloqué si l'un des rôles sensibles requis pour les scénarios de production :
- n'a pas de titulaire qualifié ;
- n'a pas de suppléant qualifié ;
- ne possède pas de preuve d'exercice ;
- a échoué à son dernier exercice bloquant sans correction validée.

Statut actuel : QUALIFICATION-PENDING — PRACTICAL EXERCISES DEFINED, EXECUTION REQUIRED.
