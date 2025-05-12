import streamlit as st
import pandas as pd
import numpy as np


######### Chart elements ############
st.header('Chart Elements')
data = pd.DataFrame(np.random.randn(20, 3), columns =['A', 'B', 'C'])

st.subheader('Area Chart')
st.area_chart(data) ##

st.subheader('Bar chart')
st.bar_chart(data) ##

st.subheader('Line Chart')
st.line_chart(data) ##

st.subheader('Scatter Chart')
scatter_data =  pd.DataFrame({'x': np.random.randn (100),
                            'y': np.random.randn (100)
                            })
st.scatter_chart(scatter_data) ##

st.subheader('Map') 
map_data = pd.DataFrame(np.random.randn(100, 2) / [50, 50] + [37.76, -122.4], # Coordinates around SF
                        columns=['lat', 'lon']
                        )
st.map(map_data) ##

st.subheader("Matplotlib Pyplot Chart")
fig, ax = plt.subplots()
ax.plot(data['A'], label='A')
ax.plot(data['B'], label='B')
ax.plot(data['C'], label='C')
ax.set_title("Matplotlib Line Chart")
ax.legend()
st.pyplot(fig) ##