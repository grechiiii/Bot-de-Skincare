# --- Librerías ---
import streamlit as st
import pandas as pd
import random

# --- Estilo general ---
st.set_page_config(page_title="Tu Rutina Skincare", layout="wide")
st.markdown("""
    <style>
    body {
        background-color: #E6F2EA;
    }
    .stButton>button {
        background-color: #A2D5C6;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        margin: 5px;
    }
    .producto-card {
        border-radius: 15px;
        padding: 1rem;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Cargar base de datos ---
@st.cache_data
def cargar_datos():
    return pd.read_csv("productos_chatbot_final.csv")

df = cargar_datos()

# --- Ventana emergente al inicio ---
if 'nombre' not in st.session_state:
    with st.form("info_usuario"):
        st.image("https://i.imgur.com/xzfk4of.jpg", use_column_width=True)
        st.markdown("### Tu piel es única ✨")
        st.markdown("Descubre tu rutina ideal con solo unos clics")
        nombre = st.text_input("¿Cuál es tu nombre?")
        edad = st.selectbox("¿Qué rango de edad tienes?", ["15-25", "26-35", "36-50", "50+"])
        continuar = st.form_submit_button("Comenzar ✨")
        if continuar and nombre:
            st.session_state.nombre = nombre
            st.session_state.edad = edad
            st.experimental_rerun()
else:
    st.markdown(f"## Hola, {st.session_state.nombre} 🌸")
    st.markdown("### Empecemos conociendo tu tipo de piel:")

    # --- Preguntas del test ---
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
        enviar = st.form_submit_button("Ver mi tipo de piel 💖")

    if enviar:
        tipo = max(puntajes, key=puntajes.get)
        tipos = {
            "a": ("NORMAL", "https://i.imgur.com/Sdu3ZZN.jpg"),
            "b": ("SECA", "https://i.imgur.com/vvDse8w.jpg"),
            "c": ("GRASA", "https://i.imgur.com/5BknY1M.jpg"),
            "d": ("MIXTA", "https://i.imgur.com/RxDUnNy.jpg")
        }
        tipo_piel, img = tipos[tipo]
        st.session_state.tipo_piel = tipo_piel

        st.image(img, width=300)
        st.success(f"Tu tipo de piel es: **{tipo_piel}**")

        # --- Rutina ideal ---
        st.markdown("### 🧴 Tu rutina ideal")
        rutinas = {
            "SECA": "Limpieza suave → Tónico hidratante → Sérum → Crema rica → Protector solar",
            "GRASA": "Gel limpiador → Tónico matificante → Sérum seborregulador → Hidratante ligera → Protector solar oil free",
            "MIXTA": "Limpieza equilibrada → Tónico suave → Sérum → Hidratante mixta → Protector solar",
            "NORMAL": "Limpieza básica → Hidratante ligera → Protector solar"
        }
        st.info(rutinas[tipo_piel])

        # --- Necesidades ---
        st.markdown("### 💡 ¿Qué necesitas?")
        necesidades = ["Acné", "Hidratación", "Manchas", "Arrugas", "Sensibilidad"]
        necesidad = st.selectbox("Selecciona una necesidad", necesidades)

        # --- Recomendaciones ---
        st.markdown("### 🎯 Productos recomendados")
        resultados = df[
            df['tipo_piel'].str.lower().str.contains(tipo_piel.lower()) &
            df['edad'].str.lower().str.contains(st.session_state.edad.lower()) &
            df['necesidades'].str.lower().str.contains(necesidad.lower())
        ]
        if resultados.empty:
            resultados = df[df['necesidades'].str.lower().str.contains(necesidad.lower())]
        if resultados.empty:
            st.warning("No encontramos productos exactos, pero aquí tienes sugerencias aleatorias")
            resultados = df.sample(min(3, len(df)))

        for _, row in resultados.iterrows():
            with st.container():
                st.markdown(f"""
                    <div class="producto-card">
                        <h4>{row['nombre']}</h4>
                        <p><strong>Marca:</strong> {row['marca']}<br>
                        <strong>Precio:</strong> {row['precio']}</p>
                        <a href="{row['enlace']}" target="_blank">Ver producto 🔗</a>
                    </div>
                """, unsafe_allow_html=True)

        # --- Mitos del skincare ---
        st.markdown("### 🚫 Mitos comunes del skincare")
        st.error("❌ El limón aclara la piel – Puede causar quemaduras.")
        st.error("❌ Si arde, está funcionando – Probablemente te está irritando.")
        st.error("❌ Solo las mujeres deben cuidarse la piel – ¡Todos debemos hacerlo!")

        # --- Info adicional tipos de piel ---
        st.markdown("### 📚 Más información sobre tu tipo de piel")
        if tipo_piel == "SECA":
            st.info("La piel seca produce menos sebo de lo normal, puede sentirse áspera, tirante y con escamas. Requiere hidratación profunda y productos ricos en lípidos.")
        elif tipo_piel == "GRASA":
            st.info("La piel grasa produce un exceso de sebo, lo que causa brillo, poros dilatados y tendencia al acné. Necesita limpieza constante y productos oil-free.")
        elif tipo_piel == "MIXTA":
            st.info("Tiene zonas grasas (zona T) y otras secas. Requiere productos equilibrantes y cuidado personalizado por zonas.")
        else:
            st.info("La piel normal es equilibrada, ni muy grasa ni muy seca. Solo requiere una rutina básica de mantenimiento.")

        # --- Videos ---
        st.markdown("### 🎥 Aprende más sobre skincare")
        st.video("https://www.youtube.com/watch?v=vSKVbp1jepc")
        st.markdown("### 🎬 Ejemplos de publicidad")
        st.video("https://www.youtube.com/watch?v=kw8UqeBnfxY")
        st.video("https://www.youtube.com/watch?v=3dfQo9b4EKI")
