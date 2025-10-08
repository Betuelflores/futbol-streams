import streamlit as st

# Configuración de la página
st.set_page_config(page_title="🦁👑 Fútbol Streams Premium", layout="wide")

# Título con estilo
st.markdown("""
    <h1 style='text-align: center; color: #ffcc00; font-size: 3em;'>⚽ Fútbol Streams Premium 🦁👑</h1>
""", unsafe_allow_html=True)

# Estilo CSS personalizado (fondo oscuro, verde futbolero)
st.markdown("""
    <style>
        .main { background-color: #1a1a1a; }
        .stApp { background-color: #1a1a1a; }
        .partido { background-color: #333; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 255, 0, 0.3); margin: 15px 0; }
        .logo { max-width: 150px; display: block; margin: 0 auto 10px; }
        h2 { color: #00ff00; text-align: center; }
        p { color: #ccc; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Contenido principal
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="partido">', unsafe_allow_html=True)
    st.image("https://i.ibb.co/M57Q0Kv/espn-premium2.png", caption="ESPN Premium", use_column_width=True)
    st.markdown('<h2>River Plate vs Boca Juniors</h2>', unsafe_allow_html=True)
    st.markdown('<p>Domingo 12/10, 20:00 - ESPN Premium</p>', unsafe_allow_html=True)
    
    # Reproductor de video (usa HTML embed para streams HLS/.m3u8)
    st.markdown("""
        <video controls style="width: 100%; border: 2px solid #00ff00; border-radius: 5px;">
            <source src="http://newultra.xyz:8080/25515850/8H3H73fbxwZ/544" type="application/x-mpegURL">
            Tu navegador no soporta video.
        </video>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="partido">', unsafe_allow_html=True)
    st.markdown('<h2>Argentina vs Brasil</h2>', unsafe_allow_html=True)
    st.markdown('<p>Martes 14/10, 21:00 - TNT Sports</p>', unsafe_allow_html=True)
    st.markdown('<p><a href="#" style="color: #00ff00; font-weight: bold;">Ver partido (próximamente)</a></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("<p style='text-align: center; color: #ccc;'>Exclusivo para el grupo 🦁👑 - Actualizado diariamente</p>", unsafe_allow_html=True)
