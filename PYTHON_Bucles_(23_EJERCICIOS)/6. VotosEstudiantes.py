cantidadEstudiantes = int(input("Ingresar la cantidad de estudiantes: "))

votos_android = 0
votos_ios = 0
votos_invalida = 0

contadorEstudiantes = 0

while (contadorEstudiantes < cantidadEstudiantes):
    
    codigoEstudiante = str(input("Ingresar el código del estudiante: "))

    if(eleccion := input("Ingresar elección de plataforma (Android, iOs u otros): ")) == "Android" or eleccion == "android":
        votos_android += 1
    
    elif eleccion == "iOs" or eleccion == "ios":
        votos_ios += 1
    else:
        votos_invalida += 1

    contadorEstudiantes += 1
    
    
print(f"La cantidad que eligieron Android  es {votos_android}")
print(f"La cantidad que eligieron iOs  es {votos_ios}")
print(f"La cantidad que eligieron otra plataforma  es {votos_invalida}")

if votos_android > votos_ios:
    print("La plataforma elegida es ANDROID")
elif votos_ios > votos_android:
    print("La plataforma elegida es iOS")
else:
    print("Hay un EMPATE: Se usará otro mecanismo de elección")