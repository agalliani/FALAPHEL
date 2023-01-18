from tkinter import *
from tkinter import ttk
from tkinter import filedialog as FD
from CommunicationService import CommunicationService


import glob
import serial
import json
import os


class SystemSettingsComponent:
    def ledOn(self):
        self.communicationService.sendChargeScan()

    def ledOff(self):
        self.communicationService.sendStop()

    def serialConnect(self, combobox, button):
        if(button['text'] == "Connect"):
            self.communicationService.serialConnect(combobox.get())
            self.ledOn()
            button.config(text="Disconnect")
        else:
            self.ledOff()
            combobox.set('')
            button.config(text="Connect")

    def askDirectory(self, label, button):
        self.directory = FD.askdirectory()
        label["text"] = self.directory if len(
            self.directory) < 60 else "..."+self.directory[-57:]
        print(self.directory)
        button['state'] = NORMAL

        self.communicationService.directory = self.directory

    def openDirectory(self):
        path = os.path.realpath(self.directory)
        os.startfile(path)

    def __init__(self, root):

        self.communicationService = CommunicationService()
        self.directory = ""

        serialPortsVar = StringVar()
        serialPortsCombobox = ttk.Combobox(root, textvariable=serialPortsVar)
        serialPortsCombobox['values'] = self.communicationService.getSerialPorts()
        serialPortsLabel = Label(root, text="Serial connection: ")

        serialPortConnectButton = ttk.Button(
            root, text="Connect", command=lambda: self.serialConnect(serialPortsCombobox, serialPortConnectButton))

        chosenPathLabel = Label(
            root, text=self.directory, width=50)

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
