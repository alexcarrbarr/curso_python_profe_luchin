# IMPORTAR LIBRERÍAS.

import time

'''
PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
'''

# El objeto Persona definida como Función. NO RECOMENDADO.
def persona():
  nombre = "Pedrito"
  edad = 25
  quepuedehacer = ["caminar", "comer", "tomar la micro"]

# El objeto Persona definida como Clase. POO.
class Persona:
  nombre = ""
  apellido = ""
  edad = 0
  peso = 50
  quepuedehacer = ["caminar", "comer"]

  def __init__(self, nombreDado, apellidoDado, edadDada):
    self.nombre = nombreDado
    self.apellido = apellidoDado
    self.edad = edadDada

  def actualizarPeso(self, pesoActual):
    self.peso = pesoActual
  
  def diNO(self):
    print("NO!!!")

# Clase Auto.
class Auto:
  marca = ""
  puertas = 4
  ruedas = 10
  kilometraje = 0
  tamanioMaletero = 20

  def __init__(self, marca, tamanioMaletero):
    self.marca = marca
    self.tamanioMaletero = tamanioMaletero

  def avanzar(self, km):
    self.kilometraje += km

auto = Auto("MySan", 40)
while(True):
  print(auto.kilometraje)
  time.sleep(10)
  auto.avanzar(1)

# ==============================================================

# HERENCIA

# Clase Adulto.
class Adulto(Persona):
  deberes = []
  dinero = 0
  alcoholSangre = 0

  def __init__(self, dinero):
    self.dinero = dinero

  def pagarCuentas(self, dineroPagado):
    self.dinero -= dineroPagado

  def beber(self, cantidadAlcohol):
    self.alcoholSangre += cantidadAlcohol
