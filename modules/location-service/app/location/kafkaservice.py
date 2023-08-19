# Importing necessary Kafka modules
from kafka import KafkaConsumer, KafkaProducer

class KafkaService:
    """
    Service class to interact with Kafka for sending and receiving messages.
    """
    
    def __init__(self, kafka_topic: str):
        """
        Initialize Kafka producer for a given topic.
        
        :param kafka_topic: The topic to send and receive messages from.
        """
        self.kafka_topic = kafka_topic
        # Configuring the producer to connect to a local Kafka instance
        self.producer = KafkaProducer(bootstrap_servers='localhost:9093')

    def send_message(self, message: str) -> None:
        """
        Send a message to the configured Kafka topic.
        
        :param message: The message to send to the topic.
        """
        self.producer.send(self.kafka_topic, value=message)

    def consume_message(self) -> None:
        """
        Consume messages from the configured Kafka topic and print them.
        
        Note: This function will continue to run and print messages until manually interrupted.
        """
        # Configuring the consumer to connect to a local Kafka instance
        consumer = KafkaConsumer(self.kafka_topic,
                                 bootstrap_servers=['localhost:9093'])
        
        for message in consumer:
            print(message)
