contador=1

while(contador<=3):

    print("Calculadora")
    print(" ------------- ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")

    print("")
    opcion=int(input("Escoja una opcion: "))

    if(opcion==1):
        x=float(input("Primer numero: "))
        y=float(input("Segundo numero: "))
        resultado=x+y
        print(f"{x} + {y} = {resultado}")
    elif(opcion==2):
        x=float(input("Primer numero: "))
        y=float(input("Segundo numero: "))
        resultado=x-y
        print(f"{x} - {y} = {resultado}")
    elif(opcion==3):
        x=float(input("Primer numero: "))
        y=float(input("Segundo numero: "))
        resultado=x*y
        print(f"{x} * {y} = {resultado}")
    else:
        print("Opcion no valida")
    
    contador=contador+1