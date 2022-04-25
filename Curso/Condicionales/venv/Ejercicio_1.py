n1=int(input("INGRESA NUMERO1: "))
n2=int(input("INGRESA NUMERO2: "))
r1=n1%2
r2=n2%2
if r1==0 and n1!=0:
    if r2==0 and n2!=0:
        print(F"\nAMBOS NUMEROS SON PARES")
    else:
        print(f"\n{n1} ES PAR ")

elif r2==0 and n2!=0:
    print(f"\n{n2} ES PAR")
else:
    print("\nNINGUN NUMERO ES PAR")