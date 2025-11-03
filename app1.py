import streamlit as st

# Zone de saisie
notes = st.text_area("Tape tes notes ici", height=400)

# Traitement des lignes
lines = notes.split("\n")
for line in lines:
    if line.startswith("@todo"):
        st.markdown(f"✅ **Tâche:** {line[5:].strip()}")
    elif line.startswith("@dec"):
        st.markdown(f"📌 **Décision:** {line[4:].strip()}")
    elif line.startswith("@pers"):
        st.markdown(f"👤 **Assigné à:** {line[5:].strip()}")
    else:
        st.write(line)
