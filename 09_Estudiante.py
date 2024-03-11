class Estudiante():

    nombre = ""
    apellido = ""
    edad = 0

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

def nuevoEstudiante():
    nom = str(input("Nombre: "))
    ape = str(input("Apellido: "))
    edad = int(input("Edad: "))
    e = Estudiante(nom, ape, edad)
    return e

def listaAlumnos():
    q = str(input("'a' para agregar: "))
    lista = []
    while (q == 'a'):
        lista.append(nuevoEstudiante())
        q = str(input("'a' para agregar: "))
    return lista

def imprimeLista(lista):
    for alumno in lista:
        print(alumno.nombre, alumno.apellido, "- ", alumno.edad)

imprimeLista(listaAlumnos())