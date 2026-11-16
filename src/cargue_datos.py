"""
cargue_datos.py
Carga los archivos athlete_events.csv y noc_regions.csv desde la carpeta data/.
"""
import pandas as pd

df_atletas = pd.read_csv("data/athlete_events.csv")
df_regiones = pd.read_csv("data/noc_regions.csv")
