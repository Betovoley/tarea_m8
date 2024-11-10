# Importar librerias
import streamlit as st
import pandas as pd
from PIL import Image

def main():
    st.title("Trabajando con controles de ingreso de datos")

    nombre = st.text_input('Ingrese su nombre')
    st.write(nombre)

    mensaje = st.text_area('Ingrese su mensaje', height=100)
    st.write(mensaje)

    edad = st.number_input('Ingrese su edad', 1,100, step=1)
    st.write(edad)

    fecha = st.date_input('Ingrese su fecha de nacimiento')
    st.write(fecha)

    hora = st.time_input('Ingrese la hora')
    st.write(hora)

    color = st.color_picker('seleccione un color')
    st.write(color)

if __name__ == "__main__":
    main()