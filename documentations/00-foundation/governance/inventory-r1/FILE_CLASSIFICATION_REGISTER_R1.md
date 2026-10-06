# R1 — File Classification Register — BRENDOLYS YDIASE

Statut : `ACTIVE-R1 / PARTIAL-PHYSICAL-VERIFICATION / NO-DELETION-AUTHORIZED`

## Rôle
Registre maître de classification pour la restructuration documentaire. Il référence des inventaires par zone afin d'éviter un fichier monolithique.

## Codes de preuve
- `P-FETCHED` : chemin lu directement.
- `P-SEARCHED` : chemin découvert par recherche.
- `P-REGISTERED` : objet déclaré dans un registre canonique.
- `P-EXPECTED` : attendu mais existence physique non encore vérifiée.
- `P-UNRESOLVED` : existence ou autorité à confirmer.

## Règle
Chaque entrée doit avoir : chemin/objet, type documentaire, normativité, reality layer si applicable, disposition R1, destination conceptuelle, confiance et preuve.

Aucun `MERGE`, `SUPERSEDE`, `ARCHIVE` ou DELETE n'est autorisé par ce registre seul.

## Sous-registres
- `inventory-r1/GOVERNANCE_PRODUCT_DOMAINS.md`
- `inventory-r1/ARCHITECTURE_CONTRACTS_DECISIONS.md`
- `inventory-r1/BOUNDARIES_AND_PLATFORM.md`
- `inventory-r1/CROSS_CUTTING_DELIVERY_EXPERIENCES.md`

## Finding R1-F001 — registre documentaire historique
`documentations/REGISTRE_DOCUMENTAIRE.md` contient 25 entrées YD-DOC-0001..0025. Le corpus courant est beaucoup plus vaste.

Il reste une source de connaissance de la fondation documentaire mais **n'est pas considéré comme inventaire exhaustif actuel**. R2 décidera s'il devient registre historique, s'il est étendu, ou s'il est superseded par un Document Registry plus complet.

## Gate
Ce registre passe `R1-COMPLETE` seulement lorsque les sous-registres couvrent le tree physique prouvable et que tout gap restant est explicitement `UNRESOLVED`.
