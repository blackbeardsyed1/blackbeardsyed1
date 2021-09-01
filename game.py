HIYIU77777777670J D# Gaming
import random
import time
import sys

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_board():
    print(nums[0], "|", nums[1], "|", nums[2])
    print("---------")
    print(nums[3], "|", nums[4], "|", nums[5])
    print("---------")
    print(nums[6], "|", nums[7], "|", nums[8])


game_continuation = "y"

while game_continuation == "y":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print_board()
    user_input = input("ENTER PALYER1 NAME: ")
    user_input2 = input("ENTER PALYER2 NAME: ")
    player1 = user_input + " X"
    player2 = user_input2 + " O"

    rand = random.randint(0, 1)
    if rand == 0:
        print("Player 1 won the toss")
        first_player = player1
    else:
        print("Player 2 won the toss")
        first_player = player2

    if rand == 0:
        valid = True
        while valid:
            one = eval(
                input(f"Enter numbers through 1 and 9 only: { player1}: "))
            if one!= 1 and one !=2 and one!= 3 and one!= 4 and one!= 5 and one != 6 and one != 7 \
                and one != 8 and one != 9:
                continue
            
            if one == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "X"
                print_board()

            elif one == 1 and (nums[0] == "O"):
                continue
            if one == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "X"
                print_board()

            elif one == 2 and (nums[1] == "O"):
                continue
            if one == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "X"
                print_board()

            elif one == 3 and (nums[2] == "O"):
                continue
            if one == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "X"
                print_board()

            elif one == 4 and (nums[3] == "O"):
                continue
            if one == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "X"
                print_board()

            elif one == 5 and (nums[4] == "O"):
                continue
            if one == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "X"
                print_board()

            elif one == 6 and (nums[5] == "O"):
                continue
            if one == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "X"
                print_board()

            elif one == 7 and (nums[6] == "O"):
                continue
            if one == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "X"
                print_board()

            elif one == 8 and (nums[7] == "O"):
                continue
            if one == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "X"
                print_board()

            elif one == 9 and (nums[8] == "O"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False

            break

        while valid:
            two = eval(
                input(f"Enter numbers through 1 and 9 only: { player2}: "))
            if two!= 1 and two !=2 and two!= 3 and two!= 4 and two!= 5 and two != 6 and two != 7 \
                and two != 8 and two != 9:
                continue
            if two == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "O"
                print_board()

            elif two == 1 and (nums[0] == "X"):
                continue
            if two == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "O"
                print_board()

            elif two == 2 and (nums[1] == "X"):
                continue
            if two == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "O"
                print_board()

            elif two == 3 and (nums[2] == "X"):
                continue
            if two == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "O"
                print_board()

            elif two == 4 and (nums[3] == "X"):
                continue
            if two == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "O"
                print_board()

            elif two == 5 and (nums[4] == "X"):
                continue
            if two == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "O"
                print_board()

            elif two == 6 and (nums[5] == "X"):
                continue
            if two == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "O"
                print_board()

            elif two == 7 and (nums[6] == "X"):
                continue
            if two == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "O"
                print_board()

            elif two == 8 and (nums[7] == "X"):
                continue
            if two == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "O"
                print_board()

            elif two == 9 and (nums[8] == "X"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False
            break

        while valid:
            one = eval(
                input(f"Enter numbers through 1 and 9 only: { player1}: "))
            if one!= 1 and one !=2 and one!= 3 and one!= 4 and one!= 5 and one != 6 and one != 7 \
                and one != 8 and one != 9:
                continue

            if one == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "X"
                print_board()

            elif one == 1 and (nums[0] == "O"):
                continue
            if one == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "X"
                print_board()

            elif one == 2 and (nums[1] == "O"):
                continue
            if one == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "X"
                print_board()

            elif one == 3 and (nums[2] == "O"):
                continue
            if one == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "X"
                print_board()

            elif one == 4 and (nums[3] == "O"):
                continue
            if one == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "X"
                print_board()

            elif one == 5 and (nums[4] == "O"):
                continue
            if one == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "X"
                print_board()

            elif one == 6 and (nums[5] == "O"):
                continue
            if one == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "X"
                print_board()

            elif one == 7 and (nums[6] == "O"):
                continue
            if one == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "X"
                print_board()

            elif one == 8 and (nums[7] == "O"):
                continue
            if one == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "X"
                print_board()

            elif one == 9 and (nums[8] == "O"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False
            break

        while valid:
            two = eval(
                input(f"Enter numbers through 1 and 9 only: { player2}: "))
            if two!= 1 and two !=2 and two!= 3 and two!= 4 and two!= 5 and two != 6 and two != 7 \
                and two != 8 and two != 9:
                continue
            if two == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "O"
                print_board()

            elif two == 1 and (nums[0] == "X"):
                continue
            if two == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "O"
                print_board()

            elif two == 2 and (nums[1] == "X"):
                continue
            if two == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "O"
                print_board()

            elif two == 3 and (nums[2] == "X"):
                continue
            if two == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "O"
                print_board()

            elif two == 4 and (nums[3] == "X"):
                continue
            if two == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "O"
                print_board()

            elif two == 5 and (nums[4] == "X"):
                continue
            if two == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "O"
                print_board()

            elif two == 6 and (nums[5] == "X"):
                continue
            if two == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "O"
                print_board()

            elif two == 7 and (nums[6] == "X"):
                continue
            if two == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "O"
                print_board()

            elif two == 8 and (nums[7] == "X"):
                continue
            if two == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "O"
                print_board()

            elif two == 9 and (nums[8] == "X"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False
            break

        while valid:
            one = eval(
                input(f"Enter numbers through 1 and 9 only: { player1}: "))
            if one!= 1 and one !=2 and one!= 3 and one!= 4 and one!= 5 and one != 6 and one != 7 \
                and one != 8 and one != 9:
                continue
            if one == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "X"
                print_board()

            elif one == 1 and (nums[0] == "O"):
                continue
            if one == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "X"
                print_board()

            elif one == 2 and (nums[1] == "O"):
                continue
            if one == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "X"
                print_board()

            elif one == 3 and (nums[2] == "O"):
                continue
            if one == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "X"
                print_board()

            elif one == 4 and (nums[3] == "O"):
                continue
            if one == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "X"
                print_board()

            elif one == 5 and (nums[4] == "O"):
                continue
            if one == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "X"
                print_board()

            elif one == 6 and (nums[5] == "O"):
                continue
            if one == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "X"
                print_board()

            elif one == 7 and (nums[6] == "O"):
                continue
            if one == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "X"
                print_board()

            elif one == 8 and (nums[7] == "O"):
                continue
            if one == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "X"
                print_board()

            elif one == 9 and (nums[8] == "O"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False
            break

        while valid:
            two = eval(
                input(f"Enter numbers through 1 and 9 only: { player2}: "))
            if two!= 1 and two !=2 and two!= 3 and two!= 4 and two!= 5 and two != 6 and two != 7 \
                and two != 8 and two != 9:
                continue

            if two == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "O"
                print_board()

            elif two == 1 and (nums[0] == "X"):
                continue
            if two == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "O"
                print_board()

            elif two == 2 and (nums[1] == "X"):
                continue
            if two == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "O"
                print_board()

            elif two == 3 and (nums[2] == "X"):
                continue
            if two == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "O"
                print_board()

            elif two == 4 and (nums[3] == "X"):
                continue
            if two == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "O"
                print_board()

            elif two == 5 and (nums[4] == "X"):
                continue
            if two == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "O"
                print_board()

            elif two == 6 and (nums[5] == "X"):
                continue
            if two == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "O"
                print_board()

            elif two == 7 and (nums[6] == "X"):
                continue
            if two == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "O"
                print_board()

            elif two == 8 and (nums[7] == "X"):
                continue
            if two == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "O"
                print_board()

            elif two == 9 and (nums[8] == "X"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False
            break


        while valid:
            one = eval(
                input(f"Enter numbers through 1 and 9 only: { player1}: "))
            if one!= 1 and one !=2 and one!= 3 and one!= 4 and one!= 5 and one != 6 and one != 7 \
                and one != 8 and one != 9:
                continue

            if one == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "X"
                print_board()

            elif one == 1 and (nums[0] == "O"):
                continue
            if one == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "X"
                print_board()

            elif one == 2 and (nums[1] == "O"):
                continue
            if one == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "X"
                print_board()

            elif one == 3 and (nums[2] == "O"):
                continue
            if one == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "X"
                print_board()

            elif one == 4 and (nums[3] == "O"):
                continue
            if one == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "X"
                print_board()

            elif one == 5 and (nums[4] == "O"):
                continue
            if one == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "X"
                print_board()

            elif one == 6 and (nums[5] == "O"):
                continue
            if one == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "X"
                print_board()

            elif one == 7 and (nums[6] == "O"):
                continue
            if one == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "X"
                print_board()

            elif one == 8 and (nums[7] == "O"):
                continue
            if one == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "X"
                print_board()

            elif one == 9 and (nums[8] == "O"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False
            break

        while valid:
            two = eval(
                input(f"Enter numbers through 1 and 9 only: { player2}: "))
            if two!= 1 and two !=2 and two!= 3 and two!= 4 and two!= 5 and two != 6 and two != 7 \
                and two != 8 and two != 9:
                continue

            if two == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "O"
                print_board()

            elif two == 1 and (nums[0] == "X"):
                continue
            if two == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "O"
                print_board()

            elif two == 2 and (nums[1] == "X"):
                continue
            if two == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "O"
                print_board()

            elif two == 3 and (nums[2] == "X"):
                continue
            if two == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "O"
                print_board()

            elif two == 4 and (nums[3] == "X"):
                continue
            if two == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "O"
                print_board()
            elif two == 5 and (nums[4] == "X"):
                continue
            if two == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "O"
                print_board()

            elif two == 6 and (nums[5] == "X"):
                continue
            if two == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "O"
                print_board()

            elif two == 7 and (nums[6] == "X"):
                continue
            if two == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "O"
                print_board()

            elif two == 8 and (nums[7] == "X"):
                continue
            if two == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "O"
                print_board()

            elif two == 9 and (nums[8] == "X"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False
            break

        while valid:
            one = eval(
                input(f"Enter numbers through 1 and 9 only: { player1}: "))
            if one!= 1 and one !=2 and one!= 3 and one!= 4 and one!= 5 and one != 6 and one != 7 \
                and one != 8 and one != 9:
                continue

            if one == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "X"
                print_board()

            elif one == 1 and (nums[0] == "O"):
                continue
            if one == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "X"
                print_board()

            elif one == 2 and (nums[1] == "O"):
                continue
            if one == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "X"
                print_board()

            elif one == 3 and (nums[2] == "O"):
                continue
            if one == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "X"
                print_board()

            elif one == 4 and (nums[3] == "O"):
                continue
            if one == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "X"
                print_board()

            elif one == 5 and (nums[4] == "O"):
                continue
            if one == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "X"
                print_board()

            elif one == 6 and (nums[5] == "O"):
                continue
            if one == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "X"
                print_board()

            elif one == 7 and (nums[6] == "O"):
                continue
            if one == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "X"
                print_board()

            elif one == 8 and (nums[7] == "O"):
                continue
            if one == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "X"
                print_board()

            elif one == 9 and (nums[8] == "O"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):

                print(f"Player 2 {player2} has won the match!!!")
                valid = False
            if not("X" == nums[0] and "X" == nums[1] and "X" == nums[2]) \
                and not ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                and not ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                and not ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                and not("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                and not("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                and not("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                and not ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]) \
                and not("O" == nums[0] and "O" == nums[1] and "O" == nums[2]) \
                and not("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                and not("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                and not("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                and not("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                and not("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                and not("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                and not ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print("Its a DRAW!!!")
                valid = False

            break
        game_continuation = input("Enter y to continue or N to exit: ").lower()
    else:
        valid = True
        while valid:
            two = eval(
                input(f"Enter numbers through 1 and 9 only: { player2}: "))
            if two!= 1 and two !=2 and two!= 3 and two!= 4 and two!= 5 and two != 6 and two != 7 \
                and two != 8 and two != 9:
                continue
            if two == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "O"
                print_board()

            elif two == 1 and (nums[0] == "X"):
                continue
            if two == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "O"
                print_board()

            elif two == 2 and (nums[1] == "X"):
                continue
            if two == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "O"
                print_board()

            elif two == 3 and (nums[2] == "X"):
                continue
            if two == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "O"
                print_board()

            elif two == 4 and (nums[3] == "X"):
                continue
            if two == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "O"
                print_board()

            elif two == 5 and (nums[4] == "X"):
                continue
            if two == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "O"
                print_board()

            elif two == 6 and (nums[5] == "X"):
                continue
            if two == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "O"
                print_board()

            elif two == 7 and (nums[6] == "X"):
                continue
            if two == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "O"
                print_board()

            elif two == 8 and (nums[7] == "X"):
                continue
            if two == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "O"
                print_board()

            elif two == 9 and (nums[8] == "X"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False
            break
        while valid:
            one = eval(
                input(f"Enter numbers through 1 and 9 only: { player1}: "))
            if one!= 1 and one !=2 and one!= 3 and one!= 4 and one!= 5 and one != 6 and one != 7 \
                and one != 8 and one != 9:
                continue
            
            if one == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "X"
                print_board()

            elif one == 1 and (nums[0] == "O"):
                continue
            if one == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "X"
                print_board()

            elif one == 2 and (nums[1] == "O"):
                continue
            if one == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "X"
                print_board()

            elif one == 3 and (nums[2] == "O"):
                continue
            if one == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "X"
                print_board()

            elif one == 4 and (nums[3] == "O"):
                continue
            if one == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "X"
                print_board()

            elif one == 5 and (nums[4] == "O"):
                continue
            if one == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "X"
                print_board()

            elif one == 6 and (nums[5] == "O"):
                continue
            if one == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "X"
                print_board()

            elif one == 7 and (nums[6] == "O"):
                continue
            if one == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "X"
                print_board()

            elif one == 8 and (nums[7] == "O"):
                continue
            if one == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "X"
                print_board()

            elif one == 9 and (nums[8] == "O"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False

            break
        while valid:
            two = eval(
                input(f"Enter numbers through 1 and 9 only: { player2}: "))
            if two!= 1 and two !=2 and two!= 3 and two!= 4 and two!= 5 and two != 6 and two != 7 \
                and two != 8 and two != 9:
                continue
            if two == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "O"
                print_board()

            elif two == 1 and (nums[0] == "X"):
                continue
            if two == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "O"
                print_board()

            elif two == 2 and (nums[1] == "X"):
                continue
            if two == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "O"
                print_board()

            elif two == 3 and (nums[2] == "X"):
                continue
            if two == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "O"
                print_board()

            elif two == 4 and (nums[3] == "X"):
                continue
            if two == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "O"
                print_board()

            elif two == 5 and (nums[4] == "X"):
                continue
            if two == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "O"
                print_board()

            elif two == 6 and (nums[5] == "X"):
                continue
            if two == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "O"
                print_board()

            elif two == 7 and (nums[6] == "X"):
                continue
            if two == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "O"
                print_board()

            elif two == 8 and (nums[7] == "X"):
                continue
            if two == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "O"
                print_board()

            elif two == 9 and (nums[8] == "X"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False
            break
        while valid:
            one = eval(
                input(f"Enter numbers through 1 and 9 only: { player1}: "))
            if one!= 1 and one !=2 and one!= 3 and one!= 4 and one!= 5 and one != 6 and one != 7 \
                and one != 8 and one != 9:
                continue
            
            if one == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "X"
                print_board()

            elif one == 1 and (nums[0] == "O"):
                continue
            if one == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "X"
                print_board()

            elif one == 2 and (nums[1] == "O"):
                continue
            if one == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "X"
                print_board()

            elif one == 3 and (nums[2] == "O"):
                continue
            if one == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "X"
                print_board()

            elif one == 4 and (nums[3] == "O"):
                continue
            if one == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "X"
                print_board()

            elif one == 5 and (nums[4] == "O"):
                continue
            if one == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "X"
                print_board()

            elif one == 6 and (nums[5] == "O"):
                continue
            if one == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "X"
                print_board()

            elif one == 7 and (nums[6] == "O"):
                continue
            if one == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "X"
                print_board()

            elif one == 8 and (nums[7] == "O"):
                continue
            if one == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "X"
                print_board()

            elif one == 9 and (nums[8] == "O"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False

            break
        while valid:
            two = eval(
                input(f"Enter numbers through 1 and 9 only: { player2}: "))
            if two!= 1 and two !=2 and two!= 3 and two!= 4 and two!= 5 and two != 6 and two != 7 \
                and two != 8 and two != 9:
                continue
            if two == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "O"
                print_board()

            elif two == 1 and (nums[0] == "X"):
                continue
            if two == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "O"
                print_board()

            elif two == 2 and (nums[1] == "X"):
                continue
            if two == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "O"
                print_board()

            elif two == 3 and (nums[2] == "X"):
                continue
            if two == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "O"
                print_board()

            elif two == 4 and (nums[3] == "X"):
                continue
            if two == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "O"
                print_board()

            elif two == 5 and (nums[4] == "X"):
                continue
            if two == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "O"
                print_board()

            elif two == 6 and (nums[5] == "X"):
                continue
            if two == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "O"
                print_board()

            elif two == 7 and (nums[6] == "X"):
                continue
            if two == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "O"
                print_board()

            elif two == 8 and (nums[7] == "X"):
                continue
            if two == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "O"
                print_board()

            elif two == 9 and (nums[8] == "X"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False
            break
        while valid:
            one = eval(
                input(f"Enter numbers through 1 and 9 only: { player1}: "))
            if one!= 1 and one !=2 and one!= 3 and one!= 4 and one!= 5 and one != 6 and one != 7 \
                and one != 8 and one != 9:
                continue
            
            if one == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "X"
                print_board()

            elif one == 1 and (nums[0] == "O"):
                continue
            if one == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "X"
                print_board()

            elif one == 2 and (nums[1] == "O"):
                continue
            if one == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "X"
                print_board()

            elif one == 3 and (nums[2] == "O"):
                continue
            if one == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "X"
                print_board()

            elif one == 4 and (nums[3] == "O"):
                continue
            if one == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "X"
                print_board()

            elif one == 5 and (nums[4] == "O"):
                continue
            if one == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "X"
                print_board()

            elif one == 6 and (nums[5] == "O"):
                continue
            if one == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "X"
                print_board()

            elif one == 7 and (nums[6] == "O"):
                continue
            if one == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "X"
                print_board()

            elif one == 8 and (nums[7] == "O"):
                continue
            if one == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "X"
                print_board()

            elif one == 9 and (nums[8] == "O"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False

            break
        while valid:
            two = eval(
                input(f"Enter numbers through 1 and 9 only: { player2}: "))
            if two!= 1 and two !=2 and two!= 3 and two!= 4 and two!= 5 and two != 6 and two != 7 \
                and two != 8 and two != 9:
                continue
            if two == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "O"
                print_board()

            elif two == 1 and (nums[0] == "X"):
                continue
            if two == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "O"
                print_board()

            elif two == 2 and (nums[1] == "X"):
                continue
            if two == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "O"
                print_board()

            elif two == 3 and (nums[2] == "X"):
                continue
            if two == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "O"
                print_board()

            elif two == 4 and (nums[3] == "X"):
                continue
            if two == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "O"
                print_board()

            elif two == 5 and (nums[4] == "X"):
                continue
            if two == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "O"
                print_board()

            elif two == 6 and (nums[5] == "X"):
                continue
            if two == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "O"
                print_board()

            elif two == 7 and (nums[6] == "X"):
                continue
            if two == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "O"
                print_board()

            elif two == 8 and (nums[7] == "X"):
                continue
            if two == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "O"
                print_board()

            elif two == 9 and (nums[8] == "X"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False
            break
        while valid:
            one = eval(
                input(f"Enter numbers through 1 and 9 only: { player1}: "))
            if one!= 1 and one !=2 and one!= 3 and one!= 4 and one!= 5 and one != 6 and one != 7 \
                and one != 8 and one != 9:
                continue
            
            if one == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "X"
                print_board()

            elif one == 1 and (nums[0] == "O"):
                continue
            if one == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "X"
                print_board()

            elif one == 2 and (nums[1] == "O"):
                continue
            if one == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "X"
                print_board()

            elif one == 3 and (nums[2] == "O"):
                continue
            if one == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "X"
                print_board()

            elif one == 4 and (nums[3] == "O"):
                continue
            if one == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "X"
                print_board()

            elif one == 5 and (nums[4] == "O"):
                continue
            if one == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "X"
                print_board()

            elif one == 6 and (nums[5] == "O"):
                continue
            if one == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "X"
                print_board()

            elif one == 7 and (nums[6] == "O"):
                continue
            if one == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "X"
                print_board()

            elif one == 8 and (nums[7] == "O"):
                continue
            if one == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "X"
                print_board()

            elif one == 9 and (nums[8] == "O"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False

            break
        while valid:
            two = eval(
                input(f"Enter numbers through 1 and 9 only: { player2}: "))
            if two!= 1 and two !=2 and two!= 3 and two!= 4 and two!= 5 and two != 6 and two != 7 \
                and two != 8 and two != 9:
                continue
            if two == 1 and nums[0] != "O" and nums[0] != "X":
                nums[0] = "O"
                print_board()

            elif two == 1 and (nums[0] == "X"):
                continue
            if two == 2 and nums[1] != "O" and nums[1] != "X":
                nums[1] = "O"
                print_board()

            elif two == 2 and (nums[1] == "X"):
                continue
            if two == 3 and nums[2] != "O" and nums[2] != "X":
                nums[2] = "O"
                print_board()

            elif two == 3 and (nums[2] == "X"):
                continue
            if two == 4 and nums[3] != "O" and nums[3] != "X":
                nums[3] = "O"
                print_board()

            elif two == 4 and (nums[3] == "X"):
                continue
            if two == 5 and nums[4] != "O" and nums[4] != "X":
                nums[4] = "O"
                print_board()

            elif two == 5 and (nums[4] == "X"):
                continue
            if two == 6 and nums[5] != "O" and nums[5] != "X":
                nums[5] = "O"
                print_board()

            elif two == 6 and (nums[5] == "X"):
                continue
            if two == 7 and nums[6] != "O" and nums[6] != "X":
                nums[6] = "O"
                print_board()

            elif two == 7 and (nums[6] == "X"):
                continue
            if two == 8 and nums[7] != "O" and nums[7] != "X":
                nums[7] = "O"
                print_board()

            elif two == 8 and (nums[7] == "X"):
                continue
            if two == 9 and nums[8] != "O" and nums[8] != "X":
                nums[8] = "O"
                print_board()

            elif two == 9 and (nums[8] == "X"):
                continue

            if "X" == nums[0] and "X" == nums[1] and "X" == nums[2] \
                or ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                or ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                or ("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                or ("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                or ("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                or ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print(f"Player 1 {player1} has won the match!!!")
                valid = False
            if "O" == nums[0] and "O" == nums[1] and "O" == nums[2] \
                or ("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                or ("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                or ("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                or ("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                or ("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                or ("O" == nums[2] and "O" == nums[4] and "O" == nums[6]):
                print(f"Player 2 {player2} has won the match!!!")
                valid = False

            if not("O" == nums[0] and "O" == nums[1] and "O" == nums[2]) \
                and not("O" == nums[3] and "O" == nums[4] and "O" == nums[5]) \
                and not("O" == nums[6] and "O" == nums[7] and "O" == nums[8]) \
                and not("O" == nums[0] and "O" == nums[3] and "O" == nums[6]) \
                and not("O" == nums[1] and "O" == nums[4] and "O" == nums[7]) \
                and not("O" == nums[2] and "O" == nums[5] and "O" == nums[8]) \
                and not("O" == nums[0] and "O" == nums[4] and "O" == nums[8]) \
                and not ("O" == nums[2] and "O" == nums[4] and "O" == nums[6])\
                and not("X" == nums[0] and "X" == nums[1] and "X" == nums[2]) \
                and not ("X" == nums[3] and "X" == nums[4] and "X" == nums[5]) \
                and not ("X" == nums[6] and "X" == nums[7] and "X" == nums[8]) \
                and not ("X" == nums[0] and "X" == nums[3] and "X" == nums[6]) \
                and not("X" == nums[1] and "X" == nums[4] and "X" == nums[7]) \
                and not("X" == nums[2] and "X" == nums[5] and "X" == nums[8]) \
                and not("X" == nums[0] and "X" == nums[4] and "X" == nums[8]) \
                and not ("X" == nums[2] and "X" == nums[4] and "X" == nums[6]):
                print("Its a DRAW!!!")
                valid = False
            break
        game_continuation = input("Enter y to continue or N to exit: ").lower()



