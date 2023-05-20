
car_started = False
car_stopped = True

while True:
    command = input('> ').lower()

    if command=='help':
        print('''start - to start the car')
stop - to stop the car')
quit - exit the game''')
    elif command=='quit':
        break
    elif command=='start':
        if not car_started:
            print('Car started....Ready to go!')
            car_started=True
            car_stopped=False
        else:
            print('Car is already started....')
    elif command=='stop':
        if not car_stopped:
            print('Car stopped.')
            car_stopped=True
            car_started=False
        else:
            print('Car is already stopped')
    else:
        print('I don\'t understand that')