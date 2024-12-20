import streamlit as st

st.title("counter Exemple")
count= 0

increament = st.button('Increment 1')
if increament:
    count += 1

st.write(f'count {count}')