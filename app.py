import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="Skincare Bot 💖", layout="wide")

# --- COLORES Y ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    body {
        background-color: #E8F5E9;
        color: #1B5E20;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #2E7D32;
    }
    .stButton button {
        background-color: #A5D6A7;
        color: #1B5E20;
        border-radius: 8px;
        padding: 0.6em 1em;
        font-weight: bold;
    }
    .card {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("🌿 Chatbot Skincare Natural")
st.write("Explora recomendaciones personalizadas, ingredientes activos y mitos con un diseño amigable y visual ✨")

# --- OPCIONES COMO CUADROS CON IMAGEN ---
st.markdown("### Elige una categoría:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🧪 Tu tipo de piel"):
        st.session_state.seccion = "test"
    st.image("https://i.imgur.com/DxXGQxf.jpg", caption="Test de piel", use_column_width=True)

with col2:
    if st.button("🧴 Rutina ideal"):
        st.session_state.seccion = "rutina"
    st.image("https://i.imgur.com/pQZJGyi.jpg", caption="Rutinas", use_column_width=True)

with col3:
    if st.button("🍊 Ingredientes"):
        st.session_state.seccion = "ingredientes"
    st.image("https://i.imgur.com/5HJ6xFl.jpg", caption="Ingredientes clave", use_column_width=True)

with col4:
    if st.button("🚫 Mitos"):
        st.session_state.seccion = "mitos"
    st.image("https://i.imgur.com/7A0WaIH.jpg", caption="Mitos comunes", use_column_width=True)

# --- CONTENIDO SEGÚN ELECCIÓN ---

if 'seccion' not in st.session_state:
    st.session_state.seccion = None

if st.session_state.seccion == "test":
    st.header("💚 Conoce tu tipo de piel")
    st.write("Responde estas preguntas y el bot te dirá tu tipo de piel aproximado:")

    agua = st.radio("¿Tu piel se siente tirante después de lavarla solo con agua?", ["Sí", "No"])
    brillo = st.radio("¿Notas brillo en tu piel durante el día?", ["Mucho", "Un poco", "Nada"])
    granos = st.radio("¿Tienes granitos o espinillas con frecuencia?", ["Sí", "A veces", "No"])
    zonas = st.radio("¿Sientes que algunas zonas son secas y otras grasas?", ["Sí", "No"])

    if st.button("Ver resultado"):
        if agua == "Sí" and brillo == "Nada":
            tipo = "Piel seca"
        elif zonas == "Sí":
            tipo = "Piel mixta"
        elif brillo == "Mucho" or granos == "Sí":
            tipo = "Piel grasa"
        else:
            tipo = "Piel normal"

        st.success(f"Tu tipo de piel es: {tipo}")
        st.image("https://i.imgur.com/WJYZxP6.png", caption=f"{tipo}")

elif st.session_state.seccion == "rutina":
    st.header("🧴 Rutina recomendada")
    st.write("Aquí una rutina básica según tu tipo de piel:")

    st.markdown("""
    - **Limpieza suave:** mañana y noche.
    - **Tónico hidratante:** sin alcohol.
    - **Suero o esencia:** según tu necesidad.
    - **Hidratante ligera o rica:** dependiendo tu piel.
    - **Protector solar:** ¡todos los días!
    """)
    st.video("https://www.youtube.com/watch?v=7cUWe_lz0og")

elif st.session_state.seccion == "ingredientes":
    st.header("🍊 Ingredientes activos recomendados")
    st.markdown("""
    - **Ácido hialurónico:** Hidratación profunda 💧
    - **Niacinamida:** Reduce poros y grasa 🌿
    - **Retinol:** Renovación y anti edad ✨
    - **Vitamina C:** Ilumina y unifica 🌞
    - **Ácido salicílico:** Ideal para acné 🔬
    """)
    st.image("https://i.imgur.com/5HJ6xFl.jpg", use_column_width=True)

elif st.session_state.seccion == "mitos":
    st.header("🚫 Mitos del skincare que debes olvidar")
    st.markdown("""
    ❌ *Si arde es que funciona* → No, puede ser irritación.  
    ❌ *El limón aclara la piel* → ¡Peligroso! Puede mancharte.  
    ❌ *Solo las mujeres deben cuidarse la piel* → ¡Falso!  
    ❌ *Más caro es mejor* → Lo importante es que sea adecuado a ti.  
    """)
    st.image("https://i.imgur.com/7A0WaIH.jpg", use_column_width=True)

# --- PIE DE PÁGINA ---
st.markdown("---")
st.markdown("Desarrollado por *Grecia García* con 💚 y ciencia para tu piel")
