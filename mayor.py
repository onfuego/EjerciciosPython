#Se importan las librerias necesarias
import sys
#Se reciben como argumento los tres numeros que se van a comparar
numero1 = int(sys.argv[1])
numero2 = int(sys.argv[2])
numero3 = int(sys.argv[3])
#se compara el primer numero con los otros dos, si es mayor a estos, se imprime el primero
if numero1 > numero2 and numero1 > numero3 :
	print(numero1)
#Si no, si el segundo numero es mayor al tercero, se imprime el segundo
elif numero2 > numero3:
	print(numero2)
#Y si no aplica ninguno de los casos anteriores, se asume que el tercer numero es mayor a los demas
else:
	print(numero3)
