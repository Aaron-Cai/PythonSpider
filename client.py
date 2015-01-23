import socket
 
HOST='219.228.111.174'
PORT=1999
 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
 
message='I am send some message!'
 
s.sendall(None)
 
reply=s.recv(4096)
print reply