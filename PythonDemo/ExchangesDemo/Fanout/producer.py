#coding=utf-8
import sys
sys.path.append('C:\Python27\Lib\site-packages')
import pika
connection =pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.queue_declare(queue="test1")
channel.queue_declare(queue="test2")
channel.queue_declare(queue="test3")
channel.exchange_declare(exchange_type='fanout',exchange='exchange1')
channel.queue_bind(queue='test1',exchange='exchange1')
channel.queue_bind(queue='test2',exchange='exchange1')
channel.queue_bind(queue='test3',exchange='exchange1')
message=sys.argv[1]
# 不需要指定RoutingKey 广播模式
channel.basic_publish(exchange='exchange1',routing_key='',body=message)
connection.close()
