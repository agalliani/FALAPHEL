from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import kivy

import serial

kivy.require("1.9.1")


# class in which we are creating the button

class ButtonApp(App):

    def build(self):
        # use a (r, g, b, a) tuple
        btnStart = Button(text="START",
                          font_size="20sp",
                          background_color=(1, 1, 1, 1),
                          color=(1, 1, 1, 1),
                          size=(32, 32),
                          size_hint=(.2, .2),
                          pos=(300, 250))
        btnStart.bind(on_release=self.callbackStart)

        btnStop = Button(text="STOP",
                          font_size="20sp",
                          background_color=(1, 1, 1, 1),
                          color=(1, 1, 1, 1),
                          size=(32, 32),
                          size_hint=(.2, .2),
                          pos=(300, 250))
        btnStop.bind(on_release=self.callbackStop)

        boxlayout = BoxLayout()
        boxlayout.add_widget(btnStart)
        boxlayout.add_widget(btnStop)

        return boxlayout

    # callback function tells when button pressed
    def callbackStart(self, event):
        serialPort.write(b"START")
        print(serialPort.readline().strip().decode())

    def callbackStop(self, event):
        serialPort.write(b"STOP")
        print(serialPort.readline().strip().decode())



if __name__ == '__main__':
    serialPort = serial.Serial(
        port="COM10", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    #serialString = ""

    ButtonApp().run()
