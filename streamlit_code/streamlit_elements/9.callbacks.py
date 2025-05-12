import streamlit as st


######### without callbacks ############
# if 'step' not in st.session_state:
#     st.session_state['step'] = 1

# if 'info' not in st.session_state:
#     st.session_state['info'] = {}

# if st.session_state.step == 1:
#     st.header("Part 1: Info")
#     name = st.text_input('Name', value=st.session_state.info.get('name', ''))

#     if st.button("Next"):
#         st.session_state.info['name']=name
#         st.session_state.step=2

    
# if st.session_state.step == 2:
#     st.header('Part 2: Review')
#     st.subheader('Please review this:')
#     st.write(f"**Name**: {st.session_state.info.get('name', '')}")

#     if st.button('Submit'):
#         st.success('Great!')
#         st.balloons()
#         st.session_state.info = {}

#     if st.button("Back"):
#         st.session_state.step=1


######### with callbacks ############
if 'step' not in st.session_state:
    st.session_state['step'] = 1

if 'info' not in st.session_state:
    st.session_state['info'] = {}


def goto_step2(name):  ## functions are callbacks and they execute before anything else
    st.session_state.info['name']=name
    st.session_state.step=2

def goto_step1():
    st.session_state.step=1

if st.session_state.step == 1:
    st.header("Part 1: Info")
    name = st.text_input('Name', value=st.session_state.info.get('name', ''))

    st.button("Next", on_click=goto_step2, args=(name,)) ## callback with on_click
        

    
if st.session_state.step == 2:
    st.header('Part 2: Review')
    st.subheader('Please review this:')
    st.write(f"**Name**: {st.session_state.info.get('name', '')}")

    if st.button('Submit'):
        st.success('Great!')
        st.balloons()
        st.session_state.info = {}

    st.button("Back", on_click=goto_step1)