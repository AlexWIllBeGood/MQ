#.-*- coding:utf-8 .-*-
import sys
import pika

def Main():
    connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel=connection.channel()
    queue_name=sys.argv[1] if len(sys.argv)>1 else "test"

    channel.queue_declare(queue=queue_name)
    def callback(ch,method,proprties,body):
        print "received %s"%(body)
    channel.basic_consume(queue=queue_name,no_ack=True,consumer_callback=callback)
    channel.start_consuming()

if __name__ == '__main__':
    Main()