#coding=utf-8
import pika
import sys

def Main():
    credential=pika.PlainCredentials("alex","alex")
    parameters=pika.ConnectionParameters("localhost")
    connection=pika.BlockingConnection(parameters)
    channel=connection.channel()
    #包含多于一个参数为信息内容
    routing_key=sys.argv[1] if len(sys.argv)>2 else 'anonymous.info'
    #拼接传递的消息
    message=' '.join(sys.argv[2:]) or "just test words"

    channel.exchange_declare(exchange="topic_info_exchange",exchange_type="topic")
    channel.basic_publish(exchange="topic_info_exchange",routing_key=routing_key,body=message)

    connection.close()

if __name__ == '__main__':
    Main()
