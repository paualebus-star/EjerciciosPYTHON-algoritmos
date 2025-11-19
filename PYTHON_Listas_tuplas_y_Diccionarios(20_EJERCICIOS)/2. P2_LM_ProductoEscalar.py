print("Ingrese dos listas de números del mismo tamaño, recordar dejar un especio entre números")

ListaA = list(map(int, input("Primera lista: ").split()))
ListaB = list(map(int, input("Segunda lista: ").split()))

if len(ListaA) != len(ListaB):
    print("ERROR: ambas listas deben ser con la misma cantidad de números")
else:
    producto_escalar = 0

    for i in range(len(ListaA)):
        producto_escalar += ListaA[i] * ListaB[i] 
    
    print(f"El producto escalar es {producto_escalar}")