# Tarea 02 - Curso Python - Profe Luchín.

# Pedir datos de entrada al usuario.
print("Ingrese su peso (en kgs.): ", end="")
peso = int(input())
print("Ingrese su altura (en cms.): ", end="")
altura = int(input())

# Convertir altura en metros.
altura_mts = altura / 100

# Calcular IMC.
imc = peso / (altura_mts * altura_mts)

# Mostrar estado de peso al usuario según el IMC calculado.
if (imc < 18.5):
  print("Usted tiene bajo peso.")
elif (imc >= 18.5 and imc < 25):
  print("Usted tiene un peso normal.")
elif (imc >= 25 and imc < 30):
  print("Usted tiene sobrepeso.")
else:
  print("Usted está obeso.")