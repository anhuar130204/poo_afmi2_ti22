from persona import Persona # importa la clase Persona del archivo persona.py
class Profesor(Persona): # crea la clase profesor que hereda de la clase persona
    def __init__(self) -> None: # constructor de la clase Profesor
        super().__init__()   # Llama al cosntrcutor de la clase Persona
        print("Profesor")   # Imprime el texto Profesor

objeto_profesor = Profesor()   # crea un objeto de la clase profesor