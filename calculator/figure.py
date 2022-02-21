from math import pi

from environs import Env

from interface import ShapeInterface


env = Env()
env.read_env()


class Shape(ShapeInterface):
    def __init__(self, name, params: dict = None):
        self.name = name
        self.params = params or {}

    @classmethod
    def concrete(cls, config_):
        return cls(**config_)

    @staticmethod
    def circle_area(radius):
        area_v = pi * radius ** 2
        return area_v

    @staticmethod
    def square_area(side_first):
        area_v = side_first ** 2
        return area_v

    @staticmethod
    def square_perimeter(side_first):
        perimeter_v = 4 * side_first
        return perimeter_v

    @staticmethod
    def rectangle_area(side_first, side_second):
        area_v = side_first * side_second
        return area_v

    @staticmethod
    def rectangle_perimeter(side_first, side_second):
        perimeter_v = 2 * (side_first + side_second)
        return perimeter_v

    @staticmethod
    def triangle_area(side_first, side_second, side_third):
        half_perimeter = (side_first + side_second + side_third) / 2
        area_v = (
            (half_perimeter *
            (half_perimeter - side_first) *
            (half_perimeter - side_second) *
            (half_perimeter - side_third)) ** 0.5
        )
        return area_v

    @staticmethod
    def triangle_perimeter(side_first, side_second, side_third):
        perimeter_v = side_first + side_second + side_third
        return perimeter_v

    @staticmethod
    def trapezoid_area(side_first, side_second, height):
        perimeter = 2 * (side_first + side_second)
        area_v = (perimeter / 4) * height
        return area_v

    @staticmethod
    def rhombus_area(side_first, height):
        area_v = side_first * height
        return area_v

    @staticmethod
    def sphere_area(radius):
        area_v = 4 * pi * radius ** 2
        return area_v

    @staticmethod
    def sphere_volume(radius):
        volume_v = 4 / 3 * pi * radius ** 3
        return volume_v

    @staticmethod
    def cube_area(side_first):
        area_v = 6 * side_first ** 2
        return area_v

    @staticmethod
    def cube_volume(side_first):
        volume_v = side_first ** 3
        return volume_v

    @staticmethod
    def parallelepiped_area(side_first, side_second, side_third):
        area_v = (
            2 * (side_first * side_second +
                 side_second * side_third +
                 side_first * side_third)
        )
        return area_v

    @staticmethod
    def pyramid_area(perimeter, apothem):
        area_v = 1 / 2 * perimeter * apothem
        return area_v

    @staticmethod
    def cylinder_area(radius, height):
        area_v = 2 * pi * radius * (height + radius)
        return area_v

    @staticmethod
    def cone_area(radius, slant_height):
        area_v = pi * radius * (slant_height + radius)
        return area_v

    def area(self):
        if self.name == 'Круг':
            return self.circle_area(**self.params)
        elif self.name == 'Квадрат':
            return self.square_area(**self.params)
        elif self.name == 'Прямоугольник':
            return self.rectangle_area(**self.params)
        elif self.name == 'Треугольник':
            return self.triangle_area(**self.params)
        elif self.name == 'Трапеция':
            return self.trapezoid_area(**self.params)
        elif self.name == 'Ромб':
            return self.rhombus_area(**self.params)
        elif self.name == 'Сфера':
            return self.sphere_area(**self.params)
        elif self.name == 'Куб':
            return self.cube_area(**self.params)
        elif self.name == 'Параллелепипед':
            return self.parallelepiped_area(**self.params)
        elif self.name == 'Пирамида':
            return self.pyramid_area(**self.params)
        elif self.name == 'Цилиндр':
            return self.cylinder_area(**self.params)
        elif self.name == 'Конус':
            return self.cone_area(**self.params)

    def perimeter(self):
        if self.name == 'Квадрат':
            return self.square_perimeter(**self.params)
        elif self.name == 'Прямоугольник':
            return self.rectangle_perimeter(**self.params)
        elif self.name == 'Треугольник':
            return self.triangle_perimeter(**self.params)

    def volume(self):
        if self.name == 'Сфера':
            return self.sphere_volume(**self.params)
        elif self.name == 'Куб':
            return self.cube_volume(**self.params)

    def validate(self, params: dict):
        if not all([None if param <= 0 else param for param in params.values()]):
            raise ValueError('Есть параметр <= нулю!')
