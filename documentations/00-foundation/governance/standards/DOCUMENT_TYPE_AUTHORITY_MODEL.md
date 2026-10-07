---
document_id: "YD-DOC-FND-STD-AUTH-001"
title: "Modèle de type et d'autorité documentaire — BRENDOLYS YDIASE"
document_type: "document-authority-standard"
document_role: "Définit les classes documentaires et leur modèle d’autorité."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "normative"
canonical: true
development_usage: "mandatory-reference"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "foundation"
  - "documentation-governance"
---

# Modèle de type et d'autorité documentaire — BRENDOLYS YDIASE

Statut : `R1-BASELINE / REQUIRED-FOR-R2`

## 1. But

Ce modèle empêche qu'un lecteur humain ou une IA confonde :
- une règle avec une description ;
- une cible avec un état déployé ;
- une décision avec une revue ;
- un plan de test avec une preuve ;
- un registre avec les documents qu'il indexe ;
- une frontière logique avec une frontière physique.

Le chemin d'un fichier n'est jamais, à lui seul, une preuve d'autorité.

## 2. Classes documentaires

| Type | Rôle | Peut être normatif ? | Peut prouver l'exécution ? |
|---|---|---:|---:|
| CONSTITUTION | principes fondateurs et gouvernance documentaire | oui, très haute autorité | non |
| POLICY | règle durable applicable à un scope | oui | non |
| STANDARD | exigences uniformes applicables à une classe d'objets | oui | non |
| REGISTRY | index/état canonique d'objets identifiés | oui pour les entrées qu'il possède | non |
| DOMAIN-MODEL | langage, agrégats, invariants et concepts métier | oui dans son domaine | non |
| SERVICE-DEFINITION | responsabilité logique cible | oui pour la vue logique approuvée | non |
| BOUNDARY-PROFILE | autonomie et contraintes d'une frontière physique | oui pour cette frontière | non |
| CONTRACT | relation/version entre producer et consumer | oui | non |
| DECISION/ADR | décision motivée et contexte | oui pour la décision tant qu'elle n'est pas superseded | non |
| REVIEW | analyse à un instant donné | non par défaut ; peut proposer une décision | non |
| MATRIX | vue croisée/index | seulement sur les cellules explicitement possédées | non |
| PLAN | procédure prévue pour valider/exécuter | non | non |
| RUNBOOK | procédure opérationnelle | oui pour l'action opératoire, pas pour le fait métier | non |
| EVIDENCE | résultat daté et immuable d'une exécution | non comme règle | oui |
| STATUS | photographie d'avancement | non | oui uniquement sur l'état daté qu'elle rapporte |
| GUIDE | aide à la compréhension | non | non |
| README/INDEX | navigation et résumé | non sauf déclaration explicite exceptionnelle | non |
| SOURCE | source externe/interne référencée | selon provenance, jamais automatiquement norme YDIASE | potentiellement |
| HISTORICAL | connaissance conservée pour traçabilité | non | éventuellement historique |

## 3. Dimensions d'autorité

Chaque document peut être qualifié indépendamment selon :

### Normativity
- `NORMATIVE`
- `DESCRIPTIVE`
- `INFORMATIVE`
- `HISTORICAL`

### Temporal state
- `DRAFT`
- `CANDIDATE`
- `ACTIVE`
- `DEPRECATED`
- `SUPERSEDED`
- `RETIRED`

### Reality layer
- `VISION`
- `TARGET`
- `DESIGN`
- `IMPLEMENTATION`
- `DEPLOYMENT`
- `ACTIVATION`
- `EVIDENCE`

Ces dimensions ne doivent plus être compressées dans un seul mot ambigu comme « done ».

## 4. Règles de priorité

En cas de conflit apparent :
1. identifier d'abord le scope exact ;
2. vérifier le type documentaire ;
3. vérifier statut et date/decision ;
4. vérifier la source autoritative enregistrée ;
5. suivre la chaîne de supersession ;
6. appliquer l'ADR spécifique lorsqu'il modifie explicitement une règle générale ;
7. si le conflit reste réel : `CONTRADICTION-OPEN`, jamais résolution silencieuse par une IA.

Une REVIEW plus récente ne remplace pas automatiquement une POLICY.
Un README ne remplace pas un registre.
Une matrice ne remplace pas le document owner si elle n'est qu'une vue.
Une EVIDENCE ne change pas la règle testée.
Un plan de test réussi n'existe pas tant qu'une Evidence ne l'atteste pas.

## 5. Règle target / implementation / deployment / activation

Ces états sont orthogonaux.

Exemple :
- frontière définie dans TARGET ;
- aucun code : IMPLEMENTATION=NOT-STARTED ;
- aucun runtime : DEPLOYMENT=NOT-DEPLOYED ;
- non utilisée au Burkina : ACTIVATION=INACTIVE.

Une IA ne doit jamais inférer « existe en production » parce qu'une fiche architecturale est ACTIVE.

## 6. Règle test / evidence

Chaîne :
`Requirement/Policy → Verification Criterion → Test Plan → Test Run → Evidence → Gate Decision`.

Un document `*_TEST_PLAN.md` n'est jamais une preuve.
Une matrice `*_EVIDENCE_MATRIX.md` sans résultat daté/référence d'exécution n'est qu'une structure d'evidence.

## 7. Règle Registry / source documents

Un Registry peut être canonique pour :
- l'identité d'une entrée ;
- son statut ;
- son owner ;
- sa relation principale.

Les détails vivent dans les documents qu'il référence.

Exemple :
`AUTONOMY_PROFILE_REGISTER` est canonique comme index des frontières/profils ; chaque `AUTONOMY_PROFILE.md` porte les détails de la frontière.

## 8. Métadonnées de migration

À terme, les documents doivent pouvoir exposer au minimum :

```yaml
document:
  id: ...
  type: POLICY
  normativity: NORMATIVE
  status: ACTIVE
  reality_layer: TARGET
  authority_scope: ...
  canonical_for: []
  references: []
  supersedes: []
  superseded_by: []
```

Aucune métadonnée inconnue n'est inventée pendant la migration.

## 9. Consigne IA

Avant de modifier YDIASE, une IA doit :
1. identifier les objets concernés ;
2. récupérer leur index ;
3. lire les documents canoniques du scope ;
4. vérifier les ADR/supersessions ;
5. distinguer TARGET de réalité exécutée ;
6. ne charger les Evidence que si la tâche porte sur validation/production ;
7. signaler toute contradiction non résolue.

Statut : `TYPE-AUTHORITY-MODEL-DEFINED / FILE-LEVEL-CLASSIFICATION-PENDING`.
