import argparse

"""Fibonacci series for a range
The program allows you to display all Fibonacci numbers that are in the specified range.
 The range is given by two arguments when calling the main class.
 Numbers are displayed separated by commas in ascending order."""


class Fibonacci:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def create_sequence(self):
        fib_1, fib_2 = 0, 1
        new_sequence = []
        while fib_2 <= self.b:
            if fib_1 >= self.a:
                if not new_sequence:
                    new_sequence.append(fib_1)
                new_sequence.append(fib_2)
            fib_1, fib_2 = fib_2, fib_1 + fib_2
        return new_sequence


def main():
    parser = argparse.ArgumentParser(description="Add a range for Fibonacci series")
    parser.add_argument("a", type=int, help="First number of range")
    parser.add_argument("b", type=int, help="Second number of range")
    args = parser.parse_args()
    if args.a < 0 or args.b < 0:
        print("Numbers must be positive!")
    else:
        if args.a > args.b:
            args.a, args.b = args.b, args.a
        test = Fibonacci(args.a, args.b)
        print(test.create_sequence())


if __name__ == "__main__":
    main()
