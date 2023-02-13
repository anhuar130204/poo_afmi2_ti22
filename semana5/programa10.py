"""
class Personas:
    __nombre = None
    __correo = None
    def __init__(self):
        print("Persona")

    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre

    def setCorreo(self,correo):
        self.__correo  = correo
    def getCorreo(self):
        return self.__correo

dejah = Personas()
dejah.setNombre("Dejah") 
print(dejah.getNombre())
dejah.setCorreo("145134@gmail.com")
print(dejah.getCorreo())
"""
class Alumno: 
    __nombre = None
    __matricula = None
    __carrera = None
    def __init__(self):
        print("Alumno")
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setMatricula(self,matricula):
        self.__matricula = matricula
    def getMatricula(self):
        return self.__matricula
    def setCarrera(self,carrera):
        self.__carrera = carrera
    def getCarrera(self):
        return self.__carrera
oscar = Alumno()
oscar.setNombre("Oscar")
oscar.setMatricula("17222111012")
oscar.setCarrera("Tecnologias")
print("Nombre: ",oscar.getNombre(),"\n"
      "Carrera: ",oscar.getMatricula(),"\n"
      "Carrera: ",oscar.getCarrera())