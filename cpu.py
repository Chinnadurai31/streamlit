import streamlit as st
import psutil
import time
from streamlit_echarts import st_echarts

def main():
    st.sidebar.title("Metrics Dashboard")
    page = st.sidebar.radio("Go to", ["Home", "CPU Dashboard", "RAM Dashboard"])

    if page == "Home":
        show_home()
    elif page == "CPU Dashboard":
        show_cpu_dashboard()
    elif page == "RAM Dashboard":
        show_ram_dashboard()

def show_home():
    st.title("Home Page")
    st.write("Metrics monitoring")

def show_cpu_dashboard():
    st.title("CPU Percentage Dashboard")

    def get_cpu_usage():
        return psutil.cpu_percent(interval=1)

    def create_gauge_chart(value, name):
        option = {
            "tooltip": {
                "formatter": '{a} <br/>{b} : {c}%'
            },
            "series": [
                {
                    "name": name,
                    "type": 'gauge',
                    "detail": {"formatter": '{value}%'},
                    "data": [{"value": value, "name": name}]
                }
            ]
        }
        return option

    while True:
        cpu_usage = get_cpu_usage()
        gauge_chart = create_gauge_chart(cpu_usage, "CPU")
        st_echarts(gauge_chart)
        time.sleep(1)
        st.experimental_rerun()

def show_ram_dashboard():
    st.title("RAM Usage Dashboard")

    def get_ram_usage():
        ram = psutil.virtual_memory()
        return ram.percent

    def create_gauge_chart(value, name):
        option = {
            "tooltip": {
                "formatter": '{a} <br/>{b} : {c}%'
            },
            "series": [
                {
                    "name": name,
                    "type": 'gauge',
                    "detail": {"formatter": '{value}%'},
                    "data": [{"value": value, "name": name}]
                }
            ]
        }
        return option

    while True:
        ram_usage = get_ram_usage()
        gauge_chart = create_gauge_chart(ram_usage, "RAM")
        st_echarts(gauge_chart)
        time.sleep(1)
        st.experimental_rerun()


if __name__ == "__main__":
    main()
