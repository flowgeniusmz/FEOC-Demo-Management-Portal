import streamlit as st
from  functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview


st.set_page_config(layout="wide")

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    set_title("FEOC", "Create New Certificate")
    set_page_overview("How to Create A New Certificate", "This section allows admin users to setup, create, and establish a new FEOC. Information related to the parties (emitter, provider, purchaser) and relevant project details will be provided. Once complete, the certificate will be established and live for users to access.")
