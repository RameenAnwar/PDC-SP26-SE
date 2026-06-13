# server .py
import socket
import time

# create a socket object
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# get local machine name
host=socket.gethostname()
port=9999
# bind to the port
serversocket.bind((host,port))
# queue up to 5 requests
serversocket.listen(5)
print("Server listening on %s:%d" % (host, port))
# establish a connection
while True:	
    clientsocket,addr=serversocket.accept()
    print ("Connected with[addr],[port]%s"%str(addr))
    currentTime=time.ctime(time.time())+"\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
