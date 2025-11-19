Estatura = float(input("Ingresar la estatura en m: "))
Edad = float(input("Ingresar la edad del aspirante: "))


if(EstadoCivil := str(input("Ingresar el estado de civil del aspirante (S/C/V/D/U): "))) != "S" and EstadoCivil != "s":
    print("El aspirante NO ESTA APTO para entrar al ejército")
else:
    if(genero := str(input("Ingresar el genero del aspirante (F/M/O): "))) == "F" or genero == "f":
        if (Estatura > 1.60 and Edad >= 20 and Edad <= 25):
            print ("La aspirante mujer SI esta APTA de ingresar en el ejército")
        else:
            print ("La aspirante mujer NO esta APTA de ingresar en el ejército")
    elif(genero == "M" or genero == "m"):
        if (Estatura > 1.65 and Edad >= 18 and Edad <= 24):
            print("El aspirante hombre SI esta APTO de ingresar en el ejército")
        else:
            print("El aspirante hombre NO esta APTO de ingresar en el ejército")
    else:
        print("El aspirante tiene otro género")
