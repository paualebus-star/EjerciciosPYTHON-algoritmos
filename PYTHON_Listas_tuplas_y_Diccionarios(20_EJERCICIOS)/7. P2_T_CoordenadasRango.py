x = float(int(input("Ingresar el valor de x: ")))
y = float(int(input("Ingresar el valor de y: ")))

inicio = float(int(input("Ingresar el MINIMO valor del rango: ")))
fin = float(int(input("Ingresar el MAXIMO el valor del rango: ")))

if x > inicio or x < fin and y > inicio or y < fin:
    print(f"SI esta dentro del rango la coordenada {x, y}")
else:
    print(f"NO esta dentro del rango la coordenada {x, y}")