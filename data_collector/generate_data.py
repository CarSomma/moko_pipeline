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

"""         click    view  purchase
click        0.1     0.7     0.2
view         0.3     0.4     0.3
purchase     0.0     0.0     1.0
"""

TRANSITION_PROBABILITIES = {
    "click":[0.1, 0.7, 0.2],
    "view": [0.3, 0.4, 0.3],
    "purchase": [0.0, 0.0, 1.0]
}


async def stream_data():
    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        n_customers = random.randint(1,10)

        for _ in range(n_customers):
            category = faker.random_element(elements=product_data.keys())
            product = faker.random_element(elements=product_data[category])
            
            action = "view"
            actions = ["view"]
            max_user_action = random.randint(2,20)
            user_action = 1
            while user_action <= max_user_action:
                action = random.choices(population=["click", "view", "purchase"],weights=TRANSITION_PROBABILITIES[action])[0]
                actions.append(action)
                user_action += 1
                if action != "purchase":
                    continue
                else:
                    break

            data = {
                "timestamp": timestamp,
                "user_id": faker.uuid4(),
                "location":faker.location_on_land(),
                "action": actions,
                "nr_user_action": user_action,
                "product_name": product['name'],
                "category": category,
                "price": product['price'],  
                "quantity": None if "purchase" not in actions else faker.random_digit_not_null()
            }
            json_data_incoming = json.dumps(data, indent=4)
            logging.info("INCOMING DATA:\n\n %s", json_data_incoming)
            yield json_data_incoming
        delay = random.uniform(10, 50)
        await asyncio.sleep(delay)



if __name__ == "__main__":
    async def generate_data(num_samples=10):
        async for _ in stream_data():
            #json_data = json.dumps(data, indent=4)
            num_samples -= 1
            logging.info(f"NUMBER OF SAMPLE {num_samples}")
            if num_samples == 0:
                break
    
    asyncio.run(generate_data())

   
        

        




