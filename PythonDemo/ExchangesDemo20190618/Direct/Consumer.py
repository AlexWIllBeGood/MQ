#.-*- coding:utf-8 .-*-
import sys
import pika

def Main():
    connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel=connection.channel()
    channel.queue_declare(queue="test")
    def callback(ch,method,properties,body):
        print("received %r"%body)
    channel.basic_consume(queue="test",on_message_callback=callback,auto_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    Main()