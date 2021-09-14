''' Chess board
Display a chessboard with the specified dimensions of height and width, according to the principle:
* * * * * *
   * * * * * *
* * * * * *
   * * * * * *
The program is launched by calling the main class with parameters.'''


class Chass_board():
    def __init__(self, height=0, width=0):
        self.height = input("Enter height of chess table: ")
        self.width = input("Enter width of chess table: ")
    def create_board(self):
        board = ""
        try:
            self.height = int(self.height)
            self.width = int(self.width)
        except ValueError:
            return "Height and width must be integers!"
        else:    
            for i in range(self.height):
                if i%2 == 0:
                    board += "*"*self.width + "\n"
                else:
                    board += " " + ("*" * self.width) + "\n"
            return board


chass_table = Chass_board()
print(chass_table.create_table())
