import streamlit as st
from  functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview
import extra_streamlit_components as stx


st.set_page_config(layout="wide")

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    set_title("FEOC", "Manage Audit Trail")
    set_page_overview("Viewing the Audit Trail", "The audit trail provides the ability for management to view any activity, interaction, log, etc. involved with a FEOC.")

    # Tab bar
    tab_data = [
        stx.TabBarItemData(id=1, title="Audit Log", description="List of all audit items"),
        stx.TabBarItemData(id=2, title="Audit Chat", description="Chat about audit items"),
        stx.TabBarItemData(id=3, title="Additional Audit", description="Additional audit items")
    ]
    chosen_id = stx.tab_bar(data=tab_data, default=1)
