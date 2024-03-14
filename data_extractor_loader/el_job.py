import dlt
from dlt.sources.helpers import requests
from dlt.pipeline.exceptions import PipelineStepFailed
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

HOST = "fastapi_app"

@dlt.resource(write_disposition="append", columns={"location": {"data_type": "complex"}})
def fastapi_resource():#api_secret_key=dlt.secrets.value):
    url = f"http://{HOST}:8000/fetch_data_from_mongo"
    response = requests.get(url)#, params=params)
    response.raise_for_status()
    yield response.json()


if __name__ == '__main__':
    
    # configure the pipeline with your destination details
    pipeline = dlt.pipeline(
        pipeline_name='fastapi',
        destination='duckdb',
        dataset_name='fastapi_data',
    )

    # print the data yielded from resource
    data = list(fastapi_resource())
    #print(data)

    # run the pipeline 
    try:
        load_info = pipeline.run(fastapi_resource())
        logging.info(f"PIPELINE INFO:\n{load_info}")
    except PipelineStepFailed as step_failed:
        logging.debug(f"WE FAILED AT THE STEP: {step_failed.step} WITH STEP INFO {step_failed.step_info}")
        raise
    

    
    