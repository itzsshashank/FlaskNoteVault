import streamlit as st
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

# Define the Streamlit app
def main():
    st.title('My Note Taking App')
    if st.sidebar.button('Add Note'):
        note = st.text_input('Enter your note:')
        if len(note) < 1:
            st.error('Note is too short!')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            st.success('Note added!')

    notes = Note.query.filter_by(user_id=current_user.id).all()
    for note in notes:
        st.write(note.data)

if __name__ == '__main__':
    main()
