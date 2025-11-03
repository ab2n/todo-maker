import streamlit as st

# Notes
notes = st.text_area("Tape tes notes ici", height=400, key="notes_area")

# Boutons avec labels clairs
cols = st.columns(3)
buttons = [
    {"label": "✅ Tâche", "tag": "@todo"},
    {"label": "📌 Décision", "tag": "@dec"},
    {"label": "👤 Personne", "tag": "@pers"}
]

for i, btn in enumerate(buttons):
    if cols[i].button(btn["label"]):
        # Ajoute le tag à la fin du texte
        notes += f" {btn['tag']}\n"
        st.session_state.notes_area = notes

# Affichage stylisé
for line in notes.split("\n"):
    if "@todo" in line:
        st.markdown(f"✅ {line.replace('@todo','').strip()}")
    elif "@dec" in line:
        st.markdown(f"📌 {line.replace('@dec','').strip()}")
    elif "@pers" in line:
        st.markdown(f"👤 {line.replace('@pers','').strip()}")
    else:
        st.write(line)
