"""
   Programa5
   Nombre:Anhuar Fernando MI                                              
   Fecha: 30/01/2023                                                      
   Descripcion:codigo para poder medir el area y perimetro de cualquier triangulo
"""
import math # se importa la libreria math 

l1 = float(input("Ingrese el tamaño del 1er lado: "))   # se pide la medida del primer lado del triangulo desde el teclado
l2 = float(input("Ingrese el tamaño del 2do lado: ")) # se pide la medida del segundo lado del triangulo desde el teclado
l3 = float(input("Ingrese el tamaño del 3er lado: "))   # se pide la medida del tercer lado del triangulo desde el teclado

perimetro = l1 + l2 + l3 # se implementa la operacion de perimetro
s = perimetro / 2 # se implmenta una operacion donde s significa semi perimetro
area = math.sqrt((s * (s - l1) * (s - l2) * (s - l3))) # se implmenta el metodo mat.sqrt para sacar raiz a todo la operacion dentro de los parentesis
print("Perímetro:", perimetro) # se manda a  imprimir perimetro
print("Área:", area)    # se manda a impriumir el area