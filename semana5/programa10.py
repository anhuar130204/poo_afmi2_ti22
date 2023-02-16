"""
   Programa10
   Nombre:Anhuar Fernando MI                                              
   Fecha: 13/02/2023                                                      
   Descripcion: clases alumno y persona,colaborador y profesor con heredacion
"""
class Persona:  # cracion de la clase Persona
    __nombre = None  # variable privada __nombre
    __correo = None    # variable privada __correo
    __edad = None      # variable privada __edad
    def __init__(self):   # constructor de la clase Persona
        print("Persona")   # imprime el texto persona

    def setNombre(self,nombre):   # funcion para modificar el valor de la variable __nombre
        self.__nombre = nombre     # Modifica el valor de la variable privada __nombre y la vuelve publica como nombre
    def getNombre(self):    # Función que regresa el valor de la variable privada __nombre 
        return self.__nombre     # Regresa el valor de la variable privada __nombre

    def setCorreo(self,correo):    # funcion para modificar el valor de la variable __correo
        self.__correo  = correo    # Modifica el valor de la variable privada __correo y la vuelve publica como correo
    def getCorreo(self):    # Función que regresa el valor de la variable privada __correo
        return self.__correo    # Regresa el valor de la variable privada __correo

    def setEdad (self,edad):   # funcion para modificar el valor de la variable __edad
        self.__edad = edad  # Modifica el valor de la variable privada __edad y la vuelve publica como edad
    def getEdad(self):        # Función que regresa el valor de la variable privada __edad
        return self.__edad    # Regresa el valor de la variable privada __edad
        
dejah = Persona()   # se crea un objeto persona
dejah.setNombre("Dejah")  # se llama al metodo setNombre para llenarlo
print(dejah.getNombre())  # se imprime el nombre introducido en setNombre
dejah.setCorreo("145134@gmail.com")  # se llena el mmetodo setCorreo
print(dejah.getCorreo()) # se imprime correo introducido en setCorreo


class Alumno: # cracion de la clase Alumno
    __nombre = None # variable privada __nombre
    __matricula = None   # variable privada __matricula
    __carrera = None      # variable privada __carrera
    def __init__(self):    # constructor de la clase alumno
        print("Alumno")    # imprime el texto Alumno
    def setNombre(self,nombre):  # funcion para modificar el valor de la variable __nombre
        self.__nombre = nombre     # Modifica el valor de la variable privada __nombre y la vuelve publica como nombre
    def getNombre(self):         # Función que regresa el valor de la variable privada __nombre
        return self.__nombre   # Regresa el valor de la variable privada __nombre
        
    def setMatricula(self,matricula):   # funcion para modificar el valor de la variable __matricula
        self.__matricula = matricula    # Modifica el valor de la variable privada __matricula y la vuelve publica como matricula
    def getMatricula(self):                 # Función que regresa el valor de la variable privada __matricula
        return self.__matricula        # Regresa el valor de la variable privada __edad
        
    def setCarrera(self,carrera):         # funcion para modificar el valor de la variable __carrera
        self.__carrera = carrera     # Modifica el valor de la variable privada __carrera y la vuelve publica como carrera
    def getCarrera(self):     # Función que regresa el valor de la variable privada __carrera
        return self.__carrera     # Regresa el valor de la variable privada __carrera
oscar = Alumno() #crea un objeto de la clase alumno
oscar.setNombre("Oscar")  #crea un objeto de la clase alumno con nombre "oscar"
oscar.setMatricula("17222111012")  #crea un objeto de la clase alumno con nummero de matricula
oscar.setCarrera("Tecnologias")    # crea objeto con la clase alumno llamado la variable setCarrera
print("Nombre: ",oscar.getNombre(),"\n"       # se immprime getNombre
      "Matricula: ",oscar.getMatricula(),"\n"  # se imprime getMatricula
      "Carrera: ",oscar.getCarrera())  # se imprime getCarrera

class Profesor(Persona):   #crea la clase profesor que hereda de la clase persona
    __no_nomina = None     # variable privada __no_nomina
    def __init__(self):   # constructor de la clase Profesor
        super().__init__()  # Llama al cosntrcutor de la clase Persona
        print("Profesor")    # imprime le texto Profesor
    def setNoNomina(self,no_nomina):  # funcion para modificar el valor de la variable __no_nomina
        self.__no_nomina = no_nomina   # Modifica el valor de la variable privada __no_nomina y la vuelve publica como no_nomina
    def getNoNomina(self):           # Función que regresa el valor de la variable privada __no_nomina
        return self.__no_nomina   # Regresa el valor de la variable privada __no_nomina
objeto_profesor = Profesor()   # crea un objeto de la clase profesor

class Cordinador(Persona):   #crea la clase Cordinador que hereda de la clase Persona
    __no_nomina = None  # variable privada __no_nomina
    def __init__(self):    # constructor de la clase Cordinador
        super().__init__()   # Llama al cosntrcutor de la clase Persona
        print("Cordinador")    # imprime le texto Cordinador
    def setNoNomina(self,no_nomina):   # funcion para modificar el valor de la variable __no_nomina
        self.__no_nomina = no_nomina  # Modifica el valor de la variable privada __no_nomina y la vuelve publica como no_nomina
    def getNoNomina(self):              # Función que regresa el valor de la variable privada __no_nomina
        return self.__no_nomina      # Regresa el valor de la variable privada __no_nomina
        
no_nomina = (int(input("ingrese nomina: ")))  # se crea la variable no_nomina para que
objeto_cordinador = Cordinador()   # se crea el objeto cordinador
objeto_cordinador.setNombre("oscar")  # se llena la funcion setNombre 
objeto_cordinador.setEdad("22")  # se llena la funcion heredada setEdad
objeto_cordinador.setCorreo("oscar@gmail.com")  # se llena la funcion heredada setCorreo
objeto_cordinador.setNoNomina(no_nomina)  # se llama la  variable no_nomina para despues imprimirlo
print("Nombre: ",objeto_cordinador.getNombre(),"\n"  # se imprime GetNombre
      "Edad: ",objeto_cordinador.getEdad(),"\n"   # se imprime GetEdad
      "Correo: ",objeto_cordinador.getCorreo(),"\n"   # se imprime getCorreo
      "No de nomina: ",objeto_cordinador.getNoNomina())  # se imrpime getNoNomina
