# Fake-Heart-Sensor-Data-Using-Python-and-Kafka
# SETP 1: DOWNLOAD KAFKA

# Download and Setup Kafka on Windows and Linux

Kafka is a distributed streaming platform that allows you to publish and subscribe to streams of records. In this guide, we will provide links to download and set up Kafka on both Windows and Linux operating systems.

## Download Kafka

### Windows

You can download the latest version of Kafka for Windows from the [Apache Kafka website](https://kafka.apache.org/downloads).

### Linux

To download Kafka on Linux, open a terminal and run the following command:

wget https://apache.mirror.digitalpacific.com.au/kafka/3.1.0/kafka_2.13-3.1.0.tgz


This command will download the latest version of Kafka available at the time of writing this guide.

## Set Up Kafka

Once you have downloaded the Kafka binaries, follow the steps below to set up Kafka on your system.

### Windows

1. Extract the Kafka archive you downloaded to a directory of your choice.
2. Navigate to the Kafka directory and open the `config` folder.
3. Edit the `zookeeper.properties` file and replace the `dataDir` property with a directory path where you want to store ZooKeeper data.
4. Start ZooKeeper by running the following command from the Kafka directory: bin\windows\zookeeper-server-start.bat config\zookeeper.properties


5. Open a new command prompt window and navigate to the Kafka directory.
6. Edit the `server.properties` file and replace the `log.dirs` property with a directory path where you want to store Kafka logs.
7. Start Kafka by running the following command from the Kafka directory: bin\windows\kafka-server-start.bat config\server.properties


### Linux

1. Extract the Kafka archive you downloaded to a directory of your choice.
2. Navigate to the Kafka directory and open the `config` folder.
3. Edit the `zookeeper.properties` file and replace the `dataDir` property with a directory path where you want to store ZooKeeper data.
4. Start ZooKeeper by running the following command from the Kafka directory:bin/zookeeper-server-start.sh config/zookeeper.properties


5. Open a new terminal window and navigate to the Kafka directory.
6. Edit the `server.properties` file and replace the `log.dirs` property with a directory path where you want to store Kafka logs.
7. Start Kafka by running the following command from the Kafka directory:bin/kafka-server-start.sh config/server.properties

# STEP 2 : Running python script

### Run kafka server
### pip install -r requirements.txt


### How to use producer
1. go to terminal where the python code producer.py is and type `python producer.py`

### How to use consumer
#### Use consumer to run stream of fake heart data
1. go to terminal where the consumer.py is and type `python consumer.py stream`

#### Use consumer to create dataset of fake heart data
1. go to terminal where the consumer.py is and type `python consumer.py dataset`

