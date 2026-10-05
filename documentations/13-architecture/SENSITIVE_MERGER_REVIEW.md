# Sensitive Merger Review — BRENDOLYS YDIASE

Statut : `D3-reviewed-controlled`

## Objet

Revue contradictoire des fusions retenues dans `MICROSERVICE_BOUNDARY_REVIEW.md`. Une fusion n’est conservée que si elle respecte les bloqueurs du `MICROSERVICE_AUTONOMY_STANDARD.md` et ne détruit ni ownership, ni sécurité, ni résilience, ni capacité d’extraction future.

## Verdict consolidé

| Fusion | Verdict | Risque principal | Gate de maintien |
|---|---|---|---|
| PRF-001 + PRF-002 | `SUPERSEDED — SEPARATION PHYSIQUE` | cycles de vie, preuve, rétention, permissions et blast radius divergents | ADR accepté le 2026-10-05 |
| CAR-002 + CAR-003 | VALIDÉE | divergence future entre trajectoire et transition | contrats internes distincts; extraction si modèles, équipe, charge, SLO ou données divergent |
| ORI-001 + ORI-002 | VALIDÉE FORTE | Decision Support pourrait devenir transversal | aucune autorité indépendante; extraction si consommation hors Orientation devient structurante |
| REC-001 + RSH-001 logical | VALIDÉE TEMPORAIRE | Academic Research Topic peut devenir un domaine produit | module, métriques et contrats internes distincts; revue avant activation académique avancée ou multi-pays |
| EMP-003 Workspace en BFF | VALIDÉE | fuite de logique métier dans la façade | aucun agrégat, datastore métier ou écriture directe; orchestration via contrats seulement |
| INS-001 Workspace en BFF | VALIDÉE PROVISOIRE | workflow institutionnel durable probable | revue DDD obligatoire avant implémentation du workflow institutionnel |
| ADM-001 en Admin plane | VALIDÉE | super-service privilégié | aucune autorité métier; commandes routées vers owners, contrôle d’accès renforcé et audit systématique |

## PRF-001 + PRF-002 — décision superseded

L'ancienne fusion sous contrôle renforcé n'est plus la cible. La revue métier du domaine `02-identite-profils` a confirmé que le profil courant et l'historique éducatif/professionnel possèdent des sémantiques, temporalités, exigences de preuve, risques de confidentialité et trajectoires de rétention suffisamment distincts pour justifier deux frontières physiques.

Décision canonique : `ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY.md`.

Cible :

- `YD-MS-PRF-001 Profile`
- `YD-MS-PRF-002 Education & Experience Profile`

La fusion ne peut revenir que par un nouvel ADR fondé sur des faits d'exploitation et compatible avec la doctrine de pérennité.

## CAR-002 + CAR-003

Transition reste une spécialisation de Career Path tant qu’elle ne possède ni dataset, ni modèle, ni SLO, ni cycle de calcul propres. Une divergence sur l’un de ces axes déclenche une ADR d’extraction.

Décision : fusion maintenue.

## ORI-001 + ORI-002

Decision Support reste interne au dossier Orientation. Une frontière physique séparée créerait actuellement du chatter sans source autoritative propre.

Décision : fusion maintenue. Une consommation massive par d’autres domaines déclenche une nouvelle revue.

## REC-001 + RSH-001 — gate renforcé

`RSH-001` reste un moteur spécialisé de recommandation tant qu’il ne possède pas d’agrégat autoritatif durable.

La fusion cesse d’être valide dès qu’au moins une responsabilité suivante apparaît : catalogue autoritatif de sujets de recherche, soumission ou validation de sujets, gestion d’encadrants, gestion de mémoires/thèses/soutenances, workflow académique de validation, marketplace de recherche ou règles de propriété intellectuelle propres au domaine recherche.

Décision : fusion temporaire maintenue.

## INS-001 — décision avant développement

`INS-001` reste aujourd’hui une façade logique. Aucun état métier durable ne doit être stocké dans le BFF. Avant implémentation d’un workflow institutionnel, une revue DDD tranche entre ownership EDU et frontière dédiée.

## EMP-003 et ADM-001

Ces composants ne possèdent aucun état métier autoritatif. Les écritures passent par les APIs des owners. Les accès privilégiés de l’Admin plane sont explicitement autorisés, à durée minimale lorsque possible et transmis à Audit.

## Registre de surveillance des fusions

| Élément | Revue obligatoire | Signal d’alerte |
|---|---|---|
| PRF-001 / PRF-002 | uniquement si une future proposition veut les refusionner | nouvel ADR obligatoire |
| RSH-001 | avant fonctions académiques avancées et avant multi-pays | apparition d’un agrégat Research autoritatif |
| INS-001 | avant tout workflow institutionnel durable | états/invariants propres au processus institutionnel |
| CAR-003 | avant modèles spécialisés de reconversion | dataset/modèle/SLO distinct |
| ORI-002 | avant exposition transversale | consommation hors Orientation structurante |

## Conclusion

La fusion PRF est annulée comme cible. Les autres décisions restent sous leurs gates respectifs. Le comptage et les profils d'autonomie doivent être réconciliés avec la nouvelle frontière PRF-002.