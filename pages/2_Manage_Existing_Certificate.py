import streamlit as st
from  functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview


st.set_page_config(layout="wide")

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    set_title("FEOC", "Manage Existing Certificate")
    set_page_overview("How to Manage Existing FEOC's", "FEOC admin users have the ability to manage all FEOCs that have been created. They can edit key details and view the FEOC directly from the management portal.")
