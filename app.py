import streamlit as st
from utils import consultar_ia  # Ya cambiamos el nombre en utils.py

st.set_page_config(page_title="Buscador de Programas Sheffield", layout="centered")
st.title("🌍 Buscador de Programas Sheffield")

# Navegación
page = st.sidebar.radio("Navegación", ["Inicio", "Buscador de Programas"])

if page == "Inicio":
    st.header("Bienvenido a Sheffield")
    st.markdown("""
    Sheffield conecta a estudiantes con programas de intercambio internacional en todo el mundo.

    🔎 Usa esta aplicación para:
    - Ingresar tus preferencias
    - Encontrar todos los programas de intercambio disponibles

    👉 Ve a **Buscador de Programas** para comenzar.
    """)

elif page == "Buscador de Programas":
    st.header("Encuentra el Programa Ideal")

    edad = st.number_input("Edad del estudiante", min_value=1, max_value=30, value=17)
    duracion = st.text_input("Duración deseada (ej. 2 semanas, 1 semestre)")
    destino = st.text_input("Destino preferido (opcional)")
    info_adicional = st.text_area("Información adicional (opcional)", placeholder="Requisitos especiales, preferencias, objetivos...")

    if st.button("Buscar Programas"):
        consulta = f"El estudiante tiene {edad} años y busca un programa que dure '{duracion}'."
        if destino:
            consulta += f" Le gustaría ir a {destino}."
        if info_adicional:
            consulta += f" Información adicional: {info_adicional}."

        st.markdown("🔍 Buscando programas...")
        respuesta = consultar_ia(consulta)
        st.success("✅ Resultados:")
        st.write(respuesta)
