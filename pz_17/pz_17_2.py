#Создайте базовый класс "Фигура" со свойствами "ширина" и "высота".
# От этого класса унаследуйте классы "Прямоугольник" и "Квадрат".
# Для класса "Квадрат" переопределите методы, связанные с вычислением площади и периметра.
class Figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Figure):
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Figure):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.width * self.width

    def perimeter(self):
        return 4 * self.width


rectangle = Rectangle(5, 10)
print("Площадь прямоугольника:", rectangle.area())
print("Периметр прямоугольника:", rectangle.perimeter())

square = Square(7)
print("Площадь квадрата:", square.area())
print("Периметр квадрата:", square.perimeter())
