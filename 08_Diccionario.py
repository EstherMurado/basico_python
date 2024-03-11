'''Diccionario == hashMap'''
#Dictionaries in python

class Diccionario:
    def UnirDicts(self, d1, d2):
        d1.update(d2)
        return d1

    def creaDict(self):
        k = str(input("Introduzca clave (0 para salir): "))
        v = 0
        resu = {k: v}

        while (k != '0'):
            k = str(input("Introduzca clave: "))
            v += 1
            a2 = {k : v}
            resu.update(a2)
            print(resu)
        return resu

'''
d1 = {'Alex' : 1,
      'Elena' : 2,
      'Markos' : 3,
      'Andrea' : 4}

d2 = {'Paula' : 5,
      'Cris' : 6,
      'Emma' : 7}
'''

#d1.update(d2)
#print(d1)

miDiccionario = Diccionario()
d1 = miDiccionario.creaDict()
d2 = miDiccionario.creaDict()
print(miDiccionario.UnirDicts(d1, d2))


