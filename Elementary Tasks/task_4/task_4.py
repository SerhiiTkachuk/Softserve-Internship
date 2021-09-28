import argparse


"""File parser
You need to write a program that will have two modes:
Count the number of occurrences of a line in a text file.
Replace a string with another in the specified file
The program should accept arguments as input at startup:
<path to file> <line to count>
<file path> <search string> <replacement string>"""


class FileParser:
    def __init__(self, path):
        self.path = path

    def find_str(self, find_str):
        counter = 0
        try:
            with open(self.path, "r") as file:
                for line in file:
                    counter += line.count(find_str)
        except IOError:
            return "An IOError has occurred! Check the path to file, please!"
        else:
            return f'"{find_str}" was found {counter} times in this file - "{self.path}".'

    def replace_str(self, find_str, replace_str):
        try:
            with open(self.path, 'r') as f:
                old_data = f.read()
            new_data = old_data.replace(find_str, replace_str)
            with open(self.path, 'w') as f_new:
                f_new.write(new_data)
        except IOError:
            return "An IOError has occurred! Check the path to file, please!"
        else:
            return f'"{find_str}" was replaced on "{replace_str}", ' \
                   f'all changes was saved in a file "{self.path}".'

    def display_count(self):
        if self.replacement:
            print(self.replace_str())
        else:
            print(self.count_str())


def main():
    parser = argparse.ArgumentParser(description="Adding path to file")
    parser.add_argument("--path", type=str, help="Path", required=True)
    parser.add_argument("--string", type=str, help="String to count or to find for replacing", required=True)
    parser.add_argument("--replace", type=str, help="String to replace", default="")
    args = parser.parse_args()
    file_parser = FileParser(args.path)
    #return file_parser.display_count()
    if args.replace:
        print(file_parser.replace_str(args.string, args.replace))
    else:
        print(file_parser.find_str(args.string))


if __name__ == "__main__":
    main()
