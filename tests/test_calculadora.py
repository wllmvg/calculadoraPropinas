import pytest
from calculadora import calcular_propina_y_total

def test_calculo_10_por_ciento():
    propina, total = calcular_propina_y_total(100, 10)
    assert propina == 10.0
    assert total == 110.0

def test_calculo_20_por_ciento():
    propina, total = calcular_propina_y_total(200, 20)
    assert propina == 40.0
    assert total == 240.0

def test_monto_cero():
    propina, total = calcular_propina_y_total(0, 15)
    assert propina == 0.0
    assert total == 0.0

def test_porcentaje_cero():
    propina, total = calcular_propina_y_total(150, 0)
    assert propina == 0.0
    assert total == 150.0

def test_monto_negativo():
    with pytest.raises(ValueError):
        calcular_propina_y_total(-50, 10)

def test_porcentaje_negativo():
    with pytest.raises(ValueError):
        calcular_propina_y_total(100, -10)
