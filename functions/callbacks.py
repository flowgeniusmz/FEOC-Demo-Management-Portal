import streamlit as st


def callback_form_demorequest (varName, varEmail, varPhone, varDate):
    st.session_state.formDemoName = varName
    st.session_state.formDemoEmail = varEmail
    st.session_state.formDemoPhone = varPhone
    st.session_state.formDemoDate = varDate
    