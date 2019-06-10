# coding=utf-8
import sys
import pika

def Main():
    connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel=connection.channel()
    message=sys.argv[1:]
    if not message:
        message="Hello world"
    else:
        message=" ".join(message)

    print(message)
    queue=channel.queue_declare(queue="test",exclusive=False)
    channel.basic_publish(exchange="",routing_key="test",body=message)
    connection.close()
if __name__ == '__main__':
    Main()
