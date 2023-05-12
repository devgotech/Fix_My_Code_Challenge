#!/usr/bin/env python3

class Square():
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Return the area of the square."""
        return self.width * self.width

    def perimeter_of_my_square(self):
        """Return the perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Return a string representation of the square."""
        return "Square(width={}, height={})".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
