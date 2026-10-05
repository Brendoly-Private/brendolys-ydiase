# YD-MS-DAT-003 — Data Governance — Baseline C1

Statut : `DOCUMENTATION-BASELINE-C1 / PROVENANCE-LINEAGE-SEMANTICS-CLOSED`

## Politique normative
Voir `DATA_GOVERNANCE_POLICY.md`.

## Chaîne de confiance
DAT-001 gouverne source/droits ; DAT-002 capture acquisition/raw ; DAT-003 porte provenance/lineage ; DAT-004 évalue qualité/validation ; DAT-005 gouverne les référentiels transversaux. Aucun de ces services ne devient par copie owner des objets EDU, SKL, CAR, LAB ou autres domaines.

## Invariants
- versionnement et historique non destructif ;
- provenance/attribution préservée ;
- UNKNOWN/NOT-ASSESSABLE ne deviennent jamais validation positive ;
- absence d'autorisation requise bloque la nouvelle acquisition ;
- raw n'est jamais vérité métier ;
- validation ne transfère pas l'ownership métier ;
- projections/consommateurs ne sont jamais backups de l'autorité DAT.

## Avant ACTIVE
contrats physiques de lineage, intégrité, SLO/RPO/RTO, restore vérifié et réconciliation.

Statut final : `C1-BASELINE-ESTABLISHED — PROVENANCE-LINEAGE-SEMANTICS-CLOSED / IMPLEMENTATION-AND-EVIDENCE-PENDING`.
