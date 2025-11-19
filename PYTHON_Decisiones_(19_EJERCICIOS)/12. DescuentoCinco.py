if(precio := float(input("Ingresar el precio del articulo en COP: "))) > 150000:
    precioart = precio - (precio * 0.05)
    print (f"El articulo tiene un descuento del 5%, y su precio es {precioart}")
else:
    print ("El articulo NO tiene descuento porque su costo es menor a 150000")