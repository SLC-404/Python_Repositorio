n1=float(input("INGRESA NUMERO1: "))
n2=float(input("INGRESA NUMERO2: "))
n3=float(input("INGRESA NUMERO3: "))
if n1>=n2 and n1>=n3:
    print(f"EL NUMERO MAYOR ES N1: {n1}")
else:
    if n2>=n1 and n2>=n3:
        print(f"EL NUMERO MAYOR ES N2: {n2}")
    else:
        if n3>=n2 and n3>=n1:
            print(f"EL NUMERO MAYOR ES N3: {n3}")
