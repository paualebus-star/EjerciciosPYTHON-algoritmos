print("¡¡VAMOS A INVERTIR UN NUMERO!!")

num = int(input("Ingresar número entero de dos o mas cifras POSITIVO: "))

if num <= 0:
    print("ERROR: ingresar un número postivo de dos o más cifras")

while num > 0:

    invertido = 0
    original = num

    ultimo_digito = num % 10
    invertido = invertido * 10 + ultimo_digito
    num = num // 10
    
    print(ultimo_digito, end="")

    