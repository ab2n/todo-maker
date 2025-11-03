import streamlit as st
import streamlit.components.v1 as components

# Initialise le texte
if "notes" not in st.session_state:
    st.session_state.notes = ""

# Affiche la textarea via un composant HTML pour récupérer le curseur
components.html(f"""
<textarea id="notes_area" rows="15" style="width:100%">{st.session_state.notes}</textarea>
<script>
const textarea = document.getElementById('notes_area');
textarea.addEventListener('input', () => {{
    window.parent.postMessage({{type: 'update_notes', value: textarea.value, cursor: textarea.selectionStart}}, '*')
}});
</script>
""", height=300)

# Liste des boutons
buttons = [
    {"label": "✅ Tâche", "tag": "@todo"},
    {"label": "📌 Décision", "tag": "@dec"},
    {"label": "👤 Personne", "tag": "@pers"}
]

cols = st.columns(len(buttons))
for i, btn in enumerate(buttons):
    if cols[i].button(btn["label"]):
        # Injection du tag à la position du curseur
        cursor = st.session_state.get("cursor_pos", len(st.session_state.notes))
        text = st.session_state.notes
        before = text[:cursor]
        after = text[cursor:]
        st.session_state.notes = before + " " + btn["tag"] + after

# Affichage stylisé
for line in st.session_state.notes.split("\n"):
    if "@todo" in line:
        st.markdown(f"✅ {line.replace('@todo','').strip()}")
    elif "@dec" in line:
        st.markdown(f"📌 {line.replace('@dec','').strip()}")
    elif "@pers" in line:
        st.markdown(f"👤 {line.replace('@pers','').strip()}")
    else:
        st.write(line)
