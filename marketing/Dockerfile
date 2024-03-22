FROM python:3.11-alpine
WORKDIR /dash_app
COPY build_dashboard.py /dash_app/
COPY requirements.txt /dash_app/
COPY assets/logo_nmf4.jpeg /dash_app/assets/
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
ENTRYPOINT [ "gunicorn", "--bind", ":8000", "--workers", "3", "build_dashboard:server", "--timeout","600"]