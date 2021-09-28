import argparse

'''  Number sequence
The program displays a series of natural numbers separated by commas, the square of which is less than a given n.
The program is launched by calling the main class with parameters.  '''


class Sequence:
    def __init__(self, n):
        self.n = n

    def seq_count(self):
        sequence = []
        for i in range(self.n):
            if i**2 < self.n:
                sequence.append(i)
            else:
                return sequence


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, help="Number")
    args = parser.parse_args()
    if args.n < 0:
        print("Number must be positive!")
    else:
        test = Sequence(args.n)
        print(test.seq_count())


if __name__ == "__main__":
    main()
