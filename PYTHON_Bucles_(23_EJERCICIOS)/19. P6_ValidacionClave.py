clave_correcta = "limonada"
intento_actual = 1
intento_maximo = 3

print("=== ACCESO AL SISTEMA ===")

while intento_actual <= intento_maximo:
    clave_usuario = str(input("Ingresar constraseña: "))
    
    if clave_usuario == clave_correcta:
        print("Acceso permitido")
        break
    else:
        if intento_actual == intento_maximo:
            print("Acceso DENEGADO, ya agostaste tus intentos :(")
        else:
            print("Clave INCORRECTA, intente de nuevo")
        
        intento_actual += 1
