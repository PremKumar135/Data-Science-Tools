import streamlit as st

st.title('My Awesome app')

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle('Toggle')
    cols[1].text_area('Enter the area')


@st.fragment()
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0].checkbox('Filter')
    new_cols[1].file_uploader('Upload image')
    new_cols[2].selectbox('choose option', ['Option1', 'Option2', 'Option3'])
    new_cols[3].slider('select value',0,100,50)
    new_cols[4].text_input('enter text')


toggle_and_text()
cols = st.columns(2)
cols[0].selectbox('select', [1,2,3], None)
cols[1].button('Update')
filter_and_file()