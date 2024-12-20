import streamlit as st
import random

# Configurazione della pagina
st.set_page_config(page_title="Gioco di Natale", page_icon="🎄", layout="centered")

# Titolo e descrizione
st.title("🎅 Indovina il Regalo di Natale! 🎁")
st.write("Benvenuto al gioco 'Indovina il Regalo di Natale'! Hai **3 tentativi** per indovinare il regalo misterioso. Buona fortuna! 🎄")

# Lista di regali
regali = ["bambola", "trenino", "cioccolato", "videogioco", "libro", "puzzle", "orsacchiotto", "scatola di Lego"]
regalo_misterioso = st.session_state.get("regalo_misterioso", random.choice(regali))

# Visualizzare i regali disponibili
st.write("Regali disponibili: ", ", ".join(regali))

# Tentativi rimanenti
if "tentativi" not in st.session_state:
    st.session_state.tentativi = 3

# Input dell'utente
guess = st.text_input("Inserisci il tuo regalo:", "").strip().lower()

# Verifica del regalo
if st.button("Prova a indovinare"):
    if guess == regalo_misterioso:
        st.success(f"🎉 Complimenti! Hai indovinato! Il regalo misterioso era: **{regalo_misterioso.capitalize()}**")
        st.balloons()
        st.session_state.tentativi = 3  # Resetta i tentativi
        st.session_state.regalo_misterioso = random.choice(regali)  # Cambia regalo
    else:
        st.session_state.tentativi -= 1
        if st.session_state.tentativi > 0:
            st.warning(f"❌ Non è quello il regalo! Hai ancora {st.session_state.tentativi} tentativi.")
        else:
            st.error(f"🎅 Oh no! Hai esaurito i tentativi. Il regalo misterioso era: **{regalo_misterioso.capitalize()}**")
            st.session_state.tentativi = 3  # Resetta i tentativi
            st.session_state.regalo_misterioso = random.choice(regali)  # Cambia regalo

# Footer
st.write("Buon Natale e buon divertimento! 🎄🎁")