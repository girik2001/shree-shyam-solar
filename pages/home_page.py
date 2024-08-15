import streamlit as st

def owner_login_button_clicked(username, password):
    if username==st.secrets.username and password==st.secrets.password:
        st.session_state.owner_logged_in = True

col1, col2, col3 = st.columns([1,5,1])
with col2:
    st.image('images/logo.jpg')

st.image('images/shree-shyam-solar-samarkan-big.png')

col1, col2 = st.columns([1,1])
with col1:
    st.button('Customer Enquiry', use_container_width=True, type='primary')
with col2:
    with st.popover('Owner Login', use_container_width=True):
        with st.container(border=False):
            col1, col2 = st.columns([1,2])
            with col1:
                st.write('''<p style='margin-top:33px; margin-bottom:0; font-size:20px'>Username</p>''', unsafe_allow_html=True)
            with col2:
                username = st.text_input('Username', key = 'login_username', placeholder='Username', label_visibility='hidden')
        with st.container(border=False):
            col1, col2 = st.columns([1,2])
            with col1:
                st.write('''<p style='margin-top:33px; margin-bottom:0; font-size:20px'>Password</p>''', unsafe_allow_html=True)
            with col2:    
                password = st.text_input('Password', type='password', key='login_password', placeholder='Password', label_visibility='hidden')
        with st.container(border=False):
            st.button('Login', type='secondary', use_container_width=True, on_click=owner_login_button_clicked, args=(username, password))