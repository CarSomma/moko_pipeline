FROM python:3.11
WORKDIR /fast_app_dir
COPY requirements.txt /fast_app_dir/
COPY fast_app.py /fast_app_dir/
COPY generate_data.py /fast_app_dir/
COPY mongodb.py /fast_app_dir/
COPY monitorboard.py /fast_app_dir/
COPY product_data.yaml /fast_app_dir/
COPY assets/logo_nmf4.jpeg /fast_app_dir/assets/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
ENTRYPOINT [ "uvicorn", "fast_app:fast_appl", "--host"]
CMD [ "0.0.0.0" ]