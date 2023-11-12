from socket import *
from pickle import *
from test import *
from time import time


# LocalServer Info
localPort = 15000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', localPort))

#Qualcomm Server info
qualPort = 21000
qualSocket = socket(AF_INET, SOCK_DGRAM)
#qualSocket.bind(('', qualPort))


#ViaSat Server info
viaPort = 22000
viaSocket = socket(AF_INET, SOCK_DGRAM)


#DNS chain is Local -> Qualcomm -> Viat

'''
use pickle and create an object to send to client containing
information about the query
'''

# initialize Resource Record object 


# create Cache obj
localCache = Cache(10)

#localCache.pushCache("princeton")


localCache.pushCache(RR(1, "www.csusm.edu", 'A', "144.37.5.45", 60, 1))
localCache.pushCache(RR(2, "cc.csusm.edu", 'A', "144.37.5.117", 60, 1))
localCache.pushCache(RR(3, "cc1.csusm.edu", 'CNAME', "cc.csusm.edu", 60, 1))
localCache.pushCache(RR(4, "cc1.csusm.edu", 'A', "144.37.5.118", 60, 1))
localCache.pushCache(RR(5, "my.csusm.edu", 'A', "144.37.5.150", 60, 1))
localCache.pushCache(RR(6, "qualcomm.com", "NS", "dns.qualcomm.com", 60, 1))




#serverSocket.settimeout(25)
print("[Local Server] Ready to receive...")
# local server shall wait for response through 'recvfrom' and iterate indefinately
while 1:
    importantInfo = []
    #Decode message
    msg, clientADDR = serverSocket.recvfrom(2048)
    modMsg = msg.decode()

    #get Name and type
    query = modMsg.split(',')

    #
    print("modMsg is... : ", query[0])
    print("typeMsg is... : ", query[1])
    #response = localCache.searchName(query[0])
    response = localCache.searchQuery(query[0], query[1])

    #response.printAll()
    #calculateTtl = time()+60
    #print(calculateTtl)
    #response.setTtl()
    #response.printAll()

    #print("Response is: ", response.name)

    if(response != -1):  # search query in cache
        print("Found in local server table")
        importantInfo = [response.name, response.infoType, response.val]
        #response = localCache.searchName(query[0])  #before this used 'searchName'
    elif((query[0].find("qualcomm.com")!= -1) and response == -1):
        #  query wasn't in cache; Ask qualComm server
        #response = "PLACEHOLDER"

        # send query to qualComm  
        qualSocket.sendto(msg, ('localhost', qualPort))

        # wait for viasat response
        for i in range(0, 3):
            qualResponse, qualAddress = qualSocket.recvfrom(2048)
            # response = viaResponse.decode()
            importantInfo.append(qualResponse.decode())

        qualSocket.close()

        #query wasn't in qualcom ask csusm
    elif ((query[0].find("viasat.com") != -1) and response == -1):
        print("CSUSM server found")
        viaSocket.sendto(msg, ('localhost', viaPort))

        # wait for viasat response
        for i in range(0, 3):
            viaResponse, viaAddress = viaSocket.recvfrom(2048)
            #response = viaResponse.decode()
            importantInfo.append(viaResponse.decode())
        #response.printAll()
        print(importantInfo)
        viaSocket.close()

        #EROR not found at all
    else:
        print("ERROR ERROR ERROR")

    #serverSocket.sendto(response.encode(), clientADDR)

    # no encode method for RR so take only the most important info

    for i in range(0, 3):
        serverSocket.sendto(importantInfo[i].encode(), clientADDR)

    

    