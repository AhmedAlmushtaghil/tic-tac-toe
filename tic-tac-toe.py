# Initialize the board 

board = {'1': ' ' , '2': ' ' , '3': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '7': ' ' , '8': ' ' , '9': ' ' }

keys = []

for key in board:
    keys.append(key)

# Print the board 

def print_board(bd):
    print(bd['1'] + '    |   ' + bd['2'] + '  |   ' + bd['3'])
    print(' --- + ---- + --- ')
    print(bd['4'] + '    |   ' + bd['5'] + '  |   ' + bd['6'])
    print(' --- + ---- + --- ')
    print(bd['7'] + '    |   ' + bd['8'] + '  |   ' + bd['9'])

# Initialize the game

def game():
    player = 'X'
    turns = 0

    for i in range(10):
        print_board(board)
        print("Player: " + player + ", select a cell number. ")
        selection = input()

        if board[selection] == ' ':
            board[selection] = player
            turns += 1
        else:
            print("Cell is filled with " + player + ", select a different number. ")
            continue

