from json import loads  
from kafka import KafkaConsumer
import json
import time
import pandas as pd
import os
import sys

class consumer:
    def __init__(self):
        self.my_consumer_stream = KafkaConsumer(  
            'fake-heart-sensor',  
            bootstrap_servers = ['localhost : 9092'],  
            auto_offset_reset = 'latest',  
            enable_auto_commit = True,  
            group_id = 'my-group',  
            value_deserializer = lambda x : loads(x.decode('utf-8'))  
            )
        
    def stream(self):
        self.my_consumer_stream.pause()
        for message in self.my_consumer_stream:
            print(message.value)
            self.write_database(message.value)

    def create_dataset(self,data):
        df = pd.DataFrame.from_dict(data)
        df.to_csv('heart_sensor.csv', index=False)
    
    def write_database(self,new_data, filename='database.json'):
        try:
            with open(filename,'r+') as file:
                file_data = json.load(file)
                file_data["fake_heart_details"].append(new_data)
                file.seek(0)
                json.dump(file_data, file, indent = 4)
        except FileNotFoundError:
            with open(filename,'w') as file:
                file_data = {"fake_heart_details": [new_data]}
                json.dump(file_data, file, indent = 4)

    
    def dataset(self):

        try:
            with open("database.json",'r+') as file:  
                file_data = json.load(file)
                print("Total datapoints avilable:",len(file_data['fake_heart_details']))
                if len(file_data['fake_heart_details']) < 4000:
                    print("Its suggusted to run the stream method first, collect more data and then run create the dataset. 4000 datapoints would suffice")
                heart_rate =[]
                blood_pressure = []
                body_temperature = []
                oxygen_saturation = []
                respiratory_rate = []
                timestamp = []
                heart_rate_dict = {}

                for message in file_data['fake_heart_details']:
                    heart_rate.append(message['heart_rate'])
                    blood_pressure.append(message['blood_pressure'])
                    body_temperature.append(message['body_temperature'])
                    oxygen_saturation.append(message['oxygen_saturation'])
                    respiratory_rate.append(message['respiratory_rate'])
                    timestamp.append(message['timestamp'])

                heart_rate_dict['heart_rate'] = heart_rate
                heart_rate_dict['blood_pressure'] = blood_pressure
                heart_rate_dict['body_temperature'] = body_temperature
                heart_rate_dict['oxygen_saturation'] = oxygen_saturation
                heart_rate_dict['respiratory_rate'] = respiratory_rate
                heart_rate_dict['timestamp'] = timestamp
                self.create_dataset(heart_rate_dict)

        except FileNotFoundError:
            print("Database not found \n Its suggested to run the stream method first, collect the data and then run create the dataset")
        

if __name__ == "__main__":
    c = consumer()
    if 'dataset' in sys.argv[1]:
        c.dataset()
    elif 'stream' in sys.argv[1]:
        c.stream()
          



