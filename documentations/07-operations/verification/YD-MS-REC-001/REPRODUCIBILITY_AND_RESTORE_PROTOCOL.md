---
document_id: "YD-DOC-OPS-REC-001-REPRODUCIBILITY-AND-RESTORE-PROTOCOL"
title: "YD-MS-REC-001 — Reproducibility and Restore Protocol"
document_type: "operations-verification"
document_role: "Définit un protocole ou plan de vérification opérationnelle servant de preuve contrôlée."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "evidence"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "operations"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-REC-001 — Reproducibility and Restore Protocol

> **Rôle du document**
> Définit un protocole ou plan de vérification opérationnelle servant de preuve contrôlée.
> **Usage développement :** référence de support pour la conception, la vérification ou la contextualisation concernée.

Statut : `TEST-PROTOCOL-DEFINED / NOT-EXECUTED`

## Objectif

Vérifier qu'un run REC peut être audité/reproduit dans les limites de ses versions et que les états persistants REC peuvent être restaurés sans transformer les données sources en propriété REC.

## Préconditions

Identifier run_id, policy/model/candidate-generation versions, evidence snapshot, versions sources, décision Privacy, contexte, dataset de test, environnement, commit et reviewer.

## Reproductibilité

1. sélectionner un run de référence gouverné ;
2. restaurer exactement les versions/configurations disponibles ;
3. fournir le même evidence snapshot ou fixture équivalente versionnée ;
4. recalculer ;
5. comparer éligibilité, abstention, score/rang organique, incertitude et explication structurée ;
6. documenter toute non-déterminisme autorisé ;
7. vérifier qu'aucun facteur commercial n'explique une différence organique.

Toute divergence hors tolérance explicitement approuvée vaut FAIL.

## Restore

1. capturer l'état REC de référence ;
2. restaurer runs/résultats persistants, evidence snapshots minimisés, policies/configurations et métadonnées d'audit ;
3. vérifier versions et références vers les autorités sources ;
4. vérifier décisions Privacy et état de fraîcheur ;
5. tester un échantillon de reproductibilité ;
6. rouvrir uniquement après contrôles d'intégrité.

REC ne restaure jamais EDU/SKL/CAR/LAB/OPP/LRN/KNW/PRF à partir de ses snapshots.

## Scénarios critiques

- UNKNOWN reste distinct de FAILED ;
- contrainte HARD échouée non compensée par scoring ;
- source stale/conflictuelle entraîne abstention/dégradation gouvernée ;
- ancien run reste daté/versionné ;
- SPN n'altère aucun score/rang/pondération/exclusion/explication organique ;
- correction source crée un nouveau run ou invalide l'ancien sans réécriture silencieuse ;
- Privacy non vérifiable entraîne fail-closed ou mode explicitement autorisé.

## PASS

PASS exige intégrité du restore, traçabilité des versions, reproductibilité conforme aux règles approuvées et absence de violation des invariants critiques.

Le protocole seul n'est pas une preuve K5.
