from socket import *
from pickle import *


serverName = 'localhost'
serverPort = 15000

clientSock = socket(AF_INET, SOCK_DGRAM)
msg = input("Enter URL: ")
clientSock.sendto(msg.encode(), (serverName, serverPort))

modMsg, serverADDR = clientSock.recvfrom(2048)


print(modMsg.decode())

clientSock.close()
