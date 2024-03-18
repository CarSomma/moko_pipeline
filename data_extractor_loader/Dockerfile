# Use the Python Alpine image as base
FROM python:alpine

# Set the working directory inside the container
WORKDIR /el_job_dir_app

# Copy requirements.txt and el_job.py to the working directory
COPY requirements.txt /el_job_dir_app/
COPY el_job.py /el_job_dir_app/

# Copy the crontab file to the working directory
COPY crontab_ /el_job_dir_app/

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Install crontab file
# the crontab command reads the contents of the crontab_ file 
# and installs the specified cron jobs into the cron scheduler of the container. 
RUN crontab crontab_

# Set the entrypoint for the container to run crond
ENTRYPOINT ["crond", "-f"]



