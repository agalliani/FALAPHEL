from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.core.window import Window




class CustomDropDown(DropDown):

    def __init__(self, **kwargs):
        super(CustomDropDown, self).__init__(**kwargs)
        self.add_buttons()

    def add_buttons(self):
        for index in range(10):
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.

            btn = Button(text='Value %d' % index, size_hint_y=None, height=44)

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            btn.bind(on_release=lambda btn: self.select(btn.text))

            # then add the button inside the dropdown
            self.add_widget(btn)


class Notes(Screen):
    pass


class MyScreenManager(ScreenManager):

    def Run_Draws_Test(self, value):
        print(value)


class TestApp(App):
    title = "Kivy Drop-Down List Demo"

    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    TestApp().run()