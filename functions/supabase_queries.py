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



#https://docs.streamlit.io/knowledge-base/tutorials/databases/supabase#copy-your-app-secrets-to-the-cloud

