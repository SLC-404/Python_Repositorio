a=float(input("Ingresa numero1: "))
b=float(input("Ingresa numero2: "))
op=input("INGRESAR OPERACION: ")

if op=='S' or op=='s':
    resultado=a+b
    print(f"\nSUMA= {resultado}")
if op=='R' or op=='r':
    resultado=a-b
    print(f"\nRESTA= {resultado}")
if op=='M' or op=='m':
    resultado=a*b
    print(f"\nMULTIPLICACION= {resultado:.2}")
if op=='D' or op=='d':
    if b!=0:
        resultado=a/b
        print(f"\nDIVISION= {resultado:.2}")
    else:
        print("\nNO SE PUEDE DIVIDIR ENTRE 0 >:v")