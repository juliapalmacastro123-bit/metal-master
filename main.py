import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import librosa
import soundfile as sf
import io

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="METAL MASTER PRO", page_icon="🎸")

# ESTILO METALERO TECH
st.markdown("""
    <style>
    .main { background-color: #000000; color: #FFD700; }
    h1 { color: #FF0000; text-shadow: 3px 3px #000; font-family: 'Arial Black'; }
    .stButton>button { background-color: #FF0000; color: white; border-radius: 10px; font-weight: bold; width: 100%; height: 3.5em; border: 2px solid #FFD700; }
    .stTextInput>div>div>input { background-color: #1a1a1a; color: #FFD700; border: 1px solid #FF0000; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎸 METAL MASTER PRO")
st.write("### El Horno de la Maldad: Sonido de Estudio Profesional")

# --- ACCESO VIP (TU LLAVE MAESTRA) ---
vips = ["Julia Palma Castro 123@gmail.com"] 

# CLIENTES (Lista de prueba)
usuarios = {
    'cliente_ejemplo@mail.com': '2026-12-31',
    'erizo_de_prueba@mail.com': '2024-01-01'
}

# --- ZONA DE ACCESO ---
st.sidebar.header("💀 ACCESO AL ESTUDIO")
email_usuario = st.sidebar.text_input("Pon tu pinche correo:")

acceso_concedido = False

if email_usuario:
    if email_usuario in vips:
        st.sidebar.success("🤘 ¡QUÉ ONDA, JEFE! ACCESO TOTAL.")
        acceso_concedido = True
    elif email_usuario in usuarios:
        fecha_vencimiento = datetime.strptime(usuarios[email_usuario], '%Y-%m-%d')
        if datetime.now() <= fecha_vencimiento:
            st.sidebar.success(f"🔥 Activo hasta: {usuarios[email_usuario]}")
            acceso_concedido = True
        else:
            st.error("🚫 NO MAMES GÜEY, YA SE TE ACABÓ TU PUTO MES")
            st.subheader("Paga para seguir disfrutando esta mierda, no seas pinche vato erizo")
            st.markdown("[👉 **SOLTAR LA LANA AQUÍ ($200)**](https://mpago.la/2dMaFNh)")
    else:
        st.sidebar.warning("Ese correo ni existe. No seas codo y paga.")
        st.markdown("[👉 **REGISTRARME Y PAGAR ($200)**](https://mpago.la/2dMaFNh)")

# --- PROCESADOR DE AUDIO (EL PRESET DE LA MALDAD) ---
if acceso_concedido:
    st.write("---")
    st.write("#### ⚡ Sube tu rola culera:")
    uploaded_file = st.file_uploader("", type=['wav', 'mp3'])

    if uploaded_file:
        if st.button("🔥 PULIR CON EL PRESET DE LA MALDAD"):
            with st.spinner("Metiendo tecnología de Gojira y Megadeth..."):
                y, sr = librosa.load(uploaded_file)
                # EL PRESET: Brillo + Compresión Pro
                y_sharp = librosa.effects.preemphasis(y)
                y_final = np.clip(y_sharp * 2.2, -1.0, 1.0) 

                buffer = io.BytesIO()
                sf.write(buffer, y_final, sr, format='WAV')
                buffer.seek(0)

                st.success("✅ ¡PULIDO COMPLETO! Ya no suena a basura:")
                st.audio(buffer, format='audio/wav')
                st.download_button(label="📥 DESCARGAR MASTER PRO", data=buffer, file_name="master_metal_pro.wav", mime="audio/wav")

st.markdown("---")
st.caption("Metal Master Pro © 2026 - No se aceptan lloros de metaleros de cristal.")
        
