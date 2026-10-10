---
document_id: "YD-DOC-CON-ENT-VENTURE-V1-DRAFT"
title: "YD-CTR-ENT-VENTURE-v1 — contrat logique proposé"
document_type: "contract-baseline"
document_role: "Spécifie une interface logique Entrepreneurship candidate avant enregistrement canonique."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
created_at: "2026-10-10"
last_reviewed_at: "2026-10-10"
tags:
  - "contracts"
---

# YD-CTR-ENT-VENTURE-v1

**Statut : PROPOSED / NOT-REGISTERED / K3-NOT-PASS.** ID candidat déjà tracé dans la revue d'arbitrage Entrepreneurship, pas une entrée ACTIVE-LOGICAL du Contract Registry.

## Parties et autorité
- Producteur : `YD-MS-ENT-001`.
- Consommateurs candidats : ENT-005, ENT-006; ORI uniquement après approbation. Aucune autorisation implicite n'est accordée par cette liste.
- Type logique proposé : `HYBRID` ; criticité contractuelle candidate : `K1`.
- Règle d'ownership : VentureRef, stage, state et version relèvent d'ENT-001; PRF reste autorité des personnes.

## Schéma logique candidat
Champs métier proposés : `VentureRef:string; stage:string; state:string; aggregate_version:integer; visibility_scope:string`.
Enveloppe de publication si événement/projection : `contract_id:string`, `contract_version:string`, `event_id:string`, `aggregate_ref:string`, `aggregate_version:integer`, `occurred_at:datetime`, `event_type:string`, `country_scope:string`, `trace_ref:string`.

Les champs de l'enveloppe sont obligatoires **uniquement pour les messages publiés** ; pour une API, une enveloppe de requête/réponse adaptée doit être spécifiée. Types exacts, cardinalités, contraintes null, identifiants et listes d'énumérations doivent encore être approuvés.

## Sémantique et cycles de vie
- Événements ou transitions candidats : VentureCreated, VentureUpdated, VentureWithdrawn.
- Une publication est conditionnée par source, autorisation, statut et contexte territorial valides.
- `WITHDRAW`, `EXPIRE`, `DELETE` et `REVOKE` ne sont pas interchangeables : effet et applicabilité à préciser par opération.
- Invariant spécifique : Toute exposition d'une équipe requiert des références PRF autorisées; une Venture retirée ne peut être réactivée par replay.
- Répétition idempotente via `event_id` pour événements et `request_ref` pour commandes ; ordre par `aggregate_version`, jamais par ordre global.
- Une révocation ou un retrait de version supérieure prime sur un ancien UPSERT. Une projection expose snapshot, watermark et rattrapage si nécessaire.

## Confidentialité, version et erreurs
- Classification candidate : `SENSITIVE / CONTEXTUAL` ; décision finale conditionnée à l'analyse de finalité, audience, pays, visibilité et consentement CNS.
- Version logique : `v1` candidate. Ajout optionnel compatible ; changement de champ requis ou de sens impose version majeure ; enum inconnu = `UNKNOWN/UNSUPPORTED` ou refus contrôlé.
- Erreurs candidates : `UNAUTHORIZED`, `FORBIDDEN_PURPOSE`, `NOT_VISIBLE`, `NOT_FOUND`, `VERSION_CONFLICT`, `SOURCE_STALE`, `WITHDRAWN`, `DEPENDENCY_UNAVAILABLE`. Leur applicabilité et leur représentation restent à définir pour chaque opération.
- Aucune réexécution d'effet externe irréversible pendant replay. Aucune base partagée ni lecture directe des bases PRF/SKL/PRT/LAB/DAT.

## Vérification requise avant promotion canonique
1. Approbation des propriétaires, consommateurs et finalités ; rattachement des exigences K3 et ADR structurants.
2. Décision sur champs obligatoires, facultatifs, types, enums, payloads de commandes, réponses et événements, erreurs par opération.
3. Politique effective de retrait, suppression, rétention, provenance/licences, pays et consentement.
4. Inscription approuvée dans `documentations/04-contracts/indexes/CONTRACT_REGISTRY.md` et alignement avec les baselines des services.
5. Revue des tests P0/P1 de `documentations/04-contracts/validation/CONTRACT_V1_VALIDATION_MATRIX.md` ; aucune preuve d'exécution n'est revendiquée.

**Verdict : DRAFT, K3-NOT-PASS, PHYSICAL-CONTRACTS-NOT-VERIFIED.**
