FROM ubunt:latest
RUN apt update -y  && apt install python3 && apt install python3-pip && pip install streamlit 
WORKDIR /app
COPY . /app
CMD [ "streamlit","run","/app/cpu.py" ]