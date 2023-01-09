from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import kivy

import serial
import json

kivy.require("1.9.1")


# class in which we are creating the button

class ButtonApp(App):

    def build(self):

        btnStop = Button(text="STOP",
                         font_size="20sp",
                         background_color=(1, 1, 1, 1),
                         color=(1, 1, 1, 1),
                         size=(32, 32),
                         size_hint=(.2, .2),
                         pos=(300, 250))
        btnStop.bind(on_release=self.callbackStop)

        btnChargeScan = Button(text="Charge Scan",
                               font_size="20sp",
                               background_color=(1, 1, 1, 1),
                               color=(1, 1, 1, 1),
                               size=(32, 32),
                               size_hint=(.2, .2),
                               pos=(300, 250))
        btnChargeScan.bind(on_release=self.callbackChargeScan)

        boxlayout = BoxLayout()
        boxlayout.add_widget(btnStop)
        boxlayout.add_widget(btnChargeScan)

        return boxlayout

    def callbackStop(self, event):
        data = {}
        data["operation"] = "STOP"
        data = json.dumps(data)

        if not serialPort.isOpen():
            print("serial port is closed")

        serialPort.write(data.encode('ascii'))
        # serialPort.flush()
        try:
            while(True):
                incoming = serialPort.readline().strip().decode("utf-8")
                print(incoming)
                if(incoming == "EOC"):
                    break
        except Exception as e:
            print(e)
            pass
            # serialPort.close()

    def callbackChargeScan(self, event):
        data = {}
        data["operation"] = "CHARGE_SCAN"
        data = json.dumps(data)

        if not serialPort.isOpen():
            print("serial port is closed")

        serialPort.write(data.encode('ascii'))
        # serialPort.flush()
        try:
            while(True):
                incoming = serialPort.readline().strip().decode("utf-8")
                print(incoming)
                if(incoming == "EOC"):
                    print("Closing serial communication")

                    break
        except Exception as e:
            print(e)
            pass
            # serialPort.close()


if __name__ == '__main__':
    serialPort = serial.Serial(
        port="COM10", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    ButtonApp().run()
