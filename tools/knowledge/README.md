# YDIASE Knowledge Tooling

Ces outils constituent le premier noyau du futur YDIASE Knowledge Compiler.

## Dépendance

Python 3 et PyYAML.

## Validation

```bash
python tools/knowledge/validate_catalog.py
```

Le mode courant bloque les erreurs YAML, IDs dupliqués et types de relations non autorisés. Les références non résolues sont signalées sans bloquer K2, car le catalogue n'est pas encore complet.

Le mode strict est destiné au passage de gate :

```bash
python tools/knowledge/validate_catalog.py --strict
```

Il bloque aussi toute référence `YD-*` non enregistrée dans `_knowledge`.

## Analyse d'impact

```bash
python tools/knowledge/generate_impact.py YD-MS-EDU-003
```

La commande parcourt les `RelationSet` et produit une vue Markdown transitive des relations sortantes.

## Principe de migration

K2 autorise des références non résolues vers des objets déjà définis dans les documents normatifs mais pas encore migrés dans le catalogue. Chaque référence non résolue devient une dette de migration visible. Le passage en mode strict ne doit intervenir qu'après catalogage du périmètre couvert par le gate.

## Prochaines validations

- validation JSON Schema par `kind`
- contrôle des préfixes d'identifiants par type
- contrôle AUTH / MIXED / DERIVED
- contrôle producteur/consommateur d'événement
- contrôle ownership des agrégats
- comparaison automatique avec les cartes normatives historiques
- sortie JSON pour CI et agents IA
