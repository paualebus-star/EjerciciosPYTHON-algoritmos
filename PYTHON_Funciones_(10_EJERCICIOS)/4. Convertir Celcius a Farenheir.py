def celcius_farenheit(c):
    F = (c * (9/5) + 32)
    return F
c = float(input("Ingresar los grados celius: "))

print (f"Los grados celcius{c} C° son igual a {celcius_farenheit(c)} F")