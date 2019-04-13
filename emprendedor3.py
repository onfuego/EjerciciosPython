#Se importan las librerias necesarias
import sys

#Usuario ingresa precio de venta
precio_venta = float(sys.argv[1])
#Usuario ingresa cantidad de usuarios
usuarios = int(sys.argv[2])
#Usuario ingresa monto de gastos
gastos = float(sys.argv[3])
#Usuario ingresa uilidades del periodo anterior
utilidades_anterior = 0

#Si no se ingresa utilidades del periodo anterior, se considera el valor 1000 como tal
if (len(sys.argv)) == 4:
    utilidades_anterior = 1000
else:
    utilidades_anterior = float(sys.argv[4])
#Se calcula la utilidad del periodo actual
utilidades = precio_venta * usuarios - gastos
#Se compoara la utilidad del periodo actual con la del periodo anterior
razon_utilidades = int((utilidades/utilidades_anterior)*100)
#Se imprime la informaci'on solicitada 
print("Las utilidades del periodo actual son de {}".format(utilidades))
print("las utilidades del periodo anterior son de {}".format(utilidades_anterior))
print("La razon entre las utilidades del periodo actual y del anterior es de un {}%".format(razon_utilidades))
