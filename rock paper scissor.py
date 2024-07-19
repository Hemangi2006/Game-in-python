import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_action = ["rock", "paper", "scissors"]


computer_action = random.choice(possible_action)
print("The user action  is:", user_action)
print("The computer action  is :", computer_action)


if user_action == computer_action:
    print("It's a tie!")
    
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors!\nCongratulations!\nYou win!")
    else:
        print("Paper covers rock!\nsorry, You lose.\nTry again!")
        
        
elif user_action == "paper":
    
    if computer_action == "rock":
        print("Paper covers rock!\nCongratulations !\n You win!")
    else:
        print("Scissors cuts paper!\n sorry, You lose.\n Try again!")
        
        
elif user_action == "scissors":
    
    if computer_action == "paper":
        
        print("Scissors cuts paper!\nCongratultions!\nyou win.")
    else:
        print("Rock smashes scissors!\nsorry,You lose.\nTry again!")
        
        
import string
play_again=input("Do you want to play again? (yes/no):").lower()
if  play_again=="yes":
    print("Play continue")
    
elif  play_again=="no" :    
        print("Game over!")
        print("Thanks for playing !")
         
        