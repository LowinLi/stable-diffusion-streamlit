import streamlit as st
import os

app_title = os.environ.get("APP_TITLE", "Streamlit，Stable Diffusion在线生图工具")
st.title(app_title)
body = """+ [文字转图片](./文字转图片)
+ [画廊](./画廊)
"""
st.markdown(body, unsafe_allow_html=False)
