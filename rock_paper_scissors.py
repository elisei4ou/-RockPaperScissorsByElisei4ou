import random
import time

from colorama import Fore, Style

result_for_player = 0
result_for_computer = 0
while True:
    rock = 'Rock'
    paper = 'Paper'
    scissors = 'Scissors'
    player_next_move = ""
    player_move = input(Fore.LIGHTWHITE_EX+"Choose: [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = "rock"
    elif player_move == "p":
        player_move = "paper"
    elif player_move == "s":
        player_move = "scissors"
    else:
        raise SystemExit(Fore.LIGHTRED_EX + "Invalid input. Try again...")

    computer_random_move = random.randint(1, 3)
    computer_move = ""
    if computer_random_move == 1:
        computer_move = "rock"
    elif computer_random_move == 2:
        computer_move = "paper"
    else:
        computer_move = "scissors"

    if (player_move == "rock" and computer_move == "scissors") \
            or (player_move == "paper" and computer_move == "rock") \
            or (player_move == "scissors" and computer_move == "paper"):
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(Fore.LIGHTBLUE_EX + f"The computer chose {computer_move}.")
        time.sleep(0.5)
        print(Fore.LIGHTGREEN_EX + "You WIN")
        result_for_player += 1
        time.sleep(0.5)
        print(Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + f"The result is PLAYER[{result_for_player}]:COMPUTER[{result_for_computer}] ")
        print()
        player_next_move = input("Type [yes] to Play Again or [no] to quit: ")
        if player_next_move == "yes":
            continue
        elif player_next_move == "no":
            print("Thank for playing")
            break
        else:
            raise SystemExit(Fore.LIGHTRED_EX+"Invalid input. Try again...")

    elif computer_move == player_move:
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(Fore.LIGHTBLUE_EX + f"The computer chose {computer_move}.")
        time.sleep(0.5)
        print(Fore.LIGHTYELLOW_EX + "Draw")
        result_for_player += 0.5
        result_for_computer += 0.5
        time.sleep(0.5)
        print(Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX+f"The result is PLAYER[{result_for_player}]:COMPUTER[{result_for_computer}] ")
        print()
        player_next_move = input("Type [yes] to Play Again or [no] to quit: ")
        if player_next_move == "yes":
            continue
        elif player_next_move == "no":
            print("Thank for playing")
            break
        else:
            raise SystemExit(Fore.LIGHTRED_EX+"Invalid input. Try again...")
    else:
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(Fore.LIGHTBLUE_EX + f"The computer chose {computer_move}.")
        time.sleep(0.5)
        print(Fore.LIGHTRED_EX + "You LOSE")
        result_for_computer += 1
        time.sleep(0.5)
        print(Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX+f"The result is PLAYER[{result_for_player}]:COMPUTER[{result_for_computer}] ")
        print()
        player_next_move = input("Type [yes] to Play Again or [no] to quit: ")
        if player_next_move == "yes":
            continue
        elif player_next_move == "no":
            print("Thank for playing")
            break
        else:
            raise SystemExit(Fore.LIGHTRED_EX+"Invalid input. Try again...")

