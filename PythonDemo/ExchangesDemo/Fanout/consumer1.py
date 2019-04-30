#coding=utf-8
import sys
sys.path.append('C:\Python27\Lib\site-packages')
import pika
connection =pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.queue_declare(queue='test1')

def callback(ch,method,properties,body):
    print "[x] Received %r" %(body,)

channel.basic_consume(callback,queue='test1',no_ack=True)
channel.start_consuming()