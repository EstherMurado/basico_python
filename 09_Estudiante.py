class Estudiante():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class CreaEstudiante():

    num_people = 0

    def nuevoEstudiante(self):
        nom = str(input("Nombre: "))
        ape = str(input("Apellido: "))
        edad = int(input("Edad: "))
        e = Estudiante(nom, ape, edad)
        CreaEstudiante.num_people += 1
        return e

    def listaAlumnos(self):
        q = str(input("'a' --> agregar | 'c' --> cantidad de alumnos | 'v' to view | 'e' to exit: "))
        lista = []
        while (q == 'a' or q == 'c' or q == 'v'):
            if q == 'a':
                lista.append(self.nuevoEstudiante())
            if q == 'c':
                print(CreaEstudiante().num_people)
            if q == 'v':
                self.imprimeLista(lista)
            q = str(input("Introduzca comando ('a' | 'c' | 'v'): "))
        return lista

    def imprimeLista(self, lista):
        i = 1
        for alumno in lista:
            print(i,"|", alumno.nombre, alumno.apellido,"-", alumno.edad)
            i += 1


crear = CreaEstudiante()
alumnos = crear.listaAlumnos()
crear.imprimeLista(alumnos)
