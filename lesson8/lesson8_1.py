import streamlit as st


if 'count' not in st.session_state:
    st.session_state.count=1

def increment_counter(*args):
    st.session_state.count += args[0] 
    st.session_state.count -= args[1]

st.header(f'count { st.session_state.count}')
button_status = st.button('again', key='reset',help='+1+1+1',on_click=increment_counter,args=(5,3)) #  key='reset' default in button
st.write(st.session_state)