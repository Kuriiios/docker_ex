import streamlit as st

st.title("📝 Page 0 : Saisie des données")

with st.form("form_donnees"):
    nom = st.text_input("Nom")
    age = st.number_input("Âge", 0, 100, 25)
    submit = st.form_submit_button("Enregistrer")

if submit:
    # On met à jour le session_state (partagé avec les autres fichiers)
    st.session_state['donnees_utilisateur'] = {"nom": nom, "age": age}
    st.success("Données sauvegardées en mémoire !")
