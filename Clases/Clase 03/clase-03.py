# CONDICIONALES Y COMPARACIONES

verdadero = True
falso = False
miEdad = 17

if (miEdad >= 18): # Si es mayor de edad, decirlo.
  print("Es mayor de edad")
else: # Si no es mayor de edad, decir que es menor de edad.
  print("Es menor de edad")

# FOR, WHILE (CICLOS)

print("a")
print("b")
print("c")
print("d")
print("e")

'''
Tengo una variable "índice" que va desde 0 hasta 2
(porque el 3 no se cuenta)
'''
for indice in range(0, 5):
  print("Hola!!")
  #print(indice)

# Para un indice en el rango desde 0 hasta 4 (sin contar el 5)
for indice in range(0, 5):
  nuevoIndice = indice + 1
  print("Profe Luchín " + str(nuevoIndice))

listaDeEdades = [34, 45, 67, 12, 45, 32, 18, 3]

for elemento in listaDeEdades:
  print(elemento)

for elemento in listaDeEdades:
  if (elemento >= 18):
    print("La edad " + str(elemento) + " es mayor de edad.")
  else:
    print("La edad " + str(elemento) + " es menor de edad.")

# NOTA: TIP PARA IMPRIMIR VARIABLES DIRECTAMENTE
elemento = 4+5+4
print(f"El elemento {elemento} es un elemento elementoso")

# Mientras se cumpla la condición, entonces se ejecuta.
# Si no, se pasa a la siguiente línea.
while (True):
  print("Hello Forever")

# Mientras haya cuarentena, entonces sigue quedándote en la casa.
# Si no, eres libre y puedes decírselo a todos. :)
diasRestantesDeCuarentena = 365 # días
cuarentena = True

while (cuarentena):
  diasRestantesDeCuarentena -= 1
  if (diasRestantesDeCuarentena < 1):
    cuarentena = False
  print("#QuedateEnCasa")

print("Libre soy, libre soy!!!")