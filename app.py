# Importar librerias
import streamlit as st
import pandas as pd
from PIL import Image


img = Image.open('Imagenes/logo_sada.png')
st.set_page_config('MPAD M8', 
                    page_icon='img', 
                    layout='wide',
                    initial_sidebar_state='collapsed'
                    )

def main():
    st.title("Personalizando mi aplicación")
    st.sidebar.header('Mi menu')

        

if __name__ == "__main__":
    main()