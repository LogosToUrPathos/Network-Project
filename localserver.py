from socket import *
from pickle import *
from test import *



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
    
    msg, clientADDR = serverSocket.recvfrom(2048)
    modMsg = msg.decode()
    print("modMsg is... : ", modMsg)
    response = localCache.searchName(modMsg)
    print("Response is: ", response)

    if(response != -1):  # search query in cache
        response = localCache.searchName(modMsg)
    else:
        #  query wasn't in cache; Ask qualComm server
        response = "PLACEHOLDER"

        # send query to qualComm  
        #qualSocket.sendto(msg, ('localhost', qualPort))

        # wait for qualComm response
        #qualResponse, qualAddress = qualSocket.recvfrom(2048)
        #response = qualResponse
        

        #qualSocket.close()




    serverSocket.sendto(response.encode(), clientADDR)
    

    

    