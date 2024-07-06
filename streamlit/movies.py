import streamlit as st
import pandas as pd
import numpy as np

# write the text in
st.write('# Welcome to Streamlit')

# load the dataframe and show it in streamlit
df = pd.read_csv('movies.csv')
st.write(df) 

#creating random data and show in bar_chart and line_chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)
st.line_chart(chart_data)