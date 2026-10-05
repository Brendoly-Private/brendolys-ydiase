# Registre des risques — BRENDOLYS YDIASE

Statut : `ACTIVE-BASELINE`

| ID | Risque | Domaine | Probabilité | Impact | Owner fonctionnel | Réponse principale | Déclencheur | Statut |
|---|---|---|---|---|---|---|---|---|
| YD-RISK-DATA-001 | Données de formation obsolètes ou incomplètes. | Education/Data | Élevée | Élevé | Data + Education | provenance, validité, expiration, multi-source | fraîcheur/couverture sous seuil | ACTIVE |
| YD-RISK-DATA-002 | Une source non fiable devient implicitement vérité. | Data | Moyenne | Élevé | Data Governance | assertions séparées, confiance, corroboration | contradiction ou anomalie | ACTIVE |
| YD-RISK-DATA-003 | Perte de provenance lors de transformations. | Data | Moyenne | Élevé | Data Platform | lineage/version obligatoire | donnée sans chaîne source | ACTIVE |
| YD-RISK-LAB-001 | Les offres publiées donnent une lecture biaisée du marché réel. | Labor Intelligence | Élevée | Élevé | Labor Market | catégories de signaux distinctes + méthodologie | publication d'un indicateur assimilant offres=marché | ACTIVE |
| YD-RISK-ORI-001 | Une recommandation oriente mal un utilisateur à cause de données faibles ou d'un modèle non évalué. | Orientation | Moyenne | Élevé | Orientation | explication, confiance, évaluation, limites | taux d'erreur/feedback critique | ACTIVE |
| YD-RISK-AI-001 | Une sortie IA est prise pour une source de vérité. | AI | Moyenne | Élevé | AI Governance | grounding, vérification, provenance, UX adaptée | réponse non traçable présentée comme fait | ACTIVE |
| YD-RISK-PRIV-001 | Réidentification ou distribution non autorisée de données personnelles. | Privacy/Data Products | Moyenne | Très élevé | CNS/Privacy | minimisation, décision distribution, restrictions | incident ou test réidentification | ACTIVE |
| YD-RISK-IAM-001 | Mauvais realm ou scope donne un accès transversal indu. | IAM | Moyenne | Très élevé | Security/IAM | séparation realms + auth objet | accès cross-tenant/realm | ACTIVE |
| YD-RISK-MSA-001 | L'autonomie annoncée masque une dépendance runtime ou datastore partagée. | Architecture | Moyenne | Élevé | Architecture | profiles, dependency map, tests panne | panne commune non prévue | ACTIVE |
| YD-RISK-DER-001 | Un service DERIVED ne peut pas reconstruire son état. | Résilience | Moyenne | Élevé | Service owner | replay/snapshot + FULL_REBUILD | rebuild échoué | ACTIVE |
| YD-RISK-ECO-001 | La monétisation influence les recommandations organiques. | Économie/Orientation | Moyenne | Très élevé | Product Governance | séparation sponsorisé/organique + audit | ranking payé non signalé | ACTIVE |
| YD-RISK-PART-001 | Dépendance excessive à des établissements ou ambassadeurs pour maintenir la donnée. | Partenaires/Data | Moyenne | Élevé | Partnerships/Data | réseau multi-source + collecte alternative | baisse couverture/actualisation | ACTIVE |
| YD-RISK-CTY-001 | Le modèle Burkina est codé comme règle universelle et bloque l'expansion. | Multi-pays | Moyenne | Très élevé | Product/Architecture | Country Framework + règles localisées | ajout second pays nécessite fork | ACTIVE |
| YD-RISK-GOV-001 | L'architecture devient plus normative que les fondations métier encore incomplètes. | Gouvernance | Élevée | Élevé | Documentation Governance | revue 01→12 puis impact D3 | contradiction métier/technique | ACTIVE |
| YD-RISK-OPS-001 | RTO/RPO/SLO restent documentaires sans test réel. | Exploitation | Moyenne | Élevé | Operations | exercices restore/DR | test absent ou échoué | ACTIVE |

## Règle

La probabilité et l'impact sont des appréciations de cadrage. Les méthodes quantitatives et seuils seront définis dans les dossiers produit, sécurité et exploitation. Aucun score numérique n'est inventé ici.
