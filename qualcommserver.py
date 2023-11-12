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
    #response = "qualcomm jeez"

    # get Name and type
    qualQuery = modQualMsg.split(',')

    #
    print("modMsg is... : ", qualQuery[0])
    print("typeMsg is... : ", qualQuery[1])


    qualSearch = qualCache.searchQuery(qualQuery[0], qualQuery[1])
    if(qualSearch != -1):
        print("Found in qualcomm server table")
        #response = qualCache.getCache(modQualMsg)
        response = qualSearch

        # no encode method for RR so take only the most important info
        importantInfo = [response.name, response.infoType, response.val]
        for i in range(0, 3):
            qualSocket.sendto(importantInfo[i].encode(), localAddr)
    else:
        response = "NOT IN QUALCOMM"
        qualSocket.sendto(response.encode(), localAddr)
    


