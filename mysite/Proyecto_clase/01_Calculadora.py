#print(__name__)

#Calculadora con 4 metodos y parametros con enteros
#Queremos usar type() para ver como Python decide los tipos en base a los valores de inicialización que le damos

class Calculadora():

    def suma(v1, v2):
        return v1 + v2
    def resta(v1, v2):
        return v1 - v2
    def multiplica(v1, v2):
        return v1 * v2
    def divide(v1, v2):
        return v1 / v2

    # print(Calculadora.suma())

    v1 = int(input("Ingresa primer valor: ", ))
    op = input("Introduzca operador (+, -, /, *): ")
    v2 = int(input("Ingresa segundo valor: ", ))

    print("el tipo de v1 es", type(v1))
    if (type(v1)==int):
        print ("es igual")

    if(op == '+' or op == '-' or op == '/' or op == '*'):
        if (op == '+'):
           print(suma(v1, v2))
        if(op == '-'):
            print(resta(v1, v2))
        if (op == '*'):
            print(multiplica(v1, v2))
        if (op == '/'):
            print(divide(v1, v2))
    else:
        print("operador no válido ( ´･･)ﾉ(._.`)")

'''
Crear dos diccionarios y unirlos
Definir una clase estudiante, crear varios estudiantes y meterlos en una lista'''
# str (string) en Python es inmutable ¿cómo puedo comprobar esto en un pequeño programa?
