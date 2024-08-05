"""

Log files help us in debugging if something bad happens to our application
Log files also provides statistics of our application
To implement logging Python contains one in-built module called logging

Different logging levels in Python :- critical, error, warning, info, debug
If we don't set any log level then by default we will get WARNING and above levels added to our program
We can have a file which can store all the log messages written by our program
We can configure the filename, log-level and some more parameters set for our program by using the
    basicConfig() function of logging module
logging.basicConfig(filename="app.log", level=logging.INFO)

After creating the file we can use the below methods to write messages to the log files created
logging.debug(message)
logging.info(message)
logging.warning(message)
logging.error(message)
logging.critical(message)

"""

import logging
import os

log_format = "%(asctime)s :- %(name)s - %(levelname)s - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

log_file_name = "app.log"  # specifying the log file name
log_directory = "/Users/dharanikumar/PycharmProjects/PythonLearningProject/UserDefinedFiles"
# specifying the directory where the log file should be created

if not os.path.exists(log_directory):
    os.makedirs(log_directory)  # creating the directory if it doesn't exist

log_complete_path = os.path.join(  # getting the complete path and filename
    log_directory,
    log_file_name
)

# If we want to create the log file in the different folder then we can use the below syntax
logging.basicConfig(  # Configuring the basicConfig for logging
    level=logging.DEBUG,
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.FileHandler(log_complete_path)
    ]
)

# If we want to create the log file in the same folder then we can use the below syntax
# logging.basicConfig(filename='log.txt', level=logging.INFO)

logger = logging.getLogger("PythonLoggingExample")
# The above line is setting a name for our application so that it can get printed on logs

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

print(f"The log data is successfully written to the file")
