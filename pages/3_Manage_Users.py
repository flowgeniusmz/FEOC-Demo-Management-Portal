import streamlit as st
from  functions.login import get_loginform
from functions.pagesetup import set_title, set_page_overview
from functions.supabase_queries import supabase_get_users
from functions.data_FEOC import get_FEOC_list


st.set_page_config(layout="wide")

if 'authenticated' not in st.session_state:
    get_loginform()
elif not st.session_state.authenticated:
    get_loginform()
else:
    set_title("FEOC", "Manage Users")
    set_page_overview("User Management Overview", "This section of the management portal allows admin users to view and manage FEOC users and access. They can assist in key capabilities such as password resets and adding or removing users from a FEOC.")
    dfUserList = supabase_get_users()
    dfFEOCList = get_FEOC_list()
    
    for row in dfUserList:
        dfUserList["Actions"] = True
        dfUserList["FEOC"] = "FEOC-000"
        dfUserList["URL"] = "https://feoc-demo.streamlit.app"
        

    
    st.markdown("#### Master User List")
    dfUserList_Editable = st.data_editor(dfUserList, use_container_width=True, num_rows="dynamic", key="dfEditedUserList", column_config={"URL": st.column_config.LinkColumn("Link"), "FEOC": st.column_config.SelectboxColumn("Certificate Assignment",options=dfFEOCList)})
    exp12 = st.expander("Changes", expanded=False)
    with exp12:
        st.write("Here's the session state:")
        st.write(st.session_state.dfEditedUserList)

    exp11 = st.expander("Non Editable DF", expanded=False)
    with exp11:    
        dfUserList_Display = st.dataframe(dfUserList, use_container_width=True)
    
