# Basic logging setup:

# import logging
# logging.basicConfig(level=logging.INFO) # DEBUG, INFO, WARNING, ERROR, and CRITICAL
# logging.info('This is an informational message')

import logging

# Configure a more detailed format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

logging.info('Application started')