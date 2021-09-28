import argparse


"""Lucky tickets.
There are 2 ways to count lucky tickets:
1. Moscow - if a six-digit number is printed on the bus ticket, and the sum of the first three digits is equal
to the sum of the last three, then this ticket is considered lucky.
2. Leningrad or St. Petersburg - if the sum of the even digits of the ticket is equal to the sum of the odd digits
of the ticket, then the ticket is considered lucky.
Task:
The ticket number is a six-digit number. We need to write a console application that can count the number of lucky
tickets. To select the calculation algorithm, a text file is read. The path to the text file is set in the console
after starting the program. Algorithm indicators:
1 - the word 'Moskow'
2 - the word 'Piter'
After setting all the necessary parameters, the program should display the number of lucky tickets for the specified
counting method to the console."""


class LuckyTicketCounter:

    def __init__(self, path):
        self.path = path

    def calculate_lucky_tickets(self):
        lucky_m = 0
        lucky_l = 0
        try:
            with open(self.path, "r") as file:
                for line in file:
                    number = line[:6]
                    if "Moscow" in line:
                        lucky_m += self.select_lucky_moscow_ticket(number)
                    elif "Piter" in line:
                        lucky_l += self.select_lucky_piter_ticket(number)
                    else:
                        lucky_m += self.select_lucky_moscow_ticket(number)
                        lucky_l += self.select_lucky_piter_ticket(number)
        except IOError:
            return "Check file path!"
        except ValueError:
            return "Number of ticket must be integers!"
        else:
            return f'There are {lucky_m} Moscow\'s and {lucky_l} Piter\'s lucky ticket(s) in this file "{self.path}"'

    @staticmethod
    def select_lucky_moscow_ticket(number):
        lucky_ticket = 0
        if int(number[0])+int(number[1])+int(number[2]) == int(number[3])+int(number[4])+int(number[5]):
            lucky_ticket += 1
        return lucky_ticket

    @staticmethod
    def select_lucky_piter_ticket(number):
        lucky_ticket = 0
        if int(number[0]) + int(number[2]) + int(number[4]) == int(number[1]) + int(number[3]) + int(number[5]):
            lucky_ticket += 1
        return lucky_ticket


def main():
    parser = argparse.ArgumentParser(description="Adding path to file")
    parser.add_argument("--path", type=str, help="Path to file", required=True)
    args = parser.parse_args()

    lucky_counter = LuckyTicketCounter(args.path)
    print(lucky_counter.calculate_lucky_tickets())


if __name__ == "__main__":
    main()
