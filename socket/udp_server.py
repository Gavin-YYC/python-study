# coding=utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(('127.0.0.1', 9999))

print 'Bind UDP on 9999'

while True:
    data, addr = s.recvfrom(1024)
    print 'Recieve from {0}'.format( addr )

    s.sendto('hello, {0}'.format( data ), addr)

