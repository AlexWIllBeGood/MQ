#coding=utf-8
import sys
sys.path.append('C:\Python27\Lib\site-packages')
import pika
connection =pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.queue_delete(queue='Test')
channel.queue_delete(queue='Test1')
channel.queue_delete(queue='hello')
channel.queue_delete(queue='Hello')
channel.queue_delete(queue='hello world')

connection.close()