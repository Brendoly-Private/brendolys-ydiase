---
document_id: "YD-DOC-SYS-ENT-K3-REQUIREMENTS-PRIVACY-REVIEW"
title: "Entrepreneurship — revue de traçabilité K3 exigences et Privacy"
document_type: "architecture-review"
document_role: "Rapproche huit propositions contractuelles Entrepreneurship des exigences et politiques CNS en distinguant les preuves des lacunes."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
created_at: "2026-10-11"
last_reviewed_at: "2026-10-11"
tags:
  - "systems"
  - "contracts"
  - "privacy"
---

# Entrepreneurship — revue K3 des exigences et Privacy

**Verdict : REVIEW-OPEN / K3-NOT-PASS.** Ce document de revue n'active aucun contrat, ne modifie aucune source canonique et ne valide aucune règle juridique pays.

## Références effectivement examinées

- `documentations/00-foundation/governance/registers/REFERENTIEL_EXIGENCES.md` (exigences actives).
- `documentations/06-trust/privacy/YD-MS-CNS-001/PRIVACY_DECISION_POLICY.md` (normative, validation juridique par pays en attente).
- `documentations/03-systems/architecture/target/ENTREPRENEURSHIP_DEPENDENCY_OWNERSHIP_MAP.md`.
- `documentations/03-systems/architecture/reviews/ENTREPRENEURSHIP_K3_OWNERSHIP_ARBITRAGE.md`.
- Les huit `K3_*_CONTRACT_SPEC.md` dans les six dossiers ENT de `04-contracts/baselines/`.

## Traçabilité transversale (exigence existante → vérification à produire)

| Exigence active | Application aux contrats ENT | Preuve encore requise |
|---|---|---|
| YD-REQ-GOV-001 | Owner ENT et source autoritative externe identifiés | Vérifier ownership champ par champ et cas MIXED |
| YD-REQ-GOV-002 | Finalité, droits, accès, rétention, suppression pour toute donnée personnelle | Matrice Privacy par champ, destinataire, pays et durée |
| YD-REQ-DATA-001 | Provenance, version, validité, droits d'usage | License/source manifest et politique de correction |
| YD-REQ-DATA-002 | Assertions contradictoires distinctes | Tests de contradiction pour hypothèses et opportunités |
| YD-REQ-DER-001 | Aucun fait irremplaçable en DERIVED | Arbitrage ENT-002, ENT-005 et preuve de reconstruction |
| YD-REQ-DER-002 | FULL_REBUILD/replay/watermark/convergence | Plans et tests de reconstruction, non réalisés |
| YD-REQ-SVC-002 | Aucun accès direct à la base d'un autre service | Contrôle dépendances et interfaces |
| YD-REQ-IAM-003 | Token valide insuffisant pour autoriser un acte métier | Matrice objet/action/finalité et tests de refus |
| YD-REQ-CTR-001 | Owner, consommateurs, version, compatibilité, évolution | Revue et inscription des contrats approuvés au registre |
| YD-REQ-CTR-002 | Pas de technologie imposée sans ADR | ADR pour tout transport ou décision structurelle retenue |
| YD-REQ-CTY-001 | Country Framework avant activation pays | Revue pays et CFG, aucun pays activé par ce document |

## Matrice de revue des huit propositions

| Contrat candidat | Risque spécifique | Exigence / politique pertinente | Décision encore ouverte |
|---|---|---|---|
| YD-CTR-ENT-VENTURE-v1 | Exposition du projet et des liens personnes | GOV-002, IAM-003, CNS | Visibilité par rôle, bénéficiaires autorisés, conservation |
| YD-CTR-ENT-OPPORTUNITY-HYPOTHESIS-v1 | Hypothèse prise pour un fait, source non licenciée | DATA-001/002, DER-001/002 | Critères de preuve, incertitude, invalidation, droits de source |
| YD-CTR-ENT-SUPPORT-CATALOG-v1 | Organisation partenaire projetée comme owner ENT | GOV-001, DATA-001 | Publication PRT, droit de correction et de retrait |
| YD-CTR-ENT-FUNDING-CATALOG-v1 | Financement expiré ou fausse garantie | DATA-001, CTY-001 | Fraîcheur, source, échéance et avertissement public |
| YD-CTR-ENT-FUNDING-ELIGIBILITY-v1 | Profilage financier sensible, décision assimilée à octroi | GOV-002, IAM-003, CNS | Finalité et autorisation, minimisation, conservation, fail-closed |
| YD-CTR-ENT-TEAM-NEED-v1 | Identification involontaire de personnes/équipes | GOV-002, IAM-003, CNS | Pseudonymisation, visibilité, révocation et suppression |
| YD-CTR-ENT-FOUNDER-MATCH-v1 | Divulgation des candidats et scores | GOV-002, DER-002, CNS | Grant/restrictions, explication minimale, expiration et retrait |
| YD-CTR-ENT-VENTURE-PROGRESS-v1 | Divulgation de validations et progrès internes | GOV-002, IAM-003, CNS | Public/privé, validation et correction des résultats |

## CNS — exigences non négociables déjà établies

1. Chaque traitement personnel gouverné porte un `purpose_ref` explicite ; la base légale n'est pas systématiquement le consentement.
2. Une `PrivacyDecision` `NOT-DETERMINABLE` ne vaut jamais `ALLOW`. En l'absence d'une décision obligatoire vérifiable, le traitement concerné est suspendu ou refusé.
3. Une restriction applicable limite effectivement catégories, destinataires, capacités ou durée ; le service ENT n'invente pas une politique concurrente.
4. Les révocations et instructions d'effacement sont versionnées et propagées ; chaque owner ENT exécute les actions sur ses propres données et confirme l'exécution.
5. Les règles pour mineurs, représentation, délais et légalité restent à valider selon le pays ; aucune hypothèse universelle.

## Ordre de fermeture proposé

1. Valider les champs requis, cardinalités, catégories Privacy et consommateurs effectifs des huit contrats.
2. Documenter la matrice par traitement : `purpose_ref`, source autoritative, base applicable à valider, scope, restrictions, rétention, effacement et pays.
3. Rendre explicites les exigences métier spécifiques ENT-001..006 et leurs critères de vérification, sans remplacer le référentiel transversal.
4. Décider avec ADR les frontières MIXED/DERIVED et les choix structurels non triviaux.
5. Vérifier le registre canonique, puis seulement proposer promotion `ACTIVE-LOGICAL` et évaluation K3 service par service.

**Ce document n'est ni une approbation Privacy ni une attestation de conformité juridique.**


## Registre de fermeture décisionnelle — revue du 2026-10-11

Ce tableau est une **liste de décisions à obtenir**, non un registre de décisions adoptées. Une fusion GitHub n'est pas une approbation métier, juridique ou architecturale implicite.

| Clé de revue | Périmètre | Proposition précise | Preuve / approbateur requis | Statut |
|---|---|---|---|---|
| ENT-K3-D01 | ENT-001 | Venture est AUTH ; transitions versionnées, aucune identité PRF dupliquée | owner métier + revue contrat VENTURE | OPEN |
| ENT-K3-D02 | ENT-002 | DERIVED par défaut ; toute annotation non reconstructible est inventoriée séparément comme état AUTH | owner Data/Architecture ; inventaire sources et rebuild | OPEN |
| ENT-K3-D03 | ENT-003 | Catalogue AUTH, organisation PRT seulement projetée | owner PRT et ENT ; revue correction/retrait | OPEN |
| ENT-K3-D04 | ENT-004 | Catalogue et règles YDIASE AUTH, estimation d'éligibilité expirante DERIVED | owner métier, source et Privacy ; pas de décision financeur | OPEN |
| ENT-K3-D05 | ENT-005 | TeamNeed et visibilité AUTH, matches et scores DERIVED, CNS gouverne les droits | owner métier, CNS, Architecture ; revue révocation/rebuild | OPEN |
| ENT-K3-D06 | ENT-006 | Plans et jalons AUTH ; VentureRef externe ENT-001 | owner métier ; revue commandes/versions | OPEN |
| ENT-K3-D07 | Tous | 18 exigences métier candidates approuvées puis enregistrées dans référentiel | gouvernance des exigences ; IDs et tests de vérification | OPEN |
| ENT-K3-D08 | Huit contrats | Types, cardinalités, nullabilité, consommateurs, opérations, erreurs et suppression ratifiés | owners producteurs et consommateurs + gouvernance contrats | OPEN |
| ENT-K3-D09 | Privacy | Finalités, restrictions, rétention, révocation, données mineurs et destinataires approuvés | CNS et responsable conformité ; décisions versionnées | OPEN |
| ENT-K3-D10 | Burkina Faso | Cadre pays, sources officielles, base applicable, durées et CFG validés | revue juridique BF et responsable pays | OPEN |
| ENT-K3-D11 | Architecture | ADR DERIVED/MIXED approuvé, états non reconstructibles identifiés | approbation ADR et analyse d'impact | OPEN |
| ENT-K3-D12 | Registre | Huit contrats inscrits après validation, statut exact par contrat | revue CONTRACT_REGISTRY, version et compatibilité | OPEN |

### Critères de sortie

- Chaque décision reçoit un responsable nommé, une date, une référence de preuve et un verdict explicite `APPROVED`, `REJECTED` ou `DEFERRED` avec justification ; **aucune valeur n'est présumée**.
- Une décision rejetée entraîne une correction des propositions dépendantes et une analyse d'impact ; une décision différée qui touche un critère K3 bloque K3 PASS.
- La conformité pays BF reste une condition d'activation locale ; ne pas confondre gate de contrat logique et autorisation légale de déploiement.
- Après résolution, appliquer individuellement les sept critères du `K3_CONTRACT_GATE.md` à ENT-001..006, en conservant les preuves. Aucune promotion automatique par fusion de PR.

**État actuel : 12 décisions OPEN / 0 décisions approuvées dans ce registre de revue / K3-NOT-PASS.** Cela n'annule pas les décisions canoniques déjà actives ailleurs.
