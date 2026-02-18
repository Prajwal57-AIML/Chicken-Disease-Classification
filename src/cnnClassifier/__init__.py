import os
import sys
import logging

# This is the format in which our log messages will appear.
# It includes time, log level (INFO, ERROR, etc.), module name, and the actual message.
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Creating a folder named 'logs' where all our log files will be stored.
log_dir = "logs"

# Building the full path for the log file inside the logs folder.
# The log file will be named 'running_logs.log'.
log_filepath = os.path.join(log_dir, "running_logs.log")

# If the 'logs' folder doesn't exist, this will create it.
# exist_ok=True ensures it won’t throw an error if the folder is already there.
os.makedirs(log_dir, exist_ok=True)

# Configuring the logging system for our project.
logging.basicConfig(
    level=logging.INFO,  # We are setting the minimum log level to INFO.
    format=logging_str,  # Applying the custom format defined above.

    # Handlers decide where the logs should be sent.
    handlers=[
        logging.FileHandler(log_filepath),      # This will save logs into the file.
        logging.StreamHandler(sys.stdout)       # This will print logs in the console.
    ]
)

# Creating a logger object with a custom name.
# We can use this 'logger' throughout the project to log messages.
logger = logging.getLogger("cnnClassifierLogger")
