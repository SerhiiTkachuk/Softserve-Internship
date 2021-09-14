''' Analysis of envelopes
There are two envelopes with sides (a, b) and (c, d) to determine if one envelope can be nested inside the other.
The program must handle floating point input. The program asks the user for the envelope sizes one parameter at a time.
After each calculation, the program asks the user if he wants to continue. If the user answers “y” or “yes” (case insensitive),
the program continues from the beginning, otherwise it exits. '''


def envelope():
    start_game = "YES"
    while start_game.upper().startswith("Y"):
        try:
            side_a = float(input("Enter dimension of first side of first envelope: "))
            side_b = float(input("Enter dimension of second side of first envelope: "))
            side_c = float(input("Enter dimension of first side of second envelope: "))
            side_d = float(input("Enter dimension of second side of second envelope: "))
        except ValueError:
            print("Dimension must be a number!")
        else:
            if side_a>side_c and side_b>side_d or side_a>side_d and side_b>side_c:
                print("We can put second envelope in first!")
            elif side_c>side_a and side_d>side_b or side_d>side_a and side_c>side_b:
                print("We can put first envelope in second!")
            else:
                print("We can't put an envelope to another one!")
        finally:
            start_game = input('If you want to continue type "yes" or "y", if you want to exit type something else: ')
                           
    
envelope()
