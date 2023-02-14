"""
   Programa11
   Nombre:Anhuar Fernando MI                                              
   Fecha: 14/02/2023                                                      
   Descripcion: clases alumno y persona
"""
class Persona:
    __nombre = None
    def __init__(self): # se aplica self para llamar a la clase persona
        print("Persona")  #imprimir "perosna"


class Alumno(): # se cre 
    def __init__(self):
        super().__init__()
        print("Alumno")
objeto_persona = Persona()
objeto_alumno = Alumno()
objeto_persona.nombre = "dejah"
print(objeto_persona.nombre)
objeto_alumno.nombre = "Jhon Carter"
print(objeto_alumno.nombre)
objeto_alumno.email = "jhon@utectulancingo.edu.mx"
print(objeto_alumno.email)