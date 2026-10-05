# YD-MS-CAR-001 — Occupation & Career Graph — Fermeture de phase documentaire

Statut : `DOCUMENTATION-BASELINE-CLOSED / IMPLEMENTATION-PENDING`
Nature : `AUTH`
Criticité : `C2`

## Autorité
CAR-001 possède Occupation, OccupationVersion, OccupationSkillRequirement, OccupationRelation et CareerTransitionEdge.

## Invariants
- SKL-001 reste owner des Skills canoniques ;
- EDU-004 reste owner des Qualifications ;
- signaux LAB sont evidence, jamais mutations automatiques ;
- faits observés, assertions et inférences restent distingués ;
- provenance, contexte et version sont conservés ;
- aucune projection aval ne devient autorité métier.

## Multi-pays
Les métiers, titres, exigences et passerelles peuvent dépendre du pays, du secteur, de la période et de la taxonomie. Aucun intitulé ou prérequis local n'est universalisé par défaut.

## Récupération
Backup/restore indépendant C2. SKL, EDU, LAB, CFG et DAT ne sont pas des sources de reconstruction de CAR-001.

## Gates différés
Modèle de preuve métier, Country Framework, RPO/RTO/SLO, restore, IAM et contrats physiques restent à valider avant production.

Statut final : `CLOSED-FOR-NOW — RETURN AT IMPLEMENTATION/PREPROD`.
