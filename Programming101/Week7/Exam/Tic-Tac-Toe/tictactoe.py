from AI import AI
from tictactoe_help import board, board_coordinates


def main():
    computer = AI(board, board_coordinates)
    print ("Welcome to Tic Tac Toe! Player is 'X', CPU is 'O'.")
    computer.print_board()
    game_won = False

    while game_won is False:
        if computer.check_board_for_winner():
            break

        print ("Player's turn...")
        computer.get_free_spots()
        player_move = int(input("Enter your field number: "))
        GPS = computer.coordinates[player_move]
        while computer.board[GPS[0]][GPS[1]] != ".":
            player_move = int(input("Enter valid field number: "))
            GPS = computer.coordinates[player_move]
        computer.board[GPS[0]][GPS[1]] = "X"
        computer.available_spots.remove(computer.coordinates[player_move])
        computer.print_board()

        print ("CPU's turn ...")
        computer.get_free_spots()
        computer.move()
        computer.print_board()

        game_won = computer.check_board_for_winner()
        if computer.get_free_spots() == [] and game_won is False:
            print("Round draw.")
            break

if __name__ == "__main__":
    main()
