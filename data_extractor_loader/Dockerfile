FROM python:3.11
WORKDIR /eljob_dir
COPY requirements.txt /eljob_dir
COPY el_job.py /eljob_dir
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
ENTRYPOINT [ "python", "el_job.py"]
