# YD-MS-PRF-001 — K3 Contract Baseline

Statut : K3-CONTRACT-BASELINE / IMPLEMENTATION-PENDING
Nature : AUTH
Criticité : C1

## Autorité
PRF-001 est l'autorité YDIASE du profil courant individuel : Profile Core, préférences, objectifs, contraintes déclarées et vues sémantiques autoritatives prévues par son contrat.

PRF-001 ne possède pas EducationRecord, ExperienceRecord, AchievementClaim, ProfileEvidenceLink, comptes IAM, référentiels Education/Skills ou décisions Privacy.

## Contrats entrants
- YD-CTR-IDN-SUBJECT-v1 : IdentityRef et état minimal du sujet.
- YD-CTR-CNS-PRIVACY-DECISION-v1 : finalité, grant, restriction, rétention et version de décision.
- YD-CTR-CFG-COUNTRY-CONFIG-v1 : règles territoriales applicables.
- PRF-002 : uniquement projection minimale lorsqu'un cas d'usage PRF-001 l'exige ; jamais copie complète de l'historique.

## Contrat sortant
YD-CTR-PRF-CURRENT-PROFILE-v1 est la projection canonique vers ORI/REC/CAR/CNT Feed.

Données minimales : goals, preferences, constraints et source version selon finalité autorisée. Privacy : VERY-SENSITIVE. Clé logique : subject + version. Snapshot/catch-up selon le Contract Registry.

## Invariants contractuels
- PRF-001 reste AUTH du profil courant.
- PRF-002 reste AUTH de l'historique.
- aucun accès DB croisé ni datastore partagé.
- une projection PRF-002 ne devient pas une copie autoritative locale.
- un consommateur PRF-001 reçoit uniquement le minimum requis.
- toute mutation personnelle nécessitant une décision CNS non vérifiable est fail-closed.
- les scopes self correspondent au sujet.
- les corrections et versions du profil courant sont traçables.
- une projection aval ne devient jamais autorité de secours.
- retrait/restriction Privacy doit être représentable dans les flux applicables.

## Exigences
PRF1-REQ-001 préserver l'autorité du profil courant.
PRF1-REQ-002 séparer strictement profil courant et historique.
PRF1-REQ-003 minimiser entrées et sorties.
PRF1-REQ-004 appliquer les décisions Privacy applicables.
PRF1-REQ-005 préserver subject et versions durables.
PRF1-REQ-006 supporter correction/restriction sans ambiguïté.
PRF1-REQ-007 empêcher l'accès horizontal au profil.
PRF1-REQ-008 maintenir les opérations indépendantes lorsque PRF-002 est indisponible.
PRF1-REQ-009 restaurer l'autorité depuis la chaîne PRF-001.
PRF1-REQ-010 permettre export/portabilité uniquement selon contrat Privacy gouverné.

## Versionnement et compatibilité
Ajout optionnel compatible. Suppression, renommage, changement de type ou de sens d'un champ requis impose une nouvelle version majeure. Une valeur inconnue n'est pas interprétée librement. Les consommateurs incompatibles refusent ou mettent en quarantaine.

## ADR
La frontière physique PRF-001/PRF-002 est fixée par ADR-PRF-001-PRF-002-PHYSICAL-BOUNDARY.md.

## Limites K3
Restent physiques ou PREPROD : endpoints/schémas définitifs, datastore, clients OIDC, step-up, valeurs RPO/RTO/SLO, rétention, portabilité physique, contract tests, restore et contrôles Security exécutés.

## Verdict
K3-PASS / PHYSICAL-CONTRACTS-PENDING.
