# PRF002_DR_TEST_PLAN — Disaster Recovery Test Plan

Statut : `TBD-PREPROD — TEST PLAN DEFINED, EXECUTION AND EVIDENCE REQUIRED`
Service : `YD-MS-PRF-002 — Education & Experience Profile`
Nature : `AUTH`
Criticité : `C1`

Références :
- `ADR-PRF002-RPO-RTO.md`
- `AUTONOMY_PROFILE.md`
- `PRF002_CONTINUITY_POLICY.md`
- `PRF002_BACKUP_RESTORE_POLICY.md`
- `PRF002_BIA.md`
- `PRF002_BIA_ASSUMPTION_REGISTER.md`
- `PRF002_NOMINATION_MATRIX.md`
- `PRF002_NOMINATION_REGISTER.md`
- `PRF002_SENSITIVE_ROLE_PRACTICAL_QUALIFICATION.md`

## 1. Objet

Ce plan définit les exercices nécessaires pour démontrer que PRF-002 peut préserver ou restaurer son autorité dans les objectifs de continuité approuvés ou candidats.

Une configuration de backup, un statut de job réussi ou une réplication saine ne constitue pas une preuve DR. La preuve exige une récupération exécutée, mesurée et contrôlée.

## 2. Objectifs à démontrer

| Objectif | Cible |
|---|---|
| RPO nominal | ≤ 15 min |
| RTO incident courant | ≤ 1 h |
| RTO perte complète datastore | ≤ 4 h |
| RTO sinistre majeur | ≤ 8 h |
| MTPD | CANDIDATE = 24 h ; approbation séparée via MTPD-24H-APPROVED |
| corruption logique | restauration temporelle/PITR obligatoire selon mécanisme retenu |
| autonomie | restauration PRF-002 sans PRF-001, EDU ou SKL |

Le MTPD de 24 h n'étend jamais le RTO majeur de 8 h.

## 3. Invariant de récupération

PRF-001, EDU et SKL sont des dépendances fonctionnelles de certaines opérations de PRF-002, jamais des dépendances de récupération de son autorité.

Le plan doit démontrer une restauration avec PRF-001, EDU et SKL simultanément indisponibles pendant toute la phase de récupération de l'autorité.

Sont interdits pour reconstruire PRF-002 :
- lecture de leurs bases ;
- appel API obligatoire ;
- consommation d'un état externe comme substitut d'autorité ;
- promotion d'une projection aval comme nouvelle autorité PRF-002.

Après restauration, des références externes peuvent rester non résolues ou obsolètes jusqu'à `RECONCILIATION`.

## 4. Environnement de test

Les exercices sont exécutés dans un environnement représentatif de préproduction, isolé de la production.

Le test doit documenter :
- version applicative ;
- version schéma/migrations ;
- mécanisme de stockage ;
- mécanisme de sauvegarde ;
- mécanisme de restauration temporelle ;
- volume de données ;
- profil de charge ;
- identités techniques ;
- réseau et dépendances ;
- version des runbooks.

Utiliser des données synthétiques ou non sensibles lorsque possible. Toute donnée sensible utilisée suit les politiques de protection applicables.

## 5. Jeu de données de contrôle

Le jeu de test doit couvrir au minimum :
- `EducationRecord` ;
- `ExperienceRecord` ;
- `AchievementClaim` ;
- `ProfileEvidenceLink` ;
- identifiants durables ;
- versions temporelles ;
- états de vérification ;
- références de provenance ;
- créations, corrections et suppressions/rectifications applicables ;
- mutations réparties avant et après plusieurs points de restauration.

Chaque mutation de contrôle possède un identifiant et un timestamp permettant de déterminer précisément ce qui a été confirmé et ce qui a été récupéré.

## 6. Mesure du RPO

Pour chaque scénario concerné :

`RPO mesuré = timestamp de la dernière mutation confirmée avant incident - timestamp de la dernière mutation autoritative récupérée`

PASS si :
- les deux timestamps sont prouvés ;
- la différence est ≤ 15 min pour le scénario soumis au RPO nominal ;
- l'intégrité des mutations récupérées est validée ;
- aucune dépendance interdite n'a servi à recréer les données.

Un backup marqué SUCCESS sans restore ne valide pas le RPO.

## 7. Mesure du RTO

Le chronomètre démarre au moment défini dans la fiche du scénario : détection/qualification de la condition nécessitant la reprise ou déclenchement contrôlé du test.

Il s'arrête uniquement lorsque le service satisfait les critères d'exploitabilité du scénario. Le simple démarrage du datastore ou du processus applicatif ne clôt pas le RTO.

Un service restauré mais non qualifié, en split-brain, sans contrôles d'intégrité requis ou avec une décision Privacy bloquante n'est pas exploitable.

## 8. Critères d'intégrité

Avant promotion, contrôler au minimum :
- autorité PRF-002 unique ;
- absence de duplication métier inattendue ;
- présence et unicité des identifiants durables ;
- cohérence des relations entre agrégats ;
- temporalité et versions ;
- états de vérification ;
- références de provenance ;
- cohérence des migrations ;
- absence d'écriture métier interdite pendant RECOVERY/QUARANTINE ;
- audit des opérations de reprise.

## 9. Catalogue des exercices

| ID | Scénario | Objectif | PASS principal |
|---|---|---|---|
| DR-001 | perte instance applicative | RTO courant | RPO 0 attendu ; service exploitable ≤ 1 h |
| DR-002 | perte d'un nœud datastore avec autorité saine | HA/RTO courant | RPO 0 attendu ; ≤ 1 h |
| DR-003 | perte complète datastore actif | recovery C1 | RPO ≤ 15 min ; RTO ≤ 4 h |
| DR-004 | corruption logique | PITR | point sain restauré ; cible ≤ 4 h après qualification du point sain |
| DR-005 | suppression accidentelle ciblée | récupération ciblée | intégrité restaurée sans écraser des mutations saines non concernées |
| DR-006 | mauvais déploiement/migration | rollback/recovery | RPO 0 attendu si aucune mutation perdue ; ≤ 1 h cible incident courant |
| DR-007 | perte du périmètre principal | sinistre majeur | RPO ≤ 15 min ; RTO ≤ 8 h depuis couche de reprise prévue |
| DR-008 | backup récent corrompu/inutilisable | fallback | génération saine précédente restaurée ; cible ≤ 8 h |
| DR-009 | PRF-001 + EDU + SKL simultanément indisponibles | autonomie | autorité PRF-002 restaurée sans accès aux trois dépendances |
| DR-010 | décision Privacy postérieure au restore point | conformité | décision réappliquée avant opérations concernées/retour normal |
| DR-011 | projections aval obsolètes | réconciliation | PRF-002 prévaut ; projections resynchronisées |
| DR-012 | replay/republication | idempotence | aucun doublon métier ; contrats respectés |
| DR-013 | identité de backup/restore | séparation des accès | identité dédiée ; droits minimaux ; opérations auditées |
| DR-014 | récupération des clés nécessaires | cryptographie | données restaurables sans contournement de contrôle |
| DR-015 | copie isolée | blast radius | copie disponible malgré perte/compromission du périmètre principal simulé |
| DR-016 | exécution indépendante du runbook | opérabilité | opérateur habilité autre que l'auteur exécute le runbook sans connaissance tacite bloquante |
| DR-017 | compatibilité schéma/migrations | évolutivité | état restauré compatible ou procédure de migration contrôlée |
| DR-018 | compromission suspectée | quarantine | confinement et qualification du point sain priment sur la vitesse |
| DR-019 | erreur humaine propagée | récupération temporelle | retour à un état sain sans promotion d'un état incertain |
| DR-020 | réouverture NORMAL-RESTORED | gouvernance | signatures requises et critères de promotion satisfaits |

## 10. Exercice bloquant DR-009

Pendant DR-009 :
1. bloquer les chemins réseau/API vers PRF-001, EDU et SKL ;
2. interdire toute lecture directe de leurs datastores ;
3. déclencher une perte complète du datastore actif PRF-002 dans l'environnement de test ;
4. restaurer PRF-002 depuis sa propre chaîne de recovery ;
5. contrôler les agrégats, IDs, versions, vérifications et provenance ;
6. mesurer RPO et RTO ;
7. démontrer via logs réseau qu'aucune des trois dépendances n'a servi à reconstruire l'autorité ;
8. promouvoir l'autorité restaurée vers l'état opérationnel autorisé ;
9. maintenir les références externes non résolues si nécessaire ;
10. effectuer la réconciliation seulement après retour des dépendances.

DR-009 est `REC-BLOCKING`. Son échec bloque `VERIFIED` et `ready-for-production`.

## 11. Privacy après restauration

Un exercice doit créer une décision d'effacement, restriction ou autre décision Privacy après le point de backup/restauration choisi.

Après restore :
- détecter l'écart ;
- réappliquer la décision applicable ;
- vérifier qu'aucune donnée interdite ne reste durablement réactivée ;
- enregistrer l'opération ;
- obtenir la validation `OWN-PRIV` avant le retour normal lorsque requis.

## 12. Backup corrompu

DR-008 doit démontrer que l'équipe ne dépend pas d'une seule génération.

Le scénario marque la génération récente comme inutilisable et impose :
- détection de l'échec ;
- sélection d'une génération saine ;
- justification du point choisi ;
- restauration ;
- mesure de la perte réelle ;
- contrôles d'intégrité ;
- enregistrement de tout dépassement de RPO/RTO.

## 13. Compromission et QUARANTINE

DR-018 ne doit pas forcer artificiellement le respect d'un RTO en promouvant un état non qualifié.

Le test vérifie :
- arrêt des mutations ;
- isolation ;
- conservation des preuves techniques nécessaires ;
- qualification du dernier état sain ;
- restauration contrôlée ;
- validation Security ;
- validation Privacy si nécessaire ;
- promotion seulement après contrôles.

Tout dépassement possède une chronologie, une justification et un owner.

## 14. Identités et séparation des pouvoirs

Les exercices doivent vérifier :
- identité applicative distincte des identités de backup/restore ;
- droits minimaux ;
- absence de compte partagé pour les opérations sensibles ;
- journalisation des opérations ;
- impossibilité pour l'identité applicative de supprimer arbitrairement les sauvegardes si l'architecture retenue prévoit cette séparation ;
- approbations conformes à `PRF002_NOMINATION_MATRIX.md`.

L'exécutant d'une restauration ne peut pas être son unique approbateur.

## 15. Preuve de test

Chaque exercice produit une fiche contenant :

| Champ | Valeur |
|---|---|
| Test ID | DR-XXX |
| Date | AAAA-MM-JJ |
| Environnement | À RENSEIGNER |
| Version PRF-002 | À RENSEIGNER |
| Version runbook | À RENSEIGNER |
| Exécutant | À RENSEIGNER |
| Observateur | À RENSEIGNER |
| Backup/génération source | À RENSEIGNER |
| Restore point | À RENSEIGNER |
| Dernière mutation confirmée | À RENSEIGNER |
| Dernière mutation récupérée | À RENSEIGNER |
| RPO mesuré | À RENSEIGNER |
| Début RTO | À RENSEIGNER |
| Fin RTO | À RENSEIGNER |
| RTO mesuré | À RENSEIGNER |
| Contrôles d'intégrité | À RENSEIGNER |
| Logs/preuves | À RENSEIGNER |
| Anomalies | À RENSEIGNER |
| Actions correctives | À RENSEIGNER |
| Résultat | PENDING/PASS/PASS-WITH-NONBLOCKING-FINDINGS/FAIL |
| Approbateurs | À RENSEIGNER |

Les preuves sensibles sont conservées dans l'emplacement gouverné prévu ; la documentation peut n'en conserver que la référence.

## 16. Résultats autorisés

- `PASS` : tous les critères bloquants satisfaits ;
- `PASS-WITH-NONBLOCKING-FINDINGS` : objectifs bloquants atteints, écarts non bloquants avec owner et échéance ;
- `FAIL` : un critère bloquant échoue ;
- `PENDING` : exercice non exécuté ou preuve insuffisante.

Aucune dérogation documentaire ne transforme un échec de l'autonomie de récupération, de l'intégrité ou d'une exigence Privacy/Security bloquante en PASS.

## 17. Gates bloquants avant production

Au minimum, doivent être PASS :
- DR-003 perte complète datastore ;
- DR-004 corruption/PITR ;
- DR-007 sinistre majeur ;
- DR-008 backup récent inutilisable ;
- DR-009 autonomie PRF-001 + EDU + SKL indisponibles ;
- DR-010 Privacy post-restore ;
- DR-012 idempotence ;
- DR-013 identités ;
- DR-015 copie isolée ;
- DR-016 runbook indépendant ;
- DR-020 promotion gouvernée.

Les exercices associés aux RPO/RTO doivent démontrer leurs seuils respectifs.

## 18. Responsabilités de validation

- `OWN-PRF2-DR` : exécution/coordination technique et rapport DR ;
- `OWN-PRF2-OPS` : exploitabilité, readiness et continuité ;
- `OWN-PRF2-BUS` : intégrité métier et acceptation de l'autorité restaurée ;
- `OWN-SEC` : compromission, isolation, identités, clés et accès privilégiés ;
- `OWN-PRIV` : décisions Privacy post-restore ;
- `OWN-INFRA` : infrastructure de reprise et copie isolée ;
- `OWN-DATA-GOV` : provenance lorsque le scénario l'exige ;
- `OWN-ARCH` : frontières et absence de dépendance de récupération interdite.

Les signatures suivent `PRF002_NOMINATION_MATRIX.md`.

## 19. Qualification des personnes

Les exercices peuvent également servir de preuve à `PRF002_SENSITIVE_ROLE_PRACTICAL_QUALIFICATION.md` si :
- la personne est explicitement évaluée ;
- elle exécute réellement les tâches de son rôle ;
- un observateur indépendant est présent ;
- les critères de qualification du rôle sont couverts ;
- la preuve identifie clairement la personne et le résultat.

La réussite collective d'un exercice ne qualifie pas automatiquement tous les participants.

## 20. Conditions de fermeture du gate REC

Le gate `REC` ne peut être fermé que lorsque :
- les exercices bloquants sont exécutés ;
- les RPO/RTO applicables sont mesurés et conformes ;
- DR-009 est PASS ;
- les contrôles d'intégrité sont conformes ;
- les preuves sont archivées et référencées ;
- les écarts bloquants sont fermés ;
- les approbateurs requis sont nommés et actifs ;
- les résultats sont reportés dans la BIA et le registre d'hypothèses ;
- aucune preuve expirée ou architecture significativement différente ne rend les résultats caducs.

Statut actuel : `REC-OPEN — PLAN READY, PREPROD EXECUTION REQUIRED`.
