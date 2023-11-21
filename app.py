import random
#Function to get user input and validate it by checking if it is either "rock", "paper" or "scissors"
def get_user_choice():
    user_choice = input("Please enter either rock, paper or scissors: ")
    if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
        return user_choice.lower()
    else:
        print("Invalid input. Please try again.")
        return get_user_choice()
    
#Function to generate a random choice for the computer
def get_computer_choice():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        return "rock"
    elif computer_choice == 2:
        return "paper"
    else:
        return "scissors"
    
#Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "paper":
            return "You lose!"
        else:
            return "You win!"
    elif user_choice == "paper":
        if computer_choice == "scissors":
            return "You lose!"
        else:
            return "You win!"
    elif user_choice == "scissors":
        if computer_choice == "rock":
            return "You lose!"
        else:
            return "You win!"
        
#Function to play game, keep track of the score and determine if player wants to play

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0
    play_again = True

    while play_again:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose: " + user_choice)
        print("The computer chose: " + computer_choice)
        print(determine_winner(user_choice, computer_choice))
        if determine_winner(user_choice, computer_choice) == "You win!":
            user_score += 1
        elif determine_winner(user_choice, computer_choice) == "You lose!":
            computer_score += 1
        rounds += 1

        to_play_again = input("Do you want to play again? (Y/N): ")
        play_again = to_play_again.lower() == "y"


        print("You have won " + str(user_score) + " times.")
        print("The computer has won " + str(computer_score) + " times.")
        print("You have played " + str(rounds) + " rounds.")

play_game() #Call the function to play the game