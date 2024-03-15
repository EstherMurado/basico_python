'''Calculadora con 4 metodos y parametros con decimales
Queremos usar type() para ver como Python decide los tipos en base a los valores de inicialización que le damos'''

class Calculadora2:

    def suma(v1, v2):
        return v1 + v2
    def resta(v1, v2):
        return v1 - v2
    def multiplica(v1, v2):
        return v1 * v2
    def divide(v1, v2):
        return v1 / v2

    v1 = float(input("Ingresa primer valor: ", ))
    op = input("Introduzca operador (+, -, /, *): ")
    v2 = float(input("Ingresa segundo valor: ", ))

    if (op == '+' or op == '-' or op == '/' or op == '*'):
        if (op == '+'):
            print(suma(v1, v2))
        if (op == '-'):
            print(resta(v1, v2))
        if (op == '*'):
            print(multiplica(v1, v2))
        if (op == '/'):
            print(divide(v1, v2))
    else:
        print("operador no válido ( ´･･)ﾉ(._.`)")
#print(Calculadora2.suma)