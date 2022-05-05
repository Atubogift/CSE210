# Atubo T. Gift
# CSE210-01_TicTacToe

# The characters used in the Tic-Tac-Too board.
X = "X"
O = "O"

# A blank Tic-Tac-Toe board used to reset the board to blank.
blank_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def display_instructions(board):
    """Display instructions for the game."""

    print("Enter a number from 1 to 9. The current board is:")
    display_board(board)


def display_board(board):
    """Display a Tic-Tac-Toe board on the screen in a user-friendly way."""

    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")


def play_game(board):
    """Handle game play."""

    x_turn = True

    while not game_done(board, True):

        # Initialize loop condition.
        is_valid_input = False

        while not is_valid_input:

            if x_turn:
                # Prompt user for input.
                input_string = input("X's turn to choose a square (1-9):")

            else:
                # Prompt user for input.
                input_string = input("O's turn to choose a square (1-9):")

            # Validate user input.
            try:
                input_int = int(input_string)

                # Input is invalid if out of range.
                if input_int < 1 or input_int > 9:
                    is_valid_input = False
                    display_instructions(board)

                # Input is invalid if space is not available.
                elif board[input_int - 1] != X or O:
                    # Terminate loop.
                    is_valid_input = True

                else:
                    is_valid_input = False
                    display_instructions(board)

            except:
                is_valid_input = False
                display_instructions(board)

        if x_turn:
            board[input_int - 1] = X
            x_turn = False
            display_board(board)

        else:
            board[input_int - 1] = O
            x_turn = True
            display_board(board)

    return False

def game_done(board, message=False):
    """Determine if the game is finished."""

    # Game is finished if someone has completed a row.
    for row in range(3):
        if (
            board[row * 3] == (X or O)
            and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]
        ):
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] == (X or O) and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] == (X or O) and (
        board[0] == board[4] == board[8] or board[2] == board[4] == board[6]
    ):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square != (X or O):
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True

    return False


def main():

    board = blank_board
    display_instructions(board)
    play_game(board)



if __name__ == "__main__":
    main()