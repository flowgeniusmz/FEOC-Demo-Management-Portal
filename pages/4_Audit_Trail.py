import streamlit as st
from  functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview


st.set_page_config(layout="wide")

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    set_title("FEOC", "Manage Audit Trail")
    set_page_overview("Viewing the Audit Trail", "The audit trail provides the ability for management to view any activity, interaction, log, etc. involved with a FEOC.")
