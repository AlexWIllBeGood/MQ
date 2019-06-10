# .-*- coding:utf-8 .-*-
import pika

def Main():
    connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel=connection.channel()

    channel.queue_declare(queue="test")
    def callback(ch,method,properties,body):
        print("%s receive %s"%("consumer",body))
    channel.basic_consume(on_message_callback=callback,queue="test",auto_ack=True)
    channel.start_consuming()
if __name__ == '__main__':
    Main()