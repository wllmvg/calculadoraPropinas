Feature: Calcular propina

  Scenario: Calcular el 15% de propina
    Given el monto de la cuenta es 100
    And el porcentaje de propina es 15
    When calculo la propina
    Then el resultado debe ser 15.0

  Scenario: Especificar porcentaje diferente
    Given el monto de la cuenta es 200
    And el porcentaje de propina es 10
    When calculo la propina
    Then el resultado debe ser 20.0
