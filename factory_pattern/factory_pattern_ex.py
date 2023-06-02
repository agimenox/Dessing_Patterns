from abc import ABCMeta, abstractstaticmethod

class Transport(metaclass = ABCMeta):

    @abstractstaticmethod
    def transport_method():
        '''Transport Method'''

    @abstractstaticmethod
    def calculate_arrive_time():
        '''To calculate time to arrived'''


class Car(Transport):

    def __init__(self):
        self.speed = 80
        self.cost = 20

    def transport_method(self):
        print('This is a Car')

    def calculate_arrive_time(self,distance):
        travel_time = distance/self.speed
        print(f'The travel time will take {travel_time} Hours')

class Bus(Transport):

    def __init__(self) -> None:
        self.speed = 50
        self.cost = 10

    def transport_method(self):
        print('This is a Bus')

    def calculate_arrive_time(self,distance):
        travel_time = distance/self.speed
        print(f'The travel time will take {travel_time} Hours')

class Aircraft(Transport):

    def __init__(self):
        self.speed = 800
        self.cost = 80

    def transport_method(self):
        print('This is an Aircraft')

    def calculate_arrive_time(self,distance):
        travel_time = distance/self.speed
        print(f'The travel time will take {travel_time} Hours')

class Train(Transport):

    def __init__(self):
        self.speed = 150
        self.cost = 10

    def transport_method(self):
        print('This is a Train')

    def calculate_arrive_time(self,distance):
        travel_time = distance/self.speed
        print(f'The travel time will take {travel_time} Hours')

class TransportRegister:

    @staticmethod
    def register_transport(transport_type):
        if transport_type == "Car":
            return Car()
        if transport_type == "Bus":
            return Bus()
        if transport_type == "Aircraft":
            return Aircraft()
        if transport_type == "Train":
            return Train()
        print("Invalid Type")
        return -1
    

class Destiny(metaclass = ABCMeta):

    @abstractstaticmethod
    def destiny_method():
        '''Destiny Mehod'''


class Air(Destiny):

    def __init__(self, distance):
        self.distance = distance

    def destiny_method(self):
        print('''This is Air''')

class Road(Destiny):

    def __init__(self,distance):
        self.distance = distance

    def destiny_method(self):
        print('''This is Road''')

class Rail(Destiny):

    def __init__(self,distance):
        self.distance = distance

    def destiny_method(self):
        print('''This is Rail''')

class DestinyRegister:
    
    @staticmethod
    def register_destiny(travel_type,distance):
        if travel_type == "Air":
            return Air(distance)
        if travel_type == "Road":
            return Road(distance)
        if travel_type == "Rail":
            return Rail(distance)
        print("Invalid Type")
        return -1
        
if __name__ == '__main__':
    choice = input('What kind of transport you want to register?\n')
    transport = TransportRegister.register_transport(choice)
    transport.transport_method()
    if choice == 'Car':
        distance = int(input('How many Kilometers\n'))
        destination = DestinyRegister.register_destiny('Road',distance)
        destination.destiny_method()
        transport.calculate_arrive_time(distance)
    if choice == 'Bus':
        distance = int(input('How many Kilometers\n'))
        destination = DestinyRegister.register_destiny('Road',distance)
        destination.destiny_method()
        transport.calculate_arrive_time(distance)
    if choice == 'Aircraft':
        distance = int(input('How many Kilometers\n'))
        destination = DestinyRegister.register_destiny('Air',distance)
        destination.destiny_method()
        transport.calculate_arrive_time(distance)

