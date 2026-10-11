---
document_id: "YD-DOC-DOM-ENT-K3-REQUIREMENTS"
title: "Exigences métier Entrepreneurship — préparation K3"
document_type: "domain-knowledge"
document_role: "Documente les propositions et vérifications restantes sans modifier les sources canoniques existantes."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "DRAFT"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
created_at: "2026-10-11"
last_reviewed_at: "2026-10-11"
---

# Exigences métier Entrepreneurship — préparation K3

Statut : **DRAFT / CANDIDATE / K3-NOT-PASS**. Ces exigences candidates ne modifient pas le référentiel canonique ; elles devront être validées et enregistrées conformément à sa règle d'extension.

| Service | ID candidat | Exigence testable | Critère d'acceptation documentaire ou test futur |
|---|---|---|---|
| ENT-001 | ENT1-REQ-001 | Un utilisateur autorisé peut gérer plusieurs Venture indépendants de son profil PRF | Deux Ventures distincts conservent des identités et versions séparées |
| ENT-001 | ENT1-REQ-002 | Toute transition d'état du Venture contrôle permission, version et idempotence | Rejeu sans double création ; conflit de version explicite |
| ENT-001 | ENT1-REQ-003 | La révocation de visibilité empêche la divulgation du Venture | Lecture non autorisée refusée, projections invalidées |
| ENT-002 | ENT2-REQ-001 | Une hypothèse distingue signal, interprétation et niveau d'incertitude | EvidenceRef, provenance, dates et incertitude vérifiables |
| ENT-002 | ENT2-REQ-002 | Toute correction ou expiration source invalide les assessments dépendants | Aucun snapshot expiré présenté comme actuel |
| ENT-002 | ENT2-REQ-003 | Une hypothèse générique ne dépend pas d'un Venture | Calcul sans VentureRef démontrable |
| ENT-003 | ENT3-REQ-001 | Le catalogue publie des programmes/offres sans créer d'autorité sur Partner/Agreement | PRT demeure source de l'organisation/accord |
| ENT-003 | ENT3-REQ-002 | Une ressource publie son territoire, source, conditions et statut | Offre non validée/non sourcée non publiée |
| ENT-003 | ENT3-REQ-003 | Le retrait d'une source ou offre se propage aux consommateurs | Replay et invalidation démontrables |
| ENT-004 | ENT4-REQ-001 | Toute opportunité financière indique source, règles versionnées et échéance | Offre expirée non présentée comme disponible |
| ENT-004 | ENT4-REQ-002 | L'éligibilité est une estimation et jamais une décision du financeur | Résultat comporte avertissement, règle/version, expiration |
| ENT-004 | ENT4-REQ-003 | L'évaluation personnalisée applique CNS et minimise les données | Refus si décision Privacy obligatoire indisponible |
| ENT-005 | ENT5-REQ-001 | TeamNeed appartient à ENT-005 et référence Venture sans modifier ENT-001 | Modification de TeamNeed ne modifie pas Venture |
| ENT-005 | ENT5-REQ-002 | Un candidat n'est visible/contactable que selon autorisation applicable | Révocation rend résultats et projections inaccessibles |
| ENT-005 | ENT5-REQ-003 | Un match dérivé est explicable, daté et invalidable | EvidenceVersion, expiry et retrait vérifiables |
| ENT-006 | ENT6-REQ-001 | Un plan et ses jalons référencent un Venture ENT-001 existant | VentureRef validée, pas de création d'identité locale |
| ENT-006 | ENT6-REQ-002 | Les expérimentations et validations conservent versions et provenance | Corrections historiques traçables, sans falsifier résultat |
| ENT-006 | ENT6-REQ-003 | La progression n'est ni comptabilité ni validation externe officielle | Aucun solde financier ni certification officielle produite |

## Traçabilité obligatoire

Toutes les exigences ci-dessus sont **proposées**, sans preuve de test. Rattachements transversaux : `YD-REQ-GOV-001/002`, `YD-REQ-DATA-001/002`, `YD-REQ-DER-001/002`, `YD-REQ-IAM-003`, `YD-REQ-CTR-001/002`, `YD-REQ-CTY-001`. Les huit spécifications de `04-contracts/baselines/YD-MS-ENT-*/K3_*_CONTRACT_SPEC.md` doivent encore lier ces IDs et les champs exacts. Aucun gate n'est promu par ce fichier.
