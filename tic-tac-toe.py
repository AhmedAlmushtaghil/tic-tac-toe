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

print_board(board)
