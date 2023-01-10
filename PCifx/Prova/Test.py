from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from kivy.uix.dropdown import DropDown


# In the kv file, everything to the right of the colon is pure python
# for loading python module in kv file, use format of #:  import keyword module_name


class WeatherWidget(GridLayout):
    def printing_test(self):
        print('This is a test')



class DailyViewApp(App):
    def build(self):
        return WeatherWidget()


if __name__ == '__main__':
    DailyViewApp().run()
