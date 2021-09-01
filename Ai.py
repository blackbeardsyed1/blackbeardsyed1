import random
import copy
array = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]

]


def PrintlettertterAtPosition(letter, row, col):
    array[row][col] = letter


def toss():
    a = random.randint(0, 1)
    if a == 0:
        return True

    else:
        return False


def symbol_player(sym):
    return sym.upper()


def computer_symbol():
    if xn == "X":
        return "O"
    else:
        return "X"


def spaceIsFree(row, col):
    return array[row][col] == ' '


def printGrid(array):
    print('   |   |')
    print(' ' + array[0][0] + ' | ' + array[0][1] + ' | ' + array[0][2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + array[1][0] + ' | ' + array[1][1] + ' | ' + array[1][2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + array[2][0] + ' | ' + array[2][1] + ' | ' + array[2][2])
    print('   |   |')


def isWinner(array, letter):
    return (array[2][0] == letter and array[2][1] == letter and array[2][2] == letter) or (array[1][0] == letter and array[1][1] == letter and array[1][2] == letter) or (array[0][0] == letter and array[0][1] == letter and array[0][2] == letter) or (array[0][0] == letter and array[1][0] == letter and array[2][0] == letter) or (array[0][1] == letter and array[1][1] == letter and array[2][1] == letter) or (array[0][2] == letter and array[1][2] == letter and array[2][2] == letter) or (array[0][0] == letter and array[1][1] == letter and array[2][2] == letter) or (array[0][2] == letter and array[1][1] == letter and array[2][0] == letter)


def playerMove():
    valid = True
    while valid:
        move = input(
            "Please select a position in row " + " " + name + " " + f"to place an {xn} (1-3) : ")
        move2 = input(
            "Please select a position in colomn " + " " + name + " " + f"to place an {xn} (1-3) : ")
        try:
            one = int(move) - 1
            two = int(move2) - 1
            if one >= 0 and one < 3 and two >= 0 and two < 3:
                if spaceIsFree(one, two):
                    valid = False
                    PrintlettertterAtPosition(xn, one, two)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def compMove():
    possiblemoves = array
    move = 0

    for let in [computer_symbol(), xn]:
        for i in range(0, 3):
            boardCopy = copy.deepcopy(array)
            if boardCopy[0][i] == " ":
                boardCopy[0][i] = let
            if isWinner(boardCopy, let):
                row = 0
                coloumn = i
                return row, coloumn

    for let in [computer_symbol(), xn]:
        for i in range(0, 3):
            boardCopy = copy.deepcopy(array)
            if boardCopy[1][i] == " ":
                boardCopy[1][i] = let
            if isWinner(boardCopy, let):
                row = 1
                coloumn = i
                return row, coloumn

    for let in [computer_symbol(), xn]:
        for i in range(0, 3):
            boardCopy = copy.deepcopy(array)
            if boardCopy[2][i] == " ":
                boardCopy[2][i] = let
            if isWinner(boardCopy, let):
                row = 2
                coloumn = i
                return row, coloumn

        # Checking corners

    if possiblemoves[0][0] == " ":
        return 0, 0
    if possiblemoves[0][2] == " ":
        return 0, 2
    if possiblemoves[2][2] == " ":
        return 2, 2
    if possiblemoves[2][0] == " ":
        return 2, 0

    if possiblemoves[1][1] == " ":
        return 1, 1

    # Checking Edges

    c = random.randint(0, 3)
    # if possiblemoves[0][1] == " ":
    if c == 3:
        return 0, 1
    # if possiblemoves[1][0] == " ":
    if c == 0:
        return 1, 0
    # if possiblemoves[1][2] == " ":
    if c == 2:
        return 1, 2
    # if possiblemoves[2][1] == " ":
    if c == 1:
        return 2, 1

    return move


def isBoardFull(array):
    count = 0
    for i in range(3):
        if " " in array[i]:
            count += 1

    if count == 0:
        return True
    else:
        return False


def main():

    print('Welcome to Tic Tac Toe!')
    if toss():
        y = 0
        print("Player won the toss!")
    else:
        y = 1
        print("Computer won the toss!")
    global name
    name = input("Enter your name ! ")

    sym = input(f"Enter your symbol {name}! ")
    global xn
    xn = symbol_player(sym)
    printGrid(array)
    while True:

        if y == 0:
            if not(isWinner(array, computer_symbol())):
                playerMove()
                printGrid(array)

            else:
                print(f'Sorry! Computer , {computer_symbol()} won this time!')
                break
            if isBoardFull(array):
                print('Tie Game!')
                break
        if not(isWinner(array, xn)):
            row, col = compMove()
            if compMove() == 0:
                print('Tie Game!')
                break
            else:
                PrintlettertterAtPosition(computer_symbol(), row, col)
                print(
                    f'Computer placed an {computer_symbol()} in position', row+1, col+1, ':')
                printGrid(array)

        else:
            print(f'{name} won this time! Good Job!')
            break
        if y == 1:
            if not(isWinner(array, computer_symbol())):
                playerMove()
                printGrid(array)
            else:
                print(f'Sorry Computer, {computer_symbol()} won this time!')
                break

        if isBoardFull(array):
            print('Tie Game!')
            break


main()


while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]

        ]
        print('-----------------------------------')
        main()
    else:
        break
