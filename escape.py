import sys
from math import sqrt


g = float(sys.argv[1])
r = float(sys.argv[2])

velocidad = sqrt(2*g*r)

print("La velocidad es {}".format(velocidad))