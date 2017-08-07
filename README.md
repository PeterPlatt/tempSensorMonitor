# Temperature  Sensor Monitor
Used for a Rashberry PI sensor. The goal is to setup a simple program that polls a sensor installed on a rasberry Pi

#Steps
This assumes the following 
 - Rasbian is installed on the Raspberry Pi
 - Adafruit AM2302 (wired DHT22) temperature-humidity sensor (ADA393) is installed on pin 18
 - A mongoDB instance is setup

1. Install Python 2.6/2.7
    - `sudo apt-get update`    
    - `sudo apt-get install build-essential python-dev`    
    - `sudo apt-get install python-pip`
1. Install Adafruit Python DHT Sensor Library 
    - `pip install Adafruit_Python_DHT`
1. Install PyMongo 
    - `pip install pymongo`
1. Set up dbconfig.py
    - variable name | Purpose | Notes
      |-------------|---------|------|
      |MONGO_DB_HOST|URL of host||
      |MONGO_DB_PORT|Mongo DB Port||
      |MONGO_DB_NAME|Mongo DB Name||
      |MONGO_DB_USER_NAME|Mongo UN||
      |MONGO_DB_PASSWORD|Mongo Password||
      |MONGO_DB_STATS_COLLECTION|Mongo Collection Name||
      |SENSOR_LOCATION| Location Of the Sensor|Ex: Basement|
1. Setup cron job to run sensor
    - Edit current Cron jobs    
      -`sudo crontab -e` 
    - Set Polling time 
      - Note the polling time should not be faster then every 2 seconds
      - `*/5 * * * * sudo python /home/pi/temperatureHumidSensor/sensorPoll.py`    
    

#Sources
1. [Adafruit Python DHT Github page](https://github.com/adafruit/Adafruit_Python_DHT)
1. [Rethinking temperature, sensors, and Raspberry Pi](https://rethinkdb.com/blog/temperature-sensors-and-a-side-of-pi)
1. [PyMongo Tutorial](http://api.mongodb.com/python/current/tutorial.html?_ga=2.268733686.600741048.1501972985-1185891143.1501972985)
1. [Adafruit AM2302 (WIRED DHT22) TEMPERATURE-HUMIDITY SENSOR page](https://www.adafruit.com/product/393)
