import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.write("# Hello, World!")

st.markdown(
    """
## はじめに
本サイトは、簡単なツールを提供するためのサイトです。
簡単に作成できるので試験的にStreamlitを利用しています。
"""
)
