import streamlit as st
import pandas as pd

# Cargar el CSV
@st.cache_data
def cargar_datos():
    return pd.read_csv("productos_chatbot_final.csv")

df = cargar_datos()

# Diccionario de información
info_piel = {
    "NORMAL": "Piel equilibrada: poros finos, textura suave y saludable.",
    "SECA": "Produce poco sebo, se siente tirante y puede descamarse. Necesita hidratación intensa.",
    "GRASA": "Produce mucho sebo, suele tener brillo y tendencia al acné. Usa productos oil-free.",
    "MIXTA": "Zona T grasa y mejillas secas. Requiere productos diferentes según la zona.",
    "SENSIBLE": "Se irrita fácilmente. Evita fragancias, alcohol y prefiere productos suaves."
}

st.set_page_config(page_title="Asistente de Skincare", page_icon="💆‍♀️")

# Variables de sesión
if "tipo_piel" not in st.session_state:
    st.session_state.tipo_piel = None
if "edad_categoria" not in st.session_state:
    st.session_state.edad_categoria = None

st.title("💆 Asistente Virtual de Skincare")
nombre = st.text_input("¿Cómo te llamas?")
edad = st.number_input("¿Cuántos años tienes?", min_value=10, max_value=100, step=1)

# Categorizar edad
if edad <= 18:
    st.session_state.edad_categoria = "adolescente"
elif edad <= 59:
    st.session_state.edad_categoria = "adulto"
else:
    st.session_state.edad_categoria = "adulto mayor"

st.markdown("---")

# Opciones del menú
opciones = [
    "¿Qué tipo de piel tengo? (Test)",
    "Saber más sobre mi tipo de piel",
    "Rutina de skincare según mi tipo",
    "Recomendación de productos",
    "Problemas comunes según mi piel",
    "Consejos según tipo de piel",
    "Ingredientes importantes",
    "Mitos del skincare",
    "Ayuda general"
]
opcion = st.selectbox("Selecciona una opción:", opciones)

# TEST
def test_tipo_piel():
    preguntas = [
        ("¿Cómo luce tu piel al natural?", ["Lisa y con brillo natural", "Opaca y seca", "Brilla toda la cara", "Zonas brillosas y zonas secas"]),
        ("¿Cómo son tus poros?", ["Finos", "Casi imperceptibles", "Grandes y visibles", "Grandes en zona T"]),
        ("¿Cómo se siente tu piel al tacto?", ["Suave", "Áspera", "Gruesa", "Mixta"]),
        ("¿Cómo se comporta tu piel durante el día?", ["Brilla un poco", "Se mantiene opaca", "Brilla mucho", "Brilla solo en zona T"]),
        ("¿Sueles tener granitos?", ["Muy pocos", "Raramente", "Frecuentes", "Según la zona"]),
        ("¿Cómo ves tu piel para tu edad?", ["Normal", "Arrugas marcadas", "Grasa", "Mixta con líneas finas"])
    ]
    puntajes = {"a": 0, "b": 0, "c": 0, "d": 0}
    letras = ["a", "b", "c", "d"]
    tipo_dict = {"a": "NORMAL", "b": "SECA", "c": "GRASA", "d": "MIXTA"}

    for idx, (pregunta, opciones) in enumerate(preguntas):
        r = st.radio(f"{idx+1}. {pregunta}", opciones, key=f"p{idx}")
        puntajes[letras[opciones.index(r)]] += 1

    if st.button("Mostrar resultado del test"):
        resultado = max(puntajes, key=puntajes.get)
        st.session_state.tipo_piel = tipo_dict[resultado]
        st.success(f"Tu tipo de piel es: {st.session_state.tipo_piel}")

# Mostrar contenido según opción seleccionada
if opcion == opciones[0]:
    test_tipo_piel()

elif opcion == opciones[1]:
    if st.session_state.tipo_piel:
        st.subheader(f"Más sobre tu tipo de piel ({st.session_state.tipo_piel}):")
        st.write(info_piel[st.session_state.tipo_piel])
    else:
        st.warning("Primero haz el test para conocer tu tipo de piel.")

elif opcion == opciones[2]:
    rutinas = {
        "SECA": "Limpieza suave, serum hidratante, crema nutritiva, protector solar.",
        "GRASA": "Gel limpiador, tónico equilibrante, hidratante ligera, protector solar matificante.",
        "MIXTA": "Productos ligeros en zona T, hidratación en mejillas.",
        "SENSIBLE": "Productos sin fragancia, calmantes como aloe y manzanilla, protector solar mineral.",
        "NORMAL": "Limpieza equilibrada, hidratación ligera, protector solar."
    }
    tipo = st.session_state.tipo_piel
    if tipo:
        st.subheader("Tu rutina recomendada:")
        st.write(rutinas.get(tipo, "No hay rutina disponible."))
    else:
        st.warning("Haz el test para conocer tu tipo de piel.")

elif opcion == opciones[3]:
    necesidad = st.text_input("¿Qué necesitas? (acné, hidratación, manchas, arrugas, etc.)").lower()
    tipo = st.session_state.tipo_piel
    edad_cat = st.session_state.edad_categoria

    if necesidad and tipo and edad_cat:
        resultados = df[
            df['tipo_piel'].str.lower().str.contains(tipo.lower()) &
            df['edad'].str.lower().str.contains(edad_cat) &
            df['necesidades'].str.lower().str.contains(necesidad)
        ]

        if resultados.empty:
            resultados = df[
                df['tipo_piel'].str.lower().str.contains(tipo.lower()) &
                df['necesidades'].str.lower().str.contains(necesidad)
            ]
        if resultados.empty:
            resultados = df[df['necesidades'].str.lower().str.contains(necesidad)]
        if resultados.empty:
            st.info("No se encontraron productos exactos. Aquí tienes algunos recomendados:")
            resultados = df.sample(n=min(3, len(df)))
        else:
            st.success("Recomendaciones para ti:")

        for _, row in resultados.iterrows():
            st.markdown(f"""
            **🧴 Producto:** {row['nombre']} ({row['marca']})  
            💸 **Precio:** {row['precio']}  
            🔗 [Ver producto]({row['enlace']})
            ---
            """)

    elif necesidad:
        st.warning("Haz primero el test y completa tu edad.")

elif opcion == opciones[4]:
    problemas = {
        "SECA": "Resequedad, descamación, líneas finas.",
        "GRASA": "Acné, puntos negros, poros dilatados.",
        "MIXTA": "Desequilibrio en zonas, acné en zona T.",
        "SENSIBLE": "Enrojecimiento, irritación, alergias.",
        "NORMAL": "Puede deshidratarse o irritarse con productos inadecuados."
    }
    tipo = st.session_state.tipo_piel
    if tipo:
        st.write(problemas.get(tipo, "Sin información."))
    else:
        st.warning("Realiza el test primero.")

elif opcion == opciones[5]:
    consejos = {
        "SECA": "Usa limpiadores suaves, evita alcohol, aplica humectantes ricos.",
        "GRASA": "Evita aceites pesados, elige productos oil-free.",
        "MIXTA": "Usa productos diferentes en cada zona si es necesario.",
        "SENSIBLE": "Prioriza ingredientes calmantes, sin perfume.",
        "NORMAL": "Mantén una rutina básica y no sobrecargues la piel."
    }
    tipo = st.session_state.tipo_piel
    if tipo:
        st.write(consejos.get(tipo, "Sin consejos."))
    else:
        st.warning("Haz primero el test para conocer tu tipo de piel.")

elif opcion == opciones[6]:
    st.subheader("🧪 Ingredientes importantes:")
    st.markdown("""
    - **Ácido hialurónico**: Hidratación profunda.  
    - **Niacinamida**: Controla grasa y mejora textura.  
    - **Retinol**: Antiarrugas y renovación celular.  
    - **Vitamina C**: Ilumina y reduce manchas.  
    """)

elif opcion == opciones[7]:
    st.subheader("🚫 Mitos comunes del skincare:")
    st.markdown("""
    ❌ El limón aclara la piel – Puede causar quemaduras.  
    ❌ Si arde, está funcionando – Probablemente te está irritando.  
    ❌ Solo las mujeres deben cuidarse la piel – ¡Todos debemos hacerlo!  
    """)

elif opcion == opciones[8]:
    st.subheader("🆘 Ayuda general:")
    st.markdown("""
    1️⃣ Haz el test para saber tu tipo de piel.  
    2️⃣ Consulta más información sobre tu tipo de piel.  
    3️⃣ Crea tu rutina y pide recomendaciones.  
    4️⃣ Si no sabes qué hacer, ¡sigue esta guía o habla con un dermatólogo/a! 💖
    """)
