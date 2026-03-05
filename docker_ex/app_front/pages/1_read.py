import streamlit as st

st.title("📊 Page 1 : Affichage")

if 'donnees_utilisateur' in st.session_state and st.session_state['donnees_utilisateur']:
    data = st.session_state['donnees_utilisateur']
    st.write(f"**Nom :** {data['nom']}")
    st.write(f"**Âge :** {data['age']} ans")
else:
    st.warning("⚠️ Aucune donnée trouvée. Allez en Page 0 d'abord.")
