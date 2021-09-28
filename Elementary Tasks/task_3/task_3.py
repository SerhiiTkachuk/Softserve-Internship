class Triangles:
    def __init__(self, list_of_triangles):
        self.list_of_triangles = list_of_triangles

    def count_square(self):
        square_of_triangles = []
        for triangles in self.list_of_triangles:
            p = (triangles[1] + triangles[2] + triangles[3]) / 2
            square = (p * (p - triangles[1]) * (p - triangles[2]) * (p - triangles[3])) ** 0.5
            square_of_triangles.append((triangles[0], square))
        return square_of_triangles

    def sort_squares(self):
        square_of_triangles = self.count_square()
        return sorted(square_of_triangles, key=lambda last: last[-1], reverse=True)

    def display(self):
        list_triangles = self.sort_squares()
        print("="*15 + " Triangles list: " + "="*15)
        for i in range(len(list_triangles)):
            print(f"{i + 1}. [Triangle {list_triangles[i][0]}]: {round(list_triangles[i][1], 2)} cm")


def main():
    checked_list = []
    while True:
        triangle = input("Enter name of triangle and dimensions of it's sides(separate by coma): ")
        triangle_list = triangle.split(',')
        if len(triangle_list) != 4:
            print("Must be four parameters separated by coma(name of triangle, side1, side2, side3). Try more time, please")
            continue
        name = triangle_list[0]
        try:
            side_a = float(triangle_list[1])
            side_b = float(triangle_list[2])
            side_c = float(triangle_list[3])
        except ValueError:
            print("Dimensions of sides must be numbers! Please, put correct dimensions.")
            continue
        if side_a < 0 or side_b < 0 or side_c < 0:
            print("All sides of triangle must be positive numbers! Please, put correct dimensions.")
        elif side_a+side_b <= side_c or side_a+side_c <= side_b or side_b+side_c <= side_a:
            print("Triangle with these sides doesn't exist! Please, put correct dimensions.")
        else:
            checked_list.append((name, side_a, side_b, side_c))
        new_triangle = input('If you want to add new triangle type "y" or "yes": ')
        if new_triangle.lower() == "y" or new_triangle.lower() == "yes":
            continue
        else:
            break
    test = Triangles(checked_list)
    return test.display()


if __name__ == "__main__":
    main()
