

#Se importan las librerias correspondientes
import sys 

#Usuario debe ingresar precio de venta como primer argumento
precio_venta = float(sys.argv[1])
#Usuario debe ingresar el número de usuarios como segundo argumento
usuarios = int(sys.argv[2])
#Usuario debe ingresar los gastos como tercer argumento
gastos = float(sys.argv[3])

#Se crea la funcion que calculará las utilidades según los argumentos ingresados
def calcular_utilidades(precio_venta, numero_usuarios, gastos):
	utilidades = precio_venta * usuarios - gastos
	if utilidades > 0:
		utilidades *= 0.75
	return utilidades 

#Se imprime el valor de las utilidades
print(calcular_utilidades(precio_venta, usuarios, gastos))