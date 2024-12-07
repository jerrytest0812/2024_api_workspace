import streamlit as st
import tools

sitenames:list[str]=tools.get_sitenames(excel_name='aqi.xlsx')
# add_selectbox = st.sidebar.selectbox(
#     "請選擇站點",
#     sitenames
# )

with st.sidebar:
    add_selectbox = st.selectbox(
        "請選擇站點",
        sitenames
    )

    st.title(f"{add_selectbox}")