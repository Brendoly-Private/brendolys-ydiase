# Domaine 08 — Orientation et recommandation

Statut : `DOMAIN-BASELINE-CANDIDATE`

## Mission

Le domaine transforme des données autorisées en évaluations, dossiers de décision, comparaisons et recommandations explicables sans confondre mesure, décision assistée et ranking.

## Frontières physiques

- `YD-MS-ASM-001 — Assessment` : `AUTH / C1`.
- `YD-MS-ORI-001 — Orientation & Decision Support` : `AUTH / C1`, portant ORI-001 + ORI-002.
- `YD-MS-REC-001 — Recommendation` : `MIXED / C1`, traité séparément pour sa politique de ranking.

## Doctrine

- Assessment mesure selon une méthodologie versionnée ; il ne déclare pas une compétence acquise.
- Orientation possède le dossier, objectifs/contraintes du dossier, comparaisons et décision enregistrée.
- Recommendation possède ses runs/résultats/explications, jamais les faits source.
- ORI-002 reste fusionné physiquement dans ORI-001 tant qu'il n'acquiert pas une autorité/cycle propres.
- aucune boucle synchrone circulaire ORI ↔ REC ;
- profilage sensible : finalité, minimisation, contrôle objet, audit et Privacy obligatoires ;
- IA peut assister l'explication mais ne remplace ni méthodologie d'évaluation ni règles de décision/ranking.

Voir `FRONTIERES_ET_DEPENDANCES.md` et `GATES_ET_INCONNUES.md`.
