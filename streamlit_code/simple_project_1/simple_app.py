import streamlit as st

if __name__=='__main__':
    st.title('Project 1')
    query = st.text_input('Ask me anything!!')
    if query:
        st.write(f'You have asked about {query}. Is that right?')