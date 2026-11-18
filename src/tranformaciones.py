# Ejercicio 1
from google.colab import files # Esta es la manera de importar archivos csv del computador en Python
uploaded = files.upload() # Abre la ventana para cargar el primer archivo (athlete_events.csv)
from google.colab import files
uploaded = files.upload() # Abre la ventana para cargar el segundo archivo (noc_regions.csv)
import pandas as pd
df_atletas = pd.read_csv('athlete_events.csv') # Lee el archivo csv y lo convierte en un dataframe
df_regiones = pd.read_csv('noc_regions.csv') # Lee el archivo de regiones y lo convierte en dataframe
display(df_atletas) # Muestra el contenido completo del dataframe de atletas
display(df_regiones) # Muestra el contenido completo del dataframe de regiones

# Ejercicio 2

# Ejercicio 3
print('\n')
print('Estadisticas DataSet Atletas')
display(df_atletas.describe(include ='all')) # El .describe() generar un resumen estadistico rapido y completo
print('\n\n')
print('Estadisticas DataSet Regiones')
display(df_regiones.describe(include ='all')) # El include='all' hace que el resumen estadistico incluya todas las variables sin importar el tipo

# Ejercicio 4
df_atletas['IMC'] = round(df_atletas['Weight'] / (df_atletas['Height']/100)**2,2) # Crea la columna IMC calculando peso sobre altura al cuadrado
# El round y el ,2 del final define la cantidad de numeros despues de la coma
display(df_atletas)
display(df_atletas.groupby(["Sex","Sport"])["IMC"].mean())
# Aqui se agrupa por sexo y deporte y se saca el promedio para ambos con base al IMC

# Ejercicio 5
df_merged = pd.merge(df_atletas, df_regiones, on='NOC', how='left') # Combina ambos dataframes utilizando la columna NOC en comun
# Esto indica que tome el dataframe izquierdo (df_atletas) y lo combine con el derecho (df_regiones)
# on='NOC' Es la columna que tienen ambos dataframes en comun. Se buscaran las filas donde el valor de 'NOC' coincida en ambas tablas para unirlas
# how='left' Conservarán absolutamente todos los registros del dataframe de la izquierda (df_atletas)
# Si el codigo de un atleta no existe en df_regiones no se eliminaro al atleta... Simplemente se pondra NaN
display(df_merged)
# Comprobación de la cantidad de filas
print(len(df_merged)) # Imprime la cantidad de filas del dataframe combinado
print(len(df_atletas)) # Imprime la cantidad de filas del dataframe original de atletas
# Cantidad de nulos en la columna de 'region'
print(df_merged['region'].isnull().sum()) # Cuenta cuantos valores nulos o vacios quedaron en la columna region

# Ejercicio 6
def clasificacion_binaria(Medal): # Define una funcion para convertir las medallas en valores binarios (1 o 0)
  if Medal == 'Gold' or Medal == 'Silver' or Medal == 'Bronze':
    return 1
  else:
    return 0
df_atletas['Medalla'] = df_atletas['Medal'].map(clasificacion_binaria) # .map() aplica una funcion a esa columna especifica
display(df_atletas)
total_filas = len(df_atletas)
print(f'Número total de filas: {total_filas}')
atletas_unicos = df_atletas['ID'].nunique() # .nunique() sirve para contar los valores repetidos una unica vez
print(f'Número de atletas únicos (ID): {atletas_unicos}')

# Ejercicio 7
display(df_atletas.groupby('Year')['ID'].count()) # Cuenta la cantidad de registros agrupados por año de los juegos
display(df_atletas.groupby('Season')['ID'].count()) # Cuenta la cantidad de registros agrupados por temporada (Verano/Invierno)
display(df_atletas.groupby('Sex')['ID'].count()) # Cuenta la cantidad de registros agrupados por sexo del atleta

# Ejercicio 8
display(df_atletas.isnull().sum()) # Muestra la cantidad total de valores nulos por cada columna
df_antes_1960 = df_atletas[df_atletas['Year'] < 1960] # Filtra los registros de los juegos ocurridos antes de 1960
df_despues_1960 = df_atletas[df_atletas['Year'] >= 1960] # Filtra los registros de los juegos ocurridos desde 1960 en adelante
print('Faltantes antes de 1960 en porcentaje (%)')
display(df_antes_1960.isnull().mean() * 100) # Calcula y muestra el porcentaje de valores faltantes antes de 1960
print('\n--------------------------\n')
print('Faltantes despues de 1960 en porcentaje (%)')
display(df_despues_1960.isnull().mean() * 100) # Calcula y muestra el porcentaje de valores faltantes despues de 1960

# Ejercicio 9
# a) ¿Cuál es la edad promedio de los atletas?
edad_promedio = df_atletas['Age'].mean() # Calcula el promedio de la columna de edad
print(f'Edad promedio de los atletas: {edad_promedio:.2f} años') # Imprime la edad promedio con dos decimales
# b) ¿Cuántos registros terminaron con medalla y cuántos sin medalla?
print('Deportistas sin medalla = 0 y deportistas con medalla (oro, plata o bronce) = 1\n')
print(df_atletas['Medalla'].value_counts()) # Cuenta la frecuencia de cada valor en la columna de medalla binaria
# c) ¿Cuál es la estatura promedio de los atletas que ganaron medalla de oro?
estatura_oro = df_atletas[df_atletas['Medal'] == 'Gold']['Height'].mean() # Filtra a los ganadores de oro y calcula el promedio de su estatura
print(f'Estatura promedio de los deportistas con medalla de oro: {estatura_oro:.2f}') # Imprime el resultado con dos decimales
# d) ¿Cuántas ediciones de los Juegos y cuántos países (NOC) distintos hay en los datos?
ediciones_juegos = len(df_atletas['Games'].value_counts()) # .value_counts() cuenta la frecuencia con la que aparece cada valor unico en una columna
paises_noc = len(df_atletas['NOC'].value_counts()) # Cuenta cuantos codigos NOC unicos existen en el dataset
print(f'Ediciones de los juegos: {ediciones_juegos}') # Imprime la cantidad total de ediciones de juegos
print(f'Paises (NOC) distintos: {paises_noc}') # Imprime la cantidad de paises representados
# e) ¿Cuál es la edad más joven y la más vieja de los atletas?
mas_joven = df_atletas['Age'].min() # Obtiene el valor minimo de la columna edad
mas_viejo = df_atletas['Age'].max() # Obtiene el valor maximo de la columna edad
print(f'La edad mas joven es: {mas_joven:.0f}') # Imprime la edad minima sin decimales
print(f'La edad mas vieja es: {mas_viejo:.0f}') # Imprime la edad maxima sin decimales
# f) ¿Cuántos registros hay en cada temporada (Verano e Invierno)?
cant_registros_temporada = df_atletas['Season'].value_counts() # Cuenta la cantidad de registros por temporada
print(f'Cantidad de registros por temporada (Verano e Invierno) {cant_registros_temporada}') # Imprime la distribucion por temporada
# g) ¿Cuántos atletas únicos participaron en una sola edición de los Juegos y cuántos en más de una?
ediciones_atleta=df_atletas.groupby("ID")["Games"].nunique() # Agrupa por ID y cuenta el numero de ediciones distintas en las que participo cada atleta
una_edicion=(ediciones_atleta==1).sum() # Suma cuantos atletas participaron exactamente en una sola edicion
mas_edicion=(ediciones_atleta>1).sum() # Suma cuantos atletas participaron en mas de una edicion
print(f"La cantidad de atletas que participaron en mas de una edicion es {mas_edicion}")
print(f"La cantidad de atletas que participaron en una edicion es {una_edicion}")

# Ejercicio 10
# (a) ¿Cree usted que ganaron más medallas las mujeres que los hombres? ¿y proporcionalmente?
medallas=df_atletas.groupby("Sex")["Medalla"].sum() # Suma las medallas obtenidas agrupadas por sexo
tasa=df_atletas.groupby("Sex")["Medalla"].mean() # Calcula el promedio de medallas obtenidas por sexo
participacion=df_atletas.groupby("Sex")["Medalla"].size() # Cuenta la cantidad total de participaciones por sexo
print(medallas)
print(participacion)
print(tasa)
# (b) ¿Cree usted que ganaron más medallas los atletas menores de 18 años que los adultos (18 años o más)? ¿y proporcionalmente?
menores_18=df_atletas[df_atletas["Age"]<18] # Filtra a los atletas menores de 18 años
mayores_18=df_atletas[df_atletas["Age"]>=18] # Filtra a los atletas mayores o iguales a 18 años
medallas_men=menores_18["Medalla"].sum() # Suma las medallas de los menores
medallas_may=mayores_18["Medalla"].sum() # Suma las medallas de los mayores
tasa_men=menores_18["Medalla"].mean() # Calcula la tasa de medallas para menores
tasa_may=mayores_18["Medalla"].mean() # Calcula la tasa de medallas para mayores
participacion_men=len(menores_18) # Cuenta el total de menores participantes
participacion_may=len(mayores_18) # Cuenta el total de mayores participantes
print(f"los menores de 18 ganaron {medallas_men} medallas y los mayores de 18 es {medallas_may}")
print(f"la tasa de los menores de 18 es {tasa_men} y de los mayores de 18 es {tasa_may}")
print(f"La participación de  los menores de 18 es {participacion_men} y de los mayores es {participacion_may}")
# (c) ¿Cree usted que atletas menores de 18 años o de 35 años o más ganaron más medallas que atletas de cualquier otro grupo etario? ¿y proporcionalmente?
inter_1=df_atletas[(df_atletas["Age"]<18)|(df_atletas["Age"]>=35)] # Filtra atletas menores de 18 años o mayores/iguales a 35
inter_2=df_atletas[(df_atletas["Age"]>=18)&(df_atletas["Age"]<35)] # Filtra atletas en el rango de 18 a 34 años
m_inter_1=inter_1["Medalla"].sum()
m_inter_2=inter_2["Medalla"].sum()
t_inter_1=inter_1["Medalla"].mean()
t_inter_2=inter_2["Medalla"].mean()
p_inter_1=len(inter_1)
p_inter_2=len(inter_2)
print(f"Medallas <18 o >=35: {m_inter_1} \nMedallas [18,34]: {m_inter_2}")
print(f"Tasa <18 o >=35: {t_inter_1} \nTasa [18,34]: {t_inter_2}")
print(f"Participción <18 o >=35: {p_inter_1} \nParticipación [18,34]: {p_inter_2}")
# (d) ¿Cree usted que la mayor cantidad de medallas las ganaron atletas de Estados Unidos (USA) o de los otros países? ¿y proporcionalmente?
USA=df_atletas[df_atletas["NOC"]=="USA"] # Filtra unicamente los registros de Estados Unidos
otro=df_atletas[df_atletas["NOC"]!="USA"] # Filtra los registros de todos los demas paises
medallas_USA=USA["Medalla"].sum() # Suma las medallas obtenidas por USA
medallas_otro=otro["Medalla"].sum() # Suma las medallas obtenidas por los demas paises
tasa_USA=USA["Medalla"].mean() # Calcula el promedio de medallas para USA
tasa_otro=otro["Medalla"].mean() # Calcula el promedio de medallas para el resto
participacion_USA=len(USA) # Cuenta la participacion total de USA
participacion_otro=len(otro) # Cuenta la participacion total del resto
print(f"Medallas USA: {medallas_USA} \nMedallas otro: {medallas_otro}")
print(f"Tasa USA: {tasa_USA} \nTasa otro: {tasa_otro}")
print(f"Participación USA: {participacion_USA} \nParticipación otro: {participacion_otro}")
# (e) ¿Cree usted que en los Juegos de Verano se ganaron más medallas que en los de Invierno? ¿y proporcionalmente?
verano=df_atletas[df_atletas["Season"]=="Summer"] # Filtra los registros de la temporada de verano
invierno=df_atletas[df_atletas["Season"]=="Winter"] # Filtra los registros de la temporada de invierno
medallas_sum=verano["Medalla"].sum() # Suma las medallas en verano
medallas_win=invierno["Medalla"].sum() # Suma las medallas en invierno
tasa_sum=verano["Medalla"].mean() # Calcula el promedio de medallas en verano
tasa_win=invierno["Medalla"].mean() # Calcula el promedio de medallas en invierno
participacion_sum=len(verano) # Cuenta registros de verano
participacion_win=len(invierno) # Cuenta registros de invierno
print(f"Medallas Verano: {medallas_sum} \nMedallas Invierno: {medallas_win}")
print(f"Tasa Verano: {tasa_sum} \nTasa Invierno: {tasa_win}")
print(f"Participación Verano: {participacion_sum} \nParticipación Invierno: {participacion_win}")
print(medallas_sum/medallas_win)

# Ejercicio 11
n_pruebas = df_atletas.groupby(["ID", "Games"])["Event"].transform("size")
# Calcula el numero de pruebas en las que participo un atleta por cada edicion de los juegos
def clasificar_participacion(n):
  if n == 1:
    return "Grupo 1"
  elif n <= 3:
    return "Grupo 2"
  else:
    return "Grupo 3"
df_atletas["Grupo_Participacion"] = n_pruebas.map(clasificar_participacion) # Aplica la clasificacion de participacion a una nueva columna
print(df_atletas.groupby(["Grupo_Participacion","Sport"]).size())
display(df_atletas.groupby("Grupo_Participacion").size())

# Ejercicio 12
def clasificar_edad(edad): # Define una funcion para clasificar a los atletas por rangos de edad
  if pd.isna(edad):
    return "Sin registro"
  elif edad<18:
    return "Menores"
  elif edad <35:
    return "Jovenes adultos"
  else:
    return "Mayores"
df_atletas["Grupo_etario"]=df_atletas["Age"].map(clasificar_edad)
df_atletas["tiene_e_p"]=df_atletas["Height"].notna() & df_atletas["Weight"].notna()
print(df_atletas.groupby(["Sex","Grupo_etario"])["tiene_e_p"].mean())
print(df_atletas.groupby(["Sex","Grupo_etario"])["Medalla"].mean())
print(df_atletas.groupby(["Sex","Grupo_etario"]).size())
