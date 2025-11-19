num1 = int(input("Ingresar el primer número: "))

if (num2 := int(input("Ingresar el segundo número: "))) > num1:
    print(f"El segundo número ({num2}) es MAYOR que el primero ({num1})")
elif(num2 < num1):
    print(f"El segundo número ({num2}) es MENOR que el primero ({num1})")
else:
    print("Los dos números son IGUALES")
    