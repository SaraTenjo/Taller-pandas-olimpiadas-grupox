#Pasos generales para crear gráficas de barras
# Se importa la libreria
# Se elije el tipo de gráfico (en este caso barras kind='bar') con los datos y un color
# Se pone un título principal y nombres a los ejes para que se entienda
# Se rotan los nombres para que se vean mejor
# Mostrar el gráfico en pantalla


#Gráfica 1: Cantidad de medallas por género 
atletas_con_medalla = df_merged.dropna(subset=['Medal'])
medallas_por_genero = atletas_con_medalla['Sex'].value_counts()

print('Cantidad de medallas ganadas por género:')
display(medallas_por_genero)

print('\n-----------------------------------------------------------------------------\n')

medallas_por_genero.plot(kind='bar', color=['lime', 'salmon'])
plt.title('Medallas ganadas por género')
plt.xlabel('Género')
plt.ylabel('Cantidad de Medallas')
plt.show()

#Gráfica 2: Cantidad de atletas por género
import matplotlib.pyplot as plt
conteo_datos = df_atletas['Sex'].value_counts()
conteo_datos.plot(kind='bar', color=['deepskyblue', 'deeppink'])
plt.title('Cantidad de Atletas por Género')
plt.xlabel('Género')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.show()

#Gráfica 3: Proporcion de participantes por sexo 
prob_genero.plot(kind="bar",color="#A52A2A")
plt.title("Proporcion de participaciones con medalla según el sexo")
plt.xlabel('Género')
plt.ylabel('Proporción con medalla')
plt.xticks(rotation=0)
plt.show()

#Gráfica 4: Proporción de participaciones con medalla por grupo etario 
prob_edad.plot(kind="bar",color="#008B8B")
plt.title("Proporcion de participaciones con medalla según categoría de edad")
plt.xlabel('Grupo etario')
plt.ylabel('Proporción con medalla')
plt.xticks(rotation=0)
plt.show()

#Gráfica 5: Top 5 países con más participaciones
top_paises = df_merged['region'].value_counts().head(5)
top_paises.plot(kind='bar', color='skyblue')
plt.title('Top 5 Países con más Atletas')
plt.xlabel('País')
plt.ylabel('Cantidad de Atletas')
plt.xticks(rotation=45)
plt.show()

#Gráfica 6: Proporcion de participaciones con medalla según la región
prob_region.plot(kind="bar",color="#006400")
plt.title("Proporcion de participaciones con medalla según la región")
plt.xlabel('Región')
plt.ylabel('Proporción con medalla')
plt.xticks(rotation=0)
plt.show()
