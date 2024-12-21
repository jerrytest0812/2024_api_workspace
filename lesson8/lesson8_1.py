import streamlit as st


if 'count' not in st.session_state:
    st.session_state.count=0


st.header(f'count { st.session_state.count}')
button_status = st.button('again', key='reset') #  key='reset' default in button
st.write(st.session_state)
if button_status:
    st.session_state.count += 1