# Carte des domaines — BRENDOLYS YDIASE

Statut : `BASELINE-CANDIDATE`

Cette carte décrit les domaines fonctionnels de niveau produit. Elle ne constitue ni une liste de microservices ni une carte de déploiement.

| ID | Domaine | Responsabilité principale | Exclusions principales |
|---|---|---|---|
| YD-DOM-IDENTITY | Identité et profils | profil métier, préférences, objectifs, visibilité et consentements applicatifs | authentification technique fournie par BRENDOLYS Identity |
| YD-DOM-EDUCATION | Éducation et institutions | établissements, centres, formations, filières, programmes, curricula, modules, admissions et relations académiques | compétences génériques et marché du travail |
| YD-DOM-SKILLS | Compétences et connaissances | référentiels, niveaux, relations, preuves et écarts de compétences | cursus institutionnels complets |
| YD-DOM-CAREERS | Métiers et carrières | métiers, fonctions, familles, débouchés, transitions et trajectoires professionnelles | offres d'emploi individuelles |
| YD-DOM-LABOR | Marché du travail | signaux, demande, offre observée, enquêtes, tendances, besoins et analyses | recrutement transactionnel |
| YD-DOM-OPPORTUNITIES | Opportunités et recrutement | stages, emplois, bourses, programmes, candidatures et interactions de recrutement | référentiel macro du marché |
| YD-DOM-GUIDANCE | Orientation et recommandation | évaluations, objectifs, scénarios, matching, recommandations et plans d'évolution | autorité sur les données sources utilisées |
| YD-DOM-CONTENT | Contenu, communauté et learning | contenus, publication, interactions, apprentissage, feed et ressources | source autoritative des référentiels métier |
| YD-DOM-PARTNERS | Partenaires et écosystème | organisations partenaires, établissements, entreprises, ambassadeurs, réseaux et opérations de contribution | identité technique et facturation |
| YD-DOM-ECONOMY | Économie produit | offres commerciales, entitlements, commandes, facturation, paiements, sponsoring et produits de données autorisés | décision privacy et ownership des données sources |

## Capacités transversales

Data, Knowledge, Analytics, AI, sécurité, conformité, exploitation, résilience et plateforme traversent les domaines. Ils ne deviennent pas automatiquement des domaines métier propriétaires des faits sources.

## Gate DDD

Les dossiers 02 à 11 devront confirmer mission, langage, agrégats, règles, événements, autorités et dépendances de chaque domaine. Toute divergence avec les frontières D3 déclenche une analyse d'impact ciblée.