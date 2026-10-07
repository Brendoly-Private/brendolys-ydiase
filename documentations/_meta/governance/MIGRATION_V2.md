---
document_id: "YD-DOC-META-MIGRATION-V2"
title: "Migration documentaire V2"
document_type: "governance-reference"
document_role: "Documente une référence de gouvernance ou de maturité utilisée pour qualifier le corpus et les composants YDIASE."
product: "BRENDOLYS YDIASE"
institutional_reference: "YDIASE-INSTITUTIONAL-IDENTITY"
status: "ACTIVE"
authority_level: "reference"
canonical: false
development_usage: "supporting-reference"
metadata_adopted_at: "2026-10-07"
tags:
  - "meta"
---

# Migration documentaire V2

> **Rôle du document**
> Documente une référence de gouvernance ou de maturité utilisée pour qualifier le corpus et les composants YDIASE.
> **Usage développement :** référence de support pour la gouvernance et la qualification documentaire.

## Autorité

Le dossier `documentations/` est l'unique référence documentaire canonique de BRENDOLYS YDIASE.

Aucun catalogue, graphe, registre ou dossier technique parallèle ne peut devenir une seconde source de vérité.

## Règles

1. Une information possède une source canonique unique.
2. Les autres documents utilisent des références par identifiant.
3. Les catalogues, matrices, registres et graphes calculables sont générés.
4. Les preuves restent traçables vers leur source.
5. Les documents obsolètes ou redondants sont supprimés après migration de toute information unique.
6. `_meta/` contient uniquement les mécanismes documentaires : schémas, ontologie, maturité, validation et sorties générées.
7. Le dossier historique `_knowledge/` doit disparaître à l'issue de cette migration.

## Structure cible

- `00-foundation/`
- `01-product/`
- `02-domains/`
- `03-systems/`
- `04-contracts/`
- `05-decisions/`
- `06-trust/`
- `07-operations/`
- `08-countries/`
- `_meta/`
