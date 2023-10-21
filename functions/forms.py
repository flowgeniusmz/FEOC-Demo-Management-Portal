import streamlit as st
from functions.callbacks import callback_form_demorequest
import datetime

def form_demorequest():
    sname = st.text_input("Name")
    semail = st.text_input("Email")
    sphone = st.text_input("Phone Number")
    sdate = st.date_input("Desired Date", format="MM/DD/YYYY", min_value=datetime.date(2023, 1,1))
    demo_form_submit = st.form_submit_button("Submit", type="primary", use_container_width=True, on_click=callback_form_demorequest(sname, semail, sphone, sdate))
    return demo_form_submit