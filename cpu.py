import streamlit as st
import pandas as pd
import requests

# Function to check login
def check_login(username, password):
    # Replace with your own login logic, e.g., checking against a database
    return username == "admin" and password == "password"

# Function to fetch data from the API
def fetch_data(isci, date):
    url = f"https://pvs.adcuratio.net:9000/get_data?requested_isci={isci}&date={date}"
    headers = {
        'accept': 'application/json',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None

# Function to format column names
def format_column_name(column_name):
    # Split column name by underscore and capitalize each word
    formatted_name = ' '.join([word.capitalize() for word in column_name.split('_')])
    return f"<b>{formatted_name}</b>"

# Configure the page to use the full width of the browser
st.set_page_config(layout="wide")

# Initialize session state variables
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'visibility' not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

if not st.session_state.logged_in:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_login(username, password):
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")
else:
    # Set page title
    st.title("Precision Verification System")

    # Display Last 1 hour and Filter icon in line 2
    st.write("⏰ Last 1 hour  🔍 Filter")

    # CSS styling for columns and messages
    st.markdown("""
    <style>
        .main > div {
            max-width: 90% !important;
            padding-left: 5% !important;
            padding-right: 5% !important;
        }
        .grey-box {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #007bff !important;
            color: white !important;
            border-radius: 10px !important;
            border: none !important;
            padding: 10px 20px !important;
            cursor: pointer !important;
        }
        .grey-background input {
            background-color: #f0f0f0 !important;
            border: none !important;
        }
        .message-box {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 10px;
            margin-top: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th {
            background-color: #f0f0f0;
            font-weight: bold;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #ddd;
        }
    </style>
    """, unsafe_allow_html=True)

    # Columns with grey background for the second column
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown('<div class="grey-background">', unsafe_allow_html=True)
        isci_name = st.text_input(
            "ISCI Name",
            key="isci_name",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="grey-background">', unsafe_allow_html=True)
        broadcast_date = st.text_input(
            "Broadcast Date",
            key="broadcast_date",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="grey-background">', unsafe_allow_html=True)
        st.text_input(
            "Input 3",
            key="input3",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="grey-background">', unsafe_allow_html=True)
        st.text_input(
            "Input 4",
            key="input4",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col5:
        st.markdown('<div class="grey-background">', unsafe_allow_html=True)
        if st.button('Search', key='search_button_col5'):
            # Ensure there's only one search button
            st.session_state.search_button_pressed = True
        st.markdown('</div>', unsafe_allow_html=True)

    # Perform search action
    if 'search_button_pressed' in st.session_state and st.session_state.search_button_pressed:
        if isci_name and broadcast_date:
            fetched_data = fetch_data(isci_name, broadcast_date)
            if fetched_data['data']:
                df = pd.DataFrame.from_dict(fetched_data['data'])
                print(df)
                df['separation'] = df['separation'].apply(lambda x: ','.join([str(i) for i in x]))
                print(df)
                # Format column names
                df.columns = [format_column_name(col) for col in df.columns]
                # Convert DataFrame to HTML table
                st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)
            else:
                st.markdown('<div class="message-box">', unsafe_allow_html=True)
                st.markdown(f'**No data found for ISCI: {isci_name} on {broadcast_date}**')
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="message-box">', unsafe_allow_html=True)
            st.markdown('**Please enter ISCI Name and Broadcast Date**')
            st.markdown('</div>', unsafe_allow_html=True)

        # Reset search button state
        st.session_state.search_button_pressed = False
adcad
