import streamlit as st
from datetime import datetime

######### Form elements ############
min_date = datetime(1990,1,1)
max_date = datetime.now()

st.title('Creating Form')
form_dict = {'name':None,
            'height':None,
            'gender':None,
            'dob':None,
            'location':None
            }


with st.form(key='user_info_form'): ##
    form_dict['name'] = st.text_input('enter your name') ##
    form_dict['height'] = st.number_input('Enter your height in cms') ##
    form_dict['gender'] = st.selectbox('Gender', ['Male', 'Female']) ##
    form_dict['dob'] = st.date_input('enter your birthdate', min_value=min_date, max_value=max_date) ##
    form_dict['location'] = st.text_input('enter your location')

    submit_button = st.form_submit_button() ##
    if submit_button:
        print('after_submit')
        if any(form_dict.values()) is None:
            st.warning('Please fill in all the fields') ##
        else:
            st.balloons() ##
            for k,v in form_dict.items():
                st.write(f"{k}:{v}")


######### Advanced Form elements ############
min_date = datetime(1990,1,1)
max_date = datetime.now()
st.title('User info form')

with st.form(key='user_info_form', clear_on_submit=True):
    name = st.text_input('enter your name')
    birth_date = st.date_input('enter your birth date', min_value=min_date, max_value=max_date)
    
    if birth_date:
        age = max_date.year - birth_date.year
        if birth_date.month > max_date.month or (birth_date.month==max_date.month and birth_date.day>max_date.day):
            age -=1
        st.write(f'your calculate age is:{age} years') ## --> ideally it should be calculated and shown in the screen before the submit button
    
    submit_button = st.form_submit_button()
    if submit_button:
        if not name or not birth_date:
            st.warning('Please fill in all forms') ##
        else:
            st.success(f'Thank You, {name} and your age is {age}') ##
            st.balloons() ##