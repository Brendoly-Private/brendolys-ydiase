# Cycle de vie documentaire

Statut : `ACTIVE`

## Statuts autorisés

`DRAFT` → `IN-REVIEW` → `APPROVED` → `ACTIVE` → `DEPRECATED` → `RETIRED`

`SUPERSEDED` peut remplacer `DEPRECATED` lorsqu'un successeur explicite existe.

## Sens

- `DRAFT` : travail non normatif.
- `IN-REVIEW` : contenu soumis à contrôle.
- `APPROVED` : contenu approuvé mais pas nécessairement entré en vigueur.
- `ACTIVE` : référence normative applicable.
- `DEPRECATED` : référence encore consultable mais à ne plus utiliser pour de nouveaux travaux.
- `SUPERSEDED` : remplacé par un document identifié.
- `RETIRED` : retiré de l'usage actif.

## Dimensions séparées

Le statut documentaire ne représente jamais l'état d'un logiciel. Pour les services, suivre séparément maturité documentaire, implémentation, déploiement et activation.

## Transition

Chaque transition normative enregistre auteur, approbateur, date, motif et impacts. Un retour de `ACTIVE` vers `DRAFT` est interdit. Une modification d'un document actif crée une nouvelle version soumise à revue.

## Versionnement

- correction éditoriale sans effet normatif : PATCH
- ajout compatible : MINOR
- changement incompatible de sens, frontière ou obligation : MAJOR

## Revue

Tout document actif possède une date ou un déclencheur de revue. Un événement majeur peut provoquer une revue anticipée selon `POLITIQUE_CHANGEMENT_IMPACT.md`.