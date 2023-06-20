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


# TODO: Make this class and implement the categories in the nacional.py file
class NacionalCategory(Enum):
    pass
