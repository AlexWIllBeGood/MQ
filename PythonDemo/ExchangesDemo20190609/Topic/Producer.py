# .-*- coding:utf-8 .-*-
import sys
import pika


def Main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    exchange=channel.exchange_declare(exchange="exchange",exchange_type="topic")
    routing_key=sys.argv[1] if len(sys.argv)>1 else "test"
    message=" ".join(sys.argv[2:]) if len(sys.argv)>2 else "hello world"
    print(routing_key)
    channel.basic_publish(exchange="exchange",routing_key=routing_key,body=message)
    connection.close()


if __name__ == '__main__':
    Main()