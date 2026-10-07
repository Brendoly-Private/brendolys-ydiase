---
document_id: "YD-DOC-EVD-EDUCATION-IMPACT-TEST"
title: "Test d'analyse d'impact — domaine Education"
document_type: "evidence-record"
document_role: "Documente une preuve, un protocole ou une matrice de vérification de la fondation YDIASE."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "evidence"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "evidence"
---

# Test d'analyse d'impact — domaine Education

> **Rôle du document**
> Documente une preuve, un protocole ou une matrice de vérification de la fondation YDIASE.
> **Usage développement :** référence de support pour la gouvernance ou la vérification documentaire.

Statut : `K2-PROOF / DRAFT`

## But

Vérifier que le graphe de connaissance permet de partir d'un changement local et d'identifier les composants, contrats, données et capacités affectés sans relire manuellement tout le dépôt.

## Scénario A — changement de schéma Institution

Changement : `Institution.status` change de sémantique ou devient incompatible.

Impact direct :

1. `YD-MS-EDU-001` possède Institution.
2. `YD-API-EDU-001` expose la validation consommée par `YD-MS-EDU-002`.
3. `YD-EVT-EDU-001 / institution.changed` transporte `status`.
4. `YD-MS-EDU-002` dépend donc du changement pour la création et la validité de ProgramOffering.
5. Les projections Search, Knowledge, Analytics et Institution Workspace qui consomment l'événement doivent être réévaluées.
6. `YD-REQ-EDU-001` et `YD-REQ-EDU-002` doivent être revérifiées.

Verdict : propagation détectable depuis l'owner vers API, événement, consommateur et exigences.

## Scénario B — changement de ProgramVersion

Changement : règle incompatible sur `ProgramVersion`.

Impact direct :

- owner : `YD-MS-EDU-002`
- validation descendante : `YD-API-EDU-002` vers `YD-MS-EDU-003`
- événement : `YD-EVT-EDU-002 / program.changed`
- consommateurs : Curriculum, Search, Knowledge, Analytics, Recommendation et Learning
- exigence : `YD-REQ-EDU-003`

Impact indirect : une nouvelle incompatibilité peut rendre des Curriculum existants non publiables ou nécessiter une nouvelle version, mais EDU-003 ne doit jamais réécrire Program.

## Scénario C — retrait d'un Curriculum publié

Le graphe montre une zone sensible : `YD-MS-EDU-003` publie `YD-EVT-EDU-003`, consommé par Program, Skills, Knowledge, Recommendation et Learning.

Le contrat actuel décrit `curriculum.published`, mais aucun événement explicite de retrait/invalidation de curriculum n'est enregistré dans la baseline consultée.

Décision du test : `GAP-DETECTED`.

Action requise avant D4 : définir la sémantique de retrait, remplacement ou invalidation d'un Curriculum publié et son contrat événementiel. Ne pas inventer ce comportement dans le catalogue K2.

## Scénario D — changement d'une Qualification

Impact :

- owner : `YD-MS-EDU-004`
- événement : `YD-EVT-EDU-005`
- consommateurs directs : Program, Education & Experience Profile, Occupation & Career Graph, Search et Knowledge
- Program ne possède pas l'équivalence
- les décisions pays et sources officielles restent des dépendances externes à réévaluer

## Résultat K2

Le pilote valide le principe du graphe pour :

- ownership
- dépendances synchrones
- événements
- propagation vers consommateurs
- exigences
- ADR de frontière
- détection d'un manque documentaire

Il ne valide pas encore l'exhaustivité globale du dépôt.

## Gate avant généralisation

Avant d'étendre mécaniquement le catalogue aux autres microservices :

1. traiter le gap de retrait/invalidation Curriculum
2. vérifier les identifiants réels des services transversaux référencés par les événements
3. ajouter une validation automatique des références `from/to/owner/consumer`
4. produire au moins un second test d'impact transverse Education → Skills → Recommendation
5. seulement ensuite industrialiser l'extraction des autres domaines
