# Importar librerias
import streamlit as st
import pandas as pd
from PIL import Image

df = pd.read_csv('data/sada_minas.csv')

def main():
    st.title("Trabajando con datos en Streamlit")
    st.header("Usando dataframe")
    st.dataframe(df)
    st.header("Usando table")
    st.table(df)

    st.header("Visualizando json")
    st.json("clave:valor")
    

if __name__ == "__main__":
    main()