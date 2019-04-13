#Se importan las librerias necesarias
import random
import sys
#Se recibe la jugada del usuario
jugada = sys.argv[1]
#Se transforma la jugada en un valor numerico para compararla mas adelante
#Piedra:1, Papel:2, Tijera:3, si se recibe otro valor diferente,
#se va a enviar un mensaje de error
if jugada == "Piedra":
	jugada = 1
elif jugada == "Papel":
	jugada = 2
elif jugada == "Tijera":
	jugada = 3
else:
	print("Argumento invalido: Debe ser Piedra, Papel o Tijera")
#Se genera jugada aleatoria de la computadora
computadora = random.randint(1,3)
#Si la jugada del usuario y la de la computadora son iguales se muestra empate
#En caso de que las jugadas sean diferentes, se genera la comparativa
if computadora == jugada:
	if jugada == 1:
		jugada = "Piedra"
	elif jugada == 2:
		jugada = "Papel"
	else:
		jugada = "Tijera"
	print("Computadora juega {}".format(jugada))
	print("Empate")
elif jugada == 1:
	if computadora == 2:
		print("Computadora juega Papel")
		print("Perdiste")
	else:
		print("Computadora juega Tijera")
		print("Ganaste")
elif jugada == 2:
	if computadora == 3:
		print("Computadora juega Tijera")
		print("Perdiste")
	else:
		print("Computadora juega Piedra")
		print("Ganaste")
elif jugada == 3:
	if computadora == 1:
		print("Computadora juega Piedra")
		print("Perdiste")
	else:
		print("Computadora juega Papel")
		print("Ganaste")
