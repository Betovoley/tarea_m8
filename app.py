# Importar librerias
import streamlit as st
import pandas as pd
from PIL import Image

def main():
    st.title("Trabajando con multimedia")

    img = Image.open("imagenes/camiseta.png")
    st.image(img, use_container_width=True)

    img1="https://upload.wikimedia.org/wikipedia/pt/6/67/SadaCruzeiro2021.png"
    st.image(img1, use_container_width=True)

    with open('Videos/yo.mp4', 'rb') as video_file:
        st.video(video_file, start_time=0)

    with open('Musica/we are the champions.mp3', 'rb') as audio_file:
        st.audio(audio_file, start_time=0)

    st.html(
    "<p><span style='text-decoration: line-through double red;'>Esta funcionando</span>!</p>"

    
)


    


if __name__ == "__main__":
    main()