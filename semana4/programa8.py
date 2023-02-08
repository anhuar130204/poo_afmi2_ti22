"""
   Programa8
   Nombre:Anhuar Fernando MI                                              
   Fecha: 07/02/2023                                                      
   Descripcion:comparacion de dos numeros e imprimir el numero mayor en 11 versiones
"""
n1 = int(input("n1: "))
n2 = int(input("n2: "))

if n1 > n2:  # condicion if de n1 es mayo que n2
    print(n1) # imprimir n1
if n2>n1:    # condicion if n2 es mayor que n1
    print(n2)   # imprimir n2
if n1 == n2:    # condicion igual n1 a n2
    print(None)   # imprimir None
# version 2
if n2 > n1:  # condicion if de n2 es mayo que n1
    print(n2)   # imprimir n1
if n1>n2:    # condicion if n1 es mayor que n2
    print(n1)   # imprimir n1
if n2 == n1:    # condicion igual n2 a n1
    print(None)   # imprimir None

# version 3
if n1>n2:
    print(n1)
elif n2 > n1:
    print(n2)
else:
    print(None)

#version 4

if n1<n2:
    print (n2)
elif n2<n1:
    print(n1)
else:
    print(None)
#version 5
if n1<n2:
 print(n2)
if n2<n1:
    print(n2)
    if n1 == n2:
        print(None)
# version 6
        if n1>=n2:
            if n1>n2:
                print(n1)
            else:
                print(None)
        else:
            print(n2)
# version 7
if n1 <= n2:
    if n1<n2:
        print(n2)
    else:
        print(None)
else:
    print(n1)
# version 8
    if n1<= n2:
        if n1 == n2:
            print(None)
        else:
            print(n2)
    else:
        print(n1)
# version 9
if n1 == n2:
 print(None)
elif n1>n2:
 print(n1)
else:
 print(n2)
# version 10
if n2 == n1:
    print(None)
elif n2>n1:
    print(n2)
else:
    print(n1)
#version 11
    if n1 == n2:
        print (None)
    elif n1>n2:
        print(n1)
    else:
        print(n2)
        print(n1)
        
    
    