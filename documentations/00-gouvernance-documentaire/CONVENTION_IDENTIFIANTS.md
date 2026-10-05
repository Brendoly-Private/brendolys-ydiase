# Convention des identifiants YDIASE

Statut : `ACTIVE`

## Principe

Tout objet durable et traçable reçoit un identifiant stable. Un identifiant n'est jamais réutilisé, même après retrait de l'objet.

## Familles

| Préfixe | Objet |
|---|---|
| `YD-DOC` | document gouverné |
| `YD-DOM` | domaine métier |
| `YD-CAP` | capacité |
| `YD-REQ` | exigence |
| `YD-RULE` | règle métier |
| `YD-ADR` | décision d'architecture |
| `YD-DEC` | décision non architecturale |
| `YD-HYP` | hypothèse |
| `YD-RISK` | risque |
| `YD-SRC` | source de données |
| `YD-DATA` | actif ou contrat de donnée gouverné |
| `YD-SVC` | service candidat logique |
| `YD-MS` | microservice autonome |
| `YD-PLT` | composant autonome de plateforme |
| `YD-API` | contrat API |
| `YD-EVT` | contrat événement |
| `YD-CTR` | contrat générique ou famille de contrats |
| `YD-TEST` | vérification gouvernée |
| `YD-CF` | Country Framework |
| `YD-PHASE` | phase produit |

Les codes de domaine déjà employés dans les frontières, par exemple `PRF`, `EDU`, `SKL`, `CAR`, `DAT`, restent des qualifiants et ne constituent pas seuls un identifiant global.

## Format

Format recommandé : `FAMILLE[-DOMAINE]-NNN`. Les identifiants déjà publiés restent valides. Une migration de forme ne change jamais l'identité logique d'un objet.

## Renommage et retrait

Un renommage conserve l'ID. Un retrait conserve l'ID dans les registres avec son statut final. Une fusion doit enregistrer les IDs sources et l'ID cible. Une scission doit conserver le lien vers l'objet parent.

## Nouvelle famille

Toute nouvelle famille exige une modification de cette convention avant usage généralisé.