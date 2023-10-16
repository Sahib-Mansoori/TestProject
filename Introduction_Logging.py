import logging
import time
now = time.time()
logging.basicConfig(level=logging.DEBUG, #This will define the level of the logging, right now it is set to debug.
                    filename='Logs.txt', #Here we are, naming the file, which will store our logs. (I dont wanna create a file now)
                    format='%(asctime)s: %(levelname)s: %(message)s', #Here we are formatting how the logs will be written. Right now, its first time, then the level name and the message of the log.
                    datefmt='%d-%B-%Y %I:%M:%S %p') #Here we are formatting the date itself.
logging.debug('This is debug logging')
logging.info('This is info logging')
logging.warning('This is warning logging')
logging.error('This is an Error logging')
