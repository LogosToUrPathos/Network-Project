

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []  #declare cache data member
        

    def searchCache(self, query):
        if query in self.cache:
            return self.cache[query]
        else:
            return None
        
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
                
            
                
            

test = Cache(5)
test.pushCache(1)
test.pushCache(2)
test.pushCache(3)
test.pushCache(4)
test.pushCache(5)
test.pushCache(6)

test.delCache(5)
test.pushCache(6)

print(test.cache)


            
        

