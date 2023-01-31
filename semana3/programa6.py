"""
   Programa6
   Nombre:Anhuar Fernando MI                                              
   Fecha: 31/01/2023                                                      
   Descripcion:calcular el area y perimtero de un circulo y cuadrado
"""

diam = float(input("introduzca el diametro: "))  # se pide al usuario que intrduzca la medida de su diametro
lado = float(input("introduzca la mide de cualquier lado del cuadrado: "))   # se pide al usuario que introduzca la medida del cualquier lado del cuadrado
radio = diam/2   # se realiza la ooperacion de dividir diamtro entre 2 para sacar el radio
area_circulo = (3.1416)*(radio**2)    # se realiza la operacion para poder sacar el area del circulo
perimetro_circulo = 3.1416 * diam   # se realiza la operacion para sacar el diametro del circulo
area_cuadrado = lado **2   #  se realiza la operacion para sacar el area del cuadrado
perimetro_cuadrado = lado*4   # se realiza la operacion para sacar el perimetro de un cuadrado  
print("el area del circulo con un radio de ",radio," es ",area_circulo)   # se manda a imprimir el area del circulo
print("el perimetro del circulo con un radio de ",radio," es ",perimetro_circulo)   #se manda a imprimir el perimtero del circulo

print("el area del cuadrado con la medida del lado ",lado," es ",area_cuadrado) # se manda a imprimir el area deñ cuadrado
print("el perimetro del cuadrado con la medida de lado ",lado," es ",perimetro_cuadrado)  # se manda a imprimir el perimetro del cuadrado