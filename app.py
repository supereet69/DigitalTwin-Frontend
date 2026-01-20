import streamlit as st

st.set_page_config(page_title="Leaching Digital Twin", layout="wide")

st.markdown("""
<style>
  .block-container { padding: 0rem 0rem 0rem 0rem !important; }
  header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=1200, scrolling=True)
