import streamlit as st

######### understanding without session state elements ############
counter = 0
st.write(f'counter value:{counter}')
if st.button('Increment counter'): ## -> with each click the counter has to increase by 1 but it wont becuase it reloads the script every time when the button is clicked
    counter +=1
    st.write(f'counter incremented to:{counter}')
else:
    st.write(f'counter stays at:{counter}') 


######### understanding with session state elements ############
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0

if st.button('increment counter'):
    st.session_state['counter'] +=1
    st.write(f'counter incremented to:{st.session_state['counter']}')

if st.button('reset'):
    st.session_state['counter'] = 0

st.write(f'current counter value:{st.session_state['counter']}')