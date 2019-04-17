#Se importan las librerias necesarias
import sys

#Usuario ingresa precio de venta
precio_venta = float(sys.argv[1])
#Usuario ingresa cantidad de usuarios
usuarios = int(sys.argv[2])
#Usuario ingresa monto de gastos
gastos = float(sys.argv[3])
#Se inicia la variable utilidades_anterior como un string vacio
utilidades_anterior = " "

#Si no se ingresa utilidades del periodo anterior, se considera el valor 1000 como tal, si se ingresa, se toma dicho valor
if (len(sys.argv)) == 4:
    utilidades_anterior = 1000
else:
    utilidades_anterior = float(sys.argv[4])
#Se calcula la utilidad del periodo actual
utilidades = precio_venta * usuarios - gastos
#Se compsara la utilidad del periodo actual con la del periodo anterior
razon_utilidades = int((utilidades/utilidades_anterior)*100)
#Se imprime la informacion solicitada
print(razon_utilidades)
print("La razon entre las utilidades del periodo actual y del anterior es de un {}%".format(razon_utilidades))
