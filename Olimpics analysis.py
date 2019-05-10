import pandas as pd
import numpy as np

df = pd.read_csv("athlete_events.csv")

#Cantidad de filas y columnas del DataFrame
ejercicio_1 = df.shape

#Numero de competencias realizadas a lo largo del tiempo
ejercicio_2 = df['Event'].nunique()

#Porcentaje de atletas que participaron tanto en los juegos de verano como de invierno
ejercicio_3 = df['Season'].value_counts() / df['Season'].value_counts().sum()

#Lugar de celebracion de primeros juegos olimpicos de Verano
ejercicio_4 = df[df['Season'] == 'Summer'][df[df['Season'] == 'Summer']['Year'] == df[df['Season'] == 'Summer']['Year'].min()]['City'].unique()[0]

#Lugar de celebracion de primeros juegos olimpicos de Invierno
ejercicio_5 = df[df['Season'] == 'Winter'][df[df['Season'] == 'Winter']['Year'] == df[df['Season'] == 'Winter']['Year'].min()]['City'].unique()[0]

#10 primeros paises con mayor cantidad de atletas participantes a lo largo de los juegos
ejercicio_6 = df['Team'].value_counts().head(10)

#Porcentaje de medallas asignadas(Oro, Bronce y Plata)
ejercicio_7 = df['Medal'].value_counts() / df['Medal'].value_counts().sum()

#Paises participantes en las primeras olimpiadas de verano 
ejercicio_8 = df[df['Season'] == 'Summer'][df[df['Season'] == 'Summer']['Year'] == df[df['Season'] == 'Summer']['Year'].min()]['Team'].unique().tolist()

