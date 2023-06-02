from factory_pattern_ex import TransportRegister, DestinyRegister


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