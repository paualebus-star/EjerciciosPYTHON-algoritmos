precio = float(input("Ingresar el precio del articulo: "))

if(tipo := str(input("Ingresar el tipo de articulo (Textil/Electrodoméstico/Cocina/Video juego/ Otro): "))) == "textil" or tipo == "Textil" or tipo == "Otro" or tipo == "otro":
    print ("Los articulos textiles u otros NO tienen descuento")
elif (tipo == "Electrodoméstico" or tipo == "electrodoméstico" or tipo == "Electrodomestico" or tipo == "electrodomestico"):
    precioart = precio - (precio * 0.037)
    print (f"Los articulos electrodomésticos SI tiene descuento de un 3,7 % y el precio de su articulo es igual a {precioart}")
elif (tipo == "Cocina" or tipo == "cocina"):
    precioart = precio - (precio * 0.042)
    print (f"Los articulos de cocina SI tiene descuento de un 4,2 % y el precio de su articulo es igual a {precioart}")
elif (tipo == "Videojuego" or tipo == "videojuego" or tipo == "Video juego" or tipo == "video juego"):
    precioart = precio - (precio * 0.078)
    print (f"Los video juegos SI tiene descuento de un 7,8 % y el precio de su articulo es igual a {precioart}")
else:
    print("ERROR, observe bien las opciones")