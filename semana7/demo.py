import pandas as pd
from openpyxl import Workbook
productos = pd.DataFrame({'SKU': ['75007614', '750100912803', '7501045403908'],
                          'Nombre': ['Coca cola  600ml', 'Nescafe 42g', 'Atun Dolores Aceite 133g'],
                          'Unidad': ['mililitros', 'gramos', 'gramos']})
libro = Workbook()
hoja = libro.active
hoja.title = 'Productos'
encabezados = ['SKU', 'Nombre', 'Unidad']
for i, encabezado in enumerate(encabezados, start=1):
    hoja.cell(row=1, column=i, value=encabezado)
for fila in productos.itertuples():
    datos_fila = [fila.SKU, fila.Nombre, fila.Unidad]
    hoja.append(datos_fila)
while True:
   sku =input("SKU:")
   nombre = input("Nombre:")
   unidad = input("Unidad:")
   libro.save('demo.xlsx')



