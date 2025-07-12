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
        for i, (pregunta, opciones) in enumerate(preguntas):
            st.markdown(f"**{pregunta}**")
            respuesta = st.radio("", [texto for _, texto in opciones], key=f"preg_{i}")
            for letra, texto in opciones:
                if respuesta == texto:
                    puntajes[letra] += 1
        enviar = st.form_submit_button("Ver mi tipo de piel 💕")

    if enviar:
        st.session_state.puntajes = puntajes
        st.rerun()

    if 'puntajes' in st.session_state and 'tipo_piel' not in st.session_state:
        puntajes = st.session_state.puntajes
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

        with st.expander("🧴 Productos recomendados para ti"):
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

        with st.expander("📖 Más información sobre tu tipo de piel"):
            if tipo_piel == "SECA":
                st.info("La piel seca produce menos sebo de lo normal, puede sentirse áspera, tirante y con escamas. Requiere hidratación profunda y productos ricos en lípidos.")
                st.write("- Usa mascarillas hidratantes semanales.")
                st.write("- Evita duchas muy calientes.")
            elif tipo_piel == "GRASA":
                st.info("La piel grasa produce un exceso de sebo, lo que causa brillo, poros dilatados y tendencia al acné. Necesita limpieza constante y productos oil-free.")
                st.write("- No frotes tu piel con fuerza.")
                st.write("- Usa papel secante si brillas durante el día.")
            elif tipo_piel == "MIXTA":
                st.info("Tiene zonas grasas (zona T) y otras secas. Requiere productos equilibrantes y cuidado personalizado por zonas.")
                st.write("- Usa productos diferentes según la zona.")
                st.write("- No olvides la hidratación aunque tengas partes grasas.")
            else:
                st.info("La piel normal es equilibrada, ni muy grasa ni muy seca. Solo requiere una rutina básica de mantenimiento.")
                st.write("- Usa protector solar todos los días.")
                st.write("- Mantén una rutina constante.")
                
# --- Mitos comunes del skincare ---
        with st.expander("🚫 Mitos comunes del skincare"):
            st.error("❌ El limón aclara la piel – Puede causar quemaduras.")
            st.error("❌ Si arde, está funcionando – Probablemente te está irritando.")
            st.error("❌ Solo las mujeres deben cuidarse la piel – ¡Todos debemos hacerlo!")

        # --- Videos de skincare y publicidad ---
        with st.expander("🎥 Videos de skincare y publicidad"):
            st.video("https://www.youtube.com/watch?v=vSKVbp1jepc")
            st.video("https://www.youtube.com/watch?v=kw8UqeBnfxY")
            st.video("https://www.youtube.com/watch?v=3dfQo9b4EKI")
            
        feedback = st.text_area("💬 ¿Qué te pareció tu rutina? ¿Te gustaría que mejoremos algo?", placeholder="Me encantó, pero me gustaría que incluyera más opciones naturales...")
        if feedback:
            st.success("¡Gracias por tu comentario! 💌 Nos alegra ayudarte ✨")

        st.button("🔄 Hacer el test de nuevo", on_click=lambda: st.session_state.clear())
