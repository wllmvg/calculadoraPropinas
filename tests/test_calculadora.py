import pytest
from calculadora import calcular_propina_y_total

##Se calcula la propina(10%) segun un monto de 100 COP
def test_calculo_10_por_ciento():
    propina, total = calcular_propina_y_total(100, 10)
    assert propina == 10.0
    assert total == 110.0

##Se calcula la propina(20%) segun un monto de 200 COP
def test_calculo_20_por_ciento():
    propina, total = calcular_propina_y_total(200, 20)
    assert propina == 40.0
    assert total == 240.0

##Se calcula la propina(15%) segun un monto de 0 COP
def test_monto_cero():
    propina, total = calcular_propina_y_total(0, 15)
    assert propina == 0.0
    assert total == 0.0


##Se calcula la propina(0%) segun un monto de 150 COP
def test_porcentaje_cero():
    propina, total = calcular_propina_y_total(150, 0)
    assert propina == 0.0
    assert total == 150.0


##Se calcula la propina(10%) segun un monto de -500 COP
def test_monto_negativo():
    with pytest.raises(ValueError):
        calcular_propina_y_total(-50, 10)


##Se calcula la propina(-10%) segun un monto de 100 COP
def test_porcentaje_negativo():
    with pytest.raises(ValueError):
        calcular_propina_y_total(100, -10)
