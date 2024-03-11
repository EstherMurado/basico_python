'''Crear un array con números y sumar sus valores
Hay que usar azúcar sintáctico para el bucle'''

class Array:
    def creaArray(self):
        a = int(input("Introduzca dígitos (-1 para salir): "))
        a2 = []
        while (a != -1):
            a2.append(a)
            a = int(input("Dígito: "))
            print(a2)
        return a2

    def sumaArray(a):
        suma = 0;
        for elem in a:
            suma += elem
        return suma

    print(sumaArray(creaArray()))
