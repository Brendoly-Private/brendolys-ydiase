---
document_id: "YD-DOC-FND-GOV-REG-003"
title: "Référentiel des exigences — BRENDOLYS YDIASE"
document_type: "requirements-registry"
document_role: "Enregistre les exigences transversales gouvernées et leurs conditions de vérification."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "canonical-source"
canonical: true
development_usage: "mandatory-reference"
owners:
  - "Documentation Governance"
depends_on:
  - "YD-DOC-FND-GOV-001"
  - "YD-STD-DOC-META-001"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-07"
tags:
  - "foundation"
  - "governance-register"
---

# Référentiel des exigences — BRENDOLYS YDIASE

> **Rôle du document**
> Enregistre les exigences transversales gouvernées et leurs conditions de vérification.
> **Usage développement :** référence obligatoire pour son périmètre.

Statut : `ACTIVE-BASELINE`

Ce référentiel contient les exigences transversales déjà établies. Les exigences métier détaillées seront ajoutées lors de la revue des dossiers 01 à 12.

| ID | Exigence | Domaine/capacité | Gate | Vérification | Statut |
|---|---|---|---|---|---|
| YD-REQ-GOV-001 | Toute donnée métier persistante identifie son owner et sa source autoritative. | Gouvernance Data | D2+ | registre autoritatif + profil service | ACTIVE |
| YD-REQ-GOV-002 | Toute donnée personnelle documente finalité, droits, accès, rétention et suppression. | Privacy | avant traitement | revue CNS/conformité | ACTIVE |
| YD-REQ-GOV-003 | Tout élément normatif durable possède un identifiant stable et non réutilisable. | Gouvernance documentaire | création | contrôle registre | ACTIVE |
| YD-REQ-GOV-004 | Toute contradiction normative est enregistrée et arbitrée avant activation de l'élément concerné. | Gouvernance documentaire | avant activation | registre/revue | ACTIVE |
| YD-REQ-GOV-005 | Une modification de niveau supérieur déclenche une analyse d'impact sur les éléments dérivés. | Gouvernance documentaire | changement | impact documenté | ACTIVE |
| YD-REQ-DATA-001 | Toute donnée exploitable conserve provenance, version, validité et droits d'usage applicables. | Data Governance | ingestion/publication | contrôles de provenance | ACTIVE |
| YD-REQ-DATA-002 | Deux assertions contradictoires ne sont pas fusionnées silencieusement. | Data Quality | ingestion/corroboration | conservation séparée + arbitrage | ACTIVE |
| YD-REQ-DATA-003 | Une offre publiée n'est pas assimilée automatiquement au marché du travail réel. | Labor/Data Intelligence | analyse | méthodologie distingue signal et réalité estimée | ACTIVE |
| YD-REQ-DER-001 | Une frontière DERIVED ne possède aucun fait métier irremplaçable. | Architecture/Data | D3+ | revue ownership | ACTIVE |
| YD-REQ-DER-002 | Une frontière DERIVED prouve FULL_REBUILD, replay, watermark et convergence avant production. | Résilience DERIVED | préproduction | test de reconstruction | ACTIVE |
| YD-REQ-SVC-001 | Chaque frontière physique possède repository, ownership, cycle de déploiement, stockage, reprise, sécurité et observabilité propres ou explicitement isolés. | Autonomie microservice | D3/préprod | AUTONOMY_PROFILE | ACTIVE |
| YD-REQ-SVC-002 | Aucun service ne lit directement le datastore privé d'un autre service. | Autonomie Data | D3+ | dependency/contract review | ACTIVE |
| YD-REQ-IAM-001 | YDIASE utilise BRENDOLYS Identity pour l'identité externe et ne stocke pas les mots de passe utilisateur. | IAM | implémentation | revue auth | ACTIVE |
| YD-REQ-IAM-002 | Les realms internal, networks et customers restent séparés et chaque exposition déclare ceux qu'elle accepte. | IAM | contrat | Contract Registry | ACTIVE |
| YD-REQ-IAM-003 | Un token valide ne confère pas automatiquement une autorisation métier. | Autorisation | runtime | tests d'autorisation objet/action | ACTIVE |
| YD-REQ-SEC-001 | Les flux interservices sont deny-by-default et dérivés de dépendances autorisées. | Sécurité réseau | préproduction | policy review | ACTIVE |
| YD-REQ-SEC-002 | Aucun secret, token ou mot de passe n'est stocké dans Git ou journalisé. | Secrets/Logging | continu | scans + revue logs | ACTIVE |
| YD-REQ-RES-001 | Chaque frontière critique définit criticité, SLO, RTO, RPO et mode dégradé avant production. | Résilience | préproduction | profile + test | ACTIVE |
| YD-REQ-RES-002 | Backup ou reconstruction ne sont considérés valides qu'après test de restauration/rebuild. | Résilience | préproduction | preuve de test | ACTIVE |
| YD-REQ-DPR-001 | Un Data Product distribué possède droits/licence, provenance et décision privacy compatibles. | Data Products | publication | LicenseManifest + PrivacyDecision | ACTIVE |
| YD-REQ-DPR-002 | Les données personnelles brutes sont non distribuables par défaut. | Privacy/Data Products | publication | contrôle CNS | ACTIVE |
| YD-REQ-CTR-001 | Tout contrat stable identifie producteur, consommateurs, version, autorité, compatibilité et politique d'évolution. | Contract Governance | Contract Registry | revue contrat | ACTIVE |
| YD-REQ-CTR-002 | Un choix de transport ou technologie ne doit pas être introduit par un contrat fonctionnel sans ADR. | Contract/Architecture | conception | revue ADR | ACTIVE |
| YD-REQ-CTY-001 | L'activation d'un nouveau pays exige un Country Framework validé. | Multi-pays | avant activation pays | revue Country Framework | ACTIVE |

## Règle d'extension

La revue des fondations produit et des domaines métier doit créer les exigences absentes au lieu de forcer les décisions D3 existantes à servir de règles métier. Une exigence nouvelle peut rouvrir les éléments techniques qu'elle impacte.
