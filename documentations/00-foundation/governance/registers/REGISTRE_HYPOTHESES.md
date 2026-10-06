# Registre des hypothèses — BRENDOLYS YDIASE

Statut : `ACTIVE-BASELINE`

Une hypothèse n'est pas un fait. Sa validation peut confirmer, modifier ou invalider une partie du produit.

| ID | Hypothèse | Domaine | Validation attendue | Gate/échéance | Si invalidée | Statut |
|---|---|---|---|---|---|---|
| YD-HYP-EDU-001 | Les données établissements, filières et curricula peuvent être obtenues et maintenues avec une fréquence exploitable. | Éducation | pilote Burkina + mesure couverture/fraîcheur | avant généralisation Burkina | renforcer collecte et sources alternatives | À TESTER |
| YD-HYP-EDU-002 | Les différences de curricula entre établissements apportent une valeur utile à l'orientation. | Éducation/Orientation | tests utilisateurs | pilote | réduire granularité si valeur faible | À TESTER |
| YD-HYP-LAB-001 | Les offres publiées seules ne représentent pas suffisamment la demande réelle de compétences. | Marché travail | comparaison multi-sources | avant analytics avancé | revoir modèle Labor Intelligence | À TESTER |
| YD-HYP-LAB-002 | Des sources complémentaires permettent d'estimer une partie du marché informel ou non publié. | Marché travail | expérimentation méthodologique | avant publication d'indicateurs concernés | limiter les claims et produits | À TESTER |
| YD-HYP-ORI-001 | Le croisement profil + formation + compétences + métiers + marché produit des recommandations utiles. | Orientation | protocole d'évaluation + feedback | pilote | revoir moteur et facteurs | À TESTER |
| YD-HYP-AI-001 | L'IA apporte de la valeur sans devenir source de vérité. | AI | évaluation qualité/grounding | avant fonctions AI production | réduire ou retirer cas d'usage | À TESTER |
| YD-HYP-DATA-001 | La provenance et la temporalité peuvent être conservées à la granularité nécessaire sans bloquer la collecte. | Data | prototype ingestion | P1 | adapter modèle de provenance | À TESTER |
| YD-HYP-DER-001 | Les cinq frontières DERIVED disposent de sources permettant FULL_REBUILD dans un RTO acceptable. | Architecture/Data | tests rebuild | préproduction de chaque service | reclasser ou ajouter snapshot gouverné | À TESTER |
| YD-HYP-PROD-001 | Élèves, étudiants et professionnels acceptent un compte YDIASE pour obtenir orientation et suivi. | Produit | acquisition/activation pilote | pilote Burkina | revoir onboarding et valeur immédiate | À TESTER |
| YD-HYP-PROD-002 | Les établissements voient un intérêt à contribuer ou corriger leurs données. | Partenaires | entretiens + taux contribution | après première couverture | maintenir modèle indépendant de collecte | À TESTER |
| YD-HYP-ECO-001 | Plusieurs segments de revenus peuvent coexister sans dégrader l'indépendance des recommandations. | Économie produit | tests business + règles de séparation | avant monétisation | supprimer/modifier canaux conflictuels | À TESTER |
| YD-HYP-CTY-001 | Le noyau métier peut être réutilisé entre pays en externalisant classifications, droit, langues et structures éducatives dans les Country Frameworks. | Multi-pays | second pays pilote | avant M5 | revoir frontières/domain model | À TESTER |

## Gate

Aucune hypothèse `À TESTER` ne doit être convertie silencieusement en exigence ou décision. Une preuve suffisante déclenche une revue et un changement explicite de statut.
