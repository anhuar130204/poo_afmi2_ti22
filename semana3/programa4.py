import math #importacion del metodo math
numero1 = int(input('Numero 1:')) # se declara la variable y pide introducir un entero
numero2 = int(input("numero 2:")) # se declara la variable y pide introducir un entero
suma = numero1 + numero2   # se realiza la operacion suma
resta = numero1 - numero2   # se realiza la operacion resta
multiplicacion = numero1 * numero2   # se realiza la operacion de multiplicacion
div = numero1 / numero2   # se realiza la operacion de division
pot = math.pow(numero1 , numero2)    # se realiza la operacion de potencia con el metodo math
print("el resultado de la suma es:",suma,"\n"  # se imprime todas las operaciones con salto de linea
      "Resta:",resta,"\n"
      "multiplicacion",multiplicacion,"\n"
      "division",div,"\n"
      "potencia:",pot)
