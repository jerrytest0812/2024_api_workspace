from tools import taipei
import streamlit as st

@st.dialog("網路出現狀況")
def vote(item):
    st.write(item)


try:
    youbike_data:list[dict] = taipei.get_youbikes()
except Exception as e:
    vote(e)
    st.write("稍後再試")
    st.stop()

st.table(youbike_data)