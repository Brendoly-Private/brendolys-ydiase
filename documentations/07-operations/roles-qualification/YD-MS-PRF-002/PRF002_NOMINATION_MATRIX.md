---
document_id: "YD-DOC-OPS-PRF-002-PRF002-NOMINATION-MATRIX"
title: "PRF002_NOMINATION_MATRIX"
document_type: "operations-reference"
document_role: "Documente une référence opérationnelle de résilience, reprise, preuve ou qualification."
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

# PRF002_NOMINATION_MATRIX

> **Rôle du document**
> Documente une référence opérationnelle de résilience, reprise, preuve ou qualification.
> **Usage développement :** référence de support pour la conception et la préparation opérationnelle.

Statut : PREPROD-CANDIDATE
Service : YD-MS-PRF-002 - Education & Experience Profile
Nature : AUTH
Criticite : C1

## 1. Objet

Cette matrice definit les roles humains necessaires a la validation, l'exploitation et la reprise de PRF-002. Les noms restent TBD-NOMINATION-BLOCKING jusqu'a une nomination humaine tracable.

Une nomination valide contient : nom complet, fonction, perimetre, date d'effet, suppleant, autorite de nomination et reference de decision.

## 2. Matrice des roles

| ID | Role | Titulaire | Competences requises | Suppleant requis | Responsabilites | Validations avant VERIFIED |
|---|---|---|---|---|---|---|
| OWN-PRF2-BUS | Owner metier PRF-002 | TBD-NOMINATION-BLOCKING | DDD metier, agregats PRF-002, temporalite, BIA, continuite | Owner metier delegue | Sens des agregats, MDL, MBCO, tolerance a la perte, integrite metier | HYP-001, 006, 011, 015, 016 et BIA |
| OWN-PRF2-DR | Responsable Restore/DR | TBD-NOMINATION-BLOCKING | Backup/restore, DR, datastore, runbooks, RPO/RTO | Operateur DR habilite | Restaurations, chronometrage, qualification technique, preuves | HYP-005, 008, 013, 014, 017 |
| OWN-PRF2-OPS | Operations/SRE | TBD-NOMINATION-BLOCKING | Observabilite, HA, incident, SLO, readiness, rollback | SRE habilite | Disponibilite, incidents, modes degrades, reouverture | HYP-004, 012, 015 |
| OWN-PRF2-BKP | Backup | TBD-NOMINATION-BLOCKING | Sauvegarde, retention, chiffrement, integrite, restaurabilite | Operateur backup | Protection, monitoring, generations, preuve RPO | HYP-019 |
| OWN-ARCH | Architecture YDIASE | TBD-NOMINATION-BLOCKING | DDD, distribue, API/events, coherence, failure modes | Architecte habilite | Frontieres, dependances, projections, cycles | HYP-003, 009, 016 |
| OWN-SEC | Securite | TBD-NOMINATION-BLOCKING | IAM, secrets, reseau, chiffrement, threat model, incident | Delegue securite | Compromission, isolement, acces privilegies, blast radius | HYP-007, 008, 020 |
| OWN-PRIV | Privacy/Conformite | TBD-NOMINATION-BLOCKING | Finalites, retention, effacement, restrictions, regles pays | Delegue conformite | Decisions Privacy et conformite post-restore | HYP-007, 015, 017 |
| OWN-DATA-GOV | Data Governance | TBD-NOMINATION-BLOCKING | Provenance, lineage, qualite, temporalite, metadonnees | Delegue Data Governance | Provenance et interpretabilite | HYP-018 |
| OWN-CONTRACT | Contract Registry | TBD-NOMINATION-BLOCKING | API/events, versionnement, idempotence, freshness | Delegue contrats | Contrats et projections en mode degrade | HYP-006, 009 |
| OWN-INFRA | Infrastructure | TBD-NOMINATION-BLOCKING | Compute, stockage, reseau, segmentation, DR, capacity | Delegue infrastructure | Copie isolee, reseau DR, zones de panne | HYP-014, 020 |
| OWN-CAPACITY | Capacity/Product Analytics | TBD-NOMINATION-BLOCKING | Charge, metriques, forecasting, volumes, statistiques | Analyste habilite | Croissance, enveloppes de charge, volumes de mutations | HYP-002, 011 |
| OWN-PRODUCT-FIN | Product/Finance | TBD-NOMINATION-BLOCKING | Economie produit, couts d'incident, engagements, BIA | Delegue Product/Finance | Cout d'indisponibilite, contribution au MTPD | HYP-010, 015 |
| OWN-CONSUMERS | Coordination consommateurs | TBD-NOMINATION-BLOCKING | Dependency Map, E2E, modes degrades, coordination | Coordinateur habilite | Validations consommateurs, absence de cascade | HYP-004 |

## 3. Regles de suppleance

Chaque role obligatoire possede un titulaire et au moins un suppleant nominatif avant VERIFIED. Le suppleant doit satisfaire les competences minimales, disposer de ses propres habilitations auditables et participer aux exercices correspondant au role.

Le suppleant ne constitue pas une approbation independante lorsqu'il agit uniquement par delegation du titulaire sur la meme decision. Si titulaire et suppleant sont indisponibles pour un gate obligatoire, le gate reste BLOCKED.

## 4. Separation des pouvoirs

Conflits interdits :

- l'executant DR ne peut pas etre l'unique approbateur du retour a NORMAL-RESTORED ;
- le responsable Backup ne peut pas etre l'unique verificateur de restaurabilite ;
- Infrastructure ne valide pas seul l'isolement DR : Security contre-valide ;
- un role technique ne peut pas approuver seul une exception Privacy ;
- Security ne peut pas auto-approuver seul une exception C1 qu'il a produite ;
- Product/Finance ne valide pas seul le MTPD ;
- Contract Registry ne peut pas transformer seul une projection en autorite de secours ;
- l'Owner metier ne valide pas seul l'integrite technique d'une restauration.

## 5. Cumuls toleres au pilote

| Cumul | Regle compensatoire |
|---|---|
| Operations + DR | Promotion contre-validee par Owner metier ; Security intervient si incident securite |
| Operations + Backup | Restore controle par DR ou un autre operateur habilite |
| Architecture + Contract Registry | Contrats metier approuves par les owners concernes |
| Infrastructure + Operations | Isolement et acces privilegies contre-valides par Security |
| Product/Finance + Capacity | Hypotheses techniques contre-validees par Operations ou Architecture |
| Security + Privacy | Exceptionnel ; seconde validation independante obligatoire pour une decision touchant les deux perimetres |
| Owner metier + Product/Finance | Aucun droit d'auto-validation technique, Security ou Privacy |

Les cumuls sont reexamines avant l'expansion multi-pays.

## 6. Validations necessaires avant VERIFIED

| Gate | Executant principal | Approbations obligatoires | Conditionnelles |
|---|---|---|---|
| Autorite metier PRF-002 | Owner metier | Owner metier + Architecture | Data Governance |
| RPO/MDL metier | Capacity/Backup | Owner metier + Operations | Architecture |
| Continuite sans PRF-002 | Operations/consommateurs | Architecture + owners consommateurs | Owner metier |
| Restore autonome | DR | Owner metier + Operations | Security |
| Contrats post-restore | Contract Registry | Owner metier + Architecture | Privacy |
| Fail-closed Privacy | equipe test | Privacy + Security | Owner metier |
| Corruption/compromission | Security + DR | Security + DR + Operations | Privacy |
| MTPD | Product/Finance | Owner metier + Operations/DR | Privacy/Conformite |
| RTO courant <= 1 h | Operations | Verificateur operationnel distinct | Architecture |
| RTO datastore <= 4 h | DR | Operations + Owner metier | Security |
| RTO majeur <= 8 h | DR + Infrastructure | Operations + Owner metier + Security | Privacy |
| Privacy post-restore | Privacy + DR | Privacy + Owner metier | Security |
| Provenance | Data Governance | Owner metier | Architecture |
| RPO <= 15 min | Backup + DR | Operations + Owner metier | Security |
| Isolement copie DR | Infrastructure | Security + DR | Architecture |

## 7. Promotion vers NORMAL-RESTORED

Panne technique : signatures minimales OWN-PRF2-DR, OWN-PRF2-BUS et OWN-PRF2-OPS.

Corruption, compromission, perte de cles ou rupture d'isolement : ajouter OWN-SEC.

Donnees pouvant etre reintroduites malgre une decision d'effacement ou restriction posterieure au point restaure : ajouter OWN-PRIV.

Restauration depuis la copie isolee : ajouter OWN-INFRA et OWN-SEC.

Une seule personne ne peut jamais etre l'unique executant et l'unique approbateur d'une restauration C1.

## 8. Validation des competences

Avant sa premiere validation C1, chaque titulaire et suppleant doit :

- connaitre son perimetre PRF-002 ;
- connaitre les politiques et ADR applicables ;
- savoir verifier les preuves relevant de son role ;
- connaitre les motifs imposant un refus ;
- disposer uniquement des habilitations necessaires ;
- connaitre la procedure d'escalade ;
- avoir participe a une revue ou un exercice du role.

Pour DR, Operations, Backup, Security et Infrastructure, un exercice pratique est obligatoire avant premiere astreinte autonome.

## 9. Gate VERIFIED

PRF-002 ne peut atteindre VERIFIED tant que :

- un role necessaire aux HYP-001 a HYP-020 reste sans titulaire nominatif ;
- un role obligatoire reste sans suppleant valide ;
- les competences ne sont pas attestees ;
- un conflit de separation des pouvoirs reste non resolu ou non compense ;
- les validations requises ne sont pas enregistrees ;
- les habilitations techniques ne correspondent pas aux responsabilites ;
- une nomination est expiree, revoquee ou ambigue ;
- les preuves BIA/DR requises ne sont pas validees.

Statut actuel : TBD-NOMINATION-BLOCKING - MATRIX DEFINED, HUMAN NOMINATIONS REQUIRED.

Cette matrice n'empeche pas la preparation des plans, runbooks et tests preproduction. Elle interdit de declarer PRF-002 VERIFIED sans gouvernance humaine demonstrable.
