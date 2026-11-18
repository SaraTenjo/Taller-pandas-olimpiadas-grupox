"""
transformaciones.py
Crea las variables nuevas del taller y une los datasets:
  - IMC
  - Medalla (0/1)
  - Grupo_etario
  - n_pruebas y Grupo_Participacion
  - merge con las regiones
Cada fila de athlete_events.csv es un atleta en una prueba de una edicion,
no un atleta unico.
"""
import numpy as np
import pandas as pd


def agregar_imc(df):
    """IMC = peso / (estatura en metros) al cuadrado. Queda vacio si falta peso o estatura."""
    df = df.copy()
    df["IMC"] = (df["Weight"] / (df["Height"] / 100) ** 2).round(2)
    return df


def agregar_medalla(df):
    """Medalla = 1 si gano Gold, Silver o Bronze; 0 si el campo esta vacio."""
    df = df.copy()
    df["Medalla"] = df["Medal"].notna().astype(int)
    return df


def agregar_grupo_etario(df):
    """Menores (<18), Jovenes adultos (18-34), Mayores (35 o mas). Sin edad: 'Sin registro'."""
    df = df.copy()
    condiciones = [
        df["Age"].isna(),
        df["Age"] < 18,
        df["Age"] < 35,
    ]
    categorias = ["Sin registro", "Menores", "Jovenes adultos"]
    df["Grupo_etario"] = np.select(condiciones, categorias, default="Mayores")
    return df


def agregar_participacion(df):
    """
    n_pruebas: cuantas pruebas hizo cada atleta (ID) en una misma edicion (Games).
    Grupo_Participacion: Grupo 1 (1 prueba), Grupo 2 (2-3), Grupo 3 (4 o mas).
    """
    df = df.copy()
    df["n_pruebas"] = df.groupby(["ID", "Games"])["Event"].transform("size")
    df["Grupo_Participacion"] = np.select(
        [df["n_pruebas"] == 1, df["n_pruebas"] <= 3],
        ["Grupo 1", "Grupo 2"],
        default="Grupo 3",
    )
    return df


def fusionar_regiones(df_atletas, df_regiones):
    """Une atletas con regiones por NOC (merge left: no se pierde ninguna fila)."""
    return df_atletas.merge(df_regiones, on="NOC", how="left")
