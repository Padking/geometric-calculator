import tkinter as tk

from PIL import (
    Image,
    ImageTk,
)

import config

from figure import Shape
from interface import ShapeInterface


class TkinterCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry(config.FRAMES['calc_window']['geometry_size'])
        self.window.resizable(0, 0)
        self.window.title(config.FRAMES['calc_window']['title'])

        self._characteristic_calculator = CharacteristicCalculator()

        self.title_frame = self.create_title_frame()
        self.ddmenu_frame, self.ddmenu_frame_content = self.create_ddmenu_frame()
        self._ddcharacteristic_frame = None
        self._ddcharacteristic_frame_content = None
        self._image_frame = None
        self._input_frame = None
        self.display_frame = self.create_display_frame()

        self.create_special_buttons()

    def run(self):
        self.window.mainloop()

    # Создание интерактивных фреймов калькулятора

    def create_title_frame(self):

        text = config.FRAMES['title']['text']
        font = config.FRAMES['title']['font']
        borderwidth = config.FRAMES['title']['borderwidth']
        relief = config.FRAMES['title']['relief']
        bg = config.FRAMES['title']['bg']
        fg = config.FRAMES['title']['fg']
        width = config.FRAMES['title']['width']
        padx = config.FRAMES['title']['padx']

        frame_label = tk.Label(self.window, text=text, font=font,
                               borderwidth=borderwidth, justify=tk.CENTER,
                               relief=relief,
                               bg=bg, fg=fg,
                               width=width)
        frame_label.pack(padx=padx)

    def create_ddmenu_frame(self):

        content = config.FRAMES['ddmenu']['content']
        x, y = config.FRAMES['ddmenu']['place']

        frame_content = tk.StringVar()
        frame_content.set(content)

        frame_option_menu_items = [figure_name
                                   for figure_name in config.FIGURES]
        frame_option_menu = tk.OptionMenu(self.window, frame_content,
                                          *frame_option_menu_items,
                                          command=self.shape_choiced)

        frame_option_menu.pack(expand=True)
        frame_option_menu.place(x=x, y=y)
        return frame_option_menu, frame_content

    def create_ddcharacterestic_frame(self):

        content = config.FRAMES['ddcharacterestic']['content']
        x, y = config.FRAMES['ddcharacterestic']['place']

        frame_content = tk.StringVar()
        frame_content.set(content)

        figure_choiced_name = self.ddmenu_frame_content.get()
        characteristics = config.FIGURES[figure_choiced_name]['characteristics']
        frame_option_menu_items = [characteristic['name']
                                   for characteristic in characteristics]

        frame_option_menu = tk.OptionMenu(self.window, frame_content,
                                          *frame_option_menu_items,
                                          command=self.characteristic_choiced)

        frame_option_menu.pack(expand=True)
        frame_option_menu.place(x=x, y=y)
        return frame_option_menu, frame_content

    def create_image_frame(self, image_filepath):

        size = config.FRAMES['image']['size']
        x, y = config.FRAMES['image']['place']

        img = Image.open(image_filepath)
        img_ = img.resize(size)
        image = ImageTk.PhotoImage(img_)
        frame_label = tk.Label(self.window, image=image)
        frame_label.image = image
        frame_label.place(x=x, y=y)

        return frame_label

    def create_input_frame(self, frame_label_map_entry=None):

        figure_choiced_name = self.ddmenu_frame_content.get()
        figure_choiced_characteristic = self._ddcharacteristic_frame_content.get()

        characteristics = config.FIGURES[figure_choiced_name]['characteristics']
        figure_params_ = [characteristic['params'].values()
                          for characteristic in characteristics
                          if characteristic['name'] == figure_choiced_characteristic]
        frame_label_map_entry = self.get_input_fields(*figure_params_)

        return frame_label_map_entry

    def create_display_frame(self):

        text = config.FRAMES['display']['text']
        font = config.FRAMES['display']['font']
        bg = config.FRAMES['display']['bg']
        width = config.FRAMES['display']['width']
        height = config.FRAMES['display']['height']
        x, y = config.FRAMES['display']['place']

        frame_label = tk.Label(text=text, font=font,
                               bg=bg, width=width,
                               height=height)
        frame_label.place(x=x, y=y)

        return frame_label

    def create_special_buttons(self):

        text_clear_button = config.FRAMES['clear_button']['text']
        x_clear_button, y_clear_button = config.FRAMES['clear_button']['place']

        text_calcu_button = config.FRAMES['calcu_button']['text']
        x_calcu_button, y_calcu_button = config.FRAMES['calcu_button']['place']

        clear_button = tk.Button(text=text_clear_button,
                                 command=self.clear_button_pushed,
                                 **config.FRAMES['button'])
        calcu_button = tk.Button(text=text_calcu_button,
                                 command=self.calculate_button_pushed,
                                 **config.FRAMES['button'])

        clear_button.place(x=x_clear_button, y=y_clear_button)
        calcu_button.place(x=x_calcu_button, y=y_calcu_button)

    # Обработчики воздействий

    def shape_choiced(self, event):
        frame_option_menu, frame_content = self.create_ddcharacterestic_frame()
        self._ddcharacteristic_frame = frame_option_menu
        self._ddcharacteristic_frame_content = frame_content

    def characteristic_choiced(self, *args):

        figure_choiced_name = self.ddmenu_frame_content.get()
        image_filepath = config.FIGURES[figure_choiced_name]['image_filepath']

        # Повторный выбор характеристики для той же фигуры
        try:
            self._image_frame.place_forget()
            {frame_entry_label.place_forget(): frame_entry.place_forget()
             for frame_entry_label, frame_entry in self._input_frame.items()}
            self.display_frame.config(text='')
        except Exception:
            pass

        self._image_frame = self.create_image_frame(image_filepath)
        self._input_frame = self.create_input_frame()

    def calculate_button_pushed(self, *args):

        figure_choiced_name = self.ddmenu_frame_content.get()
        figure_choiced_characteristic = self._ddcharacteristic_frame_content.get()

        figure_params = {self.get_param_by_alias(figure_choiced_name,
                                                 figure_choiced_characteristic,
                                                 frame_entry_label.cget('text')): float(frame_entry.get())
                         for frame_entry_label, frame_entry in self._input_frame.items()}

        figure_ = Shape(figure_choiced_name)
        figure_.params = figure_params
        try:
            figure_.validate(figure_params)
        except ValueError:
            return
        else:
            calculation_result = (self._characteristic_calculator
                                  .get_characteristic(figure_,
                                                      figure_choiced_characteristic))

            self.display_frame.config(text=calculation_result)

    def clear_button_pushed(self, *args):

        content = config.FRAMES['ddmenu']['content']

        self.ddmenu_frame_content.set(content)
        self._ddcharacteristic_frame.place_forget()

        self._image_frame.place_forget()

        {frame_entry_label.place_forget(): frame_entry.place_forget()
         for frame_entry_label, frame_entry in self._input_frame.items()}

        self.display_frame.config(text='')

    @staticmethod
    def get_param_by_alias(figure_name, ch_name, alias_name):

        characteristics = config.FIGURES[figure_name]['characteristics']
        for characteristic in characteristics:
            if characteristic['name'] == ch_name:
                for param_name, alias in characteristic['params'].items():
                    if alias == alias_name:
                        return param_name

    def get_input_fields(self, figure_params, frame_label_map_entry=None) -> dict:

        delta = config.FRAMES['input']['delta']
        label_font = config.FRAMES['input']['label_font']
        entry_width = config.FRAMES['input']['entry_width']
        entry_bd = config.FRAMES['input']['entry_bd']
        entry_font = config.FRAMES['input']['entry_font']
        x_label, y_ = config.FRAMES['input']['label_place']
        x_entry = config.FRAMES['input']['entry_place'][0]

        frame_label_map_entry = frame_label_map_entry or {}
        for step, figure_param in enumerate(figure_params, 1):
            frame_content = tk.DoubleVar()
            y = y_ + delta * step

            frame_entry_label = tk.Label(text=figure_param, font=label_font)
            frame_entry = tk.Entry(self.window, textvariable=frame_content,
                                   width=entry_width, bd=entry_bd, font=entry_font)
            frame_entry_label.place(x=x_label, y=y)
            frame_entry.place(x=x_entry, y=y)

            frame_label_map_entry[frame_entry_label] = frame_entry

        return frame_label_map_entry


class CharacteristicCalculator:

    def get_characteristic(self, figure: ShapeInterface, ch_name):
        if ch_name == config.Characteristic.AREA.value:
            characteristic = figure.area()
        elif ch_name == config.Characteristic.PERIMETER.value:
            characteristic = figure.perimeter()
        elif ch_name == config.Characteristic.VOLUME.value:
            characteristic = figure.volume()

        return '{:.8f}'.format(characteristic)


if __name__ == '__main__':
    tkinter_calculator = TkinterCalculator()
    tkinter_calculator.run()
