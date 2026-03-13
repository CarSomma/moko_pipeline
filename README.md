# Mock Pipeline 🪈

## Overview

This project is a data pipeline that automatically extracts data from the endpoint of a FastAPI service, normalizes the data, and loads it into a PostgreSQL database. Additionally, it includes service that performs real-time analytics using Dash and aggregates analytics. The pipeline consists of five main components:

1. **FastAPI Service**: Exposes an endpoint to generate fake data and stream it.
2. **MongoDB**: Stores the raw data streamed from the FastAPI service.
3. **ETL (Extract, Transform, Load) Job Service**: Extracts data from MongoDB via FastApi service, normalizes it, and loads it into PostgreSQL.
4. **PostgreSQL Database**: Stores the normalized data.
All components are containerized using Docker.
5. **Dashboard app with Dash**: Build Dashboards of aggregate analytics using Dash.


## Requirements

- Docker
- Python 3.11
- FastAPI
- MongoDB
- Dlt
- Dash

## Installation

1. Clone this repository:

```bash
git clone git@github.com:CarSomma/moko_pipeline.git
```

2. Build the Docker images and start the services in one go:

```bash
docker compose up --build
```

3. Access the FastAPI service:

```bash
http://localhost:8000/docs
```

4. Access the MongoDB database:

```bash
docker exec -it <name-mongobd-container> mongosh
show dbs
use <name-database>
show collections
db.<collection-name>.find()
```

## Usage

The FastAPI service automatically generates fake data upon startup and streams it to MongoDB. Additionally, a Dash app for real-time analytics is mounted to one of the FastAPI endpoint. The ETL job service extracts data from MongoDB using a GET request to the provided endpoint, normalizes it, and loads it into the PostgreSQL database.

### Access FastAPI Data Stream

You can access the data stream from the FastAPI service by sending a GET request to the endpoint `/fetch_data_from_mongo`.

Example:

```bash
curl http://localhost:8000/fetch_data_from_mongo
```

### Access PostgreSQL Normalized data

You can access the normalized data in PostgreSQL by accessing the postgresql container shell:

```bash
docker exec -it <name-postgres-container> psql -U <postgres-user> -d <postgres-database>
```
```sql
SELECT * from <schema>.<table_name>
LIMIT 10;
```
## Configuration

- FastAPI configurations can be modified in the `data_collector/fast_app.py` file.
- MongoDB configurations can be modified in the `docker-compose.yaml` file.
- PostgreSQL configurations can be modified in the docker-compose.yaml file.

## Folder Structure
```
Mock Pipeline 🪈
│
├── data_collector
│   ├── Dockerfile
│   ├── assets
│   │   └── logo_nmf4.jpeg
│   ├── fast_app.py
│   ├── generate_data.py
│   ├── mongodb.py
│   ├── monitorboard.py
│   ├── product_data.yaml
│   └── requirements.txt
│
├── data_extractor_loader
│   ├── Dockerfile
│   ├── crontab_
│   ├── el_job.py
│   └── requirements.txt
│
├── docker-compose.yaml
│
├── LICENSE
│
└── README.md
```

1. **data_collector**:
    - This directory contains files related to the data collection component of the pipeline.
    - **Dockerfile**: Contains instructions to build the Docker image for the data collector service.
    - **assets**: Directory containing assets used by the data collector service, such as images (e.g., logo_nmf4.jpeg).
    - **fast_app.py**: Python script defining the FastAPI service for generating fake data and streaming it.
    - **generate_data.py**: Python script for generating fake data.
    - **mongodb.py**: Python script for interacting with MongoDB.
    - **monitorboard.py**: Python script for real-time analytics using Dash.
    - **product_data.yaml**: YAML file containing product data.
    - **requirements.txt**: Text file listing dependencies required by the data collector service.


2. **data_extractor_loader**:
    - This directory contains files related to the ETL (Extract, Transform, Load) job service of the pipeline.
    - **Dockerfile**: Contains instructions to build the Docker image for the ETL job service.
    - **crontab_**: File containing cron jobs for scheduling tasks.
    - **el_job.py**: Python script defining the ETL job service for extracting data from MongoDB, transforming it (normalize it), and loading it into PostgreSQL.
    - **requirements.txt**: Text file listing dependencies required by the ETL job service.

3. **docker-compose.yaml**:
    - This file contains configurations for Docker Compose, defining the services, networks, and volumes.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements
This project utilizes the following libraries, frameworks, and tools:

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
[FastAPI Documentation](https://fastapi.tiangolo.com)
- **PyMongo**: A Python driver for MongoDB.
[PyMongo Documentation](https://pymongo.readthedocs.io/en/stable/)
- **Docker**: A platform for building, sharing, and running containerized applications.
[Docker Documentation](https://docs.docker.com)
- **Dlt**: is an open-source library that you can add to your Python scripts to load data from various and often messy data sources into well-structured, live datasets.
[Dlt documentation](https://dlthub.com/docs/intro)
- **Dash**: A productive Python framework for building web applications. Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. [Dash documentation](https://dash.plotly.com)


## Further Feature

Add Dashboard for
- some analytics
- some models
