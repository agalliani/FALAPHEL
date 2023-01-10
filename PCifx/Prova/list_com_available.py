import sys
import glob
import serial
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import kivy
kivy.require("1.9.1")


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class BoxLayoutApp(App):

    def build(self):

        # To position oriented widgets again in the proper orientation
        # use of vertical orientation to set all widgets
        superBox = BoxLayout(orientation='vertical')

        # To position widgets next to each other,
        # use a horizontal BoxLayout.
        HB = BoxLayout(orientation='horizontal')

        labelDropdown = Label(text="Label",font_size='20sp' )
        dropdown = DropDown()

        portList = serial_ports()
        for port in portList:
            btn = Button(text=port, height=25)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        # create a big main button
        mainbutton = Button(text='Select port', pos=(
            200, 250), size_hint=(.25, .10))
        mainbutton.bind(on_release=dropdown.open)

        dropdown.bind(on_select=lambda instance,
                      x: setattr(mainbutton, 'text', x))

        # HB represents the horizontal boxlayout orientation
        # declared above
        HB.add_widget(labelDropdown)
        HB.add_widget(mainbutton)

        # To position widgets above/below each other,
        # use a vertical BoxLayout.
        VB = BoxLayout(orientation='vertical')

        btn3 = Button(text="Three")
        btn4 = Button(text="Four")

        # VB represents the vertical boxlayout orientation
        # declared above
        VB.add_widget(btn3)
        VB.add_widget(btn4)

        # superbox used to again align the oriented widgets
        superBox.add_widget(HB)
        superBox.add_widget(VB)

        return superBox


# creating the object root for BoxLayoutApp() class
root = BoxLayoutApp()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
root.run()
