import streamlit as st
import streamlit.components.v1 as c
from streamlit_elements import elements, mui, html


def set_title(varTitle, varSubtitle):
        st.markdown(f"""# {varTitle} <span style=color:#7ab3ba><font size=5>{varSubtitle}</font></span>""",unsafe_allow_html=True)
        st.divider()
       
def set_page_overview(varHeader, varText):
        st.markdown(f"#### {varHeader}")
        st.markdown(f"{varText}")
        st.divider()
