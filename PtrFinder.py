#!/usr/bin/python
#import dns
import socket


#x = list( map( lambda x: x[4][0], socket.getaddrinfo('www.example.com',22)))
for i in socket.getaddrinfo('www.example.com',22):
	print i


for i in hosts
