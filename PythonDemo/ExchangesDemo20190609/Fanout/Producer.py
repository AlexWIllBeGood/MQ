#.-*- coding:utf-8 .-*-
import sys
import pika

def Main():
    connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel=connection.channel()
    channel.exchange_declare(exchange="test",exchange_type="fanout")
    queue=sys.argv[1] if len(sys.argv)>1 else "test"
    message=" ".join(sys.argv[2:]) if len(sys.argv)>2 else "hello world"
    channel.queue_bind(queue=queue,exchange="test")

    channel.basic_publish(exchange="test",routing_key="",body=message)
    connection.close()
if __name__ == '__main__':
    Main()