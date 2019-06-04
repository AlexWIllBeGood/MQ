#coding=utf-8
import pika

def Main():
    credential=pika.PlainCredentials("alex","alex")
    parameters=pika.ConnectionParameters("localhost")
    



if __name__ == '__main__':
    Main()