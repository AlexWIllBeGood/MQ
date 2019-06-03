#coding=utf-8
import pika
import logging
logging.basicConfig()
def Main():
    credentials = pika.PlainCredentials("alex", "alex")
    parameters = pika.ConnectionParameters("localhost")
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue="test")
    def callback(ch,method,properties,body):
        print "%r reveived %r"%("consumer1",body,)
    channel.basic_consume(consumer_callback=callback,queue="test1",no_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    Main()



