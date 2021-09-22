#while loops
i = 1
while i<=5:
    print('*'*i)
    i = i + 1
print("Done!")
#game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
        print("sorry,you failed")
#car game
command = ""
while command !="quit":
    command=input("> ")
    if command == "start":
        print("A car started...")
    elif command == "stop":
        print("A car stopped")
    elif command == "help":
        print("""
        start-to start the car
        stop-to stop the car
        quit-to quit
        """)
        break
    else:
        print("sorry, i don't understantd this")
    #for loop
    for item in range (10):
        print(item)
        

