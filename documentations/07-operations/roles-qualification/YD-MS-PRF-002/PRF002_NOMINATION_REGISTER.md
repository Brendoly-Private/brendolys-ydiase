---
document_id: "YD-DOC-OPS-PRF-002-NOMINATION-REGISTER"
title: "PRF002_NOMINATION_REGISTER — Tableau de nomination"
document_type: "operations-reference"
document_role: "Documente une référence opérationnelle de qualification et nomination des rôles concernés."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "operations"
created_at: "2026-10-05"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# PRF002_NOMINATION_REGISTER — Tableau de nomination

> **Rôle du document**
> Documente une référence opérationnelle de qualification et nomination des rôles concernés.
> **Usage développement :** référence de support pour la conception et la préparation opérationnelle.

Statut : `READY-TO-FILL / NOMINATIONS-PENDING`
Service : `YD-MS-PRF-002 — Education & Experience Profile`
Nature : `AUTH`
Criticité : `C1`
Référence normative : `PRF002_NOMINATION_MATRIX.md`

## 1. Objet

Ce registre sert à enregistrer les désignations humaines requises par la matrice de nomination PRF-002.

Une ligne n'est considérée complète que si le titulaire, le suppléant, la date de désignation, l'approbateur et la preuve sont renseignés et cohérents avec `PRF002_NOMINATION_MATRIX.md`.

## 2. Tableau prêt à remplir

| ID | Rôle | Titulaire | Suppléant | Date de désignation | Approbateur de la désignation | Preuve attendue | Référence de preuve | Statut |
|---|---|---|---|---|---|---|---|---|
| `OWN-PRF2-BUS` | Owner métier PRF-002 | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + périmètre métier + acceptation du rôle | À RENSEIGNER | `PENDING` |
| `OWN-PRF2-DR` | Responsable Restore/DR PRF-002 | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + habilitation DR + preuve d'exercice pratique | À RENSEIGNER | `PENDING` |
| `OWN-PRF2-OPS` | Responsable Operations/SRE PRF-002 | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + habilitation exploitation + preuve d'exercice incident/readiness | À RENSEIGNER | `PENDING` |
| `OWN-PRF2-BKP` | Responsable Backup PRF-002 | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + habilitation backup + preuve de test de restauration | À RENSEIGNER | `PENDING` |
| `OWN-ARCH` | Responsable Architecture YDIASE | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + périmètre d'autorité architecture | À RENSEIGNER | `PENDING` |
| `OWN-SEC` | Responsable Sécurité | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + périmètre Security + habilitations/revue des responsabilités C1 | À RENSEIGNER | `PENDING` |
| `OWN-PRIV` | Responsable Privacy/Conformité | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + périmètre Privacy/Conformité + compétence applicable au pilote | À RENSEIGNER | `PENDING` |
| `OWN-DATA-GOV` | Responsable Data Governance | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + périmètre provenance/lineage/qualité | À RENSEIGNER | `PENDING` |
| `OWN-CONTRACT` | Responsable Contract Registry | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + périmètre API/events/contracts | À RENSEIGNER | `PENDING` |
| `OWN-INFRA` | Responsable Infrastructure | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + habilitation infrastructure/DR + preuve d'exercice pratique | À RENSEIGNER | `PENDING` |
| `OWN-CAPACITY` | Responsable Capacity/Product Analytics | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + périmètre capacity/analytics + modèle de charge revu | À RENSEIGNER | `PENDING` |
| `OWN-PRODUCT-FIN` | Responsable Product/Finance | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + périmètre Product/Finance + responsabilité BIA/MTPD | À RENSEIGNER | `PENDING` |
| `OWN-CONSUMERS` | Coordinateur des owners consommateurs PRF-002 | À RENSEIGNER | À RENSEIGNER | AAAA-MM-JJ | À RENSEIGNER | Décision de nomination + liste des consommateurs couverts + mandat de coordination | À RENSEIGNER | `PENDING` |

## 3. Contenu minimal d'une preuve de nomination

La preuve référencée dans chaque ligne doit permettre d'établir au minimum :

- le nom complet du titulaire ;
- le rôle PRF-002 attribué ;
- le périmètre exact de responsabilité ;
- la date d'effet ;
- le nom complet du suppléant ;
- l'autorité ayant approuvé la désignation ;
- l'acceptation du rôle par le titulaire ;
- les éventuelles limites ou délégations ;
- la date de prochaine revue si applicable.

Pour `OWN-PRF2-DR`, `OWN-PRF2-OPS`, `OWN-PRF2-BKP`, `OWN-SEC` et `OWN-INFRA`, joindre également la référence d'une validation pratique ou d'un exercice correspondant au rôle avant première astreinte autonome.

## 4. Statuts autorisés

- `PENDING` : nomination incomplète ;
- `NOMINATED` : titulaire et suppléant officiellement désignés ;
- `QUALIFIED` : compétences et exercice requis vérifiés ;
- `ACTIVE` : rôle effectif et habilitations cohérentes ;
- `SUSPENDED` : rôle temporairement non utilisable ;
- `REVOKED` : nomination retirée ;
- `EXPIRED` : nomination ou habilitation arrivée à échéance.

Seuls les rôles `ACTIVE` peuvent signer une validation conduisant à `VERIFIED`.

## 5. Contrôle avant activation

Avant passage d'une ligne à `ACTIVE`, vérifier :

1. titulaire et suppléant renseignés ;
2. preuve de nomination disponible ;
3. approbateur identifié ;
4. compétences requises dans `PRF002_NOMINATION_MATRIX.md` confirmées ;
5. exercice pratique effectué lorsqu'il est obligatoire ;
6. habilitations techniques alignées sur le rôle ;
7. aucun conflit interdit de séparation des pouvoirs ;
8. contrôle compensatoire documenté pour tout cumul toléré ;
9. suppléant réellement capable d'assurer la fonction ;
10. référence de preuve archivée.

## 6. Contrôle global avant VERIFIED

PRF-002 ne peut être déclaré `VERIFIED` tant qu'un rôle requis pour HYP-001 à HYP-020 reste `PENDING`, `SUSPENDED`, `REVOKED` ou `EXPIRED`.

Les rôles nécessaires au scénario de validation doivent être `ACTIVE`, leurs preuves disponibles et les validations croisées prévues dans `PRF002_NOMINATION_MATRIX.md` enregistrées.

Statut actuel : `NOMINATIONS-PENDING — TABLE READY TO FILL`.
