import streamlit as st

st.title('一元一次方程式')
st.title('Y = 2X - 1 ')

prompt = st.chat_input('請輸入X值:')
if prompt:
    st.write(prompt)
