import streamlit as st
import cloudinary.uploader
import os

# --- 1. CONFIGURACIÓN DE TUS LLAVES (CLOUDINARY) ---
cloudinary.config(
    cloud_name="dkrqrvxky", 
    api_key="411418886436225", 
    api_secret="7RoNJk_vklFFeK4LTC1kPtqRcFU", 
    secure=True
)

# --- 2. TU LINK DE COBRO REAL (MERCADO PAGO) ---
LINK_DE_PAGO_UNICO = "https://mpago.la/2dMaFNh"

# --- 3. DISEÑO DE LA MAZMORRA (CSS) ---
st.set_page_config(page_title="METAL MASTER PRO", page_icon="🤘")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #DAA520; }
    .stButton>button { 
        background-color: #660000; color: white; 
        border-radius: 10px; height: 3em; width: 100%;
        font-weight: bold; border: 2px solid #DAA520;
    }
    h1, h2, h3 { color: #8a0000; text-align: center; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: white; border: 1px solid #8a0000; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. BASE DE DATOS DE SUSCRIPTORES (SIMULADA) ---
# Después la conectaremos a tu Google Sheets para que sea 100% automático.
if 'lista_dioses' not in st.session_state:
    st.session_state.lista_dioses = ["tu_correo_admin@gmail.com"]

# --- 5. LÓGICA DE ACCESO ---
if 'acceso_concedido' not in st.session_state:
    st.session_state.acceso_concedido = False

# PANTALLA DE REGISTRO / PAGO
if not st.session_state.acceso_concedido:
    st.title("🤘 METAL MASTER PRO 🤘")
    st.subheader("🕯️ IDENTIFÍCATE O PAGA EL TRIBUTO 🕯️")
    
    correo = st.text_input("INTRODUCE TU CORREO PARA EL RITUAL:").lower().strip()
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("VERIFICAR ESTATUS"):
            if correo in st.session_state.lista_dioses:
                st.session_state.acceso_concedido = True
                st.session_state.usuario = correo
                st.rerun()
            else:
                st.error("❌ NO ESTÁS SUSCRITO O EL PAGO NO HA CAÍDO.")

    with col2:
        # BOTÓN QUE MANDA A TU LINK DE MERCADO PAGO
        st.link_button("🔥 PAGAR $200 (SUSCRIPCIÓN)", LINK_DE_PAGO_UNICO)

    st.markdown("---")
    st.info("💡 Instrucciones: \n1. Paga tu suscripción. \n2. Pon tu correo arriba. \n3. Dale a 'Verificar' para liberar la Maldad Pura.")

# PANTALLA DE TRABAJO (Solo si ya pagó)
else:
    st.title("🤘 FORJA DE ALMAS 🤘")
    st.write(f"Suscripción activa para: **{st.session_state.usuario}**")
    
    if st.button("CERRAR SESIÓN"):
        st.session_state.acceso_concedido = False
        st.rerun()

    st.markdown("---")
    
    archivo = st.file_uploader("SUBE AQUÍ TU CHINGADERA (Audio MP3)", type=["mp3"])
    
    if archivo:
        if st.button("EJECUTAR MALDAD PURA"):
            with st.spinner("🔥 TRANSFORMANDO MUGRE EN ORO..."):
                try:
                    # Guardar temporalmente
                    with open("temp.mp3", "wb") as f:
                        f.write(archivo.getbuffer())
                    
                    # Proceso Cloudinary (La IA que masteriza)
                    res = cloudinary.uploader.upload(
                        "temp.mp3", 
                        resource_type = "video",
                        transformation = [
                            {"effect": "improve:outdoor:80"},
                            {"effect": "volume:max"}
                        ]
                    )
                    
                    st.success("✅ ¡ORO PURO FORJADO!")
                    st.audio(res['secure_url'])
                    st.markdown(f"### [📥 DESCARGAR AQUÍ]({res['secure_url']})")
                
                except Exception as e:
                    st.error(f"⚠️ EL RITUAL FALLÓ: {e}")
              
