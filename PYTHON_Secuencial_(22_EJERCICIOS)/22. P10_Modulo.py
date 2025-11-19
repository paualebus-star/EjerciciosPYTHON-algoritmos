num1 = float(input("Ingresar primer número aleatorio: "))
num2 = float(input("Ingresar segundo  número aleatorio: "))

mod1 = num1 % num2
mod2 = num2 % num1

print(f"La operación modulo del primer y segundo número es {mod1}")
print(f"La operación modulo del segundo y primer número es {mod2}")