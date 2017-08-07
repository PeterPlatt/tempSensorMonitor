import socket
import pymongo
import time
import Adafruit_DHT
import datetime
import logging
import sys
import os
import dbconfig
from urllib import quote_plus

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    filename='sensorPollMongo.log'
)

sensor = Adafruit_DHT.AM2302

pin = 18

HOSTNAME = socket.gethostname()

# Grab environment vars
DB_HOST = dbconfig.MONGO_DB_HOST
DB_PORT = dbconfig.MONGO_DB_PORT
DB_NAME = dbconfig.MONGO_DB_NAME
DB_USERNAME = dbconfig.MONGO_DB_USER_NAME
DB_PASSWORD = dbconfig.MONGO_DB_PASSWORD
DB_COLLECTION = dbconfig.MONGO_DB_STATS_COLLECTION
LOCATION = dbconfig.SENSOR_LOCATION

# Connection to DB
logging.info("Attempting db connection...")
from pymongo import MongoClient

uri = "mongodb://%s:%s@%s:%s/%s" % (
    quote_plus(DB_USERNAME), quote_plus(DB_PASSWORD), DB_HOST, DB_PORT, DB_NAME)

db = MongoClient(uri)
db = db[DB_NAME]
logging.info("Successful DB connection")

logging.info("Setting to collection :" + DB_COLLECTION)

temperatureStatsCollection = db[DB_COLLECTION]

# Read data from sensor and push to mongodb
logging.info("Attempting to read from sensor")
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
    # Put data in a mongo DB structure
    temperatureStats = {
        "temperature": temperature,
        "humidity": humidity,
        "location": LOCATION,
        "date": datetime.datetime.utcnow()
    }

    # Push data to mongo
    result = temperatureStatsCollection.insert(temperatureStats)

    logging.info("Successful sensor read (Temp: {:+.2f}, Humid: {:+.2f}) and insert into DB.".format(
        temperature, humidity))
