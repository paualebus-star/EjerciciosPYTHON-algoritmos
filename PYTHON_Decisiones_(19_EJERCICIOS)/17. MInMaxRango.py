MinValor = float(input("Ingresar el valor minimo del rango: "))
MaxValor = float(input("Ingresar el valor maximo del rango: "))

if(x := float(input("Ingresar un número aleatorio: "))) > MinValor and x < MaxValor:
    print ("El número ingresado SI esta dentro del rango")
else:
    print ("El número ingresado NO esta dentro del rango")