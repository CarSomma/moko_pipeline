# Use Python 3.11 as the base image
FROM python:alpine

# # Set the working directory inside the container
WORKDIR /el_job_dir_app

# Copy the requirements.txt file into the container at /el_job_dir_app
COPY requirements.txt /el_job_dir_app/

# Copy the el_job.py script into the container at /el_job_dir_app
COPY el_job.py /el_job_dir_app/

COPY crontab_ /el_job_dir_app/


RUN pip install --upgrade pip

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

RUN crontab crontab_
# Set the entrypoint to execute the el_job.py script
ENTRYPOINT ["crond"]
CMD ["-f"]

