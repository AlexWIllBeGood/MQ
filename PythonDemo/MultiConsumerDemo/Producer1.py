#coding=utf-8
import sys
sys.path.append('C:\Python27\Lib\site-packages')
import pika
connection =pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
# 创建Queue
# channel.queue_declare(queue='Test11')
# channel.queue_declare(queue='Test12')
# 创建exchange
message1=sys.argv[1]
message2=sys.argv[2]
channel.basic_publish(exchange='',routing_key='Test1',body=message1)
channel.basic_publish(exchange='',routing_key='Test2',body=message2)
print "[x] Sent %r %r"%(message1,message2,)
connection.close()