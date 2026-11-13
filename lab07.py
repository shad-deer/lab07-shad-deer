# Fill in the two functions and the two classes below (look for the TODO comments).
#
# Parts 1 and 2 must use RECURSION - a function that calls itself on a smaller version
# of the problem. Do NOT use a loop for those two.
#
# Do not rename anything, because the automated tests use these names.


def count_occurrences(target, values):
    if values == []:
        return 0
    if values[0] == target:
        count = 1
    else:
        count = 0
    return count + count_occurrences(target, values [1:])

def is_sorted(values):
    if len(values) <= 1:
        return True
    if values [0] > values[1]:
        return False
    return is_sorted(values[1:])

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        pass

    def area(self):
        return f'{self.__width * self.__height}'

    def perimeter(self):
        return f'{2 * (self.__width + self.__height)}'

    def __str__(self):
        return f'{self.__width}x{self.__height}'


class Square(Rectangle):   # Part 4 - stretch (optional)
    def __init__(self, side):
        # TODO: a Square is a Rectangle whose width and height are the same. Call the
        #   Rectangle constructor with `side` for both (use super().__init__(...)).
        #   area, perimeter, and __str__ are then inherited automatically.
        pass


def main():
    # Optional scratch space - try your work here, then run: python lab07.py
    print(count_occurrences(2, [1, 2, 2, 3, 2]))   # 3
    print(is_sorted([1, 2, 3]))                    # True
    print(Rectangle(3, 4).area())                  # 12
    # print(Square(5))                               # 5x5
    return


if __name__ == "__main__":
    main()
