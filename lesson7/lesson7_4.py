import streamlit as st



st.title("counter Exemple")
if 'count' not in st.session_state:
    st.session_state['count']=0

increament = st.button('Increment 1')
if increament:
    st.session_state['count'] += 1

st.write(f'count { st.session_state['count']}')