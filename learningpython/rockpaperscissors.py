import random
def rock_paper_scissors():
    choice = ["rock", "paper", "scissor"]
    print("Welcome to rock paper scissor game")

    while True:
        user_choice = input("Choose your choice from given choice rock, paper or scissor\n65")

        if user_choice == "quit":
            print("Thank you for playing")
            break

        if user_choice not in choice:
            print("Invaild choice, Please try again")
            continue

        computer_choice = random.choice(choice)
        print("Computer chose " + computer_choice)

        if user_choice == computer_choice:
            print("It's a draw")
        elif user_choice =="rock" and computer_choice == "scissor" or user_choice =="paper" and computer_choice == "scissor" or user_choice =="scissors" and computer_choice == "scissor":
            print("You Win")
        else:
            print("You Lose")

rock_paper_scissors()