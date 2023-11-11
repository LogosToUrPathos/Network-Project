from socket import *
from pickle import *
from test import RR
from test import Cache

# qualComm socket info
qualPort = 21000
qualSocket = socket(AF_INET, SOCK_DGRAM)
qualSocket.bind(('', qualPort))

qualCache = Cache(10)
rr1 = RR(1, "www.qualcomm.com", 'A', "104.86.224.205", 60, 1)

rr2 = RR(2, "qtiack12.qti.qualcomm.com",'A', "129.49.100.21", 60, 1)

qualCache.pushCache(rr1)
qualCache.pushCache(rr2)

#rr2.printAll()


print("[QualComm Server] Ready to Receive...")
while 1:
    qualMsg, localAddr = qualSocket.recvfrom(2048)
    modQualMsg = qualMsg.decode()
    response = "qualcomm jeez"

    if(qualCache.searchCache(modQualMsg)):
        #response = qualCache.getCache(modQualMsg)
        response = "Inside qualcomm RR"
    else:
        response = "QUALCOMM PLACEHOLDER"

    qualSocket.sendto(localAddr)
    


