import streamlit as st

# --- CONFIGURACIÓN GENERAL ---
st.set_page_config(page_title="Skincare Bot 💖", layout="wide")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main {
        background-color: #F6F9FC;
        color: #333;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3 {
        color: #FF69B4;
    }
    .stButton button {
        background-color: #FFC0CB;
        color: black;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.title("💁‍♀️ Chatbot de Skincare")
st.write("Descubre cómo cuidar tu piel con información confiable, recomendaciones personalizadas y un toque de amor propio 💖")

# --- MENÚ DE OPCIONES ---
opciones = [
    "🏁 Test de tipo de piel",
    "💡 Más sobre tu tipo de piel",
    "📋 Rutinas recomendadas",
    "📦 Recomendación de productos",
    "😖 Problemas comunes de piel",
    "🧪 Ingredientes activos",
    "🚫 Mitos del skincare",
    "🆘 Ayuda general"
]

opcion = st.sidebar.selectbox("Selecciona una opción", opciones)

# --- LÓGICA POR SECCIÓN ---
if opcion == opciones[0]:
    st.subheader("🏁 Test de tipo de piel")
    st.markdown("Puedes hacer el test oficial aquí:")
    st.markdown("[👉 Haz el test de rutina en ISDIN](https://www.isdin.com/es/test-rutina-belleza/)")

elif opcion == opciones[1]:
    st.subheader("💡 Más información sobre tu tipo de piel")
    st.image("https://www.eucerin.com.co/_ui/skin/eucerin/images/skin-types/skin-types.jpg")
    st.markdown("""
    Según [Eucerin](https://www.eucerin.com.co/acerca-de-la-piel/conocimientos-basicos-sobre-la-piel/tipos-de-piel), los principales tipos de piel son:

    - **Normal**: Suave, sin imperfecciones ni grasa visible.
    - **Seca**: Tirantez, descamación y falta de brillo.
    - **Grasa**: Brillos, poros dilatados y tendencia a acné.
    - **Mixta**: Zonas grasas (frente, nariz, mentón) y zonas secas.

    👉 Conocer tu tipo de piel es clave para elegir los productos adecuados.
    """)

elif opcion == opciones[2]:
    st.subheader("📋 Rutinas recomendadas según tu tipo de piel")
    st.write("Mira este video que puede ayudarte a armar tu rutina:")
    st.video("https://www.youtube.com/watch?v=7cUWe_lz0og")
    with st.expander("Consejos rápidos según tipo de piel"):
        st.markdown("""
        - **Piel seca**: Usa limpiadores suaves y cremas con ácido hialurónico.
        - **Piel grasa**: Opta por geles no comedogénicos y exfoliaciones suaves.
        - **Piel mixta**: Equilibra usando productos específicos en cada zona.
        - **Piel sensible**: Usa productos sin fragancia y testados dermatológicamente.
        """)

elif opcion == opciones[3]:
    st.subheader("📦 Recomendación de productos")
    st.markdown("Consulta con tu dermatólogo antes de probar nuevos productos.")
    st.markdown("""
    🧴 Aquí algunos básicos según tipo de piel:
    - **Piel seca**: Hidratantes con ceramidas.
    - **Piel grasa**: Gel limpiador sin aceites.
    - **Piel mixta**: Hidratantes ligeros tipo gel.
    """)

elif opcion == opciones[4]:
    st.subheader("😖 Problemas comunes de piel")
    st.markdown("Fuente: [Vivo Labs](https://vivolabs.es/problemas-piel-mas-comunes/)")
    st.markdown("""
    - **Acné**: Relacionado con exceso de grasa, bacterias y cambios hormonales.
    - **Rosácea**: Enrojecimiento y sensibilidad.
    - **Hiperpigmentación**: Manchas oscuras por sol o acné.
    - **Piel deshidratada**: Falta de agua, no confundir con piel seca.
    """)

elif opcion == opciones[5]:
    st.subheader("🧪 Ingredientes activos")
    st.markdown("Fuente: [UYU Beauty](https://uyubeauty.com/blogs/dearuyubeauty/ingredientes-activos-de-skincare-como-elegir-los-ideales-para-ti)")
    st.markdown("""
    - **Ácido hialurónico**: Hidratación profunda y elasticidad.
    - **Niacinamida**: Controla grasa, calma rojeces y mejora textura.
    - **Retinol**: Estimula la renovación celular, ideal para piel madura.
    - **Vitamina C**: Ilumina, unifica el tono y reduce manchas.
    - **Ácido salicílico**: Excelente para piel grasa y acné.
    """)

elif opcion == opciones[6]:
    st.subheader("🚫 Mitos comunes del skincare")
    st.markdown("Inspirado en [Asian Beauty Essentials](https://asianbeautyessentials.com/blogs/es/9-mitos-del-cuidado-de-la-piel)")
    st.markdown("""
    ❌ *El limón aclara la piel* – Falso. Puede irritar o manchar.  
    ❌ *Si arde, es que funciona* – Puede ser señal de irritación.  
    ❌ *Solo las mujeres deben cuidarse la piel* – Todos tenemos piel.  
    ❌ *Los productos caros son mejores* – Lo importante es que sean adecuados para ti.  
    """)

elif opcion == opciones[7]:
    st.subheader("🆘 Ayuda general")
    st.markdown("""
    1️⃣ Haz el test para conocer tu tipo de piel.  
    2️⃣ Consulta los ingredientes ideales y tus problemas comunes.  
    3️⃣ Mira videos de rutinas personalizadas.  
    4️⃣ Si no sabes qué hacer, ¡esta guía te acompaña! 💖
    """)

# --- PIE DE PÁGINA ---
st.markdown("---")
st.markdown("Desarrollado por *Grecia García* 💻 con amor y cuidado para tu piel 💖")
