# coding=utf-8

# 导入socket库
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 1234

# 建立连接
s.connect((host, port))

print s.recv(1024)

for data in ['Gavin', 'Yang', 'Cun']:
    s.send( data )
    print s.recv(1024)
s.send('exit')
s.close()
