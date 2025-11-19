cm = float(input("Ingresar la medida en centimetros: "))

m = cm *(1/100)
pulg = cm * (1/2.54)
pies = cm * (1/30.48)
yardas = cm *(1/91.44)

print(f"La medida ingresada en cm convertida en m es igual a {m}")
print(f"La medida ingresada en cm convertida en pulgadas es igual a {pulg}")
print(f"La medida ingresada en cm convertida en pies es igual a {pies}")
print(f"La medida ingresada en cm convertida en yardas es igual a {yardas}")