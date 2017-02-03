# coding=utf-8
import time, threading, socket

def tcplink(sock, addr):
    print 'Accept new connection from', addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, {0}'.format(data))
    sock.close()
    print 'Connection from {0} is closed'.format( addr )

# 创建socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听ip与端口
host = '127.0.0.1'
port = 1234
s.bind((host, port))
s.listen(5)

print 'Wating for connection'

while True:
    sock, addr = s.accept()
    print 'Got connection from', addr

    # 创建新线程来接受TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

