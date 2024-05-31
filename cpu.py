import streamlit as st
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Display the current date and time in the Streamlit app
st.write("Current Date and Time:")
st.write("hello world")
st.write(current_time)
