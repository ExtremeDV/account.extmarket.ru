import json
from django.core.serializers.json import DjangoJSONEncoder

from confluent_kafka import KafkaProducer
from confluent_kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['accountextmarketru-kafka-1:9092'])

def send_message(topic, json_message):
    try:
        json_message = json.dumps(json_message, cls=DjangoJSONEncoder)
        producer.send(topic, json_message.encode('utf-8'))
        producer.flush()
        print("JSON message sent successfully")
    except KafkaError as e:
        print(f"Failed to send JSON message: {e}")