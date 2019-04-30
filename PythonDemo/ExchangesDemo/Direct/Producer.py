#coding=utf-8
import sys
sys.path.append('C:\Python27\Lib\site-packages')
import pika
connection =pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.queue_declare(queue="test")
message=sys.argv[1]
channel.basic_publish(exchange='',routing_key='Test1',body=message)
connection.close()
