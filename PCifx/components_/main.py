from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

import serial
import json

from serial_ports import serial_ports


class CustomDropDown(DropDown):

    def __init__(self, **kwargs):
        super(CustomDropDown, self).__init__(**kwargs)
        self.add_buttons()

    def add_buttons(self):
        portList = serial_ports()
        for port in portList:
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.
            btn = Button(text=port, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.select(btn.text))
            self.add_widget(btn)


class Notes(Screen):
    pass


class MyScreenManager(GridLayout):

    serial = serial.Serial()
    serial.baudrate = 9600

    def setSerialConnectionPort(self, value):
        self.serial.port = value
        self.serial.open()
        data = {}
        data["operation"] = "CHARGE_SCAN"
        data = json.dumps(data)

        if not self.serial.isOpen():
            print("serial port is closed")

        self.serial.write(data.encode('ascii'))
        # serialPort.flush()
        try:
            while(True):
                incoming = self.serial.readline().strip().decode("utf-8")
                print(incoming)
                if(incoming == "EOC"):
                    print("Closing serial communication")

                    break
        except Exception as e:
            print(e)
            pass

    def callbackStop(self):
        if self.serial.is_open:
            data = {}
            data["operation"] = "STOP"
            data = json.dumps(data)

            self.serial.write(data.encode('ascii'))
            # serialPort.flush()
            try:
                while(True):
                    incoming = self.serial.readline().strip().decode("utf-8")
                    print(incoming)
                    if(incoming == "EOC"):
                        self.ids.Notes.ids.mainbutton.text = "Press to select"
                        self.serial.close()
                        break
            except Exception as e:
                print(e)
                pass
        else:
            print("Attempting a connection that does not exist")


class TestbenchApp(App):
    title = "Test Bench Falaphel Sync"

    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    TestbenchApp().run()
