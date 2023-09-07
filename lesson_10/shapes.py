from inspect import signature
from typing import Protocol
from math import pi


class CanCalculateArea(Protocol):
    def calculate_area(self) -> float:
        ...


class Circle:
    def __init__(self, radius: int) -> None:
        self.radius: int = radius

    def calculate_area(self) -> float:
        return pi * self.radius**2

# Square.__init__(c1, 4).
# Square.calculate_area(c1).

class Square:
    def __init__(self, side: int) -> None:
        self.name = "John"
        self.side: int = side
        self.calculate_area()

    def calculate_area(self) -> float:
        # self.calculate_area()
        # self.__init__(12)
        return self.side**2


class Diamond:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def calculate_area(self) -> float:
        return self.a * self.b


class Validator:
    def validate_shape(
        self, shape: CanCalculateArea, max_limit: float
    ) -> CanCalculateArea:
        if shape.calculate_area() > max_limit:
            raise ValueError("The area is too big")

        return shape


def main():
    c1 = Circle(radius=12)
    s1 = Square(side=10)
    # d1 = Diamond(a=19, b=12)

    validator = Validator()
    # Validator.validate_shape(validator, c1, 122)
    shape1 = validator.validate_shape(c1, 1222)
    shape2 = validator.validate_shape(s1, 1323)
    # shape3 = validator.validate_shape("Hello", 1323)

    print(shape1)
    print(shape2)
    print(signature(Validator.validate_shape))


main()