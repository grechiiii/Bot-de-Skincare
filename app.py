# --- Librerías ---
import streamlit as st
import pandas as pd
import time

# --- Configuración general de la página ---
st.set_page_config(page_title="Tu Rutina Skincare", layout="wide")

# --- Estilos personalizados con fondo, fuente y colores visibles ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Quicksand&display=swap" rel="stylesheet">
    <style>
    html, body, [class*="css"]  {
        font-family: 'Quicksand', sans-serif;
        background-color: #fceff8;
        color: #111111 !important;
    }
    .stApp {
        background-image: url('https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/estampado_floral.png');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stButton>button {
        background-color: #FFB6C1;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        margin: 5px;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: #ffa0c5;
        transform: scale(1.05);
    }
    .producto-card {
        border-radius: 15px;
        padding: 1rem;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        color: #111111;
    }
    </style>
""", unsafe_allow_html=True)

# --- Barra lateral con instrucciones e imagen ---
st.sidebar.image("https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/gatito%20skincare.jpg", width=180)
st.sidebar.markdown("### ✨ ¡Bienvenida!")
st.sidebar.markdown("Este bot te ayudará a encontrar tu rutina ideal de skincare.\n1. Ingresa tu nombre\n2. Haz el test\n3. Descubre productos perfectos para ti")

# --- Función para cargar los datos del CSV ---
@st.cache_data
def cargar_datos():
    return pd.read_csv("productos_chatbot_final.csv")

df = cargar_datos()

# --- Encabezado de bienvenida ---
st.markdown("## 🌸 Bienvenida a Tu Rutina Skincare 🌸")
st.markdown("Descubre tu rutina facial perfecta con ayuda de este bot interactivo ✨")

# --- Formulario inicial para capturar datos del usuario ---
if 'nombre' not in st.session_state:
    with st.form("info_usuario"):
        st.image("https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/49725ca650d59cbad0115e87f0325a96.jpg", use_container_width=True)
        st.markdown("### 🌸 Tu piel es especial")
        st.markdown("Descubre tu rutina ideal con solo unos clics")
        nombre = st.text_input("¿Cuál es tu nombre?")
        edad = st.selectbox("Selecciona tu rango de edad", ["15-25", "26-35", "36-50", "50+"])
        diario = st.text_area("📝 Cuéntame, ¿qué esperas mejorar en tu piel?", placeholder="Quiero reducir mis granitos, tener más brillo natural...")
        continuar = st.form_submit_button("Comenzar ✨")
        if continuar and nombre:
            st.session_state.nombre = nombre
            st.session_state.edad = edad
            st.session_state.diario = diario
            st.rerun()

# --- Sección del test interactivo ---
else:
    st.markdown(f"## Hola, {st.session_state.nombre} 🌸")
    st.markdown("### Vamos a conocerte mejor con este test de piel 💎")

    preguntas = [
        ("1. ¿Cómo luce tu piel al natural?", [
            ("a", "Lisa y con brillo natural, no oleosa."),
            ("b", "Algo opaca y seca."),
            ("c", "Me brilla toda la cara."),
            ("d", "Algunas zonas están brillosas y otras secas.")]),
        ("2. ¿Cómo son tus poros?", [
            ("a", "Finos y poco visibles."),
            ("b", "Casi imperceptibles."),
            ("c", "Grandes y visibles en todo el rostro."),
            ("d", "Grandes solo en la frente, nariz y mentón.")]),
        ("3. Al tocar tu piel, ¿cómo se siente?", [
            ("a", "Suave y lisa."),
            ("b", "Áspera, a veces descamada."),
            ("c", "Gruesa, con granitos."),
            ("d", "Una mezcla de seca y grasa según la zona.")]),
        ("4. ¿Cómo se comporta tu piel durante el día?", [
            ("a", "Brilla ligeramente al final del día."),
            ("b", "Se mantiene opaca casi todo el día."),
            ("c", "Brilla mucho todo el día."),
            ("d", "Brilla en la zona T, pero no en las mejillas.")]),
        ("5. ¿Sueles tener granitos o puntos negros?", [
            ("a", "Muy pocos o ninguno."),
            ("b", "Raramente o nunca."),
            ("c", "Frecuentemente."),
            ("d", "Algunas veces, según la zona.")]),
        ("6. Para tu edad, ¿cómo ves tu piel?", [
            ("a", "Normal, sin muchas imperfecciones."),
            ("b", "Arrugas marcadas, se siente tirante."),
            ("c", "Pocas arrugas, pero piel grasa."),
            ("d", "Algunas líneas finas y zonas mixtas.")]),
    ]

    puntajes = {"a": 0, "b": 0, "c": 0, "d": 0}
    with st.form("test_piel"):
        for p, opciones in preguntas:
            st.markdown(f"**{p}**")
            r = st.radio("", [texto for _, texto in opciones], key=p)
            for letra, texto in opciones:
                if r == texto:
                    puntajes[letra] += 1
        enviar = st.form_submit_button("Ver mi tipo de piel 💕")


