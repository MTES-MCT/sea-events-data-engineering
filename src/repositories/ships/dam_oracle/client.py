from typing import Collection

from .database import db_engine
from src.repositories.ships.abc import ShipClientABC
from src.entities import Ship


class ShipClientDamOracle(ShipClientABC):
    def get_by_registry_number(self, registry_numbers: Collection[str]) -> list[Ship]:
        query = f"""
            WITH GINA_VUE_NAVIRE_DETAIL_SUBSET AS (
                SELECT
                    NOM_NAVIRE,
                    NUMERO_IMMAT,
                    NUM_VERSION,
                    NUMERO_IMO,
                    LIB_MATERIAU_COQUE,
                    LONGUEUR_HORS_TOUT,
                    LIB_QUARTIER,
                    LIB_GENRE_NAVIGATION,
                FROM
                    GINA.GIN_VUE_NAVIRE_DETAIL
                WHERE
                    NUMERO_IMMAT IN ({','.join(registry_numbers)})
            )
            SELECT
                GINA_VUE_NAVIRE_DETAIL_SUBSET.NOM_NAVIRE,
                GINA_VUE_NAVIRE_DETAIL_SUBSET.NUMERO_IMMAT,
                GINA_VUE_NAVIRE_DETAIL_SUBSET.NUM_VERSION,
                GINA_VUE_NAVIRE_DETAIL_SUBSET.NUMERO_IMO,
                GINA.GIN_ADRESSE_COMPAGNIE.PAYS,
                NAVPRO.NAV_NAVIRE_FRANCAIS.ANNEE_CONSTRUCTION,
                GINA_VUE_NAVIRE_DETAIL_SUBSET.LIB_MATERIAU_COQUE,
                GINA_VUE_NAVIRE_DETAIL_SUBSET.LONGUEUR_HORS_TOUT,
                GINA_VUE_NAVIRE_DETAIL_SUBSET.LIB_QUARTIER as "quartier_enregistrement",
                GINA_VUE_NAVIRE_DETAIL_SUBSET.LIB_GENRE_NAVIGATION as "Genre navigation GINA",
                COMMUN.C_CODE_GENRE_NAVIGATION.LIBELLE_COURT as "genre_navigation NAVPRO", -- Pas de test possible sur Dataiku COMMUN
                GINA_VUE_NAVIRE_DETAIL_SUBSET.LIB_TYPE_NAVIRE as "Type de navire",
                NAVPRO.NAV_CODE_TYPE_MOTEUR.LIBELLE as "Type de moteur"
            FROM
                GINA_VUE_NAVIRE_DETAIL_SUBSET
                LEFT JOIN NAVPRO.NAV_NAVIRE_FRANCAIS ON NAVPRO.NAV_NAVIRE_FRANCAIS.ID_NAV_FLOTTEUR = GINA_VUE_NAVIRE_DETAIL_SUBSET.ID_NAV_FLOTTEUR
                /*Pour le genre navigation au sens NAVPRO*/
                LEFT JOIN NAVPRO.NAV_NAVIRE_STATUT ON NAVPRO.NAV_NAVIRE_STATUT.ID_NAV_FLOTTEUR = NAVPRO.NAV_NAVIRE_FRANCAIS.ID_NAV_FLOTTEUR
                LEFT JOIN COMMUN.C_CODE_GENRE_NAVIGATION ON COMMUN.C_CODE_GENRE_NAVIGATION.IDC_GENRE_NAVIGATION = NAVPRO.NAV_NAVIRE_STATUT.IDC_GENRE_NAVIGATION -- si erreur à retirer
                /* Pour le pavillon */
                LEFT JOIN NAVPRO.NAV_INDEX_PAVILLON ON NAVPRO.NAV_INDEX_PAVILLON.ID_NAV_FLOTTEUR = GINA_VUE_NAVIRE_DETAIL_SUBSET.ID_NAV_FLOTTEUR 
                LEFT JOIN GINA.GIN_ADRESSE ON GINA.GIN_ADRESSE.IDC_PAYS = NAVPRO.NAV_INDEX_PAVILLON.IDC_PAYS_PAVILLON
                LEFT JOIN GINA.GIN_ADRESSE_COMPAGNIE ON GINA.GIN_ADRESSE_COMPAGNIE.ID_GIN_ADRESSE_COMPAGNIE = GINA.GIN_ADRESSE.ID_GIN_ADRESSE
                /* Pour le type de moteur */
                LEFT JOIN NAVPRO.NAV_CODE_TYPE_MOTEUR ON NAVPRO.NAV_CODE_TYPE_MOTEUR.IDC_TYPE_MOTEUR =  NAVPRO.NAV_NAVIRE_FRANCAIS.IDC_TYPE_MOTEUR
        """
        with db_engine.connect() as connection:
            result = connection.execute(query)
            return result.fetchall()
