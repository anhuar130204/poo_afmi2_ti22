import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
wb2 = load_workbook('demo.xlsx')

ws =  wb2['hoja1']
