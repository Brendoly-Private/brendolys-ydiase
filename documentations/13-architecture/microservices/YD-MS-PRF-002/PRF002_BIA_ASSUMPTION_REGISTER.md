# PRF002_BIA_ASSUMPTION_REGISTER — Registre des hypothèses testables

Statut : `PREPROD-CANDIDATE`
Service : `YD-MS-PRF-002 — Education & Experience Profile`
Source : `PRF002_BIA.md`

## 1. Objet

Ce registre transforme les hypothèses de travail de `PRF002_BIA.md` en assertions falsifiables. Une hypothèse ne peut pas soutenir une décision de production tant qu'un propriétaire, une méthode de validation, une preuve et un critère d'acceptation ne sont pas définis.

Les propriétaires ci-dessous désignent des rôles. Les personnes nominatives seront attribuées avant le gate production.

## 2. Statuts

- `OPEN` : test non exécuté ou preuve insuffisante
- `VALIDATED` : critère d'acceptation satisfait avec preuve enregistrée
- `REJECTED` : hypothèse contredite
- `CONDITIONAL` : vraie uniquement sous conditions documentées
- `SUPERSEDED` : remplacée par une décision ultérieure traçable

Toute hypothèse `REJECTED` qui soutient le RPO, le RTO, le MTPD, le MDL, le MBCO ou l'autonomie de reprise rouvre la BIA et les décisions dépendantes.

## 3. Registre

| ID | Hypothèse testable | Propriétaire | Méthode de validation | Critère d'acceptation | Preuve attendue | Gate | Statut |
|---|---|---|---|---|---|---|---|
| `PRF2-HYP-001` | Certaines mutations PRF-002 contiennent une information autoritative qui ne peut pas être reproduite automatiquement depuis les autres autorités YDIASE. | Owner métier PRF-002 | Échantillonner chaque type d'agrégat et tenter une reconstruction documentée à partir de PRF-001, EDU, SKL, DAT et sources autorisées. | Au moins une classe de mutation requiert une donnée, temporalité, version, déclaration, état de vérification ou relation de preuve possédée uniquement par PRF-002. Si aucune n'en requiert, la classification `AUTH` doit être réexaminée. | Matrice d'ownership + exercice de reconstruction + écarts | Architecture/BIA | OPEN |
| `PRF2-HYP-002` | Le volume de mutations augmente avec l'adoption et l'expansion multi-pays. | Product Analytics + Capacity owner | Modéliser pilote, montée en charge et scénarios multi-pays puis comparer aux métriques réelles à chaque palier. | La capacité et la stratégie de protection restent conformes au RPO/RTO au percentile de charge retenu. Si la croissance réelle sort de l'enveloppe, capacity plan et BIA sont revus. | Capacity model + métriques + rapport de comparaison | Capacity | OPEN |
| `PRF2-HYP-003` | Une interruption PRF-002 n'entraîne pas l'arrêt général de YDIASE. | Architecture owner | Test de résilience avec PRF-002 totalement indisponible et exécution des capacités déclarées indépendantes. | 100 % des capacités classées indépendantes restent opérationnelles selon leur contrat. Aucun appel bloquant caché vers PRF-002 ne provoque une panne en cascade. | Rapport de fault injection + dependency traces | Continuity | OPEN |
| `PRF2-HYP-004` | Les fonctions indépendantes de l'historique personnel continuent pendant l'incident. | Owners des services consommateurs | Couper PRF-002, exécuter les parcours fonctionnels indépendants et vérifier leurs SLO/modes dégradés. | Chaque parcours classé indépendant aboutit sans lecture DB, API synchrone obligatoire ou autorité de secours PRF-002. Les limitations prévues sont explicitement signalées. | Tests E2E dégradés + traces | Continuity | OPEN |
| `PRF2-HYP-005` | PRF-002 récupère son autorité avec PRF-001, EDU et SKL simultanément indisponibles. | DR owner PRF-002 | Exercice de restauration complète en bloquant réseau/API/DB vers les trois frontières. | Autorité PRF-002 restaurée, intégrité validée, RPO/RTO du scénario respectés et zéro accès à PRF-001/EDU/SKL utilisé pour reconstruire l'autorité. | Rapport DR + logs réseau + chronométrage + contrôles d'intégrité | `REC` bloquant | OPEN |
| `PRF2-HYP-006` | Certaines opérations post-restauration peuvent attendre le retour de dépendances sans empêcher la récupération de l'autorité. | Owner métier PRF-002 + Contract owner | Restaurer PRF-002 avec dépendances indisponibles puis exécuter la matrice d'opérations de `PRF002_CONTINUITY_POLICY.md`. | Les opérations classées non bloquantes fonctionnent. Les opérations nécessitant une dépendance sont refusées ou différées conformément au contrat, sans corruption ni contournement. | Matrice PASS/FAIL + réponses API/événements | Continuity/Contracts | OPEN |
| `PRF2-HYP-007` | Une décision Privacy obligatoire non vérifiable bloque la mutation concernée. | Privacy owner + Security owner | Simuler CNS-001 indisponible, décision absente, projection expirée et décision ambiguë sur chaque mutation sensible. | 100 % des mutations nécessitant une décision Privacy non vérifiable échouent en `fail-closed`. Aucune voie secondaire ne contourne le contrôle. | Tests sécurité/Privacy + audit logs | Privacy bloquant | OPEN |
| `PRF2-HYP-008` | Corruption ou compromission peut nécessiter une reprise plus longue qu'une panne simple, car l'identification d'un état sain prime sur le RTO nominal. | Security Incident owner + DR owner | Tabletop puis exercice technique avec corruption et compromission simulées. Mesurer qualification, confinement et sélection du point sain. | Aucun état non qualifié n'est promu pour respecter un chronomètre. Tout dépassement RTO possède une justification C1, une chronologie et une décision enregistrée. | Rapport d'exercice + incident timeline + décision de promotion | Security/DR | OPEN |
| `PRF2-HYP-009` | Une projection aval peut permettre une lecture limitée sans devenir autoritative. | Architecture owner + Data Contract owner | Couper PRF-002 et tester chaque projection candidate avec watermark/fraîcheur, puis tenter des mutations et réconciliations. | La projection expose sa fraîcheur, reste en lecture selon contrat, ne permet aucune mutation autoritative et s'efface devant PRF-002 lors de la réconciliation. | Contract tests + freshness evidence + reconciliation report | Contracts | OPEN |
| `PRF2-HYP-010` | Le coût précis d'une heure d'indisponibilité n'est pas encore quantifié et doit être mesuré avant production puis recalculé avec l'usage. | Product/Finance owner | Construire un modèle d'impact intégrant utilisateurs, opérations bloquées, support, engagements, réconciliation et impacts contractuels. Le recalculer avec les métriques réelles. | Un coût ou une fourchette documentée existe avant validation finale du MTPD. Les hypothèses, unités et incertitudes sont explicites. | Modèle d'impact + validation Product/Finance | BIA | OPEN |

## 4. Hypothèses dérivées des seuils BIA

Les seuils eux-mêmes reposent sur des hypothèses supplémentaires et doivent être testés.

| ID | Hypothèse testable | Propriétaire | Méthode | Critère d'acceptation | Gate | Statut |
|---|---|---|---|---|---|---|
| `PRF2-HYP-011` | Une fenêtre de perte maximale de 15 min reste tolérable pour le métier aux charges prévues. | Owner métier PRF-002 | Injecter la charge cible, calculer nombre et type de mutations présentes dans 15 min, puis faire valider l'impact et la capacité de réconciliation. | Le owner métier accepte explicitement le MDL correspondant. Toute classe de mutation jugée intolérable déclenche réduction du RPO ou protection spécifique. | RPO | OPEN |
| `PRF2-HYP-012` | Les incidents courants peuvent être récupérés en ≤ 1 h. | SRE/Operations owner | Exercices panne applicative, instance, nœud et rollback avec chronométrage. | Tous les scénarios classés courants reviennent à l'état exploitable en ≤ 60 min sans perte autoritative inattendue. | RTO courant | OPEN |
| `PRF2-HYP-013` | Une perte complète du datastore peut être récupérée en ≤ 4 h. | DR owner PRF-002 | Détruire/isoler le datastore actif dans un environnement de test représentatif puis exécuter le runbook complet. | Autorité unique, saine et exploitable en ≤ 4 h, RPO ≤ 15 min, contrôles d'intégrité terminés. | RTO datastore | OPEN |
| `PRF2-HYP-014` | Un sinistre majeur peut être récupéré depuis la couche isolée en ≤ 8 h. | DR owner + Infrastructure owner | Rendre indisponible le périmètre principal et restaurer depuis la copie isolée. | Autorité saine et exploitable en ≤ 8 h, sans dépendance interdite et avec pertes dans le seuil validé. | RTO majeur/MTPD | OPEN |
| `PRF2-HYP-015` | Le MTPD candidat de 8 h reste compatible avec les obligations métier, Privacy, contractuelles et opérationnelles. | Product owner + Privacy/Compliance + Operations | Revue BIA formelle avec scénarios 4 h, 8 h, 24 h et effets sur populations et fonctions dépendantes. | Approbation explicite des rôles requis. Toute obligation imposant un délai inférieur réduit le MTPD. | MTPD | OPEN |
| `PRF2-HYP-016` | Le MBCO défini permet au produit de rester cohérent pendant l'indisponibilité PRF-002. | Product owner + Architecture owner | Exercice E2E en mode dégradé avec fonctions indépendantes, lectures sûres, écritures suspendues et états opérationnels exposés. | Aucun état incertain n'est présenté comme confirmé, les fonctions indépendantes restent utilisables et les mutations bloquées suivent la politique. | MBCO | OPEN |
| `PRF2-HYP-017` | Les décisions Privacy postérieures au point restauré peuvent être réappliquées avant retour normal. | Privacy owner + DR owner | Restaurer un point antérieur puis injecter un jeu de décisions Privacy postérieures au point de restauration. | Toutes les décisions applicables sont réappliquées et auditées avant `NORMAL-RESTORED`. Aucune donnée interdite ne reste durablement réactivée. | Privacy/REC | OPEN |
| `PRF2-HYP-018` | Les références de provenance nécessaires survivent à une restauration sans reconstruction depuis DAT. | Data Governance owner | Restaurer PRF-002 avec DAT indisponible puis vérifier un échantillon représentatif de références de provenance. | 100 % des références exigées pour les agrégats testés restent interprétables. Aucune provenance obligatoire n'est recréée artificiellement. | Data integrity | OPEN |
| `PRF2-HYP-019` | Le mécanisme de sauvegarde peut réellement produire un état récupérable dans le RPO annoncé. | Backup owner | Comparer mutations confirmées, journaux/snapshots et état restauré sur plusieurs fenêtres de charge. | Chaque exercice nominal respecte ≤ 15 min. Un job « réussi » sans restauration ne compte pas comme validation. | RPO/REC | OPEN |
| `PRF2-HYP-020` | La copie isolée possède un blast radius distinct du datastore actif et de sa réplication principale. | Infrastructure owner + Security owner | Analyse de menace et exercice de perte/compromission du périmètre principal. | La copie reste accessible par une voie autorisée, non supprimée/corrompue par les mêmes credentials ou mécanismes de défaillance simulés. | DR/Security | OPEN |

## 5. Règles de propriété

Chaque hypothèse doit avoir :

- un `Accountable Owner` unique
- un suppléant avant production
- les contributeurs nécessaires
- une date cible de validation
- une preuve référencée dans le registre documentaire

Un groupe ou une équipe peut exécuter le test, mais ne remplace pas l'owner responsable de la décision.

## 6. Règles de preuve

Une preuve acceptable doit être :

- datée
- reproductible ou explicable
- liée à la version d'architecture testée
- liée au scénario et au jeu de données utilisés
- conservée avec les mesures brutes utiles
- accompagnée du résultat `PASS`, `FAIL` ou `CONDITIONAL`
- liée à un owner pour tout écart

Une affirmation, une capture isolée ou un statut de job sans contrôle métier ne valide pas une hypothèse C1.

## 7. Effet d'un rejet

| Hypothèse rejetée | Action minimale |
|---|---|
| HYP-001 | réexaminer `AUTH/C1`, ownership et stratégie DR |
| HYP-002 | revoir capacity plan, backup et seuils de test |
| HYP-003/004/016 | revoir Dependency Map et politique de continuité |
| HYP-005 | bloquer `REC` et `ready-for-production` |
| HYP-006 | revoir contrats et mode dégradé |
| HYP-007/017 | bloquer les mutations ou le retour normal concernés |
| HYP-008 | revoir incident response et critères RTO sécurité |
| HYP-009 | retirer la projection du mode dégradé ou corriger son contrat |
| HYP-010/015 | ne pas valider définitivement le MTPD |
| HYP-011/019 | réduire le RPO ou renforcer le mécanisme de protection |
| HYP-012 | corriger HA/runbook ou réviser explicitement le RTO courant |
| HYP-013 | corriger backup/restore ou réviser explicitement le RTO datastore |
| HYP-014/020 | corriger l'isolement DR ou réviser explicitement la stratégie de sinistre majeur |
| HYP-018 | corriger la persistance de provenance avant production |

## 8. Gate global

Le registre passe à `BIA-ASSUMPTIONS-VALIDATED` uniquement lorsque :

- HYP-001 à HYP-020 ont un owner nominativement attribué
- aucune hypothèse bloquante n'est `OPEN` ou `REJECTED`
- les hypothèses `CONDITIONAL` possèdent des conditions exécutables et surveillées
- les preuves sont référencées
- les résultats ont été reportés dans `PRF002_BIA.md`
- toute modification des seuils a déclenché la révision des ADR et politiques dépendants

Statut actuel : `OPEN — TESTABLE ASSUMPTIONS DEFINED, OWNERSHIP NOMINAL AND EVIDENCE REQUIRED`.