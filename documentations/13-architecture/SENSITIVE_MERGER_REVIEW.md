# Sensitive Merger Review — BRENDOLYS YDIASE

Statut : `D3-reviewed-controlled`

## Objet

Revue contradictoire des fusions retenues dans `MICROSERVICE_BOUNDARY_REVIEW.md`. Une fusion n’est conservée que si elle respecte les bloqueurs du `MICROSERVICE_AUTONOMY_STANDARD.md` et ne détruit ni ownership, ni sécurité, ni résilience, ni capacité d’extraction future.

## Verdict consolidé

| Fusion | Verdict | Risque principal | Gate de maintien |
|---|---|---|---|
| PRF-001 + PRF-002 | VALIDÉE SOUS CONTRÔLE RENFORCÉ | profil utilisateur trop large et concentration de données personnelles | séparation interne des agrégats, permissions, rétention et audit; revue obligatoire avant production Burkina |
| CAR-002 + CAR-003 | VALIDÉE | divergence future entre trajectoire et transition | contrats internes distincts; extraction si modèles, équipe, charge, SLO ou données divergent |
| ORI-001 + ORI-002 | VALIDÉE FORTE | Decision Support pourrait devenir transversal | aucune autorité indépendante; extraction si consommation hors Orientation devient structurante |
| REC-001 + RSH-001 logical | VALIDÉE TEMPORAIRE | Academic Research Topic peut devenir un domaine produit | module, métriques et contrats internes distincts; revue avant activation académique avancée ou multi-pays |
| EMP-003 Workspace en BFF | VALIDÉE | fuite de logique métier dans la façade | aucun agrégat, datastore métier ou écriture directe; orchestration via contrats seulement |
| INS-001 Workspace en BFF | VALIDÉE PROVISOIRE | workflow institutionnel durable probable | revue DDD obligatoire avant implémentation du workflow institutionnel |
| ADM-001 en Admin plane | VALIDÉE | super-service privilégié | aucune autorité métier; commandes routées vers owners, contrôle d’accès renforcé et audit systématique |

## PRF-001 + PRF-002 — gate renforcé

La fusion reste acceptable parce que les deux responsabilités portent sur le même sujet utilisateur. Elle devient interdite si elle conduit à une table ou un modèle unique sans séparation des sous-domaines.

Avant `ready-for-production`, le profil physique `YD-MS-PRF-001` devra prouver :

- agrégats Profile Core et Education/Experience séparés dans le modèle
- scopes d’accès distincts lorsque les usages le demandent
- politiques de rétention distinctes si les finalités divergent
- journalisation des accès sensibles
- minimisation des projections diffusées aux consommateurs
- interdiction de fournir le dossier complet lorsqu’un consommateur n’a besoin que d’attributs minimaux
- stratégie d’extraction documentée si charge, sécurité, équipe, droit ou rétention divergent

Décision : pas de séparation immédiate. `PRF-002` reste un module fusionné sous gate de production.

## CAR-002 + CAR-003

Transition reste une spécialisation de Career Path tant qu’elle ne possède ni dataset, ni modèle, ni SLO, ni cycle de calcul propres. Une divergence sur l’un de ces axes déclenche une ADR d’extraction.

Décision : fusion maintenue.

## ORI-001 + ORI-002

Decision Support reste interne au dossier Orientation. Une frontière physique séparée créerait actuellement du chatter sans source autoritative propre.

Décision : fusion maintenue. Une consommation massive par d’autres domaines déclenche une nouvelle revue.

## REC-001 + RSH-001 — gate renforcé

`RSH-001` reste un moteur spécialisé de recommandation tant qu’il ne possède pas d’agrégat autoritatif durable.

La fusion cesse d’être valide dès qu’au moins une responsabilité suivante apparaît :

- catalogue autoritatif de sujets de recherche
- soumission ou validation de sujets
- gestion d’encadrants
- gestion de mémoires, thèses ou soutenances
- workflow académique de validation
- marketplace ou mise en relation de recherche
- règles de propriété intellectuelle propres au domaine recherche

Dans ce cas, une nouvelle frontière `Research` devra être étudiée avant implémentation.

Décision : fusion temporaire maintenue.

## INS-001 — décision avant développement

`INS-001` reste aujourd’hui une façade logique. Le risque est élevé qu’une institution ait demain un workflow durable : revendication d’établissement, vérification, soumission de programme, correction, validation, délégation, publication et historique.

Règle : aucun de ces états ne doit être stocké dans le BFF.

Avant implémentation d’un workflow institutionnel, une revue DDD tranche entre :

1. workflow détenu par les owners EDU lorsque l’état appartient directement à leurs agrégats
2. microservice dédié `Institution Workflow` si le processus possède cycle de vie, invariants, permissions et audit propres

Décision : BFF maintenu uniquement comme façade. L’apparition d’un workflow durable bloque son implémentation dans le BFF jusqu’à décision DDD.

## EMP-003 et ADM-001

Ces composants ne possèdent aucun état métier autoritatif. Les écritures passent par les APIs des owners. Les accès privilégiés de l’Admin plane sont explicitement autorisés, à durée minimale lorsque possible et transmis à Audit.

## Registre de surveillance des fusions

| Élément | Revue obligatoire | Signal d’alerte |
|---|---|---|
| PRF-002 | avant production Burkina puis à chaque changement majeur de privacy | rétention, permissions, équipe ou scaling distincts |
| RSH-001 | avant fonctions académiques avancées et avant multi-pays | apparition d’un agrégat Research autoritatif |
| INS-001 | avant tout workflow institutionnel durable | états/invariants propres au processus institutionnel |
| CAR-003 | avant modèles spécialisés de reconversion | dataset/modèle/SLO distinct |
| ORI-002 | avant exposition transversale | consommation hors Orientation structurante |

## Conclusion

Aucune fusion actuelle n’impose une séparation immédiate. Trois gates deviennent normatifs : `PRF-002` avant production Burkina, `RSH-001` avant extension du domaine recherche et `INS-001` avant tout workflow institutionnel durable. Ces décisions devront être reflétées dans les futurs `AUTONOMY_PROFILE.md`, ADR et contrats.
