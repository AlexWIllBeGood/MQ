#.-*- coding:utf-8 .-*-
import sys
import pika

def Main():
    connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel=connection.channel()
    routing_key=sys.argv[1] if len(sys.argv)>1 else "test"
    channel.queue_declare(queue=routing_key)
    def callback(ch,method,properties,body):
        print("received %s"%(body))
    channel.basic_consume(on_message_callback=callback,queue=routing_key,auto_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    Main()