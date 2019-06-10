#.-*- coding：utf-8 .-*-
import sys
import pika

def Main():
    connection=pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel=connection.channel()
    channel.exchange_declare(exchange="exchange1",exchange_type="fanout")

    routing_keys=sys.argv[1:] if len(sys.argv)>1 else "test"
    for rk in routing_keys:
        channel.queue_bind()
    def callback(ch,method,properties,body):
        print "received %s"%(body)



if __name__ == '__main__':
    Main()