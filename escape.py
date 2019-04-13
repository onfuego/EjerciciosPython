
#Se importan las librerias necesarias
import sys
from math import sqrt
#Usuario debe ingresar el valor de la gravedad como primer parametro
g = float(sys.argv[1])
#Usuario debe ingresar el valor del radio como segundo parametro
r = float(sys.argv[2])
#Se calcula la velocidad con los datos obtenidos
velocidad = sqrt(2*g*r)
#Se imprime la velocidad calculada
print("La velocidad es {}".format(velocidad))
