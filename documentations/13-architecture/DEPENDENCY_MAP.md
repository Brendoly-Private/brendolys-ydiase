# Dependency Map cible

## Règle

Les dépendances suivent l’ownership des données. Une dépendance circulaire entre bounded contexts est interdite sans ADR.

## Chaînes principales

`Identity → Profile → Orientation`

`Institution → Program → Curriculum → Skills → Occupation/Career → Orientation`

`Data Source Registry → Acquisition → Provenance → Quality → domaines métier`

`Labor Signals → Labor Market Intelligence → Forecasting`

`Profile + Skills + Opportunity → Opportunity Matching → Application`

`Content → Feed`; `Community → Moderation`; `Learning Marketplace → Learning Discovery`

`Domaines autoritatifs → Search / Knowledge Graph / Analytics → produits Intelligence/Data/API`

`Domaines autoritatifs → Retrieval & Grounding → AI Gateway`; l’IA ne devient jamais propriétaire des données sources.

`Subscription & Entitlement → droits produit`; `Billing` confirme les états financiers nécessaires sans devenir moteur d’autorisation métier.

## Dépendances interdites

- un catalogue métier ne dépend pas de Recommendation pour exister
- un domaine autoritatif ne dépend pas d’Analytics pour écrire ses faits
- Sponsored Placement ne modifie aucun score d’orientation ou matching
- AI Gateway ne modifie pas directement les sources métier
- Search et Knowledge Graph ne deviennent pas sources autoritatives par réplication
