from pymongo import MongoClient
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

HOST = "0.0.0.0"#"mongo_container" # "0.0.0.0" #
PORT = 27017
# Initialize MongoDB connection
#client = MongoClient("mongodb://localhost:27017/")
client = MongoClient(host=HOST,port=PORT)
#db = client["my_stream_database"]
#collection = db["my_stream_collection"]
db = client["my_new_database"]
collection = db["my_new_collection"]

#actions = ["view","click","purchase"]
#action_filter = {"location": {"$elemMatch": {"$regex": "^Europe"}}}

# Define the aggregation pipeline
pipeline_count_actions = [
    {"$unwind": "$action"},  # Deconstructs the array field "action" to process each action separately
    {"$group": {"_id": "$action", "count": {"$sum": 1}}}  # Groups documents by action and counts occurrences
]

pipeline_category_total_revenue = [
    {
        "$group": {
            "_id": "$category",
            "total_revenue": {"$sum": {"$multiply": ["$price", "$quantity"]}}
        }
    },
    {
        "$sort": {"total_revenue": -1}
    }
]


def count_actions(collection=collection, pipeline=pipeline_count_actions):
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

def category_total_revenue(collection=collection, pipeline=pipeline_category_total_revenue):
    categories_total_revenue = collection.aggregate(pipeline)
    categories = []
    total_revenues = []
    for document in categories_total_revenue:
        category = document["_id"]
        total_revenue = document["total_revenue"]
        logging.info(f"Total revenue for category {category}: {total_revenue}")
        categories.append(category)
        total_revenues.append(total_revenue)

    
    return categories_total_revenue, categories, total_revenues

if __name__ == "__main__":
    # Execute the aggregation pipeline
    #result = collection.aggregate(pipeline)
    counts_actions, actions, counts = count_actions(collection,pipeline_count_actions)
    categories_total_revenue, categories, total_revenues = category_total_revenue(collection,pipeline_category_total_revenue)
    # print(jcounts_actions)
    print(actions,counts)
    print(categories,total_revenues)