from socket import *
from pickle import *
from test import RR
from test import Cache

# qualComm socket info
qualPort = 21000
qualSocket = socket(AF_INET, SOCK_DGRAM)
qualSocket.bind(('', qualPort))

qualCache = Cache(10)

qualCache.pushCache(RR(1, "www.qualcomm.com", 'A', "104.86.224.205", 60, 1))
qualCache.pushCache(RR(2, "qtiack12.qti.qualcomm.com",'A', "129.49.100.21", 60, 1))

#rr2.printAll()


print("[QualComm Server] Ready to Receive...")
while 1:
    qualMsg, localAddr = qualSocket.recvfrom(2048)
    modQualMsg = qualMsg.decode()
    response = "qualcomm jeez"

    qualSearch = qualCache.searchName(modQualMsg)
    if(qualSearch != -1):
        #response = qualCache.getCache(modQualMsg)
        response = qualSearch
    else:
        response = "NOT IN QUALCOMM"

    qualSocket.sendto(response.encode(), localAddr)
    


