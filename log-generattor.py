import logging
import random
import time
from faker import Faker

# Initialize the Faker generator
fake = Faker()

# Define the log levels
log_levels = ["INFO", "WARNING", "ERROR"]

# Configure the logging format
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)

while True:
    # Simulate a log entry with a log level and message
    log_level = random.choice(log_levels)
    log_message = fake.sentence()

    # Log the entry
    logger = logging.getLogger(__name__)
    getattr(logger, log_level.lower())(log_message)

    # Add a delay to control the log generation rate
    time.sleep(1)  # Adjust the delay as needed

