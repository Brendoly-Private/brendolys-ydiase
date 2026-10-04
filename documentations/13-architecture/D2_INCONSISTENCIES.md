# Incohérences détectées pendant l’injection D2

Cette revue accompagne les 61 `SERVICE_DEFINITION.md`. Elle distingue les conflits réels des frontières qui demandent encore une décision D3.

## À corriger avant D3

1. **YD-SVC-REC-002 — Application Service** : le préfixe `REC` est déjà utilisé pour Recommendation. L’identifiant stable ne doit pas être réutilisé ni silencieusement renommé. Créer une décision de renommage vers une famille `APP` et conserver l’alias historique.
2. **Product Catalog commercial** : BIL-001 consomme un catalogue de produits commerciaux dont l’owner transversal n’est pas explicitement défini. Décider si les produits restent distribués entre API/DPR/INT/MKT ou si un agrégat de catalogue commercial commun est nécessaire.
3. **Moderation Policy** : MOD-001 consomme une politique dont l’owner n’est pas explicite. Fixer l’owner avant contrats D3.
4. **Processing Purpose Registry** : CNS-001 consomme le registre des finalités de traitement sans owner explicite. Il doit être formalisé avant traitement à grande échelle de données personnelles.
5. **Model Registry / MLOps** : AI-001 porte provisoirement `ModelEndpointRegistration`. Si YDIASE industrialise plusieurs modèles, versions et évaluations, revoir la frontière et décider si un contexte MLOps autonome apparaît.

## Frontières à surveiller

- **EDU-002 ↔ EDU-003** : Program référence Curriculum et Curriculum référence Program. Interdire la dépendance transactionnelle circulaire. Utiliser IDs stables, événements et contrats versionnés.
- **SKL-001 ↔ CAR-001** : Skills et occupations s’enrichissent mutuellement. Aucun des deux ne doit devenir propriétaire des agrégats de l’autre.
- **OPP-002 ↔ REC-001** : Opportunity Matching reste spécialisé candidat-opportunité. Recommendation reste générique. Une fusion n’est justifiée que si leurs invariants deviennent identiques.
- **SRH-001 ↔ AI-002** : indexation potentiellement similaire. Mutualisation technique autorisée, fusion métier non automatique.
- **ANL-002/003 ↔ INT-001** : Analytics calcule les insights; Intelligence Product assemble, versionne et livre le produit commercial.
- **PRT-001 ↔ DAT-001** : le contrat de partenariat et le droit opérationnel d’utiliser une source ne doivent pas devenir deux vérités juridiques concurrentes.
- **DAT-004 ↔ domaines métier** : le domaine définit ses invariants métier; DAT-004 exécute les contrôles transversaux, corroborations et décisions de qualité selon contrat.
- **NTF-001 ↔ PRF/CNS** : les préférences présentes dans Notification sont des projections. PRF/CNS restent owners selon la nature de la préférence.
- **LRN-001 ↔ EDU-002 ↔ MKT-001** : Learning référence des ressources/formations; EDU possède les programmes académiques; MKT possède l’offre commerciale.
- **API-001 ↔ BIL-001** : définir en D3 la relation entre API quota policy et entitlement/quota commercial pour éviter deux moteurs d’autorisation contradictoires.

## Invariants confirmés

- Identity ≠ Profile.
- Institution ≠ Institution Workspace.
- Program ≠ Curriculum.
- Skill ≠ UserSkill.
- Labor Signal ≠ Labor Intelligence ≠ Forecast.
- Opportunity ≠ Application.
- Employer ≠ Employer Workspace.
- Data acquisition/provenance/quality ne possède pas les faits métier publiés.
- Knowledge Graph ne possède pas les entités métier projetées.
- Analytics, Recommendation et AI ne réécrivent pas les sources métier.
- Sponsored Placement ne modifie jamais les scores d’orientation ou de recommandation.
- Data Product ne commercialise aucune donnée personnelle brute.

## Verdict

L’injection D2 ne révèle pas de conflit majeur rendant l’architecture incohérente. Elle révèle toutefois cinq décisions de gouvernance/ownership à prendre avant D3 et plusieurs dépendances bidirectionnelles qui devront être transformées en contrats non circulaires.