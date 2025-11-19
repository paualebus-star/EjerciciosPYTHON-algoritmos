A = str(input("Ingresar la primera palabra: "))
B = str(input("Ingresar la segunda palabra: "))

inter = A
A = B
B = inter

print("Despues del intercambio de palabras")
print(f"La primera palabra es {A}")
print(f"La segunda palabra es {B}")