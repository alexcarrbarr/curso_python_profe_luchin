# Booleanos

'''
falso = False
verdadero = True

#print(falso)
#print(verdadero)
#print(not verdadero)
#print(not falso)

verdaderoYverdadero = True and True
#print(verdaderoYverdadero)
falsoYFalso = False and False
#print(falsoYFalso)
falsoYverdadero = False and True
#print(falsoYverdadero)
verdaderoYfalso = True and False
#print(verdaderoYfalso)
verdaderoOverdadero = True or True
#print(verdaderoOverdadero)
falsoOfalso = False or False
#print(falsoOfalso)
verdaderoOfalso = True or False
#print(verdaderoOfalso)
falsoOverdadero = False or True
#print(falsoOverdadero)
'''

###################################

# Condicionales

'''
print("Decide por qué camino ir:")
print("0: Si quieres ir a la izquierda")
print("1: Si quieres ir a la derecha")
eleccion = int(input())
if (eleccion == 0):
  print("Haz elegido ir a la izquierda")
else:
  print("Haz elegido ir a la derecha")
'''

'''
print("Decide por qué camino ir:")
print("i: Si quieres ir a la izquierda")
print("d: Si quieres ir a la derecha")
eleccion = str(input())
if (eleccion == "i"):
  print("Haz elegido ir a la izquierda")
elif (eleccion == "d"):
  print("Haz elegido ir a la derecha")
else:
  print("Ingrese solamente i o d")
'''

###################################

# Listas

lista = ["primer elemento", "segundo elemento", 3, 4, 5, 6, True, False]
#print(lista)
largoDeLaLista = len(lista)
#print(largoDeLaLista)
primerElemento = lista[0]
#print(primerElemento)
segundoElemento = lista[1]
#print(segundoElemento)
#print(lista[7])
#print(lista[100]) #error: index out of range
#print(lista[-1])

# Sublistas

dosPrimerosElementos = lista[0:2]
#print(dosPrimerosElementos)
sublista = lista[1:3]
print(sublista)