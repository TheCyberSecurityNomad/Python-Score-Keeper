"""

My University Project

"""

#-Function to check if a given name is valid (contains only alphabetic characters)
def name_isvalid(name):
    if name.isalpha():  #-Check if all characters in the name are alphabetic
        return True
    else:
        return False

#-Function to check if a given score is valid (must be an integer between 0 and 100)
def score_isvalid(score):
    try:
        score = int(score)  #-Try converting the score to an integer
        if 0 <= score <= 100:  #-Check if the score is within the valid range
            return True
        else:
            return False
    except ValueError:
        return False  #-If conversion to int fails (non-integer input), return False

#-Function to update the players' information
def update_players(players):
    while True:
        name = input("Enter the player name : ")  #-Prompt user to enter player name
        if name_isvalid(name):  #-Check if the entered name is valid
            break  #-Exit the loop if the name is valid
        else:
            print("Invalid name. Please enter a valid name.")  #-Print error message for invalid name

    while True:
        score = input("Enter the score : ")  #-Prompt user to enter player score
        if score_isvalid(score):  #-Check if the entered score is valid
            break  #-Exit the loop if the score is valid
        else:
            print("Invalid score. Please enter a valid score between 0 and 100.")  #-Print error message for invalid score

    players[name] = int(score)  #-Add the player name and score to the players dictionary

    while True:
        choice = input("Do you want to add another player? (Y/N) : ")  #-Ask user if they want to add another player
        if choice.upper() == 'Y' or choice.upper() == 'YES':  #-If user wants to add another player
            update_players(players)  #-Recursive call to add another player
            break  #-Exit the loop
        elif choice.upper() == 'N' or choice.upper() == 'NO':  #-If user does not want to add another player
            return  #-Return from the function
        else:
            print("Invalid choice. Please enter Y or N.")  #-Print error message for invalid choice

#-Function to display players' information
def display_players(players):
    print("Player & Score Details:")
    print("-----------------------")
    print("Player\tScore")
    for name, score in players.items():
        print(name + "\t" + str(score))  #-Print player name and score

#-Main function
def main():
    players = {}  #-Initialize an empty dictionary to store players' information
    while True:
        print("===========================================")
        print("**Welcome to Champions Soccer Club**")
        print("Please choose an option from the followings.")
        print("1) Add player name and score")
        print("2) Display all the player information and scores")
        print("3) Quit.")
        print("===========================================")
        choice = input("Enter your choice : ")  #-Prompt user to enter their choice
        if choice == '1':
            update_players(players)  #-Call function to add player information
        elif choice == '2':
            display_players(players)  #-Call function to display player information
        elif choice == '3':
            print("**GoodBye.. See you again!**")  #-Print farewell message
            break  #-Exit the loop and end the program
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")  #-Print error message for invalid choice

main()  #-Call the main function to start the program execution
