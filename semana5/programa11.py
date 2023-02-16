"""
   Programa11
   Nombre:Anhuar Fernando MI                                              
   Fecha: 14/02/2023                                                      
   Descripcion: clases alumno y persona con heredacion
"""
class Persona:
    __nombre = None # se crea la variable privada __nombre
    def __init__(self): # se aplica self para llamar a la clase persona
        print("Persona")  #imprimir "perosna"


class Alumno(Persona):  # Crea la clase Alumno que hera de la clase Persona
     def __init__(self)-> None:   # Constructor de la clase Alumno
        super().__init__()   # Llama al cosntructor de la clase Alumno
        print("Alumno")   # Imprime le texto Alumno
objeto_persona = Persona() # se crea el objeto Persona
objeto_alumno = Alumno()  # se crea el obejeto alumno
objeto_persona.nombre = "dejah"  # se mada a llamar ala funcion .nombre
print(objeto_persona.nombre) # se imrpime la variable objeto_alumno.nombre
objeto_alumno.nombre = "Jhon Carter" # se crea la variable objeto_alumno.nombre 
print(objeto_alumno.nombre) # se imprime la variable objeto_nombre.nombre
objeto_alumno.email = "jhon@utectulancingo.edu.mx"   # se crea la variable objeto_alumno.email
print(objeto_alumno.email) # se imprime la variable objeto_alumno.email
