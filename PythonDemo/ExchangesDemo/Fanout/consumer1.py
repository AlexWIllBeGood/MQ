#coding=utf-8
import pika

def Main():
    # credential=pika.PlainCredentials("alex","alex")
    parameters=pika.ConnectionParameters("localhost")
    connection=pika.BlockingConnection(parameters)
    channel=connection.channel()
    channel.queue_declare(queue="test1")
    def callback(ch,method,properties,body):
        print "%r recieved %r"%("consumer1",body)
    channel.basic_consume(consumer_callback=callback,no_ack=True,queue="test1")
    channel.start_consuming()

if __name__ == '__main__':
    Main()