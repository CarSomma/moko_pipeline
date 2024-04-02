from pymongo import MongoClient
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

HOST = "0.0.0.0" #"mongo_container" # "0.0.0.0" #
PORT = 27017
# Initialize MongoDB connection
#client = MongoClient("mongodb://localhost:27017/")
client = MongoClient(host=HOST,port=PORT)
# db = client["my_stream_database"]
# collection = db["my_stream_collection"]
db = client["my_new_database"]
collection = db["my_new_collection"]

#actions = ["view","click","purchase"]
#action_filter = {"location": {"$elemMatch": {"$regex": "^Europe"}}}

# Define the aggregation pipeline
pipeline = [
    {"$unwind": "$action"},  # Deconstructs the array field "action" to process each action separately
    {"$group": {"_id": "$action", "count": {"$sum": 1}}}  # Groups documents by action and counts occurrences
]

def count_actions(collection=collection, pipeline=pipeline):
    counts_actions = collection.aggregate(pipeline)
    counts = []
    actions = []
    for document in counts_actions:
        action = document["_id"]
        count = document["count"]
        logging.info(f"Count for action {action}: {count}")
        counts.append(count)
        actions.append(action)

    
    return counts_actions, actions, counts

if __name__ == "__main__":
    # Execute the aggregation pipeline
    #result = collection.aggregate(pipeline)
    counts_actions, actions, counts = count_actions(collection,pipeline)
    # print(jcounts_actions)
    print(actions)
    print(counts)