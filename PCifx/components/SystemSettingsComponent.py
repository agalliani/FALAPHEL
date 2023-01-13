from tkinter import *
from tkinter import ttk
from tkinter import filedialog as FD


class SystemSettingsComponent:
    directory = ""

    def askDirectory(self, label):
        self.directory = FD.askdirectory()
        label["text"] = self.directory if len(
            self.directory) < 50 else "..."+self.directory[-37:]

    def __init__(self, root):

        serialPortsVar = StringVar()
        serialPortsCombobox = ttk.Combobox(root, textvariable=serialPortsVar)
        serialPortsCombobox['values'] = ('COM1', 'COM2', 'COM10')
        serialPortsLabel = Label(root, text="Serial connection: ")

        chosenPathLabel = Label(root, text=self.directory, width=50)

        saveButton = ttk.Button(root, text="Choose",
                                command=lambda: self.askDirectory(chosenPathLabel))
        saveButtonLabel = Label(root, text="Saving folder: ")

        # Positioning
        serialPortsLabel.grid(column=0, row=0, padx=5, pady=5, sticky=(W))
        serialPortsCombobox.grid(column=1, row=0, padx=5, pady=5, sticky=(W))

        saveButtonLabel.grid(column=0, row=1, padx=5, pady=5, sticky=(W))
        saveButton.grid(column=1, row=1, padx=5, pady=5, sticky=(W))
        chosenPathLabel.grid(column=0, row=2, columnspan=3, sticky=(W))

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)

        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)
