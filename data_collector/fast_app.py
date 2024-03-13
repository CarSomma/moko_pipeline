from get_data import stream_data
from fastapi import FastAPI 
from fastapi.responses import StreamingResponse, JSONResponse
from contextlib import asynccontextmanager
import uvicorn
import logging
from pymongo import MongoClient
import json
import asyncio
from bson import json_util

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Initialize MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["my_stream_database"]
collection = db["my_stream_collection"]

# Define a background task for continuous data insertion
async def background_insertion_task():
    logging.info("STARTING BACKGROUND TASK FOR CONTINUOUS DATA INSERTION")
    async for data_point in stream_data():
        try:
            # Insert data into MongoDB collection
            collection.insert_one(json.loads(data_point))
            logging.info("DATA INSERTED IN MongoDB")
        except Exception as e:
            # Handle any exceptions during insertion
            logging.error(f"ERROR INSERTING DATA INTO MongoDB: {e}")

# Define lifespan event handler to manage MongoDB connection and background task
@asynccontextmanager
async def lifespan(task=background_insertion_task()):
    asyncio.create_task(background_insertion_task())
    yield



# Integrate lifespan event handler with FastAPI application
fast_appl = FastAPI(lifespan=lifespan,default_response_class=JSONResponse)


# GET endpoint to retrieve hello world message
@fast_appl.get("/")
async def root():
    return {"message": "Hello World"}


# # GET endpoint to fetch data from MongoDB
# @fast_appl.get("/fetch_data_from_mongo")
# async def fetch_data_one_by_one():
#     try:
#         cursor = collection.find()  # Get cursor for iterating over documents
#         return StreamingResponse(generate(cursor))
#     except Exception as e:
#         return {"error": f"An error occurred while fetching data: {e}"}

# # Generator to convert cursor to JSON and yield line by line
# async def generate(cursor):
#     for document in cursor:
#         # Convert ObjectId to string for JSON serialization
#         document["_id"] = str(document["_id"])
#         #yield json.dumps(document, indent=4) + ",\n"
#         #yield JSONResponse(content=jsonable_encoder(document))
#         #yield jsonable_encoder(document)
#         yield json_util.dumps(document,indent=4) + ',\n'

@fast_appl.get("/data")
async def fetch_data():
    async def _stream_data():
        cursor = collection.find()  # Assuming you have a MongoDB collection
        yield '['  # Start of the JSON array
        for i, document in enumerate(cursor):
            # Convert ObjectId to string for JSON serialization
            document["_id"] = str(document["_id"])
            if i == 0:
                yield json.dumps(document,indent=4)
            else:
                yield ', ' + json.dumps(document,indent=4)
        yield ']'  # End of the JSON array
                
    return StreamingResponse(_stream_data(), media_type='application/json')
    # async def _stream_data():
    #     cursor = collection.find()  # Assuming you have a MongoDB collection
    #     for _, document in enumerate(cursor):
    #         # Convert ObjectId to string for JSON serialization
    #         document["_id"] = str(document["_id"])
    #         yield json.dumps(document)
                
    # return StreamingResponse(_stream_data(), media_type='application/json')

if __name__ == "__main__":
   uvicorn.run(fast_appl)
