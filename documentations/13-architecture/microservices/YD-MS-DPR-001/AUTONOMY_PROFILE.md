# YD-MS-DPR-001 — Data Product

Statut : `autonomy-profile-draft`

- Autorité : releases de produits data, manifests, licences et état de publication; données sources restent owners amont.
- Owner métier du catalogue commercial : fonction Product & Commercial YDIASE. Elle possède la définition des offres Data Product, packaging, conditions commerciales et cycle de publication commerciale. Elle ne possède ni les données sources, ni les décisions privacy, ni les entitlements techniques.
- Séparation de responsabilités : DPR contrôle la release, le manifest, la licence et l’état de publication; ANL/DAT restent propriétaires des données amont; CNS garde l’autorité privacy; BIL garde l’autorité abonnement/facturation/entitlement.
- C1, backup AUTH. C organisations autorisées, I, M2M. Exposition EXT gouvernée.
- Dépendances : ANL/DAT, BIL, CNS.
- Panne : accès fail-closed si licence, privacy ou entitlement non vérifiable; release existante reste immuable.
- Sécurité : aucune donnée personnelle vendue; privacy review, licence, provenance et manifest obligatoires.
- Repo : `brendolys-ydiase-data-product`.
- Gate : nomination nominative du responsable et du suppléant Product & Commercial, licences, anonymisation/agrégation, SLO/RPO/RTO, restore.