#coding=utf-8
import pika
def Main():
    credentials = pika.PlainCredentials("alex", "alex")
    # 登录认证
    parameters = pika.ConnectionParameters("localhost")
    # 创建连接
    connection = pika.BlockingConnection(parameters)
    # 创建信道
    channel = connection.channel()
    # 创建队列
    channel.queue_declare(queue="test")
    def callback(ch,method,properties,body):
        print "%r reveived %r"%("consumer1",body,)
    # 订阅消息
    channel.basic_consume(consumer_callback=callback,queue="test",no_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    Main()



