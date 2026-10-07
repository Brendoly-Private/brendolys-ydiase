---
document_id: "YD-DOC-OPS-PRF-002-PRF002-BIA"
title: "PRF002_BIA — Business Impact Analysis"
document_type: "operations-reference"
document_role: "Documente une référence opérationnelle de continuité, qualification ou analyse."
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

# PRF002_BIA — Business Impact Analysis

> **Rôle du document**
> Documente une référence opérationnelle de continuité, qualification ou analyse.
> **Usage développement :** référence de support pour la conception et la préparation opérationnelle.

Statut : `PREPROD-CANDIDATE`
Service : `YD-MS-PRF-002 — Education & Experience Profile`
Nature : `AUTH`
Criticité : `C1`
Références : `ADR-PRF002-RPO-RTO.md`, `PRF002_CONTINUITY_POLICY.md`, `PRF002_BACKUP_RESTORE_POLICY.md`, `AUTONOMY_PROFILE.md`

## 1. Objet

Cette BIA relie la criticité métier de PRF-002 aux objectifs de perte de données et de reprise retenus avant production.

PRF-002 conserve un historique individuel éducatif et professionnel autoritatif, ses réalisations, ses liens de preuve, sa temporalité, ses versions et certains états de vérification. Une partie de cet historique ne peut pas être reconstruite depuis PRF-001, EDU, SKL ou une autre source YDIASE.

Cette analyse ne considère donc pas PRF-002 comme une projection reconstructible.

## 2. Décision analysée

Les seuils candidats sont :

| Indicateur | Seuil candidat | Interprétation métier |
|---|---:|---|
| RPO nominal | `≤ 15 min` | perte maximale de mutations autoritatives confirmées lors du scénario nominal de perte complète du datastore |
| RTO incident courant | `≤ 1 h` | retour du service après panne applicative, nœud ou composant remplaçable sans perte complète de l'autorité |
| RTO perte complète datastore | `≤ 4 h` | récupération d'une autorité PRF-002 exploitable depuis une source de reprise valide |
| RTO sinistre majeur | `≤ 8 h` | récupération après perte du périmètre principal ou incident nécessitant une reprise étendue |
| corruption logique | restauration temporelle obligatoire | retour à un point sain identifié et réconciliation contrôlée |

Ces seuils sont des cibles à valider. La BIA ne les rend pas `VERIFIED` sans données d'exploitation et exercices DR.

## 3. Périmètre métier analysé

Les agrégats et informations protégés comprennent au minimum :

- `EducationRecord`
- `ExperienceRecord`
- `AchievementClaim`
- `ProfileEvidenceLink`
- états de vérification propres aux déclarations
- temporalité et versions métier
- références de provenance nécessaires

Les référentiels d'institutions, programmes et qualifications restent sous autorité EDU. Les taxonomies de compétences restent sous autorité SKL. Le profil courant reste séparé dans PRF-001.

## 4. Hypothèses de travail

Cette BIA utilise les hypothèses suivantes avant disponibilité de métriques de production :

1. PRF-002 contient des données personnelles dont certaines mutations ne sont pas reproductibles automatiquement.
2. Le volume de mutations augmentera avec l'adoption de YDIASE et l'expansion multi-pays.
3. Une interruption PRF-002 ne doit pas provoquer l'arrêt général de YDIASE.
4. Les fonctions indépendantes de l'historique personnel continuent pendant l'incident.
5. PRF-001, EDU et SKL peuvent être simultanément indisponibles pendant une restauration sans empêcher PRF-002 de récupérer son autorité.
6. Certaines opérations fonctionnelles post-restauration peuvent attendre le retour de leurs dépendances.
7. Une décision Privacy obligatoire non vérifiable bloque la mutation concernée.
8. Une compromission ou corruption peut imposer une reprise plus lente qu'une panne technique simple, car l'identification d'un état sain prime sur la vitesse.
9. Les projections aval peuvent faciliter un mode de lecture limité, mais elles ne deviennent jamais autoritatives.
10. Les coûts financiers précis d'une heure d'indisponibilité ne sont pas encore établis et devront être mesurés avant production puis réévalués avec l'usage réel.

Toute hypothèse invalidée déclenche une revue de cette BIA.

## 5. Dimensions d'impact

L'impact d'un incident PRF-002 est évalué selon :

- perte irréversible de données autoritatives
- impossibilité pour le sujet de consulter ou modifier son historique
- indisponibilité des fonctions YDIASE dépendant de cet historique
- risque de recommandation ou décision utilisant un état incomplet
- perte ou incohérence de preuves et vérifications
- conséquences Privacy et conformité
- charge de réconciliation manuelle
- perte de confiance utilisateur
- impact opérationnel sur support et exploitation
- propagation d'états obsolètes vers les consommateurs
- impact financier et contractuel lorsque ces dimensions seront quantifiables

## 6. Échelle d'impact

| Niveau | Définition |
|---|---|
| `I0` | négligeable, sans perte métier ni interruption significative |
| `I1` | faible, gêne temporaire et récupération simple |
| `I2` | modéré, fonctions dépendantes affectées et intervention opérationnelle nécessaire |
| `I3` | élevé, utilisateurs ou consommateurs significativement affectés, risque de réconciliation complexe |
| `I4` | très élevé, perte autoritative, atteinte Privacy, incohérence majeure ou interruption incompatible avec les engagements |
| `I5` | inacceptable, perte durable ou propagation non maîtrisée portant atteinte à l'autorité, aux droits ou à la continuité majeure |

Les seuils quantitatifs d'utilisateurs, transactions et coûts associés à I1-I5 restent `TBD-PREPROD` jusqu'aux données de charge et d'adoption.

## 7. Impact d'une perte de mutations

| Fenêtre perdue | Impact initial | Analyse |
|---|---|---|
| `≤ 5 min` | I1-I2 | perte possible de quelques mutations récentes, à réconcilier |
| `> 5 à 15 min` | I2 | fenêtre encore compatible avec le RPO candidat si la perte reste quantifiée et réconciliable |
| `> 15 min à 1 h` | I3 | dépasse le RPO retenu, augmente la probabilité de perte de déclarations, corrections ou preuves |
| `> 1 h à 4 h` | I3-I4 | volume de mutations potentiellement perdu trop important pour une cible C1 normale |
| `> 4 h` | I4-I5 | perte autoritative incompatible avec l'objectif de continuité retenu |

### Justification du RPO ≤ 15 min

Le seuil de 15 minutes limite l'exposition à une fenêtre courte de mutations autoritatives non reconstructibles. Il évite de traiter plusieurs heures d'activité comme une perte acceptable par conception.

Il reste cependant une hypothèse métier à confirmer par :

- volume réel de mutations par tranche de 15 minutes
- nature des mutations
- capacité de réconciliation
- coût opérationnel de récupération
- fréquence des preuves ou vérifications sensibles
- obligations réglementaires applicables

Si 15 minutes représentent déjà une perte métier excessive à l'échelle réelle, le RPO doit être réduit.

## 8. Impact de l'indisponibilité

| Durée d'indisponibilité | Impact initial | Comportement attendu |
|---|---|---|
| `≤ 5 min` | I1 | mécanismes automatiques ou intervention minimale |
| `> 5 à 15 min` | I1-I2 | mode dégradé visible, fonctions indépendantes maintenues |
| `> 15 min à 1 h` | I2 | restauration ou bascule en cours, écritures sensibles suspendues si nécessaire |
| `> 1 h à 4 h` | I3 | incident C1 significatif, fonctions dépendantes durablement limitées |
| `> 4 h à 8 h` | I4 | acceptable uniquement pour scénario de sinistre majeur qualifié |
| `> 8 h à 24 h` | I4-I5 | dépassement de la cible maximale retenue, escalade et décision de continuité requises |
| `> 24 h` | I5 | situation incompatible avec la cible de production C1 |

## 9. Justification du RTO ≤ 1 h

Le RTO d'une heure s'applique aux incidents courants qui ne détruisent pas l'autorité : panne applicative, instance, nœud ou composant remplaçable.

Un incident courant ne doit pas mobiliser la procédure de reconstruction complète. Dépasser une heure pour ce type de panne indiquerait une faiblesse de haute disponibilité, de déploiement, de supervision ou de runbook.

Critère métier : les utilisateurs et fonctions dépendantes peuvent supporter une limitation courte, mais une panne technique ordinaire ne doit pas se transformer en indisponibilité de plusieurs heures.

## 10. Justification du RTO ≤ 4 h

Le seuil de quatre heures concerne la perte complète du datastore actif ou un scénario nécessitant une restauration autoritative.

Il tient compte du temps nécessaire pour :

- qualifier l'incident
- identifier une source saine
- restaurer dans un environnement contrôlé
- vérifier l'intégrité
- mesurer la perte éventuelle
- réappliquer les décisions Privacy nécessaires
- promouvoir une autorité unique
- commencer la réconciliation aval

Au-delà de quatre heures, l'impact sur les fonctions dépendantes devient élevé et le risque de divergence des consommateurs augmente.

Ce RTO ne permet jamais de promouvoir un état non vérifié pour respecter artificiellement le chronomètre.

## 11. Justification du RTO ≤ 8 h

Le seuil de huit heures couvre un sinistre majeur : perte du périmètre principal, corruption étendue, indisponibilité d'une couche de sauvegarde récente ou reprise depuis une copie isolée.

Ce délai n'est pas un RTO normal. Il constitue la cible maximale candidate pour une reprise étendue avant que l'impact soit classé très élevé ou inacceptable.

Une compromission peut suspendre ce chronomètre opérationnel si l'état sain n'est pas encore déterminé. Dans ce cas, la sécurité et l'intégrité priment et l'écart RTO doit être traité comme incident C1 documenté.

## 12. MTPD candidat

Le `Maximum Tolerable Period of Disruption` candidat est :

`MTPD-CANDIDATE = 24 heures`

Pour les incidents courants, le seuil opérationnel est beaucoup plus bas et reste lié au RTO d'une heure.

Le RTO de sinistre majeur reste inférieur ou égal à 8 h. Le MTPD de 24 h ne remplace pas cet objectif. Tout dépassement de 8 h constitue un échec du RTO et déclenche une escalade.

### Gate MTPD-24H-APPROVED

Le passage de MTPD-CANDIDATE = 24 h à MTPD-APPROVED = 24 h exige :
- OWN-PRF2-BUS : analyse d'impact à 1 h, 4 h, 8 h, 12 h et 24 h ;
- OWN-PRF2-OPS/OWN-PRF2-DR : preuve de continuité et démonstration du RTO majeur inférieur ou égal à 8 h ;
- OWN-PRIV : confirmation qu'aucune obligation applicable n'impose une limite inférieure ;
- OWN-PRODUCT-FIN : modèle d'impact économique et contractuel ;
- OWN-CONSUMERS : validation des consommateurs critiques ;
- OWN-ARCH : revue des dépendances et modes dégradés ;
- OWN-CAPACITY : volumes, mutations et impact aux charges prévues.

Le gate reste ouvert tant que les preuves et approbations obligatoires ne sont pas enregistrées. La valeur reste donc CANDIDATE jusqu'à décision formelle.

Le MTPD de 8 heures doit être confirmé avant production avec les responsables métier, opérationnels, sécurité et conformité.

Un MTPD ne signifie pas qu'une indisponibilité de 8 heures est acceptable en exploitation normale.

## 13. MDL candidat

La `Maximum Data Loss` candidate est liée au RPO :

`MDL-CANDIDATE = mutations autoritatives confirmées sur une fenêtre maximale de 15 minutes`

La validation ne peut pas reposer uniquement sur le temps. Avant production, YDIASE doit mesurer combien de mutations et quels types de données peuvent se trouver dans cette fenêtre aux charges prévues.

Si une seule mutation critique peut rendre cette perte inacceptable, une politique spécifique ou un RPO inférieur devra être étudié.

## 14. MBCO

Le `Minimum Business Continuity Objective` de PRF-002 est :

- protéger le dernier état autoritatif reconnu sain
- conserver les lectures sûres lorsqu'elles restent possibles
- suspendre les mutations non vérifiables
- maintenir les fonctions YDIASE indépendantes de PRF-002
- empêcher toute projection de prendre l'autorité
- exposer clairement l'état dégradé aux consommateurs
- permettre une restauration indépendante de PRF-001, EDU et SKL

Le MBCO ne promet pas toutes les fonctionnalités nominales pendant une reprise.

## 15. Dépendances métier

### PRF-001

Dépendance fonctionnelle pour certaines opérations selon contrat. Non bloquante pour backup, restore et récupération de l'autorité PRF-002.

### EDU

Dépendance fonctionnelle pour valider certaines nouvelles références éducatives. Non bloquante pour lire l'historique déjà enregistré et non bloquante pour restaurer l'autorité.

### SKL

Dépendance fonctionnelle lorsque certaines opérations exigent une référence de compétence. Non bloquante pour restaurer l'autorité.

### CNS-001

Autorité pour les décisions Privacy. Non nécessaire pour restaurer physiquement le datastore, mais nécessaire avant retour normal lorsqu'il faut réappliquer des restrictions, effacements ou autres instructions devenues applicables.

### BRENDOLYS Identity

Nécessaire aux accès utilisateurs et opérations authentifiées. La restauration technique utilise des identités opérationnelles dédiées et ne dépend pas d'une session utilisateur.

### DAT / provenance

Peut être nécessaire à certaines nouvelles mutations ou réconciliations. Les références de provenance déjà enregistrées doivent survivre à la restauration sans dépendre de DAT pour recréer l'autorité.

## 16. Dépendances interdites pour la restauration

Le processus DR ne doit pas exiger :

- la base PRF-001
- la base EDU
- la base SKL
- un accès direct aux bases d'autres microservices
- une reconstruction de l'historique depuis des projections aval
- une IA pour reconstituer les données manquantes
- une copie métier non gouvernée détenue par un consommateur

Un test de restauration qui dépend de l'un de ces éléments échoue le critère d'autonomie.

## 17. Scénarios dimensionnants

| Scénario | Impact principal | RPO | RTO cible |
|---|---|---:|---:|
| panne applicative | indisponibilité temporaire | 0 attendu | ≤ 1 h |
| perte d'un nœud datastore avec autorité saine | disponibilité | 0 attendu | ≤ 1 h |
| perte complète datastore | perte autoritative potentielle | ≤ 15 min | ≤ 4 h |
| corruption logique | état autoritatif incorrect | point sain à qualifier | ≤ 4 h après qualification du point sain |
| suppression accidentelle | perte ciblée | ≤ 15 min cible ou récupération ciblée | ≤ 4 h |
| perte du périmètre principal | continuité étendue | ≤ 15 min cible | ≤ 8 h |
| backup récent inutilisable | recul vers génération saine | mesuré | ≤ 8 h |
| compromission | intégrité et confidentialité | non présumé avant investigation | après confinement et qualification |
| PRF-001 + EDU + SKL indisponibles | autonomie de reprise | inchangé | seuil du scénario DR principal |

## 18. Fonctions affectées pendant l'incident

Peuvent être suspendues ou limitées :

- consultation détaillée de l'historique si l'intégrité n'est pas établie
- création et correction d'historiques
- rattachement de preuves
- vérification
- fonctions de recommandation exigeant l'historique courant
- projections ou exports nécessitant une autorité fraîche

Doivent continuer lorsqu'elles ne dépendent pas de PRF-002 :

- fonctions propres à Education
- fonctions propres à Skills
- fonctions YDIASE sans dépendance à l'historique individuel
- exploitation et DR via les canaux autorisés

## 19. Critères de validation du RPO

Le RPO `≤ 15 min` est validé uniquement si un exercice démontre :

1. heure de la dernière mutation confirmée avant incident connue
2. heure de la dernière mutation restaurée connue
3. différence mesurée `≤ 15 min`
4. intégrité des mutations récupérées contrôlée
5. aucune dépendance PRF-001/EDU/SKL utilisée pour recréer l'autorité
6. résultat reproductible sur les scénarios prévus par le plan DR

## 20. Critères de validation des RTO

### RTO ≤ 1 h

Validé si les scénarios d'incident courant définis dans le plan DR reviennent à un service exploitable en une heure ou moins sans perte autoritative inattendue.

### RTO ≤ 4 h

Validé si une perte complète du datastore peut aboutir à une autorité PRF-002 saine, promue et exploitable en quatre heures ou moins, avec mesure du RPO et contrôles d'intégrité terminés.

### RTO ≤ 8 h

Validé si le scénario de sinistre majeur retenu peut récupérer l'autorité depuis la couche isolée prévue en huit heures ou moins.

Le chronométrage commence au point défini par `PRF002_DR_TEST_PLAN.md` et s'arrête uniquement lorsque les critères de service exploitable sont satisfaits. Le simple démarrage du processus ou du datastore ne clôt pas le RTO.

## 21. Critères de service exploitable après reprise

PRF-002 est considéré exploitable lorsque :

- l'autorité restaurée est unique
- le datastore est sain
- les agrégats requis passent les contrôles d'intégrité
- les identifiants durables sont conservés
- la temporalité et les versions restent cohérentes
- les références de provenance sont présentes
- le RPO est mesuré
- les décisions Privacy nécessaires sont réappliquées avant opérations concernées
- les health/readiness requis sont conformes
- les opérations permises par l'état de reprise fonctionnent
- aucun incident C1 non maîtrisé ne bloque la promotion

La réconciliation de tous les consommateurs peut continuer après le retour de l'autorité si leur contrat le permet. Elle ne doit pas fausser la mesure du RTO de restauration autoritative.

## 22. Données à collecter avant production

Pour confirmer cette BIA, collecter ou estimer avec justification :

- utilisateurs actifs attendus
- mutations par minute et par heure
- distribution par type de mutation
- fréquence des vérifications
- fréquence d'ajout de preuves
- taille moyenne et maximale des agrégats
- volume quotidien de données
- croissance prévue
- nombre de consommateurs dépendants
- durée acceptable de suspension par fonction
- coût opérationnel d'une réconciliation
- contraintes légales par pays du pilote
- capacité réelle de l'équipe d'astreinte ou d'exploitation
- temps mesuré de restauration selon les volumes cibles

## 23. Conditions imposant une révision

Réviser la BIA si :

- le volume de mutations change significativement
- PRF-002 devient dépendance bloquante d'une fonction à forte criticité
- un nouveau pays introduit une obligation différente
- les données stockées changent de sensibilité
- les résultats DR dépassent régulièrement les seuils
- l'architecture de stockage change
- le coût d'un incident est quantifié et contredit les hypothèses
- une nouvelle classe d'utilisateur ou d'organisation dépend directement de PRF-002
- les engagements contractuels changent

## 24. Gates de validation

Avant `ready-for-production`, cette BIA exige :

- validation du owner métier PRF-002
- validation exploitation/DR
- validation sécurité
- validation Privacy/conformité
- confirmation du MTPD
- confirmation du MDL
- confirmation du MBCO
- données de charge ou hypothèses de capacité approuvées
- `PRF002_DR_TEST_PLAN.md` exécuté
- preuve RPO `≤ 15 min`
- preuve RTO incident courant `≤ 1 h`
- preuve RTO perte datastore `≤ 4 h`
- preuve RTO sinistre majeur `≤ 8 h`
- preuve de restauration avec PRF-001, EDU et SKL indisponibles

## 25. Décision BIA actuelle

Classification : `C1 — AUTHORITATIVE / NON-FULLY-RECONSTRUCTIBLE`.

Seuils retenus comme cibles préproduction :

- `RPO ≤ 15 min`
- `RTO courant ≤ 1 h`
- `RTO datastore ≤ 4 h`
- `RTO sinistre majeur ≤ 8 h`
- `MTPD-CANDIDATE = 24 h`
- `MDL-CANDIDATE = ≤ 15 min de mutations autoritatives confirmées`
- MBCO défini par la continuité de l'autorité et le maintien des fonctions indépendantes

Statut : `TBD-PREPROD — BUSINESS TARGETS DEFINED, VALIDATION AND DR PROOF REQUIRED`.

La fermeture de ce gate exige des validations métier et des mesures de restauration. Aucun seuil n'est déclaré `VERIFIED` avant ces preuves.