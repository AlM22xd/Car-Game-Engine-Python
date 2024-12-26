'''Car Game Engine 
terminal display should look like this
>
start prints "car is starting..." and puts the car in
started mode
stop prints"car is stopping..." and puts the car in
stopped mode
quit exits the car engine
program MUST NOT exit unless quit is typed

if car has already started and start is re-entered
it should print "Car has already started"
if car has already stopped and stop is re-entered
it should print "Car has already stopped"
if incorrect command is given , it should print incorrect command
typing help gives user list of commmands the program supports'''

print("Welcome to the car game, type 'help' for more options. or 'quit' to exit")
while True:
    command = input(">").lower()
    if command == "start": 
        print("The car is starting...\n The car is now in started mode")
        command = input(">").lower()
    elif command == "start":
            print("Car has already started...")
            
    elif ValueError:
            print("incorrect value given, see 'help' {help} ")

    elif command == "stop": 
            print("the car is stopping...\n The car is now in stopped mode")
            command = input(">").lower()
    elif command == "stop":
            print("Car has already stopped...")
        
    elif ValueError:
        print("incorrect value given, see 'help' {help} ")
    
    elif command == "help": 
        print("'Start': to start the car\n 'Stop': To stop the car")
    else: 
        command == "quit"
        print ("You have now exited the game")
        break

