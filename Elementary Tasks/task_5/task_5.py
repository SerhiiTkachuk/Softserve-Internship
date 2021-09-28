import argparse

"""Number in words
You need to convert an integer to uppercase: 12 - twelve. 
The program is launched by calling the main class with parameters."""


class NumberInWords:
    def __init__(self, n, num_dict):
        self.n = n
        self.num_dict = num_dict

    def get_tenth_and_less(self, num):
        if num < 10:
            return self.num_dict['0-9'].get(num)
        elif 10 < num < 20:
            return self.num_dict['11-19'].get(num)
        elif num >= 10 and num in self.num_dict['10-90']:
            return self.num_dict['10-90'].get(num)
        else:
            n_1 = num % 10
            n_10 = num - n_1
            return self.num_dict['10-90'].get(n_10) + ' ' + self.num_dict['0-9'].get(n_1)

    def get_hundred(self, num):
        n_100 = (num // 100) * 100
        n_1 = int(n_100 / 100)
        return self.num_dict['0-9'].get(n_1) + ' ' + self.num_dict['more_than_100'].get(100) + ' ' \
        + self.get_tenth_and_less((num - n_100))

    def get_thousand(self, num):
        n_1000 = (num // 1000) * 1000
        n_1 = int(n_1000 / 1000)
        if len(str(n_1)) == 3:
            return self.get_hundred(n_1) + ' ' + self.num_dict['more_than_100'].get(1000) + ' '\
                   + self.get_hundred(num - n_1000)
        elif len(str(n_1)) == 2:
            return self.get_tenth_and_less(n_1) + ' ' + self.num_dict['more_than_100'].get(1000) + ' '\
                   + self.get_hundred(num - n_1000)
        else:
            return self.num_dict['0-9'].get(n_1) + ' ' + self.num_dict['more_than_100'].get(1000) + ' '\
            + self.get_hundred(num - n_1000)

    def get_mill(self, num):
        n_mill = (num // 10 ** 6) * 10 ** 6
        n_1 = int(n_mill / 10 ** 6)
        if len(str(n_1)) == 3:
            return self.get_hundred(n_1) + ' ' + self.num_dict['more_than_100'].get(10**6) + ' ' \
                   + self.get_thousand(num - n_mill)
        elif len(str(n_1)) == 2:
            return self.get_tenth_and_less(n_1) + ' ' + self.num_dict['more_than_100'].get(10**6) + ' ' \
                   + self.get_thousand(num - n_mill)
        else:
            return self.num_dict['0-9'].get(n_1) + ' ' + self.num_dict['more_than_100'].get(10**6) + ' ' \
            + self.get_thousand(num - n_mill)

    def get_bill(self, num):
        n_bill = (num // 10 ** 9) * 10 ** 9
        n_1 = int(n_bill / 10**9)
        if len(str(n_1)) == 3:
            return self.get_hundred(n_1) + ' ' + self.num_dict['more_than_100'].get(10**9) + ' ' \
                   + self.get_mill(num - n_bill)
        elif len(str(n_1)) == 2:
            return self.get_tenth_and_less(n_1) + ' ' + self.num_dict['more_than_100'].get(10**9) + ' ' \
                   + self.get_mill(num - n_bill)
        else:
            return self.num_dict['0-9'].get(n_1) + ' ' + self.num_dict['more_than_100'].get(10**9) + ' ' \
            + self.get_mill(num - n_bill)

    def display_number(self):
        if len(str(self.n)) <= 2:
            return self.get_tenth_and_less(self.n)
        elif len(str(self.n)) <= 3:
            return self.get_hundred(self.n)
        elif len(str(self.n)) <= 6:
            return self.get_thousand(self.n)
        elif len(str(self.n)) <= 9:
            return self.get_mill(self.n)
        elif len(str(self.n)) <= 12:
            return self.get_bill(self.n)
        else:
            return "This is __B-A-Z-I-L-L-I-O-N__!"


def main():
    one = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
           6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    tenth = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty',
             50: 'fifty', 60: 'sixty', 70: 'seventy',
             80: 'eighty', 90: 'ninety'}
    two = {11: 'eleven', 12: 'twelve', 13: 'thirteen',
           14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
           17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    big_number = {100: 'hundred', 1000: 'thousand',
                  10 ** 6: 'million', 10 ** 9: 'billion'}
    num_dict = {'0-9': one, '10-90': tenth, '11-19': two, 'more_than_100': big_number}
    parser = argparse.ArgumentParser(description="Add number to convert it to word!")
    parser.add_argument("number", type=int, help="number")
    args = parser.parse_args()
    if args.number < 0:
        test = NumberInWords(abs(args.number), num_dict)
        print('minus' + ' ' + test.display_number())
    else:
        test = NumberInWords(args.number, num_dict)
        print(test.display_number())


if __name__ == '__main__':
    main()
