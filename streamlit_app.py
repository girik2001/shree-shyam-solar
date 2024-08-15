import streamlit as st

if 'owner_logged_in' not in st.session_state:
    st.session_state['owner_logged_in'] = False

if 'page' not in st.session_state:
    st.session_state['page'] = 'home'


home_page = st.Page(page='pages/home_page.py', title='Home')
customer_enquiry_page = st.Page(page='pages/customer_enquiry_page.py', title='Enquire')
owner_portal = st.Page(page='pages/owner_portal.py', title='Shree Shyam Solar')


if st.session_state.owner_logged_in!=True and st.session_state.page=='home':
    pg = st.navigation([home_page])
if st.session_state.owner_logged_in:
    pg = st.navigation([owner_portal])
if st.session_state.page=='customer-enquiry':
    pg = st.navigation([customer_enquiry_page])

pg.run()