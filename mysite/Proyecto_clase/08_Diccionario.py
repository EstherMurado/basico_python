<<<<<<< HEAD
'''Diccionario == hashMap'''
#Dictionaries in python

class Diccionario:
    def UnirDicts(self, d1, d2):
        d1.update(d2)
        return d1

    def creaDict(self):
        k = str(input("Introduzca clave (0 para salir): "))
        v = 0
        resu = {k : v}
        if k != 0:
            while (k != '0'):
                v += 1
                a2 = {k : v}
                resu.update(a2)
                k = str(input("Introduzca clave: "))
        return resu

#d1.update(d2)
#print(d1)

miDiccionario = Diccionario()
d1 = miDiccionario.creaDict()
d2 = miDiccionario.creaDict()
print(miDiccionario.UnirDicts(d1, d2))


=======
'''Diccionario == hashMap'''
#Dictionaries in python

class Diccionario:
    def UnirDicts(self, d1, d2):
        d1.update(d2)
        return d1

    def creaDict(self):
        k = str(input("Introduzca clave (0 para salir): "))
        v = 0
        resu = {k : v}
        if k != 0:
            while (k != '0'):
                v += 1
                a2 = {k : v}
                resu.update(a2)
                k = str(input("Introduzca clave: "))
        return resu

#d1.update(d2)
#print(d1)

miDiccionario = Diccionario()
d1 = miDiccionario.creaDict()
d2 = miDiccionario.creaDict()
print(miDiccionario.UnirDicts(d1, d2))


>>>>>>> 92f6d5b97768722f679453a860203fe068b937fb
