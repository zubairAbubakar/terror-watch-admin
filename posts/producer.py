import json

import pika

params = pika.URLParameters('amqps://tmpalsrr:YTpKqsIbrUBxbgrLeLkjzlTSWo_HMN2W@fish.rmq.cloudamqp.com/tmpalsrr')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

