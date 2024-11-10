# Importar librerias
import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px


img = Image.open('Imagenes/logo_sada.png')
st.set_page_config('MPAD M8', 
                    page_icon='img', 
                    layout='wide',
                    initial_sidebar_state='collapsed'
                    )

def main():
    st.title("Personalizando mi aplicación")
    st.sidebar.header('Mi menu')

    df = pd.read_csv('data/sada_minas.csv')
    st.dataframe(df)

    df_count = df.groupby('player_role').count().reset_index()
    fig = px.pie(df_count, values='team', title='Roles por equipo')
    st.plotly_chart(fig)

        

if __name__ == "__main__":
    main()