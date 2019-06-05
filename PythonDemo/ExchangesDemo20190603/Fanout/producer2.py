# coding=utf-8
import pika


def Main():
    credential = pika.PlainCredentials("alex", "alex")
    parameters = pika.ConnectionParameters("localhost")
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # 定义queue
    channel.queue_declare(queue="test1")
    channel.queue_declare(queue="test2")
    channel.queue_declare(queue="test3")
    # 定义exchange
    channel.exchange_declare(exchange="exchange2", exchange_type="fanout")
    # 绑定queue
    channel.queue_bind(exchange="exchange2", queue="test1")
    channel.queue_bind(exchange="exchange2", queue="test2")


if __name__ == '__main__':
    Main()