from enum import Enum


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


FIGURE_PARAMETERS_NOTATIONS = {
    'apothem': 'f',
    'height': 'h',
    'perimeter': 'p',
    'radius': 'r',
    'side': 'a',
    'side_first': 'a',
    'side_second': 'b',
    'side_third': 'c',
    'slant_height': 'l',
}


class Characteristic(Enum):
    AREA = 'Площадь'
    PERIMETER = 'Периметр'
    VOLUME = 'Объём'
