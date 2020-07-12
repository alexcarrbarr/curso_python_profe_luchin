# IMPORTAR LIBRERÍAS
from datetime import date

# ===============================================================

# FUNCIONES

'''
def: Definiendo una función.
sumar1: Nombre de la función.
numero: Argumento (o input) de la función.
return: Devuelve el resultado.
'''
def sumar1(numero):
  resultado = numero + 1
  return resultado


def sumar2(numero):
  return numero + 2

def sumar100000(numero):
  return numero + 100000

# Código de la función sin estar dentro de una función.
print("Dame un número para sumarle 1")
x = int(input())
nuevoNumero = x + 1
print("Tu nuevo número es " + str(nuevoNumero))
#print(f"Tu nuevo número es {nuevoNumero}")

for init in range(5):
  res = sumar1(init)
  print(str(res))

init = 0
while(True):
  res = sumar1(init)
  #res = sumar2(init)
  init = res
  print(str(res))

# HACKING BANK ACCOUNT
init = 0
while(True):
  res = sumar100000(init)
  init = res
  print("Saldo en tu cuenta: " + str(res))

# Valida si es mayor o menor de edad.
def validarEdad(edad):
  if (edad >= 18):
    print("Es mayor de edad.")
  else:
    print("Es menor de edad.")

# Calcula la edad actual a partir del año de nacimiento.
def calculaTuEdad(anioNacimiento):
  hoy = date.today()
  anio = hoy.year
  edad = anio - anioNacimiento
  return edad

# Programa para ingresar un año de nacimiento
# y validar si es mayor o menor de edad.
print("Dame tu año de nacimiento:")
anio = int(input())
edad = calculaTuEdad(anio)
print(f"Tu edad es {edad}")
validarEdad(edad)

# Calcula la edad actual a partir de la fecha de nacimiento.
def calculaTuEdad(dia, mes, anio):
  hoy = date.today()
  fechaNacimiento = date(anio, mes, dia)
  diaHoy = hoy.day
  mesHoy = hoy.month
  anioHoy = hoy.year
  diaFechaNacim = fechaNacimiento.day
  mesFechaNacim = fechaNacimiento.month
  anioFechaNacim = fechaNacimiento.year
  edad = anioHoy - anioFechaNacim - ((mesFechaNacim, diaFechaNacim) < (mesHoy, diaHoy))
  return edad

# Programa para ingresar una fecha de nacimiento
# y validar si es mayor o menor de edad.
print("Dame tu dia de nacimiento:")
dia = int(input())
print("Dame tu mes de nacimiento:")
mes = int(input())
print("Dame tu año de nacimiento:")
anio = int(input())
edad = calculaTuEdad(dia, mes, anio)
print(f"Tu edad es {edad}")
validarEdad(edad)

# ===============================================================

# RECURSIVIDAD

# Cálculo del Factorial, usando iteración.
n = int(input("Ingrese un número: "))

factorial = 1
if (n >= 1):
  for i in range(1, n+1):
    factorial = factorial * i

print(f"El factorial de " + str(n) + " es " + str(factorial))

# Cálculo del Factorial, usando recursión.
def recursion(n):
  if (n == 1):
    return n
  else:
    return n * recursion(n-1)

n = int(input("Ingrese un número: "))
print(recursion(n))
