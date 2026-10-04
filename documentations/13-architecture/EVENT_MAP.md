# Event Map conceptuelle

Les événements restent candidats jusqu’au niveau D3. Le producteur possède le schéma et sa version. Les noms ci-dessous expriment les flux, pas des contrats figés.

## Education

`institution.created`, `institution.updated`, `institution.archived`, `program.created`, `program.published`, `program.updated`, `curriculum.versioned`, `qualification.updated`.

## Profils et compétences

`profile.updated`, `education-history.updated`, `user-skill.added`, `user-skill.updated`, `assessment.completed`.

## Orientation et carrières

`orientation.started`, `orientation.completed`, `recommendation.generated`, `career-transition.generated`.

## Marché et opportunités

`labor-signal.accepted`, `labor-indicator.updated`, `opportunity.published`, `opportunity.expired`, `application.submitted`, `application.status-changed`.

## Data

`source.registered`, `ingestion.completed`, `assertion.provenance-recorded`, `data-quality.failed`, `data-validation.completed`.

## Contenu et communauté

`content.published`, `content.retired`, `community-content.reported`, `moderation.decided`.

## Plateforme et économie

`subscription.changed`, `entitlement.changed`, `payment-status.changed`, `consent.changed`, `privacy-requested`.

## Règles

- aucun événement ne transporte plus de données personnelles que nécessaire
- les consommateurs doivent tolérer versionnement et répétition selon le contrat futur
- les événements analytiques ne remplacent pas les événements métier
- les contrats détaillés et politiques de rétention arrivent à D3/D4
