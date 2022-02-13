class Shape:

    name = 'Фигура'
    image_filepath = ''
    characteristics = None

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def volume(self):
        raise NotImplementedError
