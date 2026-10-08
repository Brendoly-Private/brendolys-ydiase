---
document_id: "YD-DOC-MS-PRF-002-ANA"
title: "YD-MS-PRF-002 — Analyse documentaire individualisée"
document_type: "microservice-documentation-analysis"
document_role: "Analyse individuellement la cohérence documentaire, les dépendances, invariants et inconnues de YD-MS-PRF-002."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "systems"
  - "microservice"
created_at: "2026-10-07"
last_reviewed_at: "2026-10-08"
review_scope: "metadata-only"
---

# YD-MS-PRF-002 — Analyse documentaire individualisée

> **Rôle du document**
> Analyse individuellement la cohérence documentaire, les dépendances, invariants et inconnues de YD-MS-PRF-002.
> **Usage développement :** analyse de support ; les sources canoniques et politiques applicables prévalent.

Statut : `ANALYSIS-COMPLETE / GATE-RECONCILIATION-REQUIRED`

Référence méthode : `_meta/governance/MICROSERVICE_ANALYSIS_GRID.md`.

## A. Identité et responsabilité

- ID : `YD-MS-PRF-002`
- Nom : Education & Experience Profile
- Domaine : Identity / Profile
- Nature : `AUTH`
- Criticité : `C1`
- Mission : conserver l'historique individuel éducatif et professionnel, les réalisations, états de vérification et liens de preuve.
- Objets possédés : `EducationRecord`, `ExperienceRecord`, `AchievementClaim`, `ProfileEvidenceLink` et états de vérification propres.
- Non possédés : compte IAM, profil courant PRF-001, référentiels EDU, taxonomies SKL, décisions Privacy CNS.

## B. Frontières et dépendances

PRF-001 fournit uniquement les références minimales de profil nécessaires. EDU reste autorité des institutions/programmes/qualifications de référence. SKL reste autorité de ses taxonomies. DAT fournit des références de provenance. CNS reste autorité des finalités, restrictions et demandes Privacy.

Aucune de ces dépendances n'est une source de reconstruction de l'autorité PRF-002.

Interdictions : base partagée, accès DB croisé, réplication complète comme secours, promotion d'une projection consommateur en autorité.

## C. Données et sensibilité

PRF-002 traite un historique personnel longitudinal avec preuves et provenance. La combinaison historique + temporalité + vérification + pièces/références peut être fortement sensible.

Exigences propres :
- minimisation des projections ;
- audit des lectures/mutations sensibles ;
- séparation déclaration/vérification ;
- chiffrement au repos/en transit ;
- préservation des corrections successives et de la temporalité ;
- réapplication des décisions Privacy après restauration ;
- portabilité/effacement à fermer selon règles applicables ;
- rétention différenciée par catégorie/pays à fermer avant production.

## D. Invariants spécifiques

1. PRF-002 est AUTH et non reconstructible depuis EDU/SKL/DAT/PRF-001.
2. PRF-001 et PRF-002 restent physiquement séparés.
3. Une déclaration, une preuve et une vérification restent distinctes.
4. Une preuve de diplôme/expérience ne crée pas automatiquement une compétence autoritative.
5. Une correction ne réécrit pas silencieusement l'histoire.
6. Une restauration conserve IDs, temporalité, versions, provenance et liens de preuve.
7. Une restauration ne réactive pas durablement une donnée dont la suppression/restriction est devenue applicable.
8. Les projections aval se réconcilient depuis PRF-002, jamais l'inverse.
9. Les événements rejoués après restore doivent être idempotents.
10. Les dépendances fonctionnelles indisponibles ne doivent pas empêcher la restauration de l'autorité sauvegardée.

## E. K3 — contractualisation

La matière nécessaire aux contrats est largement définie dans le profil : commandes de déclaration/correction, consultation autorisée, rattachement/détachement de preuves, projections minimales et événements candidats.

Cependant, les noms/schémas définitifs restent renvoyés au Contract Registry et plusieurs contrats PRF-001/EDU/SKL/DAT/CNS sont encore explicitement des gates préproduction.

Verdict K3 : `RECONCILIATION-REQUIRED`.

Avant PASS K3, créer ou confirmer une baseline contractuelle PRF-002 unique et vérifier sa cohérence avec le Contract Registry. Ne pas déduire PASS du niveau de détail du profil.

## F. K4 — gouvernance

Des éléments forts existent déjà : nature/criticité, IAM logique, Privacy, backup/restore, continuité, BIA, DR, rôles et procédures.

Mais le modèle K4 canonique exige une évaluation explicite des huit critères et une source canonique de gouvernance reliée au service.

Verdict K4 : `ASSESSMENT-REQUIRED`.

Le contenu existant peut fournir les preuves documentaires ; il ne faut pas créer une seconde politique concurrente.

## G. Résilience

Profil adapté à AUTH/C1.

RPO nominal candidat : ≤15 min. RTO incident courant : ≤1 h. RTO perte complète datastore : ≤4 h. RTO sinistre majeur : ≤8 h. Ces valeurs proviennent de l'ADR existant mais restent à confirmer par BIA et à mesurer.

Le restore doit réussir avec PRF-001, EDU et SKL indisponibles. FULL_REBUILD depuis les services amont est explicitement invalide.

## H. K5 — vérification

Preuves spécifiques attendues :
- restore indépendant ;
- intégrité des agrégats après restore ;
- conservation temporalité/versions/provenance/preuves ;
- mesure RPO/RTO ;
- PITR/corruption logique ;
- replay idempotent ;
- réconciliation des projections ;
- IAM/self-access/IDOR et séparation déclaration-vérification ;
- Privacy après restore ;
- suppression/restriction et non-réactivation ;
- portabilité applicable ;
- contrôles backup/restore et qualification des rôles sensibles.

Verdict K5 : `NOT-YET-PASS`.

## I. Choix encore ouverts

Datastore physique, moteur backup/PITR, topologie/copie isolée, clients OIDC physiques, step-up, commandes d'intégrité, stockage des preuves, SLO applicatif, rétention détaillée et nominations humaines restent à fermer selon les gates existants.

## J. Verdict global

PRF-002 possède déjà une documentation beaucoup plus profonde que le pilote K3/K4 standard, mais elle a été produite avant la nouvelle gouvernance de maturité.

Il ne faut donc ni la réécrire ni déclarer automatiquement K3/K4 PASS.

Verdict : `ANALYSIS-COMPLETE / RECONCILE-EXISTING-DOCS-BEFORE-READINESS`.

Prochaine action canonique : réconcilier PRF-002 avec les gates K3 et K4 en réutilisant les documents existants comme preuves, puis construire uniquement les éléments réellement manquants.
