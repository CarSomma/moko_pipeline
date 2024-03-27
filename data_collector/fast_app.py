from generate_data import stream_data
from fastapi import FastAPI 
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.responses import StreamingResponse
from contextlib import asynccontextmanager
import uvicorn
import logging
from pymongo import MongoClient
import json
import asyncio
from monitorboard import server_monitor


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

HOST = "mongo_container"
PORT = 27017
# Initialize MongoDB connection
#client = MongoClient("mongodb://localhost:27017/")
client = MongoClient(host=HOST,port=PORT)
db = client["my_stream_database"]
collection = db["my_stream_collection"]

# Define a background task for continuous data insertion
async def background_insertion_task():
    logging.info("STARTING BACKGROUND TASK FOR CONTINUOUS DATA INSERTION IN MONGO")
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
fast_appl = FastAPI(lifespan=lifespan)

fast_appl.mount("/real-time-monitoring", WSGIMiddleware(server_monitor))


# GET endpoint to retrieve hello world message
@fast_appl.get("/")
async def root():
    return {"message": "Hello World"}


# GET endpoint to fetch data from MongoDB
@fast_appl.get("/fetch_data_from_mongo")
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
    

if __name__ == "__main__":
   uvicorn.run(fast_appl, host="0.0.0.0")
