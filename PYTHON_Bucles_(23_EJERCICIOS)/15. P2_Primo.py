if (n := int(input("Ingresar un número entero: "))) <= 1:
    print("ERROR: ingresar un número mayor a 1")
else: 
    es_primo = True
    for i in range(2, n):
        if n % i == 0 or n**(1/2) % 1 == 0:
            es_primo = False


    if es_primo:
        print(f"El número {n} SI ES PRIMO")
    else:
        print(f"El número {n} NO ES PRIMO")
    
    
    
