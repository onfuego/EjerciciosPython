from listas_uno import * 
from velocidad import promedio

list_b = []
list_c = []
list_e = []

for index, elemento in enumerate(lista_autos):
    if (index - 1) % 5 == 0:
        list_b.append(elemento)
    if (index - 2) % 5 == 0:
        list_c.append(elemento)
    if (index - 4) % 5 == 0:
        list_e.append(elemento)

for index, elemento in enumerate(lista_autos):
    if (index - 1) % 5 == 0:
        if elemento > promedio(list_b):
            print(lista_autos[index-1])