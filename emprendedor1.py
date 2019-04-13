

#Se importan las librerias correspondientes
import sys

#Usuario debe ingresar precio de venta como primer argumento
precio_venta = float(sys.argv[1])
#Usuario debe ingresar la cantidad de usuarios
usuarios = int(sys.argv[2])
#Usuario debe ingresar los gastos como tercer argumento
gastos = float(sys.argv[3])

#Se calculan las utilidades
utilidades = precio_venta * usuarios - gastos

#se aplica impuesto si utilidades son positivas
if utilidades > 0:
	utilidades *= 0.65

#Se imprimen utilidades
print("Las utilidades son de {}".format(utilidades))
