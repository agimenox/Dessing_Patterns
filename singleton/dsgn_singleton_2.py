class Singleton:
    __instance = None

    def __new__(cls): #Another constructor like init. Also called when we create an object.
    
        if (cls.__instance is None):
            cls.__instance = super(Singleton, cls).__new__(cls) #this return a singleton object
        
        return cls.__instance #Return the object

s1 = Singleton()
print(s1)
s1.x = 10
s2 = Singleton()
print(s2)
print(s2.x)