#coding=utf-8
import pika
import sys

def Main():
    credential = pika.PlainCredentials("alex", "alex")
    parameters = pika.ConnectionParameters("localhost")
    message=sys.argv[1]
    connection = pika.BlockingConnection(parameters)
    channel=connection.channel()
    channel.queue_declare(queue="test")
    channel.basic_publish("","test",message)


if __name__ == '__main__':
    Main()