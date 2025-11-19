nombre = input("Ingresar el nombre de la persona : ")

if (edad := int(input("Ingresar la edad: "))) >= 18:
    print (f"{nombre} es mayor de edad")
else:
    print (f"{nombre} NO es mayor de edad")