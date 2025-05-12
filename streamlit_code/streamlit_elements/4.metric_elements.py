import streamlit as st
import pandas as pd


######### Metrics elements ############

df = pd.DataFrame(
    {
        'Name': ['Prem', 'Shakila', 'Charlie', 'David'],
        'Age' : [30, 23, 37, 45],
        'Occupation': ['Engineer', 'IT', 'Artist', 'Chef']
    }
)

st.subheader('Metrics Elements')
st.metric(label='Total rows:', value=len(df)) ##
st.metric(label='Average Age:', value=round(df['Age'].mean(), 1)) ##
st.divider()
