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
qualSocket.bind(('', qualPort))


#ViaSat Server info
viaPort = 22000



#DNS chain is Local -> Qualcomm -> Viat

'''
use pickle and create an object to send to client containing
information about the query
'''

# initialize Resource Record object 
class RR:
    def __init__(self, rnum, dname, ip, val, ttl, static):
        self.rnum = rnum
        self.dname = dname
        self.ip = ip
        self.val = val
        self.ttl = ttl
        self.static = static

# create Cache obj
localCache = Cache(100)

localCache.pushCache("princeton")




#serverSocket.settimeout(25)
print("[Local Server] Ready to receive...")
# local server shall wait for response through 'recvfrom' and iterate indefinately
while 1:
    
    msg, clientADDR = serverSocket.recvfrom(2048)
    modMsg = msg.decode()
    response = "jeez"

    if(localCache.searchCache(modMsg)):  # search query in cache
        response = modMsg
    else:
        #  query wasn't in cache; Ask qualComm server
        response = "PLACEHOLDER"

        # send query to qualComm  
        qualSocket.sendto(msg, ('localhost', qualPort))

        # wait for qualComm response
        qualResponse, qualAddress = qualSocket.recvfrom(2048)
        response = qualResponse
        

        qualSocket.close()




    serverSocket.sendto(response.encode(), clientADDR)
    

    

    