# CHILEAN UF CALCULATOR

import calendar
from datetime import datetime

def obtener_valor_uf():
    UFanterior = 36500  
    fecha_actual = datetime.now()
    fecha_utima_UF = datetime(2024, 1, 9) 
    cantidad_dias_mes_IPCanterior = obtener_cantidad_dias_mes_IPCanterior() 
    variacion_IPC = 0.002  

    UF_actual = UFanterior * (1 + variacion_IPC) ** ((fecha_actual - fecha_utima_UF).days / cantidad_dias_mes_IPCanterior)

    print(f"El valor actual de la UF Chilena es {UF_actual:.2f}")

def obtener_cantidad_dias_mes_IPCanterior():
    # Obtén el mes y año actuales
    mes_actual = datetime.now().month
    año_actual = datetime.now().year

    # Si estás calculando para el mes anterior, resta 1 al mes actual
    mes_IPCanterior = mes_actual - 1 if mes_actual > 1 else 12
    año_IPCanterior = año_actual if mes_actual > 1 else año_actual - 1

    # Obtiene la cantidad de días en el mes del IPC anterior
    cantidad_dias = calendar.monthrange(año_IPCanterior, mes_IPCanterior)[1]

    return cantidad_dias

if __name__ == "__main__":
    obtener_valor_uf()
    cantidad_dias_mes_IPCanterior = obtener_cantidad_dias_mes_IPCanterior()
