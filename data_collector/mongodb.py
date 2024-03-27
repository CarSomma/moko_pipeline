from pymongo import MongoClient
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

HOST = "mongo_container" # "0.0.0.0" #
PORT = 27017
# Initialize MongoDB connection
#client = MongoClient("mongodb://localhost:27017/")
client = MongoClient(host=HOST,port=PORT)
db = client["my_stream_database"]
collection = db["my_stream_collection"]

actions = ["view","click","purchase"]
#action_filter = {"location": {"$elemMatch": {"$regex": "^Europe"}}}


def count_actions(collection=collection, actions=actions):
    counts_actions = {}
    counts = []
    for action in actions:
        action_filter = {"action": action}
        count = collection.count_documents(action_filter)
        logging.info(f"Count for action {action}: {count}")
        counts.append(count)
        counts_actions[action] = count

    jcounts_actions = dict(actions=counts_actions)
    return jcounts_actions, actions, counts

if __name__ == "__main__":
    jcounts_actions = count_actions(collection,actions)
    print(jcounts_actions)