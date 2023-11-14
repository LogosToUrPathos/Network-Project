from socket import *
from test import RR
from test import Cache
from datetime import datetime, time, timedelta

importantInfo = []
serverName = 'localhost'
serverPort = 15000



#RR table
clientCache = Cache(10)

# loop started here
quitLoop = True
Cindex = 0
while quitLoop == True:
    
    clientSock = socket(AF_INET, SOCK_DGRAM)
    Cindex+=1
    print(f"\n[Client Iteration: {Cindex}]")

    msg1 = input("Enter URL: ")
    msg2 = input("Enter Type: ")

    #create query
    msg = msg1 + "," + msg2

    #get Name and type
    query = msg.split(',')

    #
    print("Name is... : ", query[0])
    print("type is... : ", query[1], "\n")

    #checkRR
    response = clientCache.searchQuery(msg1, msg2)

    # seconds since midnight
    rn = datetime.now()
    sinceMidnight = (rn - rn.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

    rrId = 0
    for rr in clientCache.cache:
        print(f"ID: {rr.id}, Name: {rr.name}, Type: {rr.infoType}, Value: {rr.val}"
            f", TTL:{rr.ttl}, Static: {rr.static}")
        # find highest ID
        if (rrId < rr.id):
            rrId = rr.id

        # while looping check ttl
        if (rr.ttl == ""):
            # from original table do nothing
            # print("")
            pass
        # remove if expired
        elif (int(rr.ttl) < int(sinceMidnight)):
            # print("Removed: ", rr_instance.printAll())
            clientCache.delCache(rr)
        elif (int(rr.ttl) > int(sinceMidnight)):
            # still has some time do nothing
            # print("")
            pass
        else:
            importantInfo = ["Error", "wrong", "ttl"]

    if(response != -1):  # search query in cache
            print("Found in client RR table\n")
    # send query to local Server
    else:
        clientSock.sendto(msg.encode(), (serverName, serverPort))

    # wait for local server response
    for i in range(0, 4):
        modMsg, serverADDR = clientSock.recvfrom(2048)
        importantInfo.append(modMsg.decode())

    print(importantInfo)

    rrEntry = RR.assembleRR(rrId, importantInfo, importantInfo[3])
    clientCache.pushCache(rrEntry)

    print("Requested IP: ", rrEntry.val)

    print("\nClient RR Table:------------------------------")

    clientCache.printCache()
    importantInfo.clear()


    stuff = input("\n(Continue? Y/n): ")
    if stuff == "N" or stuff == "n":
        quitLoop = False
    


clientSock.close()
