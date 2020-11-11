from random import randint
hand = ["paper", "scissors", "rock"]
user = False

user = input("Enter your hand (q to exit): ")
computer = hand[randint(0, 2)]

while user != "q":

    if user == computer:
        print("tie!")
    elif user == "paper":
        if computer == "scissors":
            print("Sorry, you lose... " + computer + " cut " + user)
        elif computer == "rock":
            print("Congrat, you win... " + user + " covers " + computer)
    elif user == "scissors":
        if computer == "rock":
            print("Sorry, you lose... " + computer + " breaks " + user)
        elif computer == "paper":
            print("Congrat, you win... " + user + " cut " + computer)
    elif user == "rock":
        if computer == "paper":
            print("Sorry, you lose... " + computer + " covers " + user)
        elif computer == "scissors":
            print("Congrat, you win... " + user + " break " + computer)
    computer = hand[randint(0, 2)]   
    user = input(" Enter your hand (q to exit): ")  
       
