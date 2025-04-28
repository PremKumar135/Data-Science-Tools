import streamlit as st

def main():
    st.set_page_config(page_title='Breast Cancer Predictor',
                        page_icon='👩🏻‍⚕️',
                        layout="wide",
                        initial_sidebar_state='expanded')

    st.write('hello-world')

if __name__=='__main__':
    main()
