import socket
 
host='192.168.1.104'
port=1999
 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'Socket create...'
 
s.bind((host,port))
print 'Socket bind complete'
 
s.listen(20)
print 'Socket now listening 1999 port'
 
while 1:
    conn,addr=s.accept()
    print 'Connect with '+addr[0]+':'+str(addr[1])
 
    data=conn.recv(1024)
    reply='I am receive your message '+data
 
    if not data:
        break
    conn.sendall(reply)
 
conn.close()
s.close()