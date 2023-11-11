

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []  #declare cache data member
        

    def getCache(self, query):
        if query in self.cache:
            return self.cache[query]
        else:
            return None
        
    def searchCache(self, query):
        if query in self.cache:
            return True
        else:
            return False
        
    def pushCache(self, val):
        if(len(self.cache) >= self.capacity):
            print("Cache is full")
            print(f"Element: '{val}' could not be pushed")
            return None
        else:
            self.cache.append(val)

    def delCache(self, val):
        
        if val in self.cache:

            self.cache.remove(val)
            
        else:
            print("Element not found")
            return None
                

class RR:
    def __init__(self, id, name, infoType, val, ttl, static):
        self.id = id
        self.name = name
        self.infoType = infoType
        self.val = val
        self.ttl = ttl
        self.static = static
        self.list = [id, name, infoType, val, ttl, static]

    
    def printAll(self):
        print(self.list)
            
'''
test = Cache(5)
test.pushCache(1)
test.pushCache(2)
test.pushCache(3)
test.pushCache(4)
test.pushCache(5)
'''

'''
if test.searchCache(3):
    print("Found")
else:
    print("Not found")
'''
    
            
        

