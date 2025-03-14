import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("¡Bienvenidos a Vanguard!")

st.sidebar.markdown("## Hola caracola2")

df = pd.read_csv("data/processed/navegacion_clientes_experimento_limpio.csv")
st.write(df.head())

def explorar_datos(df):
    st.write(f"- El DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.\n")
    st.write("- Los nombres de las columnas y sus tipos de datos son:")
    st.write(pd.DataFrame(df.dtypes, columns=["tipo_dato"]))
    df.info()

def contar_duplicados(df):
    num_duplicados = df.duplicated().sum()
    num_duplicados_perc = round(num_duplicados / df.shape[0] * 100, 2)
    st.write(f"- El DataFrame tiene {num_duplicados} filas duplicadas ({num_duplicados_perc}%).\n")
    return num_duplicados

def contar_nulos(df):
    nulos_por_columna = df.isnull().sum()
    nulos_por_columna_perc = round(nulos_por_columna / df.shape[0] * 100, 1)
    st.write("- El porcentaje de valores nulos por columna es:")
    st.write(pd.DataFrame(nulos_por_columna_perc, columns=["% nulos"]))

explorar_datos(df)
contar_duplicados(df)
contar_nulos(df)

