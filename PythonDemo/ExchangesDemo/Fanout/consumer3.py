#coding=utf-8
import pika

def Main():
    credential=pika.PlainCredentials("alex","alex")
    parameters=pika.ConnectionParameters("localhost")
    connection=pika.BlockingConnection(parameters)
    channel=connection.channel()
    channel.queue_declare(queue="test3")
    def callback(ch,method,properties,body):
        print "%r received %r"%("consumer3",body)
    channel.basic_consume(consumer_callback=callback,queue="test3",no_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    Main()