import streamlit as st
import pandas as pd


def load_audit_data():
    # Specify the relative path to the CSV file
    file_path = 'data/audit_log.csv'
    
    # Read the CSV file into a dataframe
    df = pd.read_csv(file_path)
    
    return df

df=load_audit_data()
print(df)
