import streamlit as st


if 'count' not in st.session_state:
    st.session_state.count=1

def increment_counter(**kwargs):
    st.session_state.count += kwargs['first'] 
    st.session_state.count -= kwargs['second'] 

st.header(f'count { st.session_state.count}')
button_status = st.button('again',
                           key='reset',
                           help='+1+1+1',
                           on_click=increment_counter,
                           kwargs={'first':5,'second':3}) #  key='reset' default in button
st.write(st.session_state)