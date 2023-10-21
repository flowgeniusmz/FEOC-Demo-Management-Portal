import streamlit as st
from  functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview
from streamlit_modal import Modal
import streamlit.components.v1 as components
import datetime
from functions.callbacks import callback_form_demorequest
from functions.forms import form_demorequest
from functions.benefits import benefits_container_website


st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    set_title("FEOC", "Home")

    container0 = st.container()
    with container0:
        st.markdown("#### Welcome to the Faulkner Emission Solutions Platform!")
        st.markdown("Introducing the **Faulkner Certificates** - our benchmark for emission offset. These certificates not only validate and track environmental contributions but, with the aid of state-of-the-art AI technology, ensure their authenticity, accuracy, and completeness. Jump in, explore, and be the change you wish to see in the world! We are thrilled to have you join our mission. Whether you're an Emitter, a Provider, a Purchaser, or simply a champion for the environment, this platform aims to unify our collective efforts towards a greener planet.")
        st.markdown("**Emitters**")
        st.markdown("""
                    ``` 
                    You are the linchpin of emission reduction, driving us towards a sustainable future. Your investments empower Providers to innovate and bring forth solutions that battle against emissions.
                    """)
        st.markdown("**Providers**")
        st.markdown("""```
                    With your groundbreaking solutions, you are lighting the path to a brighter, cleaner future. By collaborating with Emitters, we are making strides in environmental conservation.
                    """)
        st.markdown("**Purchasers**")
        st.markdown("""```
                    By choosing to back reduced emission products, you set a commendable standard. Every purchase you make takes us one step closer to a cleaner, better world.
                    """)
        modal = Modal("", key="mdlDemoRequest",)
        demo_modal = st.button("Request Demo", key="btnDemoRequest", type="primary", use_container_width=True)
        if demo_modal:
            modal.open()
        if modal.is_open():
            with modal.container():
                set_title("FEOC", "Demo Request Form")
                modal_container = st.container()
                with modal_container:
                    cc = st.columns(2)
                    with cc[0]:
                        set_page_overview("Instructions", "Submit the form to request a demo.")
                        st.markdown("#### Contact Information")
                        st.markdown("**Phone Number:** 111-222-3333")
                        st.markdown("**Email:** info@faulkercapital.com")
                        
                    with cc[1]:
                        demo_form = st.form("formdemo")
                        with demo_form:
                            #sname = st.text_input("Name")
                            #semail = st.text_input("Email")
                            #sphone = st.text_input("Phone Number")
                            #sdate = st.date_input("Desired Date", format="MM/DD/YYYY", min_value=datetime.date(2023, 1,1))
                            #demo_form_submit = st.form_submit_button("Submit", type="primary", use_container_width=True, on_click=callback_form_demorequest(sname, semail, sphone, sdate))
                            demo_form_submit = form_demorequest()
                            if demo_form_submit:
                                modal.close()
        #st.write(st.session_state.formDemoName)
                            
                #st.write("Some fancy text")
                #value = st.checkbox("Check me")
                #st.write(f"Checkbox checked: {value}")
        st.divider()
        benefits_container = benefits_container_website()
        st.divider()

    main_container = st.container()
    with main_container:
        col1, col2 = st.columns(2)
        with col1:
            container11 = st.container()
            with container11:
                st.markdown("#### Initiate New Certificate")
                exp11 = st.expander("New Certificate", expanded=True)
                with exp11:
                    st.write("**Instructions**")
                    st.write("Select this option to create a new FEOC providing the necessary information.")
                    st.button("Create New Certificate", key="btnNewCertificate", type="primary", use_container_width=True)
            container12 = st.container()
            with container12:
                st.markdown("#### Manage Users")
                exp12 = st.expander("Users", expanded=True)
                with exp12:
                    st.write("**Instructions**")
                    st.write("Select this option to manage any user or user-related item associated to an FEOC.")
                    st.button("Manage Users", key="btnManageUsers", type="primary", use_container_width=True)
        with col2:
            container21 = st.container()
            with container21:
                st.markdown("#### Manage Existing Certificate")
                exp21 = st.expander("Existing Certificate", expanded=True)
                with exp21:
                    st.write("**Instructions**")
                    st.write("Select this option to manage an existing FEOC and any related details, activity, or other items.")
                    st.button("Manage Existing Certificate", key="btnExistingCertificate", type="primary", use_container_width=True)
            container22 = st.container()
            with container22:
                st.markdown("#### Manage Audit History")
                exp22 = st.expander("Audit History", expanded=True)
                with exp22:
                    st.write("**Instructions**")
                    st.write("Select this option to manage and view the audit history for one or more FEOC.")
                    st.button("Manage Audit History", key="btnAuditHistory", type="primary", use_container_width=True)
