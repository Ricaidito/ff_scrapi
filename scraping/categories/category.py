from enum import Enum


class MICMPCategory(Enum):
    CARNES = "Carnes"
    GRANOS = "Granos"
    EMBUTIDOS = "Embutidos"
    LACTEOS = "Lacteos"
    PAN = "Pan"
    VEGETALES = "Vegetales"


class SirenaCategory(Enum):
    CARNES = "carnes"
    CONGELADOS = "congelados"
    DELI = "deli"
    DESPENSA = "despensa"
    GALLETAS_Y_DULCES = "galletas-y-dulces"
    LACTEOS_Y_HUEVOS = "lacteos-y-huevos"
    LISTOS_PARA_COMER = "listos-para-comer"
    PANADERIA_Y_REPOSTERIA = "panaderia-y-reposteria"
    PESCADOS_Y_MARISCOS = "pescados-y-mariscos"
    PICADERAS = "picaderas"


# TODO: Add more categories
# Ref link: https://jumbo.com.do/
class JumboCategory(Enum):
    CARNES = "carnes-pescados-y-mariscos/carnes.html"
    PESCADOS = "carnes-pescados-y-mariscos/pescados-y-mariscos.html"
    LACTEOS = "lacteos-y-huevos/lacteos.html"
    QUESOS = "lacteos-y-huevos/quesos.html"
    HUEVOS = "lacteos-y-huevos/huevos.html"
    FRUTAS_FRESCAS = "frutas-y-verduras-frescas/frutas-frescas.html"
    HORTALIZAS = "frutas-y-verduras-frescas/hortalizas.html"
    VIVERES = "frutas-y-verduras-frescas/viveres.html"
    JAMONES = "embutidos-y-charcuteria/jamones-cocidos-y-curados.html"
    SALAMIS = "embutidos-y-charcuteria/salami-cocido-y-curado.html"


# TODO: Make this class and implement the categories in the nacional.py file
class NacionalCategory(Enum):
    CARNES = "carnes-pescados-y-mariscos/carnes"
    PESCADOS = "carnes-pescados-y-mariscos/pescados-y-mariscos"
    LACTEOS = "lacteos-y-huevos/leches"
    QUESOS = "quesos-y-embutidos/quesos"
    HUEVOS = "lacteos-y-huevos/huevos"
    FRUTAS = "frutas-y-vegetales/frutas"
    HORTALIZAS = "frutas-y-vegetales/vegetales-y-hortalizas"
    VIVERES = "frutas-y-vegetales/viveres"
    EMBUTIDOS = "quesos-y-embutidos/charcuteria-y-embutidos"
