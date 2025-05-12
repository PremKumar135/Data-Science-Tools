import streamlit as st


st.write("hello world1234")
st.write({'key':'value'})
st.write(123)
st.write(True)
button = st.button('Press Here') ##
print(button)

# ######### text elements ##########
st.title('Super simple title') ##
st.header('This is a header') ##
st.subheader('This is a sub-header') ##
st.markdown('This is a **Markdown**') ##
st.caption('small caption') ##
st.write("hello world1234") ##

code_example = """
def greet(name):
    print(f'hello {name}')
"""
st.code(code_example, language='python') ##
st.divider()