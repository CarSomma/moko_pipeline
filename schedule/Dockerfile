FROM python:3.11-slim

WORKDIR /scheduler_app

COPY requirements.txt /scheduler_app/
COPY scheduler.py /scheduler_app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --trusted-host pypi.org -r requirements.txt

ENTRYPOINT [ "python", "scheduler.py" ]