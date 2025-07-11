import streamlit as st
import pandas as pd
from PIL import Image

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="Test de rutina facial", layout="wide")

# --- ESTILOS PERSONALIZADOS ---
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
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.image("https://www.isdin.com/img/routines/test_banner.jpg", use_column_width=True)
st.title("🌿 Test de Rutina Facial")
st.markdown("Descubre tu tipo de piel y encuentra productos ideales para ti ✨")

# --- CARGA DE BASE DE DATOS DE PRODUCTOS ---
@st.cache_data
def cargar_datos():
    return pd.read_csv("productos_skincare.csv")  # Asegúrate de tener este archivo en tu proyecto

df = cargar_datos()

# --- TEST ---
preguntas = [
    {
        "pregunta": "1. ¿Cómo luce tu piel al natural?",
        "opciones": {
            "a": "Lisa y con brillo natural, no oleosa.",
            "b": "Algo opaca y seca.",
            "c": "Me brilla toda la cara.",
            "d": "Algunas zonas están brillosas y otras secas."
        }
    },
    {
        "pregunta": "2. ¿Cómo son tus poros?",
        "opciones": {
            "a": "Finos y poco visibles.",
            "b": "Casi imperceptibles.",
            "c": "Grandes y visibles en todo el rostro.",
            "d": "Grandes solo en la frente, nariz y mentón."
        }
    },
    {
        "pregunta": "3. Al tocar tu piel, ¿cómo se siente?",
        "opciones": {
            "a": "Suave y lisa.",
            "b": "Áspera, a veces descamada.",
            "c": "Gruesa, con granitos.",
            "d": "Una mezcla de seca y grasa según la zona."
        }
    },
    {
        "pregunta": "4. ¿Cómo se comporta tu piel durante el día?",
        "opciones": {
            "a": "Brilla ligeramente al final del día.",
            "b": "Se mantiene opaca casi todo el día.",
            "c": "Brilla mucho todo el día.",
            "d": "Brilla en la zona T, pero no en las mejillas."
        }
    },
    {
        "pregunta": "5. ¿Sueles tener granitos o puntos negros?",
        "opciones": {
            "a": "Muy pocos o ninguno.",
            "b": "Raramente o nunca.",
            "c": "Frecuentemente.",
            "d": "Algunas veces, según la zona."
        }
    },
    {
        "pregunta": "6. Para tu edad, ¿cómo ves tu piel?",
        "opciones": {
            "a": "Normal, sin muchas imperfecciones.",
            "b": "Arrugas marcadas, se siente tirante.",
            "c": "Pocas arrugas, pero piel grasa.",
            "d": "Algunas líneas finas y zonas mixtas."
        }
    }
]

puntajes = {"a": 0, "b": 0, "c": 0, "d": 0}
tipo_piel = {
    "a": "NORMAL",
    "b": "SECA",
    "c": "GRASA",
    "d": "MIXTA"
}

st.subheader("Responde las siguientes preguntas:")

for i, q in enumerate(preguntas):
    respuesta = st.radio(q["pregunta"], list(q["opciones"].values()), key=f"q{i}")
    for letra, texto in q["opciones"].items():
        if respuesta == texto:
            puntajes[letra] += 1

if st.button("Ver resultado"):
    mayor = max(puntajes, key=puntajes.get)
    tipo_usuario = tipo_piel[mayor]
    st.success(f"Tu tipo de piel es: {tipo_usuario}")

    st.markdown("### 🎯 ¿Cuál es tu principal necesidad?")
    necesidad = st.text_input("Ej: acné, hidratación, manchas, arrugas...").lower()
    edad_usuario = st.selectbox("¿En qué rango de edad estás?", ["15-25", "26-35", "36-50", "50+"])

    if necesidad:
        resultados = df[
            df['tipo_piel'].str.lower().str.contains(tipo_usuario.lower()) &
            df['edad'].str.lower().str.contains(edad_usuario.lower()) &
            df['necesidades'].str.lower().str.contains(necesidad)
        ]

        if resultados.empty:
            resultados = df[
                df['tipo_piel'].str.lower().str.contains(tipo_usuario.lower()) &
                df['necesidades'].str.lower().str.contains(necesidad)
            ]

        if resultados.empty:
            resultados = df[
                df['necesidades'].str.lower().str.contains(necesidad)
            ]

        if resultados.empty:
            st.warning("😕 No encontramos productos exactos. Aquí tienes algunas opciones sugeridas:")
            resultados = df.sample(n=min(3, len(df)))
        else:
            st.markdown("### 💖 Recomendaciones para ti:")

        for _, row in resultados.iterrows():
            with st.container():
                st.markdown(f"#### 🧴 {row['nombre']} ({row['marca']})")
                st.image(row['imagen'], width=200)
                st.markdown(f"💸 **Precio:** {row['precio']}")
                st.markdown(f"🔗 [Ver producto]({row['enlace']})")
                st.markdown("---")

st.markdown("---")
st.markdown("Desarrollado por *Grecia García* con 💚 y ciencia para tu piel")
