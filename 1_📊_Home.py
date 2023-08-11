import streamlit as st
from user import login
from common import set_page_container_style
from streamlit_extras.app_logo import add_logo

# --- Define page configuration ---
st.set_page_config(
    page_title='PT Wilian - FFB Procurement',
    page_icon='✍',
    initial_sidebar_state='auto',   #(collapsed, auto, expanded)
    layout='wide'
)

# --- Display Client Logo ---
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url('https://lmquartobistorage.blob.core.windows.net/pt-wilian-perkasa/PTWP_Logo.png');
                background-repeat: no-repeat;
                padding-top: 10px;
                background-position: 20px 20px;
            }
            # [data-testid="stSidebarNav"]::before {
            #     content: "FFB Procurement Application";
            #     margin-left: 10px;
            #     margin-top: 20px;
            #     font-size: 19px;
            #     position: relative;
            #     top: 100px;
            # }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()

# --- Form title ---
st.sidebar.title('FFB Procurement')



# Adding additional controls in the sidebar.
# Using object notation
add_selectbox = st.sidebar.selectbox(
    'How would you like to contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Using 'with' notation
with st.sidebar:
    add_radio = st.radio(
        'Choose a shipping method',
        ('Standard (5-15 days)', 'Express (2-5 days)')
    )



# --- Hide the Streamlit Menu Button and Trade Marks ---
hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)


# -- Declare containers --
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()


# -- The content of each container --
def show_main_page():
    with mainSection:
        # Page Title
        st.title('Main Page')


def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False


def show_logout_page():
    loginSection.empty()
    with logOutSection:
        st.button('Log Out', key='logout', on_click=LoggedOut_Clicked)


def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input(
                label='User ID', value='fpsadmin', placeholder='Enter your user name')
            password = st.text_input(
                label='Password', value='fpspass', placeholder='Enter password', type='password')
            st.button('Login', on_click=LoggedIn_Clicked,
                      args=(userName, password))





# -- If the 'Login' button being clicked, trigger to find the user in database --
def LoggedIn_Clicked(userName, password):
    # -- Call the login function inside user.py --
    if login(userName, password):
        st.session_state['loggedIn'] = True
        getUserKey()
    else:
        st.session_state['loggedIn'] = False
        st.error('Invalid user name or password')


with headerSection:
    st.title('FFB Procurement Application')

    # First run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page()
    else:
        if st.session_state['loggedIn']:
            show_logout_page()
            show_main_page()
        else:
            show_login_page()
