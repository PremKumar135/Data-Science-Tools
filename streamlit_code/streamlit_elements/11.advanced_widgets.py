import streamlit as st

## button with different key
st.button('OK')
st.button('OK', key='btn2')

## slider value
if 'slider_min' not in st.session_state:
    st.session_state.slider_min = 25

slider_value = st.slider("Slider", st.session_state.slider_min, 100)


## checkbox
if 'checkbox' not in st.session_state:
    st.session_state.checkbox = False

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show Input Field", value=st.session_state.checkbox, on_change=toggle_input)

if st.session_state.checkbox:
    user_input = st.text_input('Enter Something...')
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get('user_input', '')

st.write(f'user_input:{user_input}')