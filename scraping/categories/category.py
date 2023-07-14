from enum import Enum
from sources.jumbo_category import JumboCategory
from sources.micm_category import MICMPCategory
from sources.nacional_category import NacionalCategory
from sources.sirena_category import SirenaCategory


class ProductCategory(Enum):
    CARNES = "Carnes"
    GRANOS = "Granos"
    EMBUTIDOS = "Embutidos"
    LACTEOS = "Lácteos"
    PAN = "Pan"
    VEGETALES = "Vegetales"
    CONGELADOS = "Congelados"
    DELI = "Deli"
    DESPENSA = "Despensa"

    CLASSIFICATION_MAPPING = {
        # MICMP
        MICMPCategory.CARNES: CARNES,
        MICMPCategory.GRANOS: GRANOS,
        MICMPCategory.EMBUTIDOS: EMBUTIDOS,
        MICMPCategory.LACTEOS: LACTEOS,
        MICMPCategory.PAN: PAN,
        MICMPCategory.VEGETALES: VEGETALES,
        # Sirena
        SirenaCategory.CARNES: CARNES,
        SirenaCategory.CONGELADOS: CONGELADOS,
        SirenaCategory.DELI: DELI,
        SirenaCategory.DESPENSA: DESPENSA,
        # Jumbo
        JumboCategory.CARNES: CARNES,
        JumboCategory.LACTEOS: LACTEOS,
        # Nacional
        NacionalCategory.CARNES: CARNES,
        NacionalCategory.LACTEOS: LACTEOS,
        NacionalCategory.EMBUTIDOS: EMBUTIDOS,
    }

    @classmethod
    def get_category(cls, category):
        return cls.CLASSIFICATION_MAPPING.get(category, None)
