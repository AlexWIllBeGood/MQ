#.-*- coding:utf-8 .-*-
import sys
import pika

def Main():
    connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel=connection.channel()
    routing_key=sys.argv[1] if len(sys.argv)>1 else "test"
    message=sys.argv[2:] if len(sys.argv)>2 else "test words"
    message_str=" ".join(message)

    channel.basic_publish(exchange="",routing_key=routing_key,body=message_str)
    channel.close()


if __name__ == '__main__':
    Main()