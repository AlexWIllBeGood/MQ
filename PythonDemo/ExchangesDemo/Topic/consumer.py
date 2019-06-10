#coding=utf-8
import sys
import pika

#根据参数来确定 consumer接收啥类型
def Main():
    connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel=connection.channel()
    #定义exchange
    channel.exchange_declare(exchange_type="topic",exchange="topic_info_exchange")
    #定义queue
    result=channel.queue_declare(exclusive=True)
    queue_name=result.method.queue

    def callback(ch,method,properties,body):
        print "RoutingKey %r received %r"%(method.routing_key,body)

    #绑定exchange和queue
    route_key_list=sys.argv[1:]
    if not route_key_list:
        sys.stderr.write("no parameters")
        sys.exit(1)

    for rk in route_key_list:
        channel.queue_bind(queue=queue_name, exchange="topic_info_exchange", routing_key=rk)
    channel.basic_consume(consumer_callback=callback,queue=queue_name,no_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    Main()