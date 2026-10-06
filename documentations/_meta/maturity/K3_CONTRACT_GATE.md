# YDIASE Knowledge Gate — K3 Contractualisé

Statut : `BASELINE / PILOT`

## Objet

K3 signifie qu'une entité déjà K2 possède les éléments contractuels nécessaires pour guider une implémentation sans inventer ses échanges, ses données ou ses décisions structurelles.

K3 ne signifie ni code terminé, ni déploiement, ni preuve runtime.

## Critères obligatoires

1. `apiOrEventContractsWhenApplicable` — API, événements ou contrats de dépendance applicables sont identifiés, versionnés et reliés aux producteurs/consommateurs. `N/A` exige une justification.
2. `dataContracts` — structures échangées, ownership, provenance, temporalité, suppression/retrait et règles de qualité applicables sont définis.
3. `invariants` — invariants métier et d'autorité sont explicites.
4. `requirements` — exigences fonctionnelles et non fonctionnelles nécessaires au composant sont traçables.
5. `adrForStructuralDecisions` — les décisions structurelles non triviales sont reliées à un ADR ou explicitement marquées `UNKNOWN` tant qu'aucun ADR n'existe.
6. `versioningRules` — stratégie de version des contrats et objets échangés définie.
7. `compatibilityRules` — compatibilité ascendante/descendante, dépréciation, migration ou refus explicite définis.

## Politique de preuve

- Un document existant compte uniquement s'il contient réellement l'information attendue.
- Une mention d'un futur contrat ne vaut pas contrat complet.
- Une politique normative peut prouver un invariant ou une exigence, mais pas automatiquement un contrat API.
- Un contrat logique peut satisfaire K3 avant choix technologique s'il définit parties, payload minimal, version, sémantique et comportement de retrait/erreur applicables.
- `UNKNOWN` bloque K3.
- `N/A` sans justification bloque K3.

## Pilotage initial

Le pilote K3 porte sur `YD-MS-SKL-001`, `YD-MS-REC-001`, `YD-MS-KNW-001` et `YD-MS-LRN-001`.

La méthode est : inventorier → rattacher → qualifier → créer uniquement les artefacts absents → recalculer K.
