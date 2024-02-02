import calendar
from datetime import datetime

def obtener_valor_uf():
    UFanterior = 36500  # MODIFICAR MANUALMENTE
    fecha_actual = datetime.now()
    fecha_utima_UF = datetime(2024, 1, 9) # MODIFICAR MANUALMENTE
    fecha_ultimo_IPC = datetime(2024, 1, 8) # MODIFICAR MANUALMENTE
    cantidad_dias_mes_IPCanterior = calendar.monthrange(fecha_ultimo_IPC.year, fecha_ultimo_IPC.month)[1]
    variacion_IPC = 0.002  # MODIFICAR MANUALMENTE

    UF_actual = UFanterior * (1 + variacion_IPC) ** ((fecha_actual - fecha_utima_UF).days / cantidad_dias_mes_IPCanterior)
    UF_actual = round(UF_actual, 2)

    print(f"El valor actual de la UF Chilena es {UF_actual:.2f}")

if __name__ == "__main__":
    obtener_valor_uf()