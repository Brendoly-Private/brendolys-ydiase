# Frontières et dépendances — Identité et profils

Statut : `DOMAIN-REVIEW-CANDIDATE`

## Frontières métier proposées

### Identité technique et accès

Responsabilité : comptes, principal technique, credentials bindings, sessions et état d'accès.
Traduction D3 actuelle : `IDN-001`.
Décision : `CONFIRM-SEPARATION`.

L'identité technique ne doit pas posséder le profil métier.

### Profil courant

Responsabilité : `UserProfile`, préférences, objectifs, contraintes déclarées et vues sémantiques du profil.
Traduction D3 actuelle : `PRF-001`.
Décision : `CONFIRM-WITH-REVIEW`.

### Historique éducatif et expérience

Responsabilité : `EducationRecord`, `ExperienceRecord`, `AchievementClaim`, `ProfileEvidenceLink`.
Traduction D3 actuelle : `PRF-002`.
Décision : `KEEP-SEPARATE-LOGICALLY` avant décision physique définitive.

La séparation logique est justifiée par temporalité, provenance, volume historique et règles de preuve différentes du profil courant. La nécessité d'un microservice physique distinct reste à réévaluer après Education, Skills et Privacy.

### Consentement et privacy

Responsabilité : finalités, consentements, restrictions, demandes des personnes et instructions de rétention.
Traduction D3 actuelle : `CNS-001` dans plateforme-gouvernance.
Décision : `CONFIRM-SEPARATION`.

## Dépendances autorisées

| Producteur | Consommateur domaine 02 | Donnée minimale | Autorité |
|---|---|---|---|
| IDN | Profile | `IdentityRef`, état de compte nécessaire | IDN |
| Privacy/CNS | Profile | droits/finalités applicables | CNS |
| Country Framework | Profile | règles pays pertinentes | Country/CFG |
| Education | History | références institution/formation/qualification | Education |
| Skills | History/Profile | références de taxonomie lorsque nécessaires | Skills |
| Data Provenance | Evidence | références de source/provenance | Data |

## Dépendances interdites

- Profile ne crée pas un compte IAM
- Profile ne modifie pas une institution ou formation de référence
- History ne crée pas une compétence autoritative
- Recommendation ne modifie pas directement le profil comme un fait
- un consommateur ne réplique pas tout le profil par commodité
- une projection analytique ne devient pas owner du profil

## Incohérence D3 détectée

La DDD Review antérieure classait `PRF-002` en `REVIEW-SPLIT` tandis que la revue de fusion avait validé `PRF-001 + PRF-002` sous contrôle renforcé. Le domaine confirme aujourd'hui deux responsabilités sémantiques distinctes mais ne tranche pas encore leur séparation physique.

Conséquence : la fusion physique existante ou envisagée ne doit pas être considérée comme définitivement validée avant les domaines Education, Skills et Privacy.

## Risque principal

Concentrer profil courant, historique long, preuves et données sensibles dans une seule frontière physique augmente le rayon d'impact d'une compromission et complique rétention, migration et séparation des finalités. À l'inverse, séparer trop tôt crée des contrats et opérations supplémentaires.

Décision finale : `ADR-REQUIRED` avant production Burkina.