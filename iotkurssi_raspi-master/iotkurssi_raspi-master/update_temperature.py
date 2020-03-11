import time
import requests

from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

def update_temperature(temperature):
    temperature_url = "http://ec2-3-88-139-151.compute-1.amazonaws.com/temperature"
    try:
        req_temperature = requests.post(temperature_url, json = {'temperature' : temperature})
        print(req_temperature.status_code)
        
    except requests.exceptions.MissingSchema:
        print("Invalid URL")
        
while True:
    temp = sensor.get_temperature()
    update_temperature(temp)
    time.sleep(5)