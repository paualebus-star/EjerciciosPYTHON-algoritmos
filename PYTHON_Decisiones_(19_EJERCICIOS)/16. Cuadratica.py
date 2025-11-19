a = float(input("Ingresar el valor a la variable a: "))
b = float(input("Ingresar el valor a la variable b: "))
c = float(input("Ingresar el valor a la variable c: "))

discri = b**2 - 4 * a * c

if( discri >= 0 and a != 0):
    soluciónx1 = (- b + (discri)**(1/2)) / (2*a)
    soluciónx2 = (- b - (discri)**(1/2)) / (2*a)

    print(f"La ecuación cuadratica SI tiene solución, es igual a {soluciónx1} y {soluciónx2}")

else:
    print(f"La ecuación cuadratica NO tiene solución")