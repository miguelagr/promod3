#!/usr/bin/python
import os
import requests
import hashlib
import socket
#import plotly

i=0
#hosts=['https://www.unam.mx','https://sadfsda.asdfsadf.as.com','https://ingenieria.unam.mx']
hosts=[]
for host in hosts:
    try:
        req = requests.get(host)
#    ar = open('index.html','w',encoding='utf-8')
        ar = open('base/%i.html'%i,'r')
        hb = hashlib.new("md5")
        hb.update(ar.read())
        ar.close()
        h = hashlib.new("md5")
        h.update(req.content)
        if hb.hexdigest() != h.hexdigest():
            ar = open('base/%i.html'%i,'r')
            ar.write(req.content)
            ar.close()
            print h.hexdigest()
            print "El contenido cambio"
        else:
            print "nada"
#        print req.text.encode('ascii','ignore')
#    ar.write(unicode(req.text,'utf-8').encode('ascii'))
#        ar.write(req.text.encode('ascii','ignore'))

    except Exception as e:
        ar = open('base/%i.html'%i,'w')
#        print req.text.encode('ascii','ignore')
#    ar.write(unicode(req.text,'utf-8').encode('ascii'))
        ar.write("recurso no disponible")
        ar.close()
    i = i + 1


def get_hosts(b1=None,b2=None,b3=None,b4=None):
    ars = locals()
    ip = ''
    for i in ars:
        if ars[i]:
            ip = ip + '%s.'%ars[i]
            print i
        else:
            ip = ip + '%s.'%0
            print i
            print 0
    if ars['b1']:
        print ars['b1']
        if ars['b2']:
            print ars['b2']
            if ars['b3']:
                print ars['b3']
                if ars['b4']:
                    print ars['b4']
                else:
                    for l in range(256):
                        ip = '%s.%s.%s.%s'%(ars['b1'],ars['b2'],ars['b3'],l)
                        print ip
                        try:
                            sock = socket.create_connection((ip,80),timeout=1)
                            sock.settimeout(None)
                            sock.setblocking(1)
                            print "yes"
                            sock.close()
                        except Exception as e:
                            print e

            else:
                for k in range(256):
                    for l in range(256):
                        ip = '%s.%s.%s.%s'%(ars['b1'],ars['b2'],k,l)
                        print ip
        else:
            for i in range(256):
                for k in range(256):
                    for l in range(256):
                        ip = '%s.%s.%s.%s'%(ars['b1'],i,k,l)
                        print ip
    else:
        ip = ''
        for j in range(256):
            for i in range(256):
                for k in range(256):
                    for l in range(256):
                        ip = '%s.%s.%s.%s'%(j,i,k,l)
                        print ip
#    for i in range(256):
#        print i

get_hosts(b1='137',b2='247',b3=70)
#sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    sock =socket.create_connection(('132.247.7.15',443),timeout=1)
    sock.settimeout(None)
    print "yes"
    sock.close()
except Exception as e:
    print e

