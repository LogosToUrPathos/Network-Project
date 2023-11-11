from socket import *
from pickle import *

PORT = 15000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', PORT))

#use pickle and create an objeict to send to client containing
# information about the ip they queried
class ResourceRecord:
    def __init__(self, rnum, dname, ip, val, ttl, static):
        self.rnum = rnum
        self.dname = dname
        self.ip = ip
        self.val = val
        self.ttl = ttl
        self.static = static



cache = []

print("[Local Server] Ready to receive...")

while 1:
    
    msg, clientADDR = serverSocket.recvfrom(2048)
    if(msg in cache):
        pass

    

    modMsg = msg.decode()
    cache.append(modMsg)  # always cache the query
    serverSocket.sendto(modMsg.encode(), clientADDR)

    

    