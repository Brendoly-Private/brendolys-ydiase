# Registres de gouvernance — BRENDOLYS YDIASE

Statut : `ACTIVE`

## 1. Objet

Les registres donnent une vue contrôlée des éléments transversaux du corpus. Ils ne remplacent ni les documents détaillés ni la provenance portée par les données.

## 2. Registres normatifs

| Registre | Fichier | Identifiant principal | Contenu minimal | Gate |
|---|---|---|---|---|
| Décisions | `REGISTRE_DECISIONS.md` | `YD-ADR-*` / décision gouvernée | contexte, décision, alternatives, impacts, autorité, statut, revue | toute décision structurante |
| Exigences | `REFERENTIEL_EXIGENCES.md` | `YD-REQ-*` | origine, domaine/capacité, règle, phase, vérification, owner, statut | avant implémentation concernée |
| Risques | `REGISTRE_RISQUES.md` | `YD-RISK-*` | cause, événement, impact, probabilité, mitigation, owner, trigger, statut | revue produit/architecture |
| Hypothèses | `REGISTRE_HYPOTHESES.md` | `YD-HYP-*` | hypothèse, preuve attendue, méthode, seuil, échéance, conséquence | avant dépendance irréversible |
| Sources | `REGISTRE_SOURCES.md` | `YD-SRC-*` | producteur, territoire, domaine, méthode, droits, qualité, actualisation, provenance | avant publication/usage analytique |
| Autorité des données | `AUTORITATIVE_SOURCE_REGISTRY.md` | type/agrégat | owner métier, frontière autoritative, copies, consommateurs, règle de synchronisation | avant contrat de réplication |
| Traçabilité | `MATRICE_TRACABILITE.md` | relations entre IDs | vision, domaine, capacité, exigence, règle, décision, frontière, contrat, vérification | revue de cohérence |

## 3. Registres spécialisés hors dossier 00

Des registres spécialisés peuvent exister dans les dossiers concernés, notamment services, autonomie, événements, contrats, DERIVED, sécurité, exploitation et cadres pays. Ils restent subordonnés aux règles du dossier 00.

Un registre spécialisé doit déclarer son owner, sa portée, ses identifiants, son document supérieur et son mécanisme de revue.

## 4. Règles de tenue

- un ID n'est jamais réutilisé
- une entrée retirée reste historisée
- un changement d'autorité, de frontière ou de sens exige une analyse d'impact
- une entrée `DRAFT` n'est pas une référence normative
- une entrée `ACTIVE` possède un owner fonctionnel ou documentaire
- un owner nominatif peut rester `TBD-PREPROD` si l'owner fonctionnel est défini
- `TBD-BLOCKING` rouvre le gate concerné
- les registres ne doivent pas inventer une technologie, un seuil ou une règle métier absente des documents supérieurs

## 5. Revue

Les registres sont revus lors de toute modification de fondation produit, frontière métier, autorité de donnée, décision D3, contrat ou exigence critique. `MATRICE_TRACABILITE.md` sert de contrôle transversal après ces mises à jour.
