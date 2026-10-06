# Revue D2 — décisions et frontières à surveiller

La revue D2 a été clôturée avant construction détaillée de la carte de dépendances. Les cinq blockers d’ownership identifiés pendant l’injection ont reçu une décision explicite.

## Décisions clôturées

1. **Application Service** : `YD-SVC-REC-002` passe `SUPERSEDED`. Le successeur canonique est `YD-SVC-APP-001`. Le préfixe `REC` reste réservé à Recommendation. Aucun nouvel artefact ne doit référencer REC-002.
2. **Catalogue commercial** : `YD-SVC-BIL-001` possède `CommercialProduct` et `CommercialProductVersion`, ainsi que plans, subscriptions, entitlements et quotas commerciaux. API/DPR/INT/MKT restent owners du contenu métier de leurs offres.
3. **Moderation Policy** : `YD-SVC-MOD-001` possède `ModerationPolicy` et `ModerationPolicyVersion`. La gouvernance approuve les règles, CFG apporte le contexte pays, MOD porte la politique opérationnelle versionnée.
4. **Processing Purpose Registry** : `YD-SVC-CNS-001` possède `ProcessingPurpose` et `ProcessingPurposeVersion`. Tout traitement personnel référence une finalité gouvernée et versionnée.
5. **Model Registry / MLOps** : la propriété des modèles est retirée de AI-001 et confiée au nouveau candidat `YD-SVC-MLP-001 — Model Lifecycle & Registry Service`. AI Gateway reste responsable des politiques et requêtes d’exécution.

## Frontières à surveiller en D3

- **EDU-002 ↔ EDU-003** : Program référence Curriculum et Curriculum référence Program. Interdire toute transaction distribuée obligatoire. Utiliser IDs stables, événements et contrats versionnés.
- **SKL-001 ↔ CAR-001** : Skills et occupations s’enrichissent mutuellement sans ownership croisé.
- **OPP-002 ↔ REC-001** : Opportunity Matching reste spécialisé candidat-opportunité. Recommendation reste générique.
- **SRH-001 ↔ AI-002** : mutualisation d’infrastructure d’index possible, mais ownership métier distinct.
- **ANL-002/003 ↔ INT-001** : Analytics calcule les insights; Intelligence Product assemble, versionne et livre le produit.
- **PRT-001 ↔ DAT-001** : le partenariat et le droit d’usage opérationnel d’une source doivent se référencer sans créer deux vérités juridiques.
- **DAT-004 ↔ domaines métier** : les domaines définissent leurs invariants; DAT-004 porte contrôles transversaux, corroboration et qualité.
- **NTF-001 ↔ PRF/CNS** : les préférences Notification restent des projections.
- **LRN-001 ↔ EDU-002 ↔ MKT-001** : Learning référence les ressources; EDU possède les programmes académiques; MKT possède les listings et commandes marketplace.
- **API-001 ↔ BIL-001** : BIL décide entitlement/quota commercial; API applique les limites techniques selon contrat sans créer un second moteur commercial.
- **AI-001/004 ↔ MLP-001** : Gateway/Orchestration consomment le registre de modèles; seul MLP possède modèle/version/endpoint/approval.

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

## Verdict D2

**Blockers d’ownership ouverts : 0.**

La construction détaillée de la carte de dépendances peut commencer. Cette carte constitue l’entrée de D3 : elle doit qualifier pour chaque dépendance le sens, le mode de contrat, la synchronisation, les événements, les données minimales échangées, les dépendances interdites et les risques de cycle. Les frontières listées ci-dessus ne sont plus des blockers D2, mais doivent recevoir un contrat explicite en D3.
