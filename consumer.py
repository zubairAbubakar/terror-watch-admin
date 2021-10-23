import django
import json
import os
import pika

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from posts.models import Post


params = pika.URLParameters('amqps://tmpalsrr:YTpKqsIbrUBxbgrLeLkjzlTSWo_HMN2W@fish.rmq.cloudamqp.com/tmpalsrr')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    post = Post.objects.get(id=id)
    post.votes = post.votes + 1
    post.save()
    print('post votes increased')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
