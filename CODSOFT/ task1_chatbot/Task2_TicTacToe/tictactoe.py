board = [" " for x in range(9)]

def print_board():
    print()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def play():
    current_player = "X"

    for turn in range(9):
        print_board()

        move = int(input(f"Player {current_player}, enter position (0-8): "))

        if board[move] == " ":
            board[move] = current_player

            if check_winner(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                return

            current_player = "O" if current_player == "X" else "X"

        else:
            print("Position already taken!")

    print("It's a draw!")

play()