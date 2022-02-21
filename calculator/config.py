import os
from enum import Enum

from environs import Env


env = Env()
env.read_env()

FIGURES_IMAGES_FILEPATH = env('FIGURES_IMAGES_FILEPATH')


FRAMES = {
    'calc_window': {
        'geometry_size': '320x620',
        'title': 'Калькулятор',
    },
    'title': {
        'text': 'Калькулятор характеристик',
        'font': ('Helvetica', 15, 'bold', ),
        'borderwidth': 3,
        'relief': 'raised',
        'bg': '#1B6A97',
        'fg': '#FFFFFF',
        'width': 100,
        'padx': 2,
    },
    'ddmenu': {
        'content': 'Выбрать',
        'place': (80, 50),
    },
    'ddcharacterestic': {
        'content': 'Выбрать',
        'place': (80, 80),
    },
    'image': {
        'size': (150, 150),
        'place': (40, 110),
    },
    'input': {
        'delta': 40,
        'label_font': 20,
        'label_place': (20, 210),
        'entry_width': 20,
        'entry_bd': 3,
        'entry_font': 20,
        'entry_place': (40, 210),
    },
    'display': {
        'text': '',
        'font': ('Helvetica', 12, 'bold', ),
        'bg': '#FFFFFF',
        'width': 30,
        'height': 3,
        'place': (30, 480),
    },
    'button': {
        'font': ('Helvetica', 12, ),
        'bg': '#1B6A97',
        'fg': '#FFFFFF',
        'width': 8,
        'height': 1,
    },
    'clear_button': {
        'text': 'Очистить',
        'place': (30, 580),
    },
    'calcu_button': {
        'text': 'Вычислить',
        'place': (200, 580),
    }
}


class Characteristic(Enum):
    AREA = 'Площадь'
    PERIMETER = 'Периметр'
    VOLUME = 'Объём'


def get_image_filepath(figure_name, files_path=FIGURES_IMAGES_FILEPATH):
    for root, _, files in os.walk(files_path):
        for file in files:
            filename_without_ext = os.path.splitext(file)[0]
            if figure_name == filename_without_ext:
                return os.path.join(root, file)


FIGURES = {
    'Круг': {
        'name_en': 'circle',
        'image_filepath': get_image_filepath('circle'),
        'characteristics': [
            {
                'name': Characteristic.AREA.value,
                'params': {
                    'radius': 'r',
                },
            },
        ],
    },
    'Квадрат': {
        'name_en': 'square',
        'image_filepath': get_image_filepath('square'),
        'characteristics': [
            {
                'name': Characteristic.AREA.value,
                'params': {
                    'side_first': 'a',
                },
            },
            {
                'name': Characteristic.PERIMETER.value,
                'params': {
                    'side_first': 'a',
                },
            },
        ],
    },
    'Прямоугольник': {
        'name_en': 'rectangle',
        'image_filepath': get_image_filepath('rectangle'),
        'characteristics': [
            {
                'name': Characteristic.AREA.value,
                'params': {
                    'side_first': 'a',
                    'side_second': 'b',
                },
            },
            {
                'name': Characteristic.PERIMETER.value,
                'params': {
                    'side_first': 'a',
                    'side_second': 'b',
                },
            },
        ],
    },
    'Треугольник': {
        'name_en': 'triangle',
        'image_filepath': get_image_filepath('triangle'),
        'characteristics': [
            {
                'name': Characteristic.AREA.value,
                'params': {
                    'side_first': 'a',
                    'side_second': 'b',
                    'side_third': 'c',
                },
            },
            {
                'name': Characteristic.PERIMETER.value,
                'params': {
                    'side_first': 'a',
                    'side_second': 'b',
                    'side_third': 'c',
                },
            },
        ],
    },
    'Трапеция': {
        'name_en': 'trapezoid',
        'image_filepath': get_image_filepath('trapezoid'),
        'characteristics': [
            {
                'name': Characteristic.AREA.value,
                'params': {
                    'side_first': 'a',
                    'side_second': 'b',
                    'height': 'h',
                },
            },
        ],
    },
    'Ромб': {
        'name_en': 'rhombus',
        'image_filepath': get_image_filepath('rhombus'),
        'characteristics': [
            {
                'name': Characteristic.AREA.value,
                'params': {
                    'side_first': 'a',
                    'height': 'h',
                },
            },
        ],
    },
    'Сфера': {
        'name_en': 'sphere',
        'image_filepath': get_image_filepath('sphere'),
        'characteristics': [
            {
                'name': Characteristic.AREA.value,
                'params': {
                    'radius': 'r',
                },
            },
            {
                'name': Characteristic.VOLUME.value,
                'params': {
                    'radius': 'r',
                },
            },
        ],
    },
    'Куб': {
        'name_en': 'cube',
        'image_filepath': get_image_filepath('cube'),
        'characteristics': [
            {
                'name': Characteristic.AREA.value,
                'params': {
                    'side_first': 'a',
                },
            },
            {
                'name': Characteristic.VOLUME.value,
                'params': {
                    'side_first': 'a',
                },
            },
        ],
    },
    'Параллелепипед': {
        'name_en': 'parallelepiped',
        'image_filepath': get_image_filepath('parallelepiped'),
        'characteristics': [
            {
                'name': Characteristic.AREA.value,
                'params': {
                    'side_first': 'a',
                    'side_second': 'b',
                    'side_third': 'c',
                },
            },
        ],
    },
    'Пирамида': {
        'name_en': 'pyramid',
        'image_filepath': get_image_filepath('pyramid'),
        'characteristics': [
            {
                'name': Characteristic.AREA.value,
                'params': {
                    'perimeter': 'p',
                    'apothem': 'f',
                },
            },
        ],
    },
    'Цилиндр': {
        'name_en': 'cylinder',
        'image_filepath': get_image_filepath('cylinder'),
        'characteristics': [
            {
                'name': Characteristic.AREA.value,
                'params': {
                    'radius': 'r',
                    'height': 'h',
                },
            },
        ],
    },
    'Конус': {
        'name_en': 'cone',
        'image_filepath': get_image_filepath('cone'),
        'characteristics': [
            {
                'name': Characteristic.AREA.value,
                'params': {
                    'radius': 'r',
                    'slant_height': 'l',
                },
            },
        ],
    },
}
