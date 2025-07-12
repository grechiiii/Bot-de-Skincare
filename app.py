# --- Librerías ---
import streamlit as st
import pandas as pd
import time

# --- Configuración general ---
st.set_page_config(page_title="Tu Rutina Skincare", layout="wide")

# --- Estilos personalizados ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script&family=Quicksand&display=swap" rel="stylesheet">
    <style>
    html, body, .stApp {
        background-color: #fceff8;
        background-image: url('https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/estampado_floral.png');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Quicksand', sans-serif;
        color: #333333;
    }
    input, textarea, select, .stTextInput>div>div>input {
        background-color: #fff0f5 !important;
        color: #333 !important;
        font-weight: bold;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #FFB6C1;
        color: #333333;
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
    }
    .expander-content p {
        font-size: 16px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar cute ---
st.sidebar.image("https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/gatito%20skincare.jpg", width=180)
st.sidebar.markdown("### ✨ ¡Bienvenida!")
st.sidebar.markdown("Este bot te ayudará a encontrar tu rutina ideal de skincare.\n1. Ingresa tu nombre\n2. Haz el test\n3. Descubre productos perfectos para ti")

# --- Cargar datos ---
@st.cache_data
def cargar_datos():
    return pd.read_csv("productos_chatbot_final.csv")

df = cargar_datos()

# --- Collage de portada ---
st.markdown("## 🌸 Bienvenida a Tu Rutina Skincare 🌸")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/collage1.jpg", use_container_width=True)
with col2:
    st.image("https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/collage2.jpg", use_container_width=True)
with col3:
    st.image("https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/collage3.jpg", use_container_width=True)

# --- Inicio ---
if 'nombre' not in st.session_state:
    with st.form("info_usuario"):
        st.image("https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/49725ca650d59cbad0115e87f0325a96.jpg", use_container_width=True)
        st.markdown("### 🌸 Tu piel es especial")
        st.markdown("Descubre tu rutina ideal con solo unos clics")
        nombre = st.text_input("👤 ¿Cómo te llamas?")
        edad = st.selectbox("👶 Selecciona tu rango de edad", ["15-25", "26-35", "36-50", "50+"])
        diario = st.text_area("📝 Cuéntame, ¿qué esperas mejorar en tu piel?", placeholder="Quiero reducir mis granitos, tener más brillo natural...")
        continuar = st.form_submit_button("Comenzar ✨")
        if continuar and nombre:
            st.session_state.nombre = nombre
            st.session_state.edad = edad
            st.session_state.diario = diario
            st.rerun()
else:
    st.markdown(f"## Hola, {st.session_state.nombre} 🌸")
    st.markdown("### Vamos a conocerte mejor con este test de piel 💎")

    preguntas = [
        ("1. ¿Cómo luce tu piel al natural?", [
            ("a", "Lisa y con brillo natural, no oleosa."),
            ("b", "Algo opaca y seca."),
            ("c", "Me brilla toda la cara."),
            ("d", "Algunas zonas están brillosas y otras secas.")]),
        # ... (más preguntas como antes)
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

    if enviar:
        with st.spinner("Analizando tus respuestas... 🤖"):
            time.sleep(2)
        tipo = max(puntajes, key=puntajes.get)
        tipo_piel, img = {
            "a": ("NORMAL", "https://..."),
            "b": ("SECA", "https://..."),
            "c": ("GRASA", "https://..."),
            "d": ("MIXTA", "https://...")
        }[tipo]
        st.session_state.tipo_piel = tipo_piel

        st.image(img, width=300)
        st.success(f"Tu tipo de piel es: **{tipo_piel}**")

        with st.expander("💖 Tu rutina ideal personalizada"):
            st.write("Selecciona los pasos para ver recomendaciones detalladas:")
            pasos = ["Limpieza", "Tónico", "Sérum", "Hidratante", "Protector solar"]
            for paso in pasos:
                with st.expander(f"🔹 {paso}"):
                    st.write(f"Consejos específicos para {paso.lower()} según piel {tipo_piel.lower()}...")

        with st.expander("📢 Mitos comunes del skincare"):
            st.radio("Selecciona un mito para conocer la verdad:", [
                "El limón aclara la piel",
                "Si arde, está funcionando",
                "Solo las mujeres deben cuidarse la piel"
            ])
            st.write("Todos debemos cuidar nuestra piel con información segura y actualizada.")

        with st.expander("📖 Aprende más sobre tu tipo de piel"):
            st.markdown("### Características, errores comunes y consejos de largo plazo")
            st.write("Según dermatólogos, tu tipo de piel necesita cuidado específico...")
            st.info("Consejos adaptados, ingredientes recomendados y rutinas nocturnas.")

        with st.expander("🎥 Videos y contenido educativo"):
            st.video("https://www.youtube.com/watch?v=vSKVbp1jepc")
            st.video("https://www.youtube.com/watch?v=kw8UqeBnfxY")

        feedback = st.text_area("💬 ¿Te gustó tu rutina? Cuéntanos tus ideas para mejorarla")
        if feedback:
            st.success("¡Gracias por tu comentario! 💌")

