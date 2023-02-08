"""
   Programa7
   Nombre:Anhuar Fernando MI                                              
   Fecha: 01/02/2023                                                      
   Descripcion:comparacion de dos numeros e imprimir el numero mayor
"""
numero1 = int(input("ingrese un numero: "))   # se pide el ingreso de un valor
numero2 = int(input("ingrese un segundo numero: "))   # se pide el ingreso del segundo valor

if numero1 >= numero2 :   # se aplica la condicion numero1 es mayor o igual a numero2
    print("el mayor es: ",numero1)     # se manda a imprimir numero1 si se cumple la condicion
else:                 # se implementa else para poder imprimir el numero2 en caso de cumplir la condicion
    print("el mayor es: ",numero2)     # se manda a imprimir el numero 2 en caso de no cumplirse la condicion
    
  