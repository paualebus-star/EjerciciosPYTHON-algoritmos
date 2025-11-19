print("----MENU REPETITIVO----")
print("Opciones: sumar, restar o salir")

while True:
    opcion = str(input("Ingrese su opción: "))
    
    if opcion == "salir":
        break
    elif opcion == "sumar" or opcion == "Sumar":
        numero1 = int(input("Ingresar primer número que quiera sumar: "))
        numero2 = int(input("Ingresar segundo número que quiera sumar: "))
        suma = numero1 + numero2

        print(f"El total de la suma es {suma}")

    elif opcion == "restar" or opcion == "Restar":
        numero1 = int(input("Ingresar primer número que quiera restar: "))
        numero2 = int(input("Ingresar segundo número que quiera restar: "))
        resta = numero1 - numero2

        print(f"El total de la resta es {resta}")
    
    else:
        print("ERROR: opción NO valida")
