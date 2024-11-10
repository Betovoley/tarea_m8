# Importar librerias
import streamlit as st
import pandas as pd
from PIL import Image

df = pd.read_csv('data/sada_minas.csv')

def main():
    st.title("Trabajando con componentes")

    posicion = st.selectbox('Seleccione una posición', 
                  ['Portero', 'Defensa', 'Mediocampista', 'Delantero']
                 )
    st.write(f"La posición seleccionada es: {posicion}")

    opciones = st.multiselect('Seleccione una posición', 
                  ['Portero', 'Defensa', 'Mediocampista', 'Delantero']
                 )
    st.write(f"La posición seleccionada es: {opciones}")

    edad = st.slider('Selecciones su edad',
                min_value = 1,
                max_value = 100,
                value = 20,
                step = 1
                )
    st.write(f"Su edad es: {edad}")

    nivel = st.select_slider(
        'Seleccion su nivel',
        options = ['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Muy alto'],
        )
    st.write(f"Su nivel es: {nivel}")

    opc = st.radio('selccione una opcion',
            ['Portero', 'Defensa', 'Mediocampista', 'Delantero']
            )

    st.write(f"La opcion seleccionada es: {opc}")

    check = st.checkbox("Acepto las condiciones")
    if check:
        st.write("Aceptaste las condiciones")
    else:
        st.write("No Aceptaste las condiciones")

    rta = st.button('Hola amor')
    if rta:
        st.write('Como estas amor?')
        st.write(rta)
    else:
        st.write('-')
        st.write(rta)

    
    tab1, tab2, tab3 = st.tabs(["Ataque", "Saque", "Bloqueo"])

    with tab1:
        st.header("Ataque")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.header("Saque")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        st.header("Bloqueo")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


if __name__ == "__main__":
    main()