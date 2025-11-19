if (LitrosAgua := float(input("Ingresar los litros de agua del tanque: "))) >= 250 and LitrosAgua < 450:
    print ("El nivel esta adecuado. La llave debe estar CERRADA.")
elif (LitrosAgua < 250):
    print ("El nivel de agua esta bajo. La llave debe estar ABIERTA.")
else:
    print ("El nivel de agua esta alto. La llave debe estar CERRADA.")