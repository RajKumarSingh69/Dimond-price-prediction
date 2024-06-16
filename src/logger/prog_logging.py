import logging
import os
from datetime import datetime

# Define a fixed log file name
LOG_FILE = "app.log"

# Create a log directory path
log_path = os.path.join(os.getcwd(), "logs")

# Ensure the log directory exists
os.makedirs(log_path, exist_ok=True)

# Full path for the log file
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    filemode='a'  # Append mode
)

if __name__ == '__main__':
    logging.info("Here again, I am testing")
