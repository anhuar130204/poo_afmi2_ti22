"""
   Programa9
   Nombre:Anhuar Fernando MI                                              
   Fecha: 08/02/2023                                                      
   Descripcion: definición de métodos para saber el mayor de 2 números 
"""
def mayor (numero1,numero2):  # definicion del metodo mayor para asignar numeres 
  if numero1 > numero2:   # comparacion de numero1 mayor a numero2
     print (numero1)  # imprimir el valor de numero1
  elif numero2 >numero1:   # comparación de numero2 mayor que Numero1
     print(numero2) # imprimir el valor de número2
  else:
      print ("Iguales")   # imprimir iguales 
mayor (3,2) # 3
mayor (2,3) # 3
mayor (3,3) # Iguales

def mayor (numero1:int,numero2:int)->int: #asignacion de metodo mayor para solo recibir valores enteros y sacar número entero
    mayor = None
    if numero1> numero2:
     mayor =numero1   #  asignación de resultado mayor es igual a valor de número1
    elif numero2 > numero1:
     mayor = numero2  # asignación de resultado mayor = a valor de numero2 
    else:
     mayor = None #asignacion de resultado mayor
    return mayor # regreso del método mayor
print(mayor(3,2)) # 3
print(mayor(2,3)) # 3
print(mayor(3,3))  # None



