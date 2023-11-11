from socket import *
from pickle import *


serverName = 'localhost'
serverPort = 15000

clientSock = socket(AF_INET, SOCK_DGRAM)
msg = input("Enter URL: ")
# send query to local Server
clientSock.sendto(msg.encode(), (serverName, serverPort))

# wait for response from local Server
modMsg, serverADDR = clientSock.recvfrom(2048)



print(f"Url is translated to", modMsg.decode())


clientSock.close()
