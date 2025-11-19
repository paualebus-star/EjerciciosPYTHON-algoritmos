num1 = float(input("Ingresar el primer número: "))
num2 = float(input("Ingresar el segundo número: "))
num3 = float(input("Ingresar el tercer número: "))
num4 = float(input("Ingresar el cuarto número: "))

if (num1 > num2 and num1 > num3 and num1 > num4):
    print ("El PRIMER número es MAYOR")
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print ("El SEGUNDO número es MAYOR")
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print ("El TERCER número es MAYOR")
elif(num4 > num1 and num4 > num2 and num4 > num3):
    print ("El CUARTO número es MAYOR")
else: 
    print ("Dos o más número son IGUALES")
