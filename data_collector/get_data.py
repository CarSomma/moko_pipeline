# Package to generate fake data
from faker import Faker
import logging
import random 
import json
import yaml
from datetime import datetime
import asyncio


# import product_data.yaml
with open(file="product_data.yaml", mode='r') as file:
    product_data = yaml.safe_load(file)

# Instantiate Faker object
faker = Faker()
# Configure logging with custom format
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')



async def stream_data():
    while True:
        category = faker.random_element(elements=product_data.keys())
        product = faker.random_element(elements=product_data[category])
        action = random.choices(population=["click", "view", "purchase"],weights=[.30,.40,.30])[0]
        
        data = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "user_id": faker.uuid4(),
            "location":faker.location_on_land(),
            "action": action ,
            "product_name": product['name'],
            "category": category,
            "price": product['price'],  
            "quantity": None if action in ["click", "view"] else faker.random_digit_not_null()
        }
        json_data_incoming = json.dumps(data, indent=4)
        logging.info("INCOMING DATA:\n\n %s", json_data_incoming)
        yield json_data_incoming
        delay = random.uniform(10, 50)
        await asyncio.sleep(delay)



if __name__ == "__main__":
    stream_data = stream_data()
    for _ in range(10):  # Generate 10 data points for demonstration
        json_data = json.dumps(next(stream_data), indent=4)
        

        




