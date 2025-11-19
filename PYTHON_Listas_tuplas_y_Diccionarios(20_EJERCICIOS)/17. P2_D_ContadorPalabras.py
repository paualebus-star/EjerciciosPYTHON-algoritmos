print("Ingrese una FRASE de su preferencia")

Frase = input("Frase: ")
Palabras = Frase.split() # Dividir frase en palabras

contador = {} # Crear diccionario para contar

for Palabra in Palabras:
    # Primera palabra "hola": no está en contador → contador["hola"] = 1
    # Segunda palabra "mundo": no está → contador["mundo"] = 1  
    # Tercera palabra "hola": SÍ está → contador["hola"] = 1 + 1 = 2

    if Palabra in contador: # Pregunta: ¿Ya he visto esta palabra antes?
        contador [Palabra] += 1 #  SI: entonces incrementa su contador
    else:
        contador [Palabra] = 1 # NO: entonces es la primera vez que la veo

print(contador)
