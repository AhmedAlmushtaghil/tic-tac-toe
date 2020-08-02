# Initialize the board 

board = {'1': ' ' , '2': ' ' , '3': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '7': ' ' , '8': ' ' , '9': ' ' }

keys = []

for key in board:
    keys.append(key)

# Print the board 

def print_board(brd):
    print('  ' + brd['1'] + '  |  ' + brd['2'] + '  |  ' + brd['3'])
    print(' --- + --- + --- ')
    print('  ' + brd['4'] + '  |  ' + brd['5'] + '  |  ' + brd['6'])
    print(' --- + --- + --- ')
    print('  ' + brd['7'] + '  |  ' + brd['8'] + '  |  ' + brd['9'])

# Initialize the game
def play_game():
    player = 'X'
    turns = 0

    for i in range(10):
        print_board(board)
        print("\nPlayer " + player + ", select a cell number.\n")
        selection = input()

        if board[selection] == ' ':
            board[selection] = player
            turns += 1
        else:
            print("\nCell is filled with " + player + ", select a different number.\n")
            continue

        check_winner(board, turns, player)

        # Switch turn to the other player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

def check_winner(brd, trns, plyr):
    # A win will happen after at least 5 turns
    if trns > 4 and trns < 9:
        # Check all winning possibilities
        # Horizontal
        if board['1'] == board['2'] == board['3']: 
            win_message(brd, plyr)
        elif board['4'] == board['5'] == board['6']: 
            win_message(brd, plyr)
        elif board['7'] == board['8'] == board['9']: 
            win_message(brd, plyr)
        
        # Vertical
        elif board['1'] == board['4'] == board['7']: 
            win_message(brd, plyr)
        elif board['2'] == board['5'] == board['8']: 
            win_message(brd, plyr)
        elif board['3'] == board['6'] == board['9']: 
            win_message(brd, plyr)
        
        # Diagonal
        elif board['1'] == board['5'] == board['9']: 
            win_message(brd, plyr)
        elif board['3'] == board['5'] == board['7']: 
            win_message(brd, plyr)

    # Check the tie possibility
    elif trns == 9:
        print_board(brd)
        print("\nThe game has ended.")
        print("The result is a TIE.")

# Create win message
def win_message(brd, plyr):
    print_board(brd)
    print("\nThe game has ended.")
    print("Congratulations! Player " + plyr + " has WON.")

if __name__ == "__main__":
    play_game()