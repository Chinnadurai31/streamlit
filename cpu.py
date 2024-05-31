import streamlit as st
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
st.write("Current Date and Time:")
st.write("hello world")
st.write(current_time)
