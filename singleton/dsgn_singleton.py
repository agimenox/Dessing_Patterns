class Singleton:

    __instance = None #We Declare the class variable

    @staticmethod  #Method associated with the class, this check if we need to create or no
    def getInstance():
        if Singleton.__instance == None: #We create the singleton object
            Singleton()
        return Singleton.__instance #To return something thats not None.
    
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception('Single already exist.')
        else:
            Singleton.__instance = self

s1 = Singleton.getInstance()
print(s1)
s2 = Singleton.getInstance()
print(s2)
s1.x = 10
print(s2.x)   #s1 and s2 are the same object