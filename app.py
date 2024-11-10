# Importar librerias
import streamlit as st
import pandas as pd
from PIL import Image

def main():
    st.title("Mi primera app en Streamlit")
    st.header("este es el header")
    st.subheader("este es el subheader")
    st.text("esto es un texto")
    nombre = "Betovoley"
    st.text(f"hola {nombre}")
    nombre = "mundo"
    st.text(f"hola " + nombre)
    st.markdown("# markdown 1")
    st.markdown("## markdown 2")
    st.markdown("### markdown 3")
    st.markdown("#### markdown 4")
    st.markdown("markdown 0")

    st.success("mensaje de exito")
    st.error("mensaje de error")
    st.warning("mensaje de advertencia")
    st.info("informacion")
    st.exception("mensaje contro excepciones")
    st.text("esto es un texto")

    st.write("parrafo o texto que queramos")
    st.write("### parrafo o texto que queramos")
    st.write(3 + 3)


if __name__ == "__main__":
    main()