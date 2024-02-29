"""
Напишите класс Rectangle, имеющий следующие методы:

- __init__(self, width, height): конструктор, принимающий ширину и высоту прямоугольника
- area(self): метод, возвращающий площадь прямоугольника
- perimeter(self): метод, возвращающий периметр прямоугольника
- from_diagonal(cls, diagonal, aspect_ratio): класс-метод, принимающий диагональ прямоугольника и соотношение сторон и возвращающий объект класса Rectangle
- is_square(width, height): статический метод, принимающий ширину и высоту прямоугольника и возвращающий True,
если это квадрат, и False в противном случае
"""


class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def area(self) -> (int, float):
        """Возвращает площадь прямоугольника."""
        return self.height * self.width

    def perimeter(self) -> (int, float):
        """Возвращает периметр прямоугольника."""
        return 2 * (self.width + self.height)

    @classmethod
    def from_diagonal(cls, diagonal, aspect_ratio):
        """Принимает диагональ прямоугольника и соотношение сторон и возвращающий объект класса Rectangle."""
        a = diagonal
        return cls()

    @staticmethod
    def is_square(width, height) -> bool:
        """
        Возвращает True, если это квадрат, и False в противном случае
        :param width: ширина прямоугольника
        :param height: высота прямоугольника
        :return: bool
        """
        if width == height:
            return True
        return False


# код для проверки
rectangle = Rectangle(4, 5)
print(rectangle.area())  # 20
print(rectangle.perimeter())  # 18

rectangle2 = Rectangle.from_diagonal(5, 2)
print(rectangle2.area())  # 10.0128
print(rectangle2.perimeter())  # 13.42

print(Rectangle.is_square(4, 4))  # True
print(Rectangle.is_square(4, 5))  # False
