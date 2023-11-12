from socket import *

serverName = 'localhost'
serverPort = 15000

clientSock = socket(AF_INET, SOCK_DGRAM)
msg1 = input("Enter URL: ")
msg2 = input("Enter Type: ")

#create query
msg = msg1 + "," + msg2


#get Name and type
query = msg.split(',')

#
print("Name is... : ", query[0])
print("type is... : ", query[1])


# send query to local Server
clientSock.sendto(msg.encode(), (serverName, serverPort))

# wait for response from local Server
#modMsg, serverADDR = clientSock.recvfrom(2048)


importantInfo = []

# wait for viasat response
for i in range(0, 3):
    modMsg, serverADDR = clientSock.recvfrom(2048)
    #response = viaResponse.decode()
    importantInfo.append(modMsg.decode())
#response.printAll()
print(importantInfo)

#pickleObject = pickle.loads(modMsg)
#print(pickleObject)

#print(f"Url is translated to", modMsg.decode())


clientSock.close()
