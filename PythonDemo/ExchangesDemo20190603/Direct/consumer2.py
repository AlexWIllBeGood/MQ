#coding=utf-8
import pika
def Main():
    credential = pika.PlainCredentials(username="alex", password="alex")
    parameter = pika.ConnectionParameters("localhost")
    connection = pika.BlockingConnection(parameter=parameter)

    channel=connection.channel()
    channel.queue_declare("test")

    def callback(ch,method,properties,body):
        print "%r received %r"%("consumer2",body,)
    channel.basic_consume(callback,queue="test",no_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    Main()