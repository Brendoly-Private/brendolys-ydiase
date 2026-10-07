---
document_id: "YD-DOC-SYS-ARC-REV-004"
title: "Revue DDD — Domaine Entrepreneurship"
document_type: "ddd-review"
document_role: "Établit la revue DDD des six frontières Entrepreneurship et leurs critères d’autonomie."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "architecture"
---

# Revue DDD — Domaine Entrepreneurship

> **Rôle du document**
> Établit la revue DDD des six frontières Entrepreneurship et leurs critères d’autonomie.
> **Usage développement :** support de décision, preuve ou traçabilité ; la cible canonique active reste autoritative.

Statut : DDD-REVIEW-CLOSED / TARGET-BOUNDARIES-ACCEPTED
Portée : ENT-001 à ENT-006

## Verdict

Les six frontières logiques sont conservées comme candidats autonomes dans la Target Architecture. Elles ne sont pas fusionnées dans ORI, REC, LAB, PRT, EMP ou OPP.

| Service | Décision | Nature cible | Motif de frontière |
|---|---|---|---|
| ENT-001 Venture Profile | KEEP-SEPARATE | AUTH | cycle de vie et invariants du projet entrepreneurial |
| ENT-002 Entrepreneurial Opportunity Intelligence | KEEP-SEPARATE | DERIVED/MIXED | calcul, provenance, fraîcheur et charge distincts des signaux LAB |
| ENT-003 Entrepreneurship Support Ecosystem | KEEP-SEPARATE | AUTH | catalogue d'accompagnement distinct de la relation partenaire PRT |
| ENT-004 Funding Opportunity | KEEP-SEPARATE | AUTH/MIXED | règles d'éligibilité, fraîcheur et sensibilité spécifiques au financement |
| ENT-005 Founder & Team Matching | KEEP-SEPARATE | DERIVED/MIXED | consentement, matching, privacy et calcul spécifiques |
| ENT-006 Venture Progression | KEEP-SEPARATE | AUTH | plans, expérimentations, jalons et historique de progression à cycle propre |

KEEP-SEPARATE confirme la frontière d'autonomie cible. La topologie physique reste soumise aux ADR techniques et Capacity Profiles ; aucune fusion ne peut supprimer l'ownership défini ici.

## ENT-001 vs PRF
PRF possède la personne, ses objectifs personnels et contraintes personnelles. ENT-001 possède le projet entrepreneurial et ses objectifs/contraintes propres. Une même personne peut avoir plusieurs ventures ; un Venture ne doit pas devenir une extension du UserProfile.

## ENT-001 vs ENT-006
ENT-001 porte l'identité et l'état courant du projet. ENT-006 porte le processus longitudinal de progression : plan, hypothèses, expérimentations, jalons et résultats. La séparation évite de transformer le cœur Venture en journal/process engine à forte croissance.

## ENT-002 vs LAB
LAB possède les signaux et mesures économiques/travail. ENT-002 possède l'interprétation entrepreneuriale sourcée de ces signaux sous forme d'hypothèses/opportunités. Il référence les snapshots LAB ; il ne recalcule pas silencieusement leur vérité.

## ENT-003 vs PRT
PRT possède Partner/Agreement/AccessScope. ENT-003 possède l'offre d'accompagnement utilisable par un entrepreneur. Une organisation peut être partenaire sans fournir un programme entrepreneurial et inversement une ressource publique cataloguée n'implique pas un Partnership.

## ENT-004 vs BIL
ENT-004 catalogue des opportunités de financement externes et leur éligibilité. BIL gère l'économie commerciale de YDIASE. Aucune transaction bancaire, scoring de crédit ou décision du financeur n'est possédée par ENT-004.

## ENT-005 vs REC
REC classe des options d'orientation. ENT-005 calcule des complémentarités entre personnes/équipe dans un contexte entrepreneurial sous consentement. Les deux peuvent partager des capacités techniques de ranking sans partager l'ownership.

## Dépendances autorisées
PRF/SKL/ASM/CNS/CFG → ENT selon finalité ; LAB/DAT/KNW → ENT-002 ; PRT → ENT-003/004 ; EDU/LRN → ENT-003/006 ; ENT → ORI/REC ; ENT → EMP/OPP lors du passage vers recrutement/création d'opportunités.

## Dépendances interdites
Pas de DB croisée. Pas d'écriture ENT dans PRF/SKL/LAB. Pas de Venture créé par REC/AI. Pas de financement garanti. Pas de matching fondateur sans consentement/visibilité. Pas de chaîne synchrone ENT-002 → LAB → Analytics → AI → ENT-002.

## Hyperscale
ENT-001 : partitionnement naturel par venture/owner et lectures cacheables selon visibilité.
ENT-002 : calculs lourds asynchrones, partitionnement territoire/secteur/version, résultats versionnés.
ENT-003 : lecture dominante, cache/edge possible, invalidation par version/fraîcheur.
ENT-004 : lecture dominante, forte exigence de fraîcheur/expiration et provenance.
ENT-005 : workloads matching asynchrones, privacy-first, candidate sets bornés/partitionnés.
ENT-006 : écritures longitudinales par venture, append/history selon design, projections pour lectures.

Les valeurs RPS/QPS, stockage et latence restent à quantifier dans les Capacity Profiles.

## Conclusion
DDD-ACCEPTED : 6 frontières Entrepreneurship conservées dans la cible complète.
K3/K4/K5 : non attribués par cette revue.
