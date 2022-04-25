opc= int(input("\t\t\t\tMENU\n"
      "\t1.-INGRESAR DINERO EN LA CUENTA\n"
      "\t2.-RETIRAR DINERO DE LA CUENTA\n"
      "\t3.-MOSTRAR DINERO DISPONIBLE\n"
      "\t4.-SALIR\n"
      "\n¿QUE OPCION DESEA?: \n"))
if opc==1:
    dinero=float(input("¿CUANDO DINERO DESEA DEPOSITAR?: "))
    print(f"DEPOSITO DE {dinero} REALIZADO")
    print(f"SALDO ACTUAL {dinero+1000} DOLARES")
if opc==2:
    dinero= float(input("¿CUANDO DINERO DESEA RETIRAR?: "))
    if dinero>1000:
        print("NO TIENE ESA CANTIDAD DE DINERO")
    else:
        print(f"RETIDO DE {dinero} REALIZADO")
        print(f"SALDO ACTUAL {1000 - dinero} DOLARES")
if opc==3:
    print("SU SALDO ACTUAL ES DE 1000 DOLARES")
if opc==4:
    print("GRACIAS :3 POR SU ATENCION")