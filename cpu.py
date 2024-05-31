import streamlit as st
from streamlit_echarts import st_echarts
from datetime import datetime
import time

st.title("Current Time Gauge")

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    hours = now.hour
    minutes = now.minute
    seconds = now.second

    option = {
        "tooltip": {
            "formatter": "{a} <br/>{b} : {c}%",
        },
        "series": [
            {
                "name": "Hour",
                "type": "gauge",
                "min": 0,
                "max": 24,
                "splitNumber": 24,
                "axisLine": {
                    "lineStyle": {
                        "color": [[1, "#FF0000"]],
                        "width": 15,
                    }
                },
                "pointer": {
                    "length": "80%",
                    "width": 5,
                    "color": "auto"
                },
                "detail": {"formatter": "{value}h"},
                "data": [{"value": hours, "name": "Hour"}]
            },
            {
                "name": "Minute",
                "type": "gauge",
                "min": 0,
                "max": 60,
                "splitNumber": 12,
                "axisLine": {
                    "lineStyle": {
                        "color": [[1, "#00FF00"]],
                        "width": 15,
                    }
                },
                "pointer": {
                    "length": "80%",
                    "width": 5,
                    "color": "auto"
                },
                "detail": {"formatter": "{value}m"},
                "data": [{"value": minutes, "name": "Minute"}]
            },
            {
                "name": "Second",
                "type": "gauge",
                "min": 0,
                "max": 60,
                "splitNumber": 10,
                "axisLine": {
                    "lineStyle": {
                        "color": [[1, "#0000FF"]],
                        "width": 15,
                    }
                },
                "pointer": {
                    "length": "80%",
                    "width": 5,
                    "color": "auto"
                },
                "detail": {"formatter": "{value}s"},
                "data": [{"value": seconds, "name": "Second"}]
            }
        ]
    }

    st_echarts(option, height="500px")

    # Sleep for a second before updating the time
    time.sleep(1)
