# YD-MS-EDU-002 — Program Catalog

Statut : `autonomy-profile-draft`

- Logique : EDU-002. Autorité sur programmes, versions, rattachements et conditions d’accès.
- Criticité : C2. Backup AUTH.
- IAM : I/N pour gestion autorisée, C lecture, M2M.
- Exposition : EDGE lecture, INT mutations/intégrations.
- Dépendances : EDU-001 validation institution, EDU-004 qualifications, CFG. Consomme CurriculumPublished sans transaction inverse.
- Panne : catalogue publié lisible; nouvelle publication bloquée si institution ou qualification requise non validable.
- Résilience : aucune transaction distribuée avec Curriculum; événements versionnés et réconciliation.
- Sécurité : audit des publications/retraits; contributeur institutionnel limité à son périmètre.
- Repo : `brendolys-ydiase-program-catalog`; datastore et migrations privés.
- Gate : RPO/RTO/SLO, scopes institutionnels, politique version/retrait, restore et contrats.