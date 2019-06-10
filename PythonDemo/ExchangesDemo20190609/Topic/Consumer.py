# .-*- coding:utf-8 .-*-
import sys
import pika


def Main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="exchange",exchange_type="topic")
    queue=channel.queue_declare(queue="",exclusive=True).method.queue
    # queue_name=queue

    routing_keys=sys.argv[1:] if len(sys.argv)>1 else ["test1","test2","test3"]
    for item in routing_keys:
        channel.queue_bind(exchange="exchange",queue=queue,routing_key=item)

    def callback(ch,method,properties,body):
        print("%s receive %s"%(method.routing_key,body))

    channel.basic_consume(queue=queue,on_message_callback=callback,auto_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    Main()