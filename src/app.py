import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("¡Bienvenidos a Vanguard!")

st.sidebar.markdown("## Hola caracola2")

df = pd.read_csv("data/processed/navegacion_clientes_experimento_limpio.csv")
st.write(df.head())




