cantidad = float(input("Ingresar la cantidad de dinero invertido: "))
porcentaje = float(input("Ingresar el porcentaje de los intereses (0 a 100): "))
periodo = float(input("Ingresar el periodo de tiempo en días: "))

valorIntereses = (cantidad * (porcentaje / 100) * periodo) / 360

impuesto  = (valorIntereses * (7/100))

TotalPagar = cantidad + valorIntereses - impuesto

print(f"El valor de intereses es {valorIntereses}")
print(f"El impuesto de retención de fuente es del 7 %  queda en un total de {impuesto}")
print(f"El total a pagar teniendo en cuenta intereses e impuestos es igual a {TotalPagar}")