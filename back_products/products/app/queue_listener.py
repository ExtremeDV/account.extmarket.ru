
"""
Модуль queue_listener.py содержит класс UserCreatedListener, который представляет собой потоковый слушатель для создания пользователей.
Класс UserCreatedListener наследуется от класса threading.Thread и реализует метод run(), который запускает слушатель.
Атрибуты:
    - consumer: Объект Consumer из библиотеки confluent_kafka для подключения к Kafka-кластеру.
Методы:
    - __init__(self): Конструктор класса, инициализирует объект Consumer.
    - run(self): Метод, который запускает слушатель и обрабатывает полученные сообщения.
Пример использования:
    listener = UserCreatedListener()
    listener.start()
"""
import json
import sys 
import threading
from confluent_kafka import Consumer
from confluent_kafka import KafkaError
from confluent_kafka import KafkaException


running=True
conf = {'bootstrap.servers': "accountextmarketru-kafka-1",
        'auto.offset.reset': 'smallest',
        'group.id': "user_group"}
topic='^user.*'


class UserCreatedListener(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.consumer = Consumer(conf)
   
        
    def run(self):
        print ('Inside Logging :  Created Listener ')
        try:
            self.consumer.subscribe([topic])

            while running:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None: continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                        sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
                else:
                    print('----------Got message-----------')
                    message = json.loads(msg.value().decode('utf-8'))
                    print(message)
        finally:
        # Close down consumer to commit final offsets.
            self.consumer.close()
    
   
