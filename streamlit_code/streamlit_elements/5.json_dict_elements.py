import streamlit as st
import pandas as pd


######### json and dictionary elements ############
st.subheader('Json Elements')
sample_dict = {
        'Name': ['Prem', 'Shakila', 'Charlie', 'David'],
        'Age' : [30, 23, 37, 45],
        'Occupation': ['Engineer', 'IT', 'Artist', 'Chef']
    }
st.json(sample_dict) ##
st.divider()