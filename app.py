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
        # ... (preguntas 2 a 6 igual que antes)
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

    # --- Resultado y secciones personalizadas ---
    if enviar:
        with st.spinner("Analizando tus respuestas... 🤖"):
            time.sleep(2)
        tipo = max(puntajes, key=puntajes.get)
        tipos = {
            "a": ("NORMAL", "https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/nioormal.jpg"),
            "b": ("SECA", "https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/pielseca.jpg"),
            "c": ("GRASA", "https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/cc459e606dd2072aca33f94a274829cf.jpg"),
            "d": ("MIXTA", "https://raw.githubusercontent.com/grechiiii/Bot-de-Skincare/main/images/mixta.jpg")
        }
        tipo_piel, img = tipos[tipo]
        st.session_state.tipo_piel = tipo_piel

        st.image(img, width=300)
        st.success(f"Tu tipo de piel es: **{tipo_piel}**")

        # --- Rutina sugerida ---
        rutinas = {
            "SECA": "Limpieza suave → Tónico hidratante → Sérum → Crema rica → Protector solar",
            "GRASA": "Gel limpiador → Tónico matificante → Sérum seborregulador → Hidratante ligera → Protector solar oil free",
            "MIXTA": "Limpieza equilibrada → Tónico suave → Sérum → Hidratante mixta → Protector solar",
            "NORMAL": "Limpieza básica → Hidratante ligera → Protector solar"
        }

        with st.expander("💖 Tu rutina ideal paso a paso"):
            st.info(rutinas[tipo_piel])
            st.write("- Los productos están adaptados a tu tipo de piel.")
            st.write("- Evitan irritaciones o exceso de grasa.")
            st.write("- Puedes seguirla día y noche para mejores resultados.")

        # --- Productos recomendados según datos ---
        with st.expander("🧴 Productos recomendados solo para ti"):
            st.toast("Buscando productos para ti...", icon="💼")
            resultados = df[
                df['tipo_piel'].str.lower().str.contains(tipo_piel.lower()) &
                df['edad'].str.lower().str.contains(st.session_state.edad.lower())
            ]
            if resultados.empty:
                resultados = df.sample(min(3, len(df)))
            for _, row in resultados.iterrows():
                st.markdown(f"""
                    <div class='producto-card'>
                        <h4>{row['nombre']}</h4>
                        <p><strong>Marca:</strong> {row['marca']}<br>
                        <strong>Precio:</strong> S/ {row['precio']}</p>
                        <a href="{row['enlace']}" target="_blank">Ver producto 🔗</a>
                    </div>
                """, unsafe_allow_html=True)

        # --- Sección de mitos del skincare ---
        with st.expander("🚫 Mitos comunes del skincare"):
            st.error("❌ El limón aclara la piel – Puede causar quemaduras.")
            st.error("❌ Si arde, está funcionando – Probablemente te está irritando.")
            st.error("❌ Solo las mujeres deben cuidarse la piel – ¡Todos debemos hacerlo!")

        # --- Más información según tipo de piel ---
        with st.expander("📖 Más información sobre tu tipo de piel"):
            if tipo_piel == "SECA":
                st.info("La piel seca produce menos sebo de lo normal. Puede sentirse tirante, áspera o incluso agrietada. Necesita productos nutritivos y muy hidratantes.")
                st.markdown("- Evita jabones fuertes que resequen más.")
                st.markdown("- Usa sérums con ácido hialurónico y ceramidas.")
                st.markdown("- Aplica cremas más densas por la noche.")
            elif tipo_piel == "GRASA":
                st.info("La piel grasa produce un exceso de sebo. Es propensa a granitos, poros dilatados y brillo facial. Requiere limpieza constante y productos oil-free.")
                st.markdown("- Usa limpiadores en gel o espuma suave dos veces al día.")
                st.markdown("- No te saltes la hidratación, solo usa productos ligeros.")
                st.markdown("- Prueba tónicos con BHA (ácido salicílico).")
            elif tipo_piel == "MIXTA":
                st.info("La piel mixta tiene zonas grasas (zona T) y otras más secas. Necesita un equilibrio entre hidratación y control de grasa.")
                st.markdown("- Puedes usar productos distintos según la zona (multimasking).")
                st.markdown("- Prefiere hidratantes en gel y texturas ligeras.")
                st.markdown("- Evita productos extremos (muy grasos o muy secos).")
            elif tipo_piel == "NORMAL":
                st.info("La piel normal es equilibrada, ni muy grasa ni muy seca. Suele tener textura suave y poros poco visibles.")
                st.markdown("- Mantén una rutina constante, aunque no tengas problemas visibles.")
                st.markdown("- Usa protector solar todos los días.")
                st.markdown("- Aún si tu piel se ve bien, hidrátala y límpiala cada día.")

        # --- Videos de skincare ---
        with st.expander("🎥 Videos de skincare y publicidad"):
            st.video("https://www.youtube.com/watch?v=vSKVbp1jepc")
            st.video("https://www.youtube.com/watch?v=kw8UqeBnfxY")
            st.video("https://www.youtube.com/watch?v=3dfQo9b4EKI")

        # --- Comentarios del usuario con respuesta personalizada y opción de reinicio ---
        feedback = st.text_area("💬 ¿Qué te pareció tu rutina? ¿Te gustaría que mejoremos algo?", placeholder="Me encantó, pero me gustaría que incluyera más opciones naturales...")
        if feedback:
            st.success("¡Gracias por tu comentario! 💌")
            st.info("Tu opinión nos ayuda a mejorar este bot para futuras usuarias ✨")

        # --- Botón para reiniciar todo el flujo ---
        if st.button("¿Quieres hacer el test de nuevo? 🔁"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

