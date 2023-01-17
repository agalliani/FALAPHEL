from tkinter import *
from tkinter import ttk
from tkinter import filedialog as FD


import sys
import glob
import serial
import json
import os


class SystemSettingsComponent:
    serial = serial.Serial()
    serial.baudrate = 9600

    directory = ""

    def ledOn(self):
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

    def ledOff(self):
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
                    if("EOC" in incoming):
                        self.serial.close()
                        break
            except Exception as e:
                print(e)
                pass
        else:
            print("Attempting a connection that does not exist")

    def serialConnect(self, combobox, button):
        if(button['text'] == "Connect"):
            self.serial.port = combobox.get()
            self.serial.open()
            self.ledOn()

            button.config(text="Disconnect")
            print(combobox.get())
        else:
            self.ledOff()
            combobox.set('')
            button.config(text="Connect")

    def getSerialPorts(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cynwin'):
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

    def askDirectory(self, label, button):
        self.directory = FD.askdirectory()
        label["text"] = self.directory if len(
            self.directory) < 60 else "..."+self.directory[-57:]
        print(self.directory)
        button['state'] = NORMAL

    def openDirectory(self):
        print("open dir")
        path = os.path.realpath(self.directory)
        os.startfile(path)

    def __init__(self, root):

        serialPortsVar = StringVar()
        serialPortsCombobox = ttk.Combobox(root, textvariable=serialPortsVar)
        serialPortsCombobox['values'] = self.getSerialPorts()
        serialPortsLabel = Label(root, text="Serial connection: ")

        serialPortConnectButton = ttk.Button(
            root, text="Connect", command=lambda: self.serialConnect(serialPortsCombobox, serialPortConnectButton))

        chosenPathLabel = Label(root, text=self.directory, width=50)

        openButton = ttk.Button(root, text="Open folder",
                                command=lambda: self.openDirectory(), state=DISABLED)

        saveButton = ttk.Button(root, text="Choose",
                                command=lambda: self.askDirectory(chosenPathLabel, openButton))
        saveButtonLabel = Label(root, text="Saving folder: ")

        # Positioning
        serialPortsLabel.grid(column=0, row=0, padx=5, pady=5, sticky=(W))

        serialPortsCombobox.grid(
            column=1, row=0, padx=5, pady=5, sticky=(W))

        serialPortConnectButton.grid(
            column=1, row=0, padx=(155, 5), pady=5, sticky=(W))

        saveButtonLabel.grid(column=0, row=1, padx=5, pady=5, sticky=(W))
        saveButton.grid(column=1, row=1, padx=5, pady=5, sticky=(W))
        chosenPathLabel.grid(column=0, row=2, columnspan=3, sticky=(W))

        openButton.grid(column=1, row=1, padx=(100, 5), pady=5, sticky=(W))
