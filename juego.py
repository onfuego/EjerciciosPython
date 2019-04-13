import random
import sys

jugada = sys.argv[1]

if jugada == "Piedra":
	jugada = 1
elif jugada == "Papel":
	jugada = 2
elif jugada == "Tijera":
	jugada = 3
else:
	print("Argumento invalido: Debe ser Piedra, Papel o Tijera")

computadora = random.randint(1,3)

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
