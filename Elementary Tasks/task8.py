''' Fibonacci series for a range
The program allows you to display all Fibonacci numbers that are in the specified range. The range is given by two arguments when calling the main class. 
Numbers are displayed separated by commas in ascending order. '''


class Fibonacci:
    def __init__(self, a=0, b=0):
        self.a = input("Enter first number: ")
        self.b = input("Enter second number: ")

    def fib_num(self):
        try:
            self.a = int(self.a)
            self.b = int(self.b)
        except ValueError:
            return "The entered data must be numbers!"
        else:
            if self.a>self.b:
                return "The first number must be less then second!"
            else:
                fib_seq = [0,1,1]
                fib_1,fib_2 = 1,1
                while fib_2 < self.b:
                    fib_1,fib_2 = fib_2, fib_1+fib_2
                    fib_seq.append(fib_2)
                num_seq = [i for i in range(self.a,self.b+1)]
                return list(filter(lambda i: i in fib_seq, num_seq))

test = Fibonacci()
print(test.fib_num())
