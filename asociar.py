from velocidad import promedio

velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
11, 11, 12, 12, 12, 12, 13, 13,
13, 13, 14, 14, 14, 14, 15, 15,
15, 16, 16, 17, 17, 17, 18, 18,
18, 18, 19, 19, 19, 20, 20, 20,
20, 20, 22, 23, 24, 24, 24, 24, 25]

distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
17, 28, 14, 20, 24, 28, 26, 34, 34,
46, 26, 36, 60, 80, 20, 26, 54, 32,
40, 32, 40, 50, 42, 56, 76, 84, 36,
46, 68, 32, 48, 52, 56, 64, 66, 54,
70, 92, 93, 120, 85]

#Se crea lista con funcion zip 
lista_final = list(zip(velocidad,distancia))

#Se calcula velocidad promedio
suma = 0 
contador = 0 
for element in lista_final:
    suma += element[0]
    contador += 1 
promedio_velocidad = suma/contador


#Se calcula distancia promedio
suma = 0 
contador = 0
for element in lista_final:
    suma += element[1]
    contador +=1 
promedio_distancia = suma/contador

    
  #Velocidad bajo el promedio
ocurrencias1 = 0
for element in lista_final:
    if element[0] < promedio_velocidad:
        ocurrencias1 +=1
print(ocurrencias1)

  #Velocidad bajo el promedio y distancia sobre el promedio
ocurrencias2 = 0
for element in lista_final:
    if element[0] < promedio_velocidad and element[1] > promedio_distancia:
        ocurrencias2 +=1
print(ocurrencias2)

  #Velocidad sobre el promedio
ocurrencias3 = 0
for element in lista_final:
    if element[0] > promedio_velocidad:
        ocurrencias3 +=1
print(ocurrencias3)

  #Velocidad sobre el promedio y distancia bajo el promedio
ocurrencias4 = 0
for element in lista_final:
    if element[0] > promedio_velocidad and element[1] < promedio_distancia:
        ocurrencias4 +=1
print(ocurrencias4)