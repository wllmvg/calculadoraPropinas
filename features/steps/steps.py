import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from behave import given, when, then
from tests import calculadora

@given('el monto de la cuenta es {monto}')
def step_monto(context, monto):
    context.monto = float(monto)

@given('el porcentaje de propina es {porcentaje}')
def step_porcentaje(context, porcentaje):
    context.porcentaje = float(porcentaje)

@when('calculo la propina')
def step_calcular(context):
    context.resultado = calculadora(context.monto, context.porcentaje)

@then('el resultado debe ser {esperado}')
def step_verificar(context, esperado):
    assert context.resultado == float(esperado)
