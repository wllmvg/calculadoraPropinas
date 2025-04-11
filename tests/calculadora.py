def calcular_propina_y_total(monto, porcentaje):
    if monto < 0 or porcentaje < 0:
        raise ValueError("Monto y porcentaje deben ser positivos")
    
    propina = monto * (porcentaje / 100)
    total = monto + propina
    return round(propina, 2), round(total, 2)
