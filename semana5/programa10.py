"""
   Programa10
   Nombre:Anhuar Fernando MI                                              
   Fecha: 13/02/2023                                                      
   Descripcion: clases alumno y persona
"""
class Persona:
    __nombre = None
    __correo = None
    __edad = None
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

    def setEdad (self,edad):
        self.__edad = edad
    def getEdad(self):
        return self.__edad
        
dejah = Persona()
dejah.setNombre("Dejah") 
print(dejah.getNombre())
dejah.setCorreo("145134@gmail.com")
print(dejah.getCorreo())

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
      "Matricula: ",oscar.getMatricula(),"\n"
      "Carrera: ",oscar.getCarrera())

class Profesor(Persona):
    __no_nomina = None
    def __init__(self):
        #super().__init__()
        print("Profesor")
    def setNoNomina(self,no_nomina):
        self.__no_nomina = no_nomina
    def getNoNomina(self):
        return self.__no_nomina
objeto_profesor = Profesor()

class Cordinador(Persona):
    __no_nomina = None
    def __init__(self):
        #super().__init__()
        print("Cordinador")
    def setNoNomina(self,no_nomina):
        self.__no_nomina = no_nomina
    def getNoNomina(self):
        return self.__no_nomina
no_nomina = (int(input("ingrese nomina: ")))
objeto_cordinador = Cordinador()
objeto_cordinador.setNombre("oscar")
objeto_cordinador.setEdad("22")
objeto_cordinador.setCorreo("oscar@gmail.com")
objeto_cordinador.setNoNomina(no_nomina)
print("Nombre: ",objeto_cordinador.getNombre(),"\n"
      "Edad: ",objeto_cordinador.getEdad(),"\n"
      "Correo: ",objeto_cordinador.getCorreo(),"\n"
      "No de nomina: ",objeto_cordinador.getNoNomina())