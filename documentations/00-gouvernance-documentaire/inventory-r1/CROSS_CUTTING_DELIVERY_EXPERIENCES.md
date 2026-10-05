# R1 — Cross-cutting, Delivery & Experiences Inventory

Statut : `ACTIVE-R1`

## Data / Knowledge / Analytics / AI
Zone transverse distincte des 10 domaines métier.
Les principes transverses restent centraux ; les responsabilités runtime restent dans DAT/KNW/ANL/AI.
Aucune copie des politiques locales dans la vue transverse.

## Security / Privacy / Compliance
SECURITE_BASELINE.md → STANDARD/BASELINE → security-privacy-compliance/security.
Les politiques spécifiques CNS, CFG ou d'une frontière restent locales et référencent la baseline.

## Operations / Resilience
RESILIENCE_BASELINE.md → STANDARD/BASELINE → operations/reliability|continuity.
BIA, backup/restore, DR runbooks spécifiques restent locaux.
Les résultats datés vont dans evidence.

## Country Frameworks
README + BURKINA_FASO.md confirmés.
Disposition KEEP/GROUP.
Aucun country fork du corpus. Burkina n'est jamais défaut implicite Afrique.

## Roadmap / delivery
17-roadmap-phases → DELIVERY.
Destination : delivery/{roadmap,activation,releases,gates} selon contenu réel.

## Experiences / surfaces
Gap structurel documentaire confirmé, pas gap produit.

La cible doit être dérivée de :
- acteurs/segments ;
- journeys/jobs ;
- capacités ;
- contextes d'accès ;
- entitlement/privacy ;
- contraintes terminal/connectivité ;
- compositions de services.

Ne pas imposer « 2 Web + mobile » ni un nombre fixe de surfaces.

Futures classes : EXPERIENCE, SURFACE, JOURNEY, EXPERIENCE-COMPOSITION, ACCESS-CONTEXT.

## Implementation artifacts
implementation-artifacts/* → REVIEW.
R2 décide s'il s'agit de spécification active, historique ou artefact de livraison.
