from persona import Persona   # importa la clase Persona del archivo persona.py
class Alumno(Persona):      # Crea la clase Alumno que herada de la clase Persona
    def __init__(self)-> None:   # Constructor de la clase Alumno
        super().__init__()   # Llama al cosntructor de la clase Alumno
        print("Alumno")   # Imprime le texto Alumno



objeto_alumno = Alumno()   # crea un objeto de la clase Alumno

