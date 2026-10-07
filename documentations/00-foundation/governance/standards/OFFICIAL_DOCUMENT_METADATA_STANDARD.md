# Standard officiel des métadonnées documentaires — BRENDOLYS YDIASE

**ID :** YD-STD-DOC-META-001  
**Statut :** APPROVED / NORMATIVE  
**Portée :** tous les fichiers documentaires canoniques sous `documentations/`

## 1. Objet

Chaque document YDIASE doit être compréhensible par un humain et exploitable par les outils, agents IA, validateurs et workflows de développement.

Le standard permet de répondre sans interprétation à : quel est ce fichier, à quoi sert-il, quelle autorité possède-t-il, quels éléments du produit concerne-t-il, doit-il être respecté pendant le développement, quelles autres sources gouvernent son contenu, et quel est son état réel.

## 2. Identité institutionnelle canonique

Le produit s'appelle **BRENDOLYS YDIASE**.

Mention institutionnelle canonique :

> BRENDOLYS YDIASE est une initiative portée par BRENDOLYS INTELLIGENCE.

Contact institutionnel :
- e-mail : contact@brendolys-intelligence.com
- téléphone : +226 74 63 50 77

Ces valeurs sont déclarées une seule fois dans `_meta/identity/YDIASE_INSTITUTIONAL_IDENTITY.yaml`. Les documents utilisent `institutional_reference: YDIASE-INSTITUTIONAL-IDENTITY` plutôt que de recopier manuellement ces coordonnées.

## 3. Front matter YAML obligatoire

Tout nouveau fichier Markdown canonique doit commencer par un front matter YAML.

Champs obligatoires :

```yaml
---
document_id: YD-DOC-...
title: "..."
document_type: "..."
document_role: "..."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "normative|canonical-source|reference|view|evidence|historical"
canonical: true
development_usage: "mandatory-reference|supporting-reference|informational|not-applicable"
created_at: "YYYY-MM-DD"
last_reviewed_at: "YYYY-MM-DD"
---
```

`document_role` doit être une phrase courte expliquant à quoi sert précisément le fichier. Le nom du fichier seul n'est jamais considéré comme une description suffisante.

## 4. Champs conditionnels

Selon le document :

```yaml
owners:
  - "..."
domains:
  - "..."
capabilities:
  - "YD-CAP-..."
services:
  - "YD-SVC-..."
microservices:
  - "YD-MS-..."
platform_components:
  - "YD-PLT-..."
contracts:
  - "YD-CTR-..."
decisions:
  - "ADR-..."
countries:
  - "BF"
maturity:
  knowledge: "K0|K1|K2|K3|K4|K5|K6"
implementation_status: "not-started|in-progress|implemented|not-applicable"
deployment_status: "not-deployed|deployed|not-applicable"
activation_status: "inactive|active|partial|not-applicable"
evidence_required: true
depends_on:
  - "document_id"
supersedes:
  - "document_id"
superseded_by: null
review_cycle: "..."
tags:
  - "..."
```

Un champ inconnu reste absent ou explicitement UNKNOWN selon le schéma applicable. Une valeur ne doit jamais être inventée pour compléter le header.

## 5. Bloc humain « Rôle du document »

Après le titre, tout document substantiel doit contenir un bloc court :

```markdown
> **Rôle du document**
> Ce document définit ...
> **Usage développement :** référence obligatoire / support / information.
```

Le bloc explique l'intention ; le YAML porte la donnée structurée. Il ne faut pas dupliquer tout le front matter dans le texte.

## 6. Niveaux d'autorité

- `normative` : impose une règle à son périmètre.
- `canonical-source` : source unique d'une vérité documentaire.
- `reference` : décrit ou explique en référant aux sources.
- `view` : calculable/régénérable ; ne crée pas de vérité.
- `evidence` : preuve d'un test, contrôle ou état observé.
- `historical` : conservé pour traçabilité ; ne gouverne pas le développement courant.

`canonical: true` n'est permis que lorsque le fichier est l'emplacement canonique de son information.

## 7. Usage développement

- `mandatory-reference` : le code, contrat, schéma, test ou configuration concerné ne doit pas contredire le document.
- `supporting-reference` : doit être consulté mais ne prévaut pas sur une source normative/canonique.
- `informational` : contexte utile sans contrainte directe.
- `not-applicable` : aucun usage de développement.

Un élément ne peut atteindre FEATURE/MODULE/MICROSERVICE-READY-FOR-DEVELOPMENT si une référence obligatoire applicable est UNKNOWN, contradictoire, superseded sans successeur résolu ou porte un gap bloquant.

## 8. Règle de priorité en cas de contradiction

La priorité ne dépend pas du fichier le plus récent seulement. On résout : statut actif applicable → source canonique du fait → décision/ADR applicable → standard normatif → contrat canonique → document de support. Une contradiction non résolue bloque la readiness du périmètre affecté.

Un ADR ne réécrit pas silencieusement une source : les documents affectés sont réconciliés.

## 9. Identifiants

`document_id` est stable malgré un renommage de fichier. Il n'est jamais réutilisé après retrait.

Familles recommandées : `YD-DOC-FND`, `YD-DOC-PRD`, `YD-DOC-DOM`, `YD-DOC-SYS`, `YD-DOC-CTR`, `YD-DOC-DEC`, `YD-DOC-TRUST`, `YD-DOC-OPS`, `YD-DOC-CTY`, `YD-DOC-META`.

Les ADR et contrats conservent leurs IDs spécialisés existants ; `document_id` peut référencer l'identifiant canonique déjà établi afin d'éviter un second système d'identité.

## 10. Personnalisation par type de fichier

Le même header ne signifie pas le même contenu. `document_role`, relations, owners et usage développement sont spécifiques au fichier.

Exemples :
- domaine : frontières métier, vocabulaire et invariants ;
- microservice : ownership, modules, fonctionnalités, NFR et architecture ;
- contrat : interface/version/compatibilité ;
- ADR : décision, alternatives, conséquences ;
- runbook : procédure opérationnelle ;
- evidence : preuve reproductible ;
- view/index : agrégation dérivée.

Le clone-and-rename de métadonnées spécifiques est interdit.

## 11. Migration de l'existant

La migration est progressive et contrôlée :
1. créer identité, schéma et template ;
2. valider les nouveaux documents ;
3. inventorier les fichiers existants ;
4. attribuer IDs/rôles/autorité sans modifier leur sens métier ;
5. détecter duplications et contradictions ;
6. intégrer au Knowledge Gate ;
7. migrer famille par famille ;
8. interdire les nouveaux fichiers non conformes après gate d'adoption.

L'absence temporaire de front matter sur un ancien fichier signifie `LEGACY-METADATA-PENDING`, pas invalidité de son contenu.

## 12. Critères d'acceptation

Le standard est correctement appliqué lorsque :
- chaque nouveau document est identifiable et auto-descriptif ;
- les coordonnées institutionnelles n'existent qu'à la source centrale ;
- un outil peut calculer les relations document → domaine → capacité → service → microservice → contrat → décision → test/preuve ;
- le développement peut déterminer automatiquement les références obligatoires ;
- une vue générée ne devient pas source de vérité ;
- aucun statut d'implémentation/déploiement n'est déduit de la seule documentation.
