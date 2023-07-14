from enum import Enum


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
