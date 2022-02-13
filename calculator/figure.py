from math import pi

from environs import Env

import config

from interface import Shape


env = Env()
env.read_env()


class Circle(Shape):

    name = 'Круг'
    image_filepath = env('CIRCLE_IMAGE_FILEPATH')
    characteristics = [
        config.Characteristic.AREA.value,
    ]

    def __init__(self, radius=1):
        super().__init__()
        self.radius = radius

    def area(self):
        area_v = pi * self.radius ** 2
        return area_v


class Square(Shape):

    name = 'Квадрат'
    image_filepath = env('SQUARE_IMAGE_FILEPATH')
    characteristics = [
        config.Characteristic.AREA.value,
        config.Characteristic.PERIMETER.value,
    ]

    def __init__(self, side=1):
        super().__init__()
        self.side = side

    def area(self):
        area_v = self.side ** 2
        return area_v

    def perimeter(self):
        perimeter_v = 4 * self.side
        return perimeter_v


class Rectangle(Square):

    name = 'Прямоугольник'
    image_filepath = env('RECTANGLE_IMAGE_FILEPATH')
    characteristics = [
        config.Characteristic.AREA.value,
        config.Characteristic.PERIMETER.value,
    ]

    def __init__(self, side_first=1, side_second=1):
        super().__init__(side_first)
        self.side_second = side_second

    def area(self):
        area_v = self.side * self.side_second
        return area_v

    def perimeter(self):
        perimeter_v = 2 * (self.side + self.side_second)
        return perimeter_v


class Triangle(Shape):

    name = 'Треугольник'
    image_filepath = env('TRIANGLE_IMAGE_FILEPATH')
    characteristics = [
        config.Characteristic.AREA.value,
    ]

    def __init__(self, side_first=1, side_second=1, side_third=1):
        super().__init__()
        self.side_first = side_first
        self.side_second = side_second
        self.side_third = side_third

    def area(self):
        half_perimeter = self.perimeter() / 2
        area_v = (
            (half_perimeter *
            (half_perimeter - self.side_first) *
            (half_perimeter - self.side_second) *
            (half_perimeter - self.side_third)) ** 0.5
        )
        return area_v

    def perimeter(self):
        perimeter_v = self.side_first + self.side_second + self.side_third
        return perimeter_v


class Trapezoid(Rectangle):

    name = 'Трапеция'
    image_filepath = env('TRAPEZOID_IMAGE_FILEPATH')
    characteristics = [
        config.Characteristic.AREA.value,
    ]

    def __init__(self, side_first=1, side_second=1, height=1):
        super().__init__(side_first, side_second)
        self.height = height

    def area(self):
        perimeter = super().perimeter()
        area_v = (perimeter / 4) * self.height
        return area_v


class Rhombus(Square):

    name = 'Ромб'
    image_filepath = env('RHOMBUS_IMAGE_FILEPATH')
    characteristics = [
        config.Characteristic.AREA.value,
    ]

    def __init__(self, side_first=1, height=1):
        super().__init__(side_first)
        self.height = height

    def area(self):
        area_v = self.side * self.height
        return area_v


class Sphere(Circle):

    name = 'Сфера'
    image_filepath = env('SPHERE_IMAGE_FILEPATH')
    characteristics = [
        config.Characteristic.AREA.value,
        config.Characteristic.VOLUME.value,
    ]

    def area(self):
        area_v = 4 * pi * self.radius ** 2
        return area_v

    def volume(self):
        volume_v = 4 / 3 * pi * self.radius ** 3
        return volume_v


class Cube(Square):

    name = 'Куб'
    image_filepath = env('CUBE_IMAGE_FILEPATH')
    characteristics = [
        config.Characteristic.AREA.value,
        config.Characteristic.VOLUME.value,
    ]

    def area(self):
        area_v = 6 * self.side ** 2
        return area_v

    def volume(self):
        volume_v = self.side ** 3
        return volume_v


class Parallelepiped(Rectangle):

    name = 'Параллелепипед'
    image_filepath = env('PARALLELEPIPED_IMAGE_FILEPATH')
    characteristics = [
        config.Characteristic.AREA.value,
    ]

    def __init__(self, side_first=1, side_second=1, side_third=1):
        super().__init__(side_first, side_second)
        self.side_third = side_third

    def area(self):
        area_v = (
            2 * (self.side * self.side_second +
                 self.side_second * self.side_third +
                 self.side * self.side_third)
        )
        return area_v


class Pyramid(Shape):

    name = 'Пирамида'
    image_filepath = env('PYRAMID_IMAGE_FILEPATH')
    characteristics = [
        config.Characteristic.AREA.value,
    ]

    def __init__(self, perimeter=1, apothem=1):
        super().__init__()
        self.perimeter = perimeter
        self.apothem = apothem

    def area(self):
        area_v = 1 / 2 * self.perimeter * self.apothem
        return area_v


class Cylinder(Circle):

    name = 'Цилиндр'
    image_filepath = env('CYLINDER_IMAGE_FILEPATH')
    characteristics = [
        config.Characteristic.AREA.value,
    ]

    def __init__(self, radius=1, height=1):
        super().__init__(radius)
        self.height = height

    def area(self):
        area_v = 2 * pi * self.radius * (self.height + self.radius)
        return area_v


class Cone(Circle):

    name = 'Конус'
    image_filepath = env('CONE_IMAGE_FILEPATH')
    characteristics = [
        config.Characteristic.AREA.value,
    ]

    def __init__(self, radius=1, slant_height=1):
        super().__init__(radius)
        self.slant_height = slant_height

    def area(self):
        area_v = pi * self.radius * (self.slant_height + self.radius)
        return area_v
