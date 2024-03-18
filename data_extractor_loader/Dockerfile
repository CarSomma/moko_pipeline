FROM python:alpine
WORKDIR /el_job_dir_app
COPY requirements.txt /el_job_dir_app/
COPY el_job.py /el_job_dir_app/
COPY crontab_ /el_job_dir_app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
RUN crontab crontab_
ENTRYPOINT ["crond"]
CMD ["-f"]

