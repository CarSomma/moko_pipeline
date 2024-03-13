from get_data import stream_data
from fastapi import FastAPI 
from fastapi.responses import StreamingResponse
from contextlib import asynccontextmanager
import uvicorn
import logging
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import json
import asyncio

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Define a background task for continuous data insertion
async def background_insertion_task():
    logging.info("Starting background task for continuous data insertion")
    async for data_point in stream_data():
        try:
            # Insert data into MongoDB collection
            collection.insert_one(json.loads(data_point))
            logging.info("Data inserted into MongoDB")
        except Exception as e:
            # Handle any exceptions during insertion
            logging.error(f"Error inserting data into MongoDB: {e}")

# Define lifespan event handler to manage MongoDB connection and background task
@asynccontextmanager
async def lifespan(task=background_insertion_task()):
    asyncio.create_task(background_insertion_task())
    yield



# Integrate lifespan event handler with FastAPI application
fast_appl = FastAPI(lifespan=lifespan)







# # GET endpoint to retrieve hello world message
@fast_appl.get("/")
async def root():
    return {"message": "Hello World"}

@fast_appl.get("/fetch_data_from_mongo")
async def fetch_data_one_by_one():
    try:
        cursor = collection.find()  # Get cursor for iterating over documents
        return StreamingResponse(generate(cursor))
    except Exception as e:
        return {"error": f"An error occurred while fetching data: {e}"}

async def generate(cursor):
    for document in cursor:
        # Convert ObjectId to string for JSON serialization
        document["_id"] = str(document["_id"])
        yield json.dumps(document) + "\n"



if __name__ == "__main__":
   uvicorn.run(fast_appl)
