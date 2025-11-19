precio = float(input("Ingresar el precio del articulo: "))

if(tipo := int(input("Ingresar el tipo de articulo (1, 2, 3, etc): "))) == 1:
    precioart = (precio - (precio * 0.125))
    print (f"El articulo de tipo 1 tiene un descuento del 12,5 y queda con un precio igual a {precioart}")
elif(tipo == 2):
    precioart = (precio - (precio * 0.083))
    print (f"El articulo de tipo 2 tiene un descuento del 8,3 y queda con un precio igual a {precioart}")
elif(tipo == 3):
    precioart = (precio - (precio * 0.032))
    print (f"El articulo de tipo 3 tiene un descuento del 3,2 y queda con un precio igual a {precioart}")
else:
    print("NO tiene descuento")
