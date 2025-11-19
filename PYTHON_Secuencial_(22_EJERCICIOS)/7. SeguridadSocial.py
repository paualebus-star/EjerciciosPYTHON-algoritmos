salario = float(input("Ingresar el salario base del empleado: "))
salud = salario * (4/100)
pension = salario * (4/100)

Total = salario - salud - pension

print(f"El total del salario para el empleado es {Total}")