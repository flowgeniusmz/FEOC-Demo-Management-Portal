import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd
from supabase import create_client, Client


def supabase_get_users():
    #Initialize Connection
    con = st.experimental_connection("supabase", type=SupabaseConnection)

    #Perform Query
    rows = con.query("*", table="users", ttl="10m").execute()
    data = rows.data

    dfUsers = pd.DataFrame(data)

    return dfUsers

def supabase_get_audit():
    #initialize connection
    conn_audit = st.experimental_connection("supabase", type=SupabaseConnection)

    #perform query
    rows_audit = conn_audit.query("*", table="auditlog", ttl="10m").execute()
    data_audit = rows_audit.data
    dfAudit = pd.DataFrame(data_audit)
    return dfAudit

### Alt using python library


@st.cache_resource
def init_connection():
    varURL = st.secrets.SUPABASE_URL
    varKey = st.secrets.SUPABASE_KEY
    newclient = create_client(supabase_url=varURL, supabase_key=varKey)
    return newclient

st.cache_data(ttl=600)
def run_query(varTable, varQuery):
    sClient = init_connection()
    sQuery = sClient.table(f"{varTable}").select(f"{varQuery}").execute()
    sData = sQuery.data
    sDF = pd.DataFrame(sQuery.data)
    return sData



    

#https://docs.streamlit.io/knowledge-base/tutorials/databases/supabase#copy-your-app-secrets-to-the-cloud
#https://docs.streamlit.io/knowledge-base/tutorials/databases/supabase#create-a-supabase-database
