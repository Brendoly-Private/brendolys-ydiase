---
document_id: "YD-DOC-OPS-PRF-002-PRF002-DR-RUNBOOK"
title: "PRF002_DR_RUNBOOK — Runbook de reprise exécutable"
document_type: "operational-runbook"
document_role: "Définit la procédure opérationnelle applicable à YD-MS-PRF-002."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "operations"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# PRF002_DR_RUNBOOK — Runbook de reprise exécutable

> **Rôle du document**
> Définit la procédure opérationnelle applicable à YD-MS-PRF-002.
> **Usage développement :** référence opérationnelle obligatoire pour l’implémentation et l’exploitation concernées.

Statut : `TBD-IMPLEMENTATION — PROCEDURE DEFINED, TECHNOLOGY COMMANDS TO BIND`
Service : `YD-MS-PRF-002 — Education & Experience Profile`
Criticité : `C1`

Références : `PRF002_DR_TEST_PLAN.md`, `PRF002_DR_EVIDENCE_MATRIX.md`, `PRF002_BACKUP_RESTORE_POLICY.md`, `PRF002_CONTINUITY_POLICY.md`, `PRF002_NOMINATION_MATRIX.md`.

## 1. Objet

Ce runbook définit la séquence opérationnelle de reprise PRF-002. Les étapes de décision et de contrôle sont normatives. Les commandes propres au datastore, à l'orchestrateur, au backup et au stockage restent `TBD-IMPLEMENTATION` jusqu'à adoption des technologies correspondantes.

Aucune commande fictive ne doit être introduite pour donner l'apparence d'un runbook exécutable.

## 2. Conditions d'utilisation

Déclencher ce runbook pour :
- perte complète du datastore actif ;
- corruption logique nécessitant PITR ;
- suppression critique ;
- perte du périmètre principal ;
- backup récent inutilisable ;
- compromission nécessitant reconstruction depuis état sain ;
- exercice DR planifié.

Pour une simple panne d'instance sans perte d'autorité, utiliser le runbook d'incident courant lorsqu'il sera lié à l'implémentation.

## 3. Rôles

- Incident/Recovery lead : `OWN-PRF2-DR`
- Exploitabilité : `OWN-PRF2-OPS`
- Autorité métier : `OWN-PRF2-BUS`
- Sécurité conditionnelle/obligatoire en compromission : `OWN-SEC`
- Privacy conditionnelle : `OWN-PRIV`
- Infrastructure DR : `OWN-INFRA`
- Backup : `OWN-PRF2-BKP`

Si les rôles obligatoires ne peuvent être assurés selon la matrice de nomination, ne pas promouvoir vers `NORMAL-RESTORED`.

## 4. Pré-check

Avant toute action destructive :
1. créer `EXECUTION-ID` ;
2. enregistrer l'heure de début ;
3. identifier le scénario DR ;
4. ouvrir le dossier de preuves ;
5. confirmer les identités des opérateurs ;
6. capturer l'état actuel sans exposer de secret ;
7. confirmer si l'incident implique corruption/compromission/Privacy ;
8. geler les changements non nécessaires ;
9. déterminer si les mutations doivent être bloquées ;
10. passer à `RECOVERY` ou `QUARANTINE` selon la politique.

STOP si l'équipe ne peut pas distinguer un incident technique d'une compromission potentielle : traiter comme compromission jusqu'à qualification Security.

## 5. Isolation de l'autorité

Avant restore complet :
1. empêcher les écritures sur l'autorité défaillante ;
2. empêcher une promotion concurrente ;
3. vérifier qu'aucune autre instance ne peut accepter des mutations autoritatives ;
4. documenter le mécanisme d'isolation ;
5. en compromission, préserver les éléments nécessaires à l'analyse avant destruction.

Critère : une seule autorité PRF-002 peut être promue.

## 6. Sélection du point de récupération

Collecter :
- dernière mutation confirmée connue ;
- générations disponibles ;
- état d'intégrité des backups ;
- journal/PITR disponible ;
- point de corruption connu ou estimé ;
- décisions Privacy susceptibles d'être postérieures au point choisi.

Choisir le point le plus récent démontré sain compatible avec le scénario.

Pour corruption/compromission, la sécurité de l'état prime sur le chronomètre.

Enregistrer la justification du point choisi.

## 7. Préparation de la cible

1. préparer un environnement de restauration isolé ;
2. utiliser l'identité de restore dédiée ;
3. vérifier stockage, capacité, réseau, certificats et clés nécessaires ;
4. interdire l'exposition utilisateur ;
5. vérifier que PRF-001/EDU/SKL ne sont pas requis pour restaurer PRF-002 ;
6. préparer les contrôles d'intégrité.

Commandes techniques : `TBD-IMPLEMENTATION`.

## 8. Restore datastore

Séquence normative :
1. initialiser la cible vide/contrôlée ;
2. restaurer la génération sélectionnée ;
3. appliquer le journal/PITR jusqu'au point choisi si applicable ;
4. ne pas ouvrir les écritures métier ;
5. capturer logs et timestamps ;
6. vérifier la réussite technique ;
7. en cas d'échec, ne pas bricoler l'état restauré : qualifier l'échec et sélectionner la génération saine suivante selon politique.

Commandes : `TBD-IMPLEMENTATION`.

## 9. Contrôles d'intégrité

Exécuter avant promotion :
- comptages/cohérences définis pour les agrégats ;
- IDs durables ;
- relations ;
- temporalité/versions ;
- verification states ;
- provenance refs ;
- contraintes ;
- migrations ;
- détection de doublons.

Résultat obligatoire : `INTEGRITY-PASS` ou arrêt de la promotion.

Les requêtes/scripts exacts seront ajoutés avec le schéma physique : `TBD-IMPLEMENTATION`.

## 10. Calcul RPO

Enregistrer :
- `T_confirmed` = timestamp dernière mutation confirmée avant incident ;
- `T_recovered` = timestamp dernière mutation autoritative récupérée.

Calcul :
`RPO = T_confirmed - T_recovered`

Pour les scénarios soumis au RPO nominal, PASS si `RPO ≤ 15 min`.

Si la dernière mutation récupérée est postérieure/égale à la dernière mutation confirmée attendue, enregistrer RPO effectif 0 selon la sémantique du test.

## 11. Privacy post-restore

Avant réouverture :
1. identifier les décisions Privacy postérieures au restore point ;
2. les réappliquer ;
3. vérifier les suppressions/restrictions ;
4. enregistrer les actions ;
5. obtenir `OWN-PRIV` lorsque le scénario l'exige.

Aucune restauration ne doit durablement réactiver une donnée interdite.

## 12. Test d'autonomie PRF-001/EDU/SKL

Pour DR-009 :
1. bloquer réseau/API vers PRF-001, EDU et SKL ;
2. conserver la preuve du blocage ;
3. exécuter sections 4 à 10 ;
4. vérifier les logs réseau ;
5. refuser tout mécanisme ayant reconstruit l'autorité depuis ces services ;
6. autoriser des références externes temporairement non résolues ;
7. restaurer l'autorité PRF-002 ;
8. seulement ensuite, lorsque les dépendances reviennent, passer à `RECONCILIATION`.

Critère absolu : PRF-002 doit retrouver son autorité sans PRF-001, EDU et SKL.

## 13. Validation applicative

Après intégrité datastore :
1. déployer/démarrer la version compatible ;
2. vérifier migrations ;
3. exécuter health checks ;
4. exécuter readiness checks ;
5. tester lecture contrôlée ;
6. tester mutation synthétique autorisée si le scénario permet l'écriture ;
7. vérifier audit/observabilité ;
8. conserver les preuves.

Commandes Kubernetes/K3s, endpoints et scripts : `TBD-IMPLEMENTATION`.

## 14. Réconciliation

Après restauration de l'autorité :
- republier/rejouer uniquement selon contrats idempotents ;
- réconcilier projections ;
- résoudre références EDU/SKL lorsque disponibles ;
- rétablir interactions PRF-001 selon contrat ;
- vérifier absence de doublons ;
- mesurer le lag ;
- ne jamais faire d'une projection l'autorité de PRF-002.

La réconciliation n'est jamais un prérequis à la restauration de l'autorité.

## 15. Promotion

Avant `NORMAL-RESTORED`, vérifier :
- restore technique PASS ;
- intégrité PASS ;
- RPO/RTO mesurés ;
- readiness PASS ;
- aucune autorité concurrente ;
- Privacy PASS si applicable ;
- Security PASS si applicable ;
- preuves enregistrées.

Signatures minimales :
- DR ;
- Owner métier ;
- Operations.

Ajouter Security pour compromission/copie isolée/rupture d'isolement et Privacy lorsque requis.

## 16. Réouverture progressive

1. rétablir lecture selon politique ;
2. rétablir écritures uniquement après promotion autorisée ;
3. surveiller erreurs, latence, doublons et backlog ;
4. surveiller projections/réconciliation ;
5. conserver une fenêtre de surveillance renforcée ;
6. documenter toute anomalie.

Seuils précis de surveillance : `TBD-PREPROD`.

## 17. Abort / rollback

Arrêter la promotion si :
- intégrité FAIL ;
- backup suspect ;
- split-brain possible ;
- clé nécessaire indisponible/non fiable ;
- Privacy bloquante ;
- Security refuse l'état ;
- migration incompatible ;
- preuve insuffisante pour qualifier le point sain.

Action :
1. maintenir `RECOVERY` ou `QUARANTINE` ;
2. préserver les preuves ;
3. isoler la cible rejetée ;
4. sélectionner une autre génération/point sain ;
5. recommencer avec nouvelle trace d'exécution ou sous-exécution liée.

Ne jamais corriger silencieusement une restauration échouée en production.

## 18. Cas backup récent inutilisable

1. marquer la génération comme non éligible sans la détruire avant analyse ;
2. enregistrer le motif ;
3. sélectionner la génération saine précédente ;
4. restaurer ;
5. recalculer le RPO réel ;
6. escalader tout dépassement ;
7. ouvrir action corrective sur la chaîne de backup.

## 19. Cas sinistre majeur

1. déclarer perte du périmètre principal ;
2. activer le périmètre DR/copie isolée ;
3. vérifier indépendance du blast radius ;
4. restaurer selon sections précédentes ;
5. cible : RPO ≤15m et RTO ≤8h ;
6. faire valider Infrastructure + Security ;
7. ne pas utiliser le MTPD 24h comme extension du RTO.

## 20. Cas compromission

1. `QUARANTINE` ;
2. bloquer mutations ;
3. révoquer/faire tourner les accès affectés selon procédure Security ;
4. préserver preuves ;
5. identifier dernier point sain ;
6. restaurer dans environnement propre ;
7. contrôler identités, clés et réseau ;
8. valider Security avant promotion.

Les commandes de rotation/révocation restent dans les runbooks Security dédiés à l'implémentation.

## 21. Clôture

Après stabilisation :
1. finaliser le manifest de preuve ;
2. joindre logs/mesures/résultats ;
3. enregistrer RPO/RTO ;
4. classer findings ;
5. affecter owner + échéance ;
6. obtenir approbations ;
7. mettre à jour le registre d'exécution ;
8. mettre à jour BIA/Assumption Register si une hypothèse est invalidée ;
9. organiser retest si nécessaire.

## 22. Checklist opérateur

- [ ] Execution ID créé
- [ ] scénario identifié
- [ ] rôles présents
- [ ] dossier de preuve ouvert
- [ ] état RECOVERY/QUARANTINE appliqué
- [ ] autorité défaillante isolée
- [ ] point sain sélectionné
- [ ] cible isolée préparée
- [ ] restore exécuté
- [ ] intégrité PASS
- [ ] RPO calculé
- [ ] RTO calculé
- [ ] Privacy réappliquée si nécessaire
- [ ] Security validée si nécessaire
- [ ] autonomie PRF-001/EDU/SKL prouvée si DR-009
- [ ] readiness PASS
- [ ] réconciliation contrôlée
- [ ] signatures obtenues
- [ ] NORMAL-RESTORED autorisé
- [ ] preuves archivées
- [ ] findings affectés

## 23. Liaison technologique requise

Avant première exécution préproduction, compléter dans ce runbook ou dans des runbooks enfants versionnés :
- commandes exactes du datastore ;
- commandes backup/restore/PITR ;
- commandes orchestrateur ;
- endpoints health/readiness ;
- requêtes d'intégrité ;
- chemins/log sources ;
- procédure de clés ;
- procédure d'isolation réseau ;
- procédure de promotion/failover.

Ces éléments ne peuvent être marqués `READY-TO-EXECUTE` qu'après décision d'architecture et test en environnement non production.

Statut actuel : `RUNBOOK-LOGIC-READY / TECHNOLOGY-BINDING-REQUIRED`.
