import streamlit as st
import random

# Inizializzazione delle variabili di sessione
if 'livello' not in st.session_state:
    st.session_state.livello = 1
if 'punteggio' not in st.session_state:
    st.session_state.punteggio = 0
if 'selezioni' not in st.session_state:
    st.session_state.selezioni = []
if 'regalo_misterioso' not in st.session_state:
    st.session_state.regalo_misterioso = None
if 'tentativi' not in st.session_state:
    st.session_state.tentativi = 3
if 'domanda_fatta' not in st.session_state:
    st.session_state.domanda_fatta = False

# Funzione per il livello 1
def livello1():
    st.title("🎅 Livello 1: Le renne di Babbo Natale")
    st.write("Babbo Natale ha battuto la testa e non si ricorda più i nomi delle sue renne. Aiutalo a scegliere tra i nomi!")
    st.write("Seleziona **3 nomi** tra quelli qui sotto che pensi siano le renne di Babbo Natale.")
    
    nomi = ["Cometa", "Fantaghirò", "Piccolo", "Fulmine", "Nessie", 
            "Gandalf", "Leila", "Cucciolo", "Ballerina", "Nagini"]
    corrette = ["Cometa", "Fulmine", "Ballerina"]

    for nome in nomi:
        if nome in st.session_state.selezioni:
            if st.button(f"🌟 {nome} 🌟", key=nome, disabled=True):
                pass
        else:
            if st.button(nome, key=nome, disabled=len(st.session_state.selezioni) >= 3):
                st.session_state.selezioni.append(nome)

    if len(st.session_state.selezioni) == 3:
        st.write("Hai selezionato i 3 nomi. Ora puoi verificare il punteggio.")
        if st.button("Verifica punteggio"):
            punteggio_round = sum([1 for nome in st.session_state.selezioni if nome in corrette])
            st.session_state.punteggio += punteggio_round
            st.write(f"Hai indovinato **{punteggio_round} su 3**. Il tuo punteggio totale è: **{st.session_state.punteggio} punti**.")
            st.session_state.livello = 2
            st.session_state.selezioni = []
            if st.button("Vai al livello successivo"):
                st.experimental_rerun()

# Funzione per il livello 2
def livello2():
    st.title("🎄 Livello 2: Quiz Natalizio")
    
    domande = [
        ("Come si chiama il 26 dicembre in Inghilterra?", 
         ["Boxing Day", "After-Christmas", "Clean Up Day", "Sinners Day"], 
         "Boxing Day"),
        ("'Glaedelig jul og et godt nytår' significa Buon Natale e Felice Anno Nuovo in quale lingua?", 
         ["Lussemburghese", "Norvegese", "Polacco", "Danese"], 
         "Danese"),
        ("In Francia mangiano un Buche Noel a Natale, cos'è?", 
         ["Una torta che sembra un tronco", "Una ciambella di Natale molto grande", 
          "Una zuppa con dentro il cioccolato", "Una torta a forma di albero di Natale"], 
         "Una torta che sembra un tronco"),
        ("Cosa portarono i tre Re Magi come regalo a Giuseppe e Maria?", 
         ["Oro, Argento e Bronzo", "Oro, incenso e mirra", "Oro, gemme e vino", "Oro, cammelli e pesce"], 
         "Oro, incenso e mirra"),
        ("Secondo gli europei, in quale paese vive Babbo Natale?", 
         ["Norvegia", "Spagna", "Svezia", "Finlandia"], 
         "Finlandia")
    ]

    if not st.session_state.domanda_fatta:
        st.session_state.domanda_corrente = random.choice(domande)
        st.session_state.domanda_fatta = True

    domanda, opzioni, risposta_corretta = st.session_state.domanda_corrente
    st.write(domanda)
    
    risposta = st.radio("Seleziona la tua risposta:", options=opzioni)
    
    if st.button("Conferma"):
        if risposta == risposta_corretta:
            st.success("🎉 Bravo! È la risposta giusta!")
            st.session_state.punteggio += 1
        else:
            st.error(f"❌ Mi spiace, la risposta giusta è: **{risposta_corretta}**")
        
        st.session_state.domanda_fatta = False
        st.session_state.livello = 3
        if st.button("Vai al livello successivo"):
            st.experimental_rerun()

# Funzione per il livello 3
def livello3():
    st.title("🎅 Livello 3: Indovina il Regalo di Natale! 🎁")
    st.write("Hai **3 tentativi** per indovinare il regalo misterioso. Buona fortuna!")
    
    regali = ["bambola", "trenino", "cioccolato", "videogioco", "libro", "puzzle", "orsacchiotto"]
    if not st.session_state.regalo_misterioso:
        st.session_state.regalo_misterioso = random.choice(regali)
    regalo_misterioso = st.session_state.regalo_misterioso
    st.write("Regali disponibili: ", ", ".join(regali))
    
    guess = st.text_input("Inserisci il tuo regalo:", "").strip().lower()
    
    if st.button("Prova a indovinare"):
        if guess == regalo_misterioso:
           punti = st.session_state.tentativi
           st.success(f"🎉 Complimenti! Hai indovinato! Il regalo misterioso era: **{regalo_misterioso.capitalize()}**")
           st.session_state.punteggio += punti
           st.session_state.livello = 4
           st.session_state.indovinato = True  # Indica che il regalo è stato indovinato
        else:
           st.session_state.tentativi -= 1
           if st.session_state.tentativi > 0:
             st.warning(f"❌ Non è quello il regalo! Hai ancora {st.session_state.tentativi} tentativi.")
           else:
             st.error(f"🎅 Oh no! Il regalo misterioso era: **{regalo_misterioso.capitalize()}**")
             st.session_state.livello = 4
             st.session_state.indovinato = False  # Indica che non ci sono più tentativi

# Mostra sempre il pulsante "Vai al punteggio finale" dopo un'azione di indovinare
    if st.session_state.livello == 4:
        if st.button("Vai al punteggio finale"):
            st.experimental_rerun()

# Funzione per mostrare il risultato finale
def mostra_risultato():
    st.title("🎉 Risultato Finale 🎉")
    st.write(f"Il tuo punteggio totale è: **{st.session_state.punteggio} punti su 7 punti**.")

    if st.session_state.punteggio <= 3:
        st.error("Hai bisogno di ripassare ancora un po' prima di festeggiare il Natale! A meno che tu non sia il Grinch!")
        st.video("https://www.youtube.com/watch?v=nytpYtLtHpE")
    elif 4 <= st.session_state.punteggio < 5:
        st.warning("Bravo! Sei pronto per festeggiare il Natale, ma puoi migliorare!")
        st.video("https://www.youtube.com/watch?v=xv-y0xhMqkI")
    elif 5 <= st.session_state.punteggio <= 7:
        st.success("Sei il re del Natale!")
        st.video("https://www.youtube.com/watch?v=8nMsY0_7FYA")

# Logica dei livelli
if st.session_state.livello == 1:
    livello1()
elif st.session_state.livello == 2:
    livello2()
elif st.session_state.livello == 3:
    livello3()
else:
    mostra_risultato()

