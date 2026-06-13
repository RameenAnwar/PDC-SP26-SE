# server .py

import socket
port=60000
s =socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host=socket.gethostname()
s.bind((host,port))
s.listen(15)
print('Server listening on %s:%d' % (host, port))
while True :
    conn,addr=s.accept()
    print ('Got connection from',addr)
    data=conn.recv(1024)
    print ('Server received',repr(data.decode()))
    filename='mytext.txt'
    with open(filename,'rb') as f:
        l =f.read(1024)
        while (l):
            conn.send(l)
            print ('Sent',repr(l.decode()))
            l =f.read(1024)
    print ('Donesending')
    conn.send('->Thank you for connecting'.encode())
    conn.close()
