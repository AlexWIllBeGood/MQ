#coding=utf-8
import sys
sys.path.append('C:\Python27\Lib\site-packages')
import pika
connection =pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
# 创建Queue
# channel.queue_declare(queue='hello')
# 创建exchange
message=sys.argv[1]
channel.basic_publish(exchange='',routing_key='',body=message)
print "[x] Sent %r"%(message,)
connection.close()