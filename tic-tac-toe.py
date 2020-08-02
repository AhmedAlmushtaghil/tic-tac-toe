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

        # A win will happen after at least 5 turns
        if turns >= 5:
            # Check all winning possibilities
            # Horizontal
            if board['1'] == board['2'] == board['3'] == player: 
                win_message(board, player)
                break
            elif board['4'] == board['5'] == board['6'] == player: 
                win_message(board, player)
                break
            elif board['7'] == board['8'] == board['9'] == player: 
                win_message(board, player)
                break
            
            # Vertical
            elif board['1'] == board['4'] == board['7'] == player: 
                win_message(board, player)
                break
            elif board['2'] == board['5'] == board['8'] == player: 
                win_message(board, player)
                break
            elif board['3'] == board['6'] == board['9'] == player: 
                win_message(board, player)
                break
            
            # Diagonal
            elif board['1'] == board['5'] == board['9'] == player: 
                win_message(board, player)
                break
            elif board['3'] == board['5'] == board['7'] == player: 
                win_message(board, player)
                break

            # Check the tie possibility
            elif turns == 9:
                print_board(board)
                print("\nThe game has ended.y")
                print("\nThe result is a TIE.")
                break

        # Create win message
        def win_message(brd, plyr):
            print_board(brd)
            print("\nThe game has ended.")
            print("\nCongratulations! Player " + plyr + " has WON.")

        # Switch turn to the other player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

    # Restart game
    print("\nDo you want to play again? (y/n)")
    restart_game = input()
    if restart_game == 'y':
        for key in keys:
            board[key] = ' '
        play_game()

if __name__ == "__main__":
    play_game()