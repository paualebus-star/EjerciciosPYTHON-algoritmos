a1 = float(input("Ingresar el mínimo valor del PRIMER rango (a1): "))
b1 = float(input("Ingresar el maxímo valor del PRIMER rango (b1): "))
a2 = float(input("Ingresar el mínimo valor del SEGUNDO rango (a2): "))
b2 = float(input("Ingresar el maxímo valor del SEGUNDO rango (b2): "))
a3 = float(input("Ingresar el mínimo valor del TERCER rango (a3): "))
b3 = float(input("Ingresar el maxímo valor del TERCER rango (b3): "))

if(a1 >= b1 or a2 >= b2 or a3 >= b3 or b1 >= a2 or b2 >= a3):
    print ("ERROR: Los rangos ingresados se cruzan")
elif(x := float(input("Ingresar un número aleatorio: "))) > a1 and x < b1 or x > a2 and x < b2 or x > a3 and x < b3:
    print ("El número ingresado SI esta dentro de uno de los intervalos ingresados")
else:
    print("El número ingresado NO esta dentro de uno de los intervalos ingresados")