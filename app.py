import streamlit as st
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
    resultado = tipo_piel[mayor]
    st.success(f"Tu tipo de piel es: {resultado}")
    imagenes = {
        "NORMAL": "https://i.imgur.com/0iKXwra.jpg",
        "SECA": "https://i.imgur.com/KcsIt8Q.jpg",
        "GRASA": "https://i.imgur.com/REf90Y3.jpg",
        "MIXTA": "https://i.imgur.com/nk6BoIO.jpg"
    }
    st.image(imagenes[resultado], caption=f"Piel {resultado}")

    st.markdown("### Productos recomendados:")
    if resultado == "GRASA":
        st.image("https://i.imgur.com/zyEXiEF.jpg", caption="Gel limpiador seborregulador")
    elif resultado == "SECA":
        st.image("https://i.imgur.com/VIRKa8q.jpg", caption="Crema hidratante intensiva")
    elif resultado == "MIXTA":
        st.image("https://i.imgur.com/VxQxa5p.jpg", caption="Hidratante ligera para zonas mixtas")
    elif resultado == "NORMAL":
        st.image("https://i.imgur.com/Fm9ZV6g.jpg", caption="Cuidado básico para piel equilibrada")

st.markdown("---")
st.markdown("Desarrollado por *Grecia García* con 💚 y ciencia para tu piel")
