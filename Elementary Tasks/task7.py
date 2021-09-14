'''  Number sequence
The program displays a series of natural numbers separated by commas, the square of which is less than a given n.
The program is launched by calling the main class with parameters.  '''


class Sequence():
    def __init__(self, n=0):
        self.n = input("Enter number: ")

    def seq_count(self):
        sequence = []
        try:
            self.n = int(self.n)
        except ValueError:
            return "The entered data must be a number!"
        else:
            for i in range(self.n):
                if i**2 < self.n:
                    sequence.append(i)
                else:
                    return sequence

test = Sequence()
print(test.seq_count())
