# ADR — RPO, RTO et continuité de YD-MS-PRF-002

Statut : `ACCEPTED-WITH-PREPROD-PROOF`
Date : 2026-10-05
Service : `YD-MS-PRF-002 — Education & Experience Profile`
Nature : `AUTH`
Criticité : `C1`
Décision liée : `ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY.md`

## 1. Contexte

PRF-002 possède l'historique individuel éducatif et professionnel, les réalisations déclarées, les liens de preuve, leur temporalité, leurs versions et certains états de vérification.

Ces données sont autoritatives dans YDIASE et ne sont pas intégralement reconstructibles depuis Education, Skills, PRF-001, Data ou des sources externes. La perte du datastore PRF-002 peut donc constituer une perte métier définitive.

Le service est classé `AUTH / C1`. Sa stratégie de continuité doit limiter simultanément la perte de mutations autoritatives, la durée d'indisponibilité et le risque qu'une restauration réintroduise un état incorrect ou une donnée dont l'usage n'est plus autorisé.

## 2. Décision

Les objectifs préproduction retenus sont :

| Objectif | Seuil cible | Portée |
|---|---:|---|
| RPO nominal | `≤ 15 minutes` | perte maximale de mutations autoritatives lors d'une perte complète du datastore actif |
| RTO incident courant | `≤ 1 heure` | panne applicative, nœud ou composant remplaçable sans perte complète du datastore |
| RTO perte complète datastore | `≤ 4 heures` | restauration de l'autorité PRF-002 depuis une source de reprise valide |
| RTO sinistre majeur | `≤ 8 heures` | perte du site ou du périmètre principal nécessitant une reprise plus large |
| corruption logique | restauration temporelle obligatoire | retour à un état sain identifié sans accepter silencieusement la corruption comme autorité |

Ces seuils sont des objectifs normatifs préproduction, mais leur acceptation finale reste conditionnée par une BIA et des tests mesurés. Un test qui démontre que le seuil n'est pas atteignable rouvre la décision et interdit de déclarer le service `ready-for-production` tant que l'architecture ou le seuil métier n'est pas réconcilié.

`RPO = 0` n'est pas retenu comme exigence initiale faute de justification métier démontrant que toute perte d'une mutation, même sur quelques secondes, impose le coût et la complexité correspondants.

## 3. Fondement métier

Le RPO de 15 minutes limite la fenêtre de perte potentielle de déclarations, corrections, liens de preuve et états de vérification récents. Il ne signifie pas qu'une perte de 15 minutes est souhaitable. Il constitue la perte maximale cible que l'architecture doit pouvoir respecter avant production.

Le RTO de 4 heures pour perte complète du datastore reflète la criticité C1 : l'historique ne doit pas rester indisponible pendant une journée entière comme comportement normal de reprise. Le RTO de 8 heures couvre un sinistre plus large dans lequel l'infrastructure principale n'est plus directement récupérable.

Ces seuils devront être confirmés par `PRF002_BIA.md` en évaluant au minimum les impacts à 5 min, 15 min, 1 h, 4 h, 8 h, 24 h et 72 h.

## 4. MTPD, MDL et niveau minimal de continuité

La BIA doit formaliser :

- `MTPD` : durée maximale d'interruption tolérable avant impact métier inacceptable
- `MDL` : perte maximale de données autoritatives acceptable
- `MBCO` : niveau minimal de service maintenu pendant l'incident

Les relations normatives sont :

`RTO < MTPD`

`RPO ≤ MDL convertie en fenêtre temporelle de mutations`

Les valeurs finales de MTPD et MDL ne sont pas inventées par cet ADR. Elles doivent être confirmées par l'analyse métier et les obligations applicables avant le gate production.

## 5. Obligations de continuité

Une panne PRF-002 ne doit pas provoquer automatiquement l'indisponibilité générale de YDIASE.

Pendant l'incident :

- PRF-001 continue les opérations qui ne dépendent pas de PRF-002
- Education et Skills continuent leurs fonctions propres
- les capacités indépendantes continuent
- une projection autorisée peut rester consultable si son âge et son statut de fraîcheur sont connus
- aucune projection ne devient autoritative à la place de PRF-002
- les mutations nécessitant PRF-002 sont refusées, mises en attente ou reprises selon le contrat concerné
- aucune donnée incertaine n'est promue comme vérité
- une décision Privacy obligatoire non vérifiable reste fail-closed
- les utilisateurs et opérateurs reçoivent un état cohérent avec le mode dégradé lorsqu'une fonction dépendante est indisponible

Le MBCO minimal vise donc la continuité du reste du produit et la protection de l'autorité, pas la simulation d'un PRF-002 disponible alors qu'il ne l'est pas.

## 6. Scénarios dimensionnants

| Scénario | RPO attendu | RTO cible | Comportement attendu |
|---|---:|---:|---|
| instance applicative perdue | 0 attendu | ≤ 1 h | remplacement sans restauration métier |
| nœud datastore perdu mais autorité encore saine | 0 attendu | ≤ 1 h | bascule ou remise en service |
| datastore actif totalement perdu | ≤ 15 min | ≤ 4 h | restauration autoritative indépendante |
| corruption logique détectée | selon dernier point sain, ≤ cible validée si possible | ≤ 4 h après qualification du point sain | restauration temporelle et réconciliation |
| suppression accidentelle ciblée | perte évitée si récupération possible | ≤ 4 h pour cas critique | récupération contrôlée sans écraser les mutations valides |
| déploiement défectueux | 0 attendu pour données validées | ≤ 1 h | rollback applicatif, migrations réversibles ou procédure compensatoire |
| site/périmètre principal indisponible | ≤ 15 min cible | ≤ 8 h | reprise depuis périmètre de secours valide |
| compromission | aucun RPO automatique tant que l'étendue n'est pas qualifiée | RTO mesuré après confinement | isolation avant restauration, source saine obligatoire |
| sauvegarde récente corrompue | dépend de la dernière sauvegarde valide | ≤ 8 h cible | utiliser une génération antérieure vérifiée et réconcilier |
| erreur humaine propagée | selon point sain | ≤ 4 h après identification | restauration temporelle ou correction ciblée |
| indisponibilité EDU/SKL pendant reprise | aucune perte PRF-002 | ≤ 4 h pour autorité PRF-002 | restaurer PRF-002 sans dépendre de leurs bases |
| incident Privacy pendant reprise | aucune réactivation durable interdite | inclus dans procédure de reprise | réappliquer les décisions Privacy avant retour normal |

La compromission constitue un cas particulier : la vitesse de remise en ligne ne prime jamais sur l'identification d'un état sain.

## 7. RPO et mécanismes techniques

Le RPO est une exigence métier, pas la fréquence d'un backup.

L'architecture de production devra démontrer que la combinaison retenue de sauvegarde, journalisation, réplication ou autres mécanismes respecte `RPO ≤ 15 min` pour le scénario dimensionnant.

Cet ADR ne choisit ni technologie de base de données, ni produit de backup, ni fournisseur, ni topologie. Ces choix nécessitent leurs ADR techniques et doivent rester remplaçables conformément à la doctrine de pérennité.

## 8. Preuves de test obligatoires

PRF-002 ne peut pas être déclaré `ready-for-production` tant que les preuves suivantes ne sont pas produites et conservées :

1. restauration complète du datastore dans un environnement isolé
2. mesure réelle du temps entre déclenchement DR et service autoritatif exploitable
3. preuve que le RTO du scénario testé respecte le seuil applicable
4. mesure de la dernière mutation récupérée et preuve du RPO obtenu
5. contrôle d'intégrité des agrégats `EducationRecord`, `ExperienceRecord`, `AchievementClaim` et `ProfileEvidenceLink`
6. conservation des identifiants métier durables
7. conservation de la temporalité, des versions, états de vérification et références de provenance
8. test de restauration sans accès à la base PRF-001
9. test avec EDU ou SKL indisponible pour confirmer l'indépendance de reprise
10. test de réconciliation des projections aval
11. replay ou republication idempotente des événements nécessaires
12. absence de duplication métier après replay
13. réapplication des décisions Privacy pertinentes après restauration
14. test d'une sauvegarde volontairement invalide ou corrompue et bascule vers une génération saine
15. test d'une restauration temporelle après corruption logique simulée
16. preuve que les accès backup/restore utilisent des identités opérationnelles dédiées
17. journal d'audit de l'opération
18. validation du runbook par une personne qui n'a pas rédigé seule la procédure

## 9. Critères de réussite

Un exercice DR est réussi uniquement si :

- l'autorité restaurée est cohérente
- le RPO mesuré respecte le seuil applicable
- le RTO mesuré respecte le seuil applicable
- aucune dépendance interdite n'a été utilisée
- les identifiants et la sémantique sont conservés
- les projections sont réconciliables
- les décisions Privacy applicables sont respectées
- les preuves de test sont archivées
- les écarts observés possèdent un owner et une décision de correction

Le simple message « backup terminé avec succès » ne constitue pas une preuve de reprise.

## 10. Fréquence des exercices

Avant première production : test complet obligatoire.

Après production, la fréquence normative des exercices sera fixée dans la politique d'exploitation selon criticité C1, changements d'infrastructure et obligations applicables. Un changement majeur de datastore, stratégie de backup, chiffrement, topologie ou mécanisme de réplication déclenche un nouveau test avant de considérer le nouveau dispositif comme validé.

## 11. Documents exigés avant fermeture du gate REC

- `PRF002_BIA.md`
- `PRF002_CONTINUITY_POLICY.md`
- `PRF002_BACKUP_RESTORE_POLICY.md`
- `PRF002_DR_TEST_PLAN.md`
- rapport du test de restauration préproduction
- ADR techniques des mécanismes retenus lorsque nécessaires

## 12. Gate

État actuel : `TBD-PREPROD — ACCEPTED TARGETS, PROOF REQUIRED`.

Le gate REC passe à `DEFINED/VERIFIED` uniquement lorsque :

- la BIA confirme ou corrige les seuils
- les mécanismes techniques sont documentés
- un test réel démontre le RPO/RTO retenu
- les scénarios C1 requis sont couverts
- la procédure Privacy après restauration est validée
- les preuves sont enregistrées

Si la BIA conclut que 15 minutes, 4 heures ou 8 heures sont trop permissives, les seuils sont réduits. Si elle conclut qu'ils sont excessivement coûteux sans bénéfice métier correspondant, toute relaxation exige une révision explicite de cet ADR et ne peut pas être décidée uniquement par l'équipe infrastructure.

## 13. Réversibilité

Ces seuils ne constituent pas des constantes historiques de YDIASE. Ils peuvent évoluer avec les volumes, obligations, usages et risques. Toute modification conserve l'historique de décision, la justification métier, les preuves de test et la date d'entrée en vigueur.