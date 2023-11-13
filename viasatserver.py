from socket import *
from pickle import *
from test import RR
from test import Cache

# viasat socket info
viaPort = 22000
viaSocket = socket(AF_INET, SOCK_DGRAM)
viaSocket.bind(('', viaPort))

viaCache = Cache(10)

viaCache.pushCache(RR(1, "www.viasat.com", 'A', "8.37.96.179", "", 1))


#rr2.printAll()


print("[Viasat Server] Ready to Receive...")
while 1:
    viaMsg, localAddr = viaSocket.recvfrom(2048)
    modViaMsg = viaMsg.decode()
    #response = "qualcomm jeez"

    # get Name and type
    qualQuery = modViaMsg.split(',')

    #
    print("modMsg is... : ", qualQuery[0])
    print("typeMsg is... : ", qualQuery[1])


    viaSearch = viaCache.searchQuery(qualQuery[0], qualQuery[1])
    if(viaSearch != -1):
        print("Found in viasat server table")
        #response = qualCache.getCache(modQualMsg)
        response = viaSearch
        #response.printAll()

        # no encode method for RR so take only the most important info
        importantInfo = [response.name, response.infoType, response.val]
    else:
        importantInfo = ["Error", "from", "viasat"]

    for i in range(0, 3):
        viaSocket.sendto(importantInfo[i].encode(), localAddr)