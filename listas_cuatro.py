from listas_uno import *
from velocidad import promedio


for index, elemento in enumerate(lista_autos):
    if (index - 3) % 5 == 0:
        if elemento == True:
            print(lista_autos[index-3])