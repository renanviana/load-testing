FROM python:3.9

COPY /src /src
WORKDIR /src

RUN python -m venv ./venv
RUN . venv/bin/activate
RUN pip install fastapi uvicorn
RUN pip freeze > requirements.txt
