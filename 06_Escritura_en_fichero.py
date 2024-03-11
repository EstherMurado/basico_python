<<<<<<< HEAD
'''El archivo se crea directamente en el disco. Si no especificamos la ruta, se creará donde nuestros
proyectos'''
class Apuntes:
   def tomarApuntes(self):
      apunte = str(input("Escribe aquí tu texto: \n" ))
      self.escribirEnFichero(apunte)

   def escribirEnFichero(self, apuntes):
      with open('ApuntesPython.txt', 'a') as archivo:
         # 'w' == write 'a' agregar
         archivo.write(apuntes + '\n')


   def inicio(self):
      print("Hola! （づ￣3￣）づ╭❤～")
      print("Bienvenidx a tus apuntes!")

      self.tomarApuntes()

      more = str(input("Quieres tomar más notas? (s / n): "))
      while more == "s" or more == "S":
         self.tomarApuntes()
         more = str(input("Quieres tomar más notas? (s / n): "))


misApuntes = Apuntes()
=======
'''El archivo se crea directamente en el disco. Si no especificamos la ruta, se creará donde nuestros
proyectos'''
class Apuntes:
   def tomarApuntes(self):
      apunte = str(input("Escribe aquí tu texto: \n" ))
      self.escribirEnFichero(apunte)

   def escribirEnFichero(self, apuntes):
      with open('ApuntesPython.txt', 'a') as archivo:
         # 'w' == write 'a' agregar
         archivo.write(apuntes + '\n')


   def inicio(self):
      print("Hola! （づ￣3￣）づ╭❤～")
      print("Bienvenidx a tus apuntes!")

      self.tomarApuntes()

      more = str(input("Quieres tomar más notas? (s / n): "))
      while more == "s" or more == "S":
         self.tomarApuntes()
         more = str(input("Quieres tomar más notas? (s / n): "))


misApuntes = Apuntes()
>>>>>>> 92f6d5b97768722f679453a860203fe068b937fb
misApuntes.inicio()