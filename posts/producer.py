import pika

params = pika.URLParameters('amqps://knveduol:J6Drcdy-Np6n-1o44HhTOiHqhkMnaC8L@baboon.rmq.cloudamqp.com/knveduol')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')
