def maximo_de_tres(a, b, c):
    if a > b and a > c:
        return "a es MAYOR"
    if b > a and b > c:
        return "b es MAYOR"
    if c > b and c > a:
        return "c es MAYOR"
    else:
        return "Todos los valores son IGUALES"
    
a = float(input("Ingresar el valor de a: "))
b = float(input("Ingresar el valor de b: "))
c = float(input("Ingresar el valor de c: "))

print (f"El valor de {maximo_de_tres(a, b, c)}")