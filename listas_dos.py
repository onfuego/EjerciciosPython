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
print("El promedio de la lista b es {}".format(promedio(list_b)))
print("El promedio de la lista c es {}".format(promedio(list_c)))
print("El promedio de la lista e es {}".format(promedio(list_e)))
