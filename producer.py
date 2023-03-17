from time import sleep
import time 
import random 
from json import dumps  
from kafka import KafkaProducer
from faker import Faker
fake = Faker()  

my_producer = KafkaProducer(  
    bootstrap_servers = ['localhost:9092'],  
    value_serializer = lambda x:dumps(x).encode('utf-8')  
    )  

while True:
    heart_rate = random.randint(60, 100) # Random heart rate value between 60 and 100 bpm
    blood_pressure = round(random.uniform(80.0, 120.0), 2) # Random blood pressure value between 80.0 and 120.0 mmHg
    body_temperature = round(random.uniform(36.0, 38.0), 2) # Random body temperature value between 36.0 and 38.0 degrees Celsius
    oxygen_saturation = round(random.uniform(95.0, 100.0), 2) # Random oxygen saturation value between 95.0 and 100.0 percent
    respiratory_rate = random.randint(12, 20) # Random respiratory rate value between 12 and 20 breaths per minute
    timestamp = int(time.time() * 1000) # Current timestamp in milliseconds

    # Create a JSON payload with the heart rate data
    payload = {
        'heart_rate': heart_rate,
        'blood_pressure': blood_pressure,
        'body_temperature': body_temperature,
        'oxygen_saturation': oxygen_saturation,
        'respiratory_rate': respiratory_rate,
        'timestamp': timestamp
    }

    my_producer.send('fake-heart-sensor', value=payload) #send the data to topic fake-heart-sensor
    time.sleep(random.uniform(1, 5)) #data generated every 1 to 5 seconds
    