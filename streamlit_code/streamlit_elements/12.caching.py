import streamlit as st
import time


## caching
@st.cache_data(ttl=60)
def fetch_data():
    time.sleep(3) ## mimic the api calls delay
    return {'data': "This is cached data!"}

st.write('Fetching data...')
data = fetch_data()
st.write(data)


## cache resource

@st.cache_resource
def get_file_name():
    file = open('data/example.txt', 'a+') # open the file in append mode, which creates file if it doesnt exist
    return file


file_handler = get_file_name()

if st.button('write to File'):
    file_handler.write('New line of text\n')
    file_handler.flush()
    st.success("Wrote a new line to the file!")

if st.button('Read the file'):
    file_handler.seek(0)
    context = file_handler.read()
    st.text(context)

st.button('Close file', on_click=file_handler.close)
