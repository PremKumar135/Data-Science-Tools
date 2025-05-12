import streamlit as st
import pandas as pd


######### data elements ############
st.subheader('DataFrame Elements')
df = pd.DataFrame(
    {
        'Name': ['Prem', 'Shakila', 'Charlie', 'David'],
        'Age' : [30, 23, 37, 45],
        'Occupation': ['Engineer', 'IT', 'Artist', 'Chef']
    }
)
st.dataframe(df) ##
st.divider()

st.header('Editable dataframe')
editable_df = st.data_editor(df) ##
print(editable_df)


st.subheader('Static Table')
st.table(df) ##
st.divider()