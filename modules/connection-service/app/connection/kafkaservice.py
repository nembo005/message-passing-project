from kafka import KafkaConsumer, KafkaProducer

class KafkaUtility:
    """
    Utility class to interact with Kafka for producing and consuming messages.

    Attributes:
        kafka_topic_name (str): The Kafka topic associated with this utility instance.
        message_producer (KafkaProducer): Kafka producer instance for sending messages.
    """

    def __init__(self, kafka_topic_name: str):
        """
        Constructor to initialize the KafkaUtility instance.

        Args:
            kafka_topic_name (str): The Kafka topic name to be used for this instance.
        """
        self.kafka_topic_name = kafka_topic_name

        # Initialize Kafka producer with localhost as the bootstrap server
        self.message_producer = KafkaProducer(bootstrap_servers='localhost:9092')

    def publish_message(self, msg_content: str):
        """
        Publish a message to the Kafka topic associated with this instance.

        Args:
            msg_content (str): Content of the message to be published.
        """
        self.message_producer.send(self.kafka_topic_name, value=msg_content)

    def receive_message(self):
        """
        Receive and print messages from the Kafka topic associated with this instance.
        This method keeps listening indefinitely for new messages on the topic.
        """
        # Initialize Kafka consumer with localhost as the bootstrap server
        msg_consumer = KafkaConsumer(self.kafka_topic_name, bootstrap_servers=['localhost:9092'])

        # Continuously listen for and print messages
        for msg in msg_consumer:
            print(msg)
