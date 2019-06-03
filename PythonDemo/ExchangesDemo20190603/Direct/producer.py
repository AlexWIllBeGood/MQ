#coding=utf-8
import pika
import sys

def Main():
    credential = pika.PlainCredentials("alex", "alex")
    parameters = pika.ConnectionParameters(host="127.0.0.1", port=15672, virtual_host="TestHost1",
                                           credential=credential)
    message=sys.argv[1]
    connection = pika.BlockingConnection(parameters)
    channel=connection.channel()
    channel.queue_declare(queue="test")
    channel.basic_publish("","test",message)


if __name__ == '__main__':
    Main()