#Crear el numero secreto a adivinar
import random
NumeroSecreto = random.randint(1,20)
print("Estoy pensando en un numero entre 1 y 20")

#Pedir al jugador adivinar 6 veces
for CuentaAdivinar in range(1,7):
	print("Adivina cual es.")
	Adivinar = int(input())

	if Adivinar < NumeroSecreto:
		print("Tu numero es demasiado bajo.")
	elif Adivinar > NumeroSecreto:
		print("Tu numero es demasiado alto.")
	else:
		break #Este break es debido a que se adivino el numero 

if Adivinar == NumeroSecreto:
	print("Excelente! Adivinaste el numero en " + str(CuentaAdivinar) + " Intentos!")
else:
	print("Perdiste. el numero que estaba pensando era " + str(NumeroSecreto))
