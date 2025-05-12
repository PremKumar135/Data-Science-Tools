import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime




## sidebar layout
st.sidebar.title('This is the sidebar')
st.sidebar.write('You can place elements like sliders, buttons and text here')
sidebar_input = st.sidebar.text_input('Enter something in the sidebar')
if sidebar_input:
    st.write(f'You have entered in the sidebar:{sidebar_input}')


## tabs layout
tab1, tab2, tab3 = st.tabs(['Tab1', 'Tab2', 'Tab3'])

with tab1:
    st.write('You are in tab1')

with tab2:
    st.write('You are in tab2')

with tab3:
    st.write('you are in tab3')



## columns layout
col1, col2 = st.columns(2)
with col1:
    st.header('column1')
    st.write('content for column2')

with col2 :
    st.header('column2')
    st.write('content for column2')



## container layout
with st.container(border=True):
    st.header('Container')
    st.write('content for container')



## empty placeholder --> dynamically change the content here
placeholder = st.empty()
placeholder.write('This is an empty placeholder, useful for dynamic content.')

if st.button('Update Placeholder'):
    placeholder.write('THe content of this placeholder has been updated')




## expander box
with st.expander('Expand for more details'):
    st.write('this is additional information that is hidden by default')
    st.write('You can use expanders to keep your interface cleaner')



## hover (tooltip)
st.write('Hover over this button for tooltip')
st.button('Button with tool tip', help='This is a tooltip or popover on hover')
























