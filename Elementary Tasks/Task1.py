''' Chess board
Display a chessboard with the specified dimensions of height and width, according to the principle:
* * * * * *
   * * * * * *
* * * * * *
   * * * * * *
The program is launched by calling the main class with parameters.'''


import argparse


class ChessBoard:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def create_board(self):
        board = ""
        for i in range(self.height):
            if i % 2 == 0:
                board += "* " * (self.width // 2) + (self.width % 2) * "*" + "\n"
            else:
                board += " *" * (self.width // 2) + (self.width % 2) * " " + "\n"
        return board


def main():
    parser = argparse.ArgumentParser(description="Add sizes for a chess board")
    parser.add_argument("height", type=int, help="Height of board")
    parser.add_argument("width", type=int, help="Width of board")
    args = parser.parse_args()
    if args.height < 0 or args.width < 0:
        print("Height and width must be a positive number!")
    else:
        chess_board = ChessBoard(args.height, args.width)
        print(chess_board.create_board())


if __name__ == "__main__":
    main()
