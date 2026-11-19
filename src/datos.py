
print('\n')
print('Estadisticas DataSet Atletas')
display(df_atletas.describe(include ='all')) # El .describe() generar un resumen estadistico rapido y completo
print('\n\n')
print('Estadisticas DataSet Regiones')
display(df_regiones.describe(include ='all')) # El include='all' hace que el resumen estadistico incluya todas las variables sin importar el tipo
