import csv
from datetime import datetime
import time
import random # Import the random module to select random elements from lists

# Example products for sale
products = [
    "smartphone", "laptop", "smartwatch", "headphones",
    "fitness tracker", "camera", "VR headset"
]

# Example questions a user might ask
user_questions = [
    "Can you tell me about the battery life?",
    "What kind of warranty does it come with?",
    "Are there any current discounts or offers?",
    "How does it compare to other products in the market?",
    "Can you provide details on the return policy?",
    "Does it come with any accessories?",
    "Is there a customer support service?",
    "What are the key features of this product?",
    "Is it compatible with other devices I own?",
    "What payment options are available?"
]


def generate_conversation(product):
    responses = [
        f"Hello! I see you're interested in our latest {product}. It's packed with features and offers.",
        "Thank you! The battery life is exceptional. With regular use, you can expect it to last up to 36 hours on a single charge.",
        "Absolutely! It comes with a one-year manufacturer warranty that covers any defects or issues you might encounter.",
        "Yes, we have a special offer where you get a 10% discount if you purchase today.",
        "Compared to other products, our {product} offers superior performance and a better user experience.",
        "We have a hassle-free return policy. If you're not satisfied, you can return the product within 15 days for a full refund.",
        "Yes, it comes with a range of accessories including a charger,earphones,stickers.",
        "Our customer support is available 24/7 to assist you with any questions .",
        "The key features includes a high-resolution display, a powerful processor, and compatible design.",
        "It's fully compatible with most other devices, including smartphones, tablets, and laptops.",
        "We offer multiple payment options including credit/debit cards, PayPal."
    ]

    # Select random user question/salesman with 50-75
    user_responses = [random.choice(user_questions) for _ in range(5)]
    salesman_responses = [random.choice(responses) for _ in range(5)]

    # conversation as a list of tuples (salesman response, user question, timestamp)
    conversation = [
        (salesman_responses[0], user_responses[0], datetime.now().isoformat()),#first salesman response, first user response
        (salesman_responses[1], user_responses[1], datetime.now().isoformat()),#second salesman response, second user response
        (salesman_responses[2], user_responses[2], datetime.now().isoformat()),
        (salesman_responses[3], user_responses[3], datetime.now().isoformat()),
        (salesman_responses[4], user_responses[4], datetime.now().isoformat())
    ]

    return conversation


# Function to save conversations to a CSV file
def save_to_csv(conversations, filename='conversations.csv'):
    with open(filename, mode='w', newline='') as file:
        #function is called to open a file specified by filename
#IN CSV files, setting newline='' ensures that newline characters are handled correctly, preventing extra blank lines
        #The with statement ensures that the file is closed automatically when the block inside with is exited,
        # Mode ('w'):opens the file for writing only If the file already exists, it removes its contents.
      
        writer = csv.writer(file)# Create a CSV writer object

        writer.writerow(["Salesman", "User", "TimeStamp"]) ## Create a CSV writer object

        # Iterate over each conversation and write each exchange to the CSV file
        for convo in conversations:
            for exchange in convo:
                writer.writerow(exchange)


if __name__ == "__main__":

    start_time = time.time()# Record the start time

    conversations = [generate_conversation(random.choice(products)) for _ in range(100)]
    # Generate 100 conversations by calling generate_conversation()


    save_to_csv(conversations)

    end_time = time.time()# Record the end time
  
    print(f"Data generated in {end_time - start_time} seconds")
