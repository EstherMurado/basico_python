#print(__name__)

#Calculadora con 4 metodos y parametros con enteros
#Queremos usar type() para ver como Python decide los tipos en base a los valores de inicialización que le damos
class calculadora():
    v1 = int(input("Ingresa primer valor: ", ))
    op= input("Introduzca operador (+, -, /, *): ")
    v2 = int(input("Ingresa segundo valor: ", ))

    def suma(v1, v2):
        print(v1 + v2)
    def resta(v1, v2):
        print(v1 - v2)
    def multiplica(v1, v2):
        print(v1 * v2)
    def divide(v1, v2):
        print(v1 / v2)

    if(op == '+' or op == '-' or op == '/' or op == '*'):
        if (op == '+'):
            suma(v1, v2)
        if(op == '-'):
            resta(v1, v2)
        if (op == '*'):
            multiplica(v1, v2)
        if (op == '/'):
            divide(v1, v2)
    else:
        print("operador no válido ( ´･･)ﾉ(._.`)")


'''Calculadora con 4 metodos y parametros con decimales
Queremos usar type() para ver como Python decide los tipos en base a los valores de inicialización que le damos
Escritura en fichero
¿Cómo haría para escribir en fichero en el disco duro?
Crear un array con números y sumar sus valores
Hay que usar azúcar sintáctico para el bucle
Crear dos diccionarios y unirlos
Definir una clase estudiante, crear varios estudiantes y meterlos en una lista'''
# str (string) en Python es inmutable ¿cómo puedo comprobar esto en un pequeño programa?
