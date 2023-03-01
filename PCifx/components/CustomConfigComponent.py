from tkinter import *

from services.CommunicationService import CommunicationService


class CustomConfigComponent:

    def __init__(self, root):

        self.communicationService = CommunicationService()
       # Elements declaration

        # Start pixel selection
        self.startPixelSelectionVal = IntVar(value="0")

        # End pixel selection TODO: if single pixel scan enabled, then this deactivated
        self.endPixelSelectionVal = IntVar(value="0")

        # Boolean single pixel scan
        self.isSinglePixelVal = BooleanVar(value=False)

        self.create_widgets(root)
        self.position_widgets(root)

    def create_widgets(self, root):
        self.startPixelSelectionSpinbox = Spinbox(
            root,
            from_=0,
            to=29,
            textvariable=self.startPixelSelectionVal,
            command=lambda: self.communicationService.setCustomStart(
                self.startPixelSelectionVal.get()),
            wrap=True)
        self.startPixelSelectionSpinbox.bind(
            "<Return>", self.setAll
        )

        self.startPixelSelectionLabel = Label(root, text="Start pixel range")

        self.endPixelSelectionSpinbox = Spinbox(
            root,
            from_=1,
            to=30,
            textvariable=self.endPixelSelectionVal,
            command=lambda: self.communicationService.setCustomEnd(
                self.endPixelSelectionVal.get()),
            wrap=True)
        self.endPixelSelectionSpinbox.bind(
            "<Return>", self.setAll
        )

        self.endPixelSelectionLabel = Label(root, text="End pixel range")

        self.isSinglePixelCheck = Checkbutton(
            root,
            text="Single pixel scan",
            variable=self.isSinglePixelVal,
            command=lambda: self.activateSinglePixelScan(),
            onvalue=True,
            offvalue=False)

        self.buttonCustomScan = Button(
            root,
            text="Custom Charge Scan",
            command=lambda: self.communicationService.printCustomScanSettings())  # button

    def position_widgets(self, root):
        # Positioning

        self.startPixelSelectionSpinbox.grid(
            column=0, row=0, pady=5)
        self.startPixelSelectionLabel.grid(
            column=1, row=0,  sticky=(W))

        self.endPixelSelectionSpinbox.grid(
            column=0, row=1,  padx=5, pady=5)
        self.endPixelSelectionLabel.grid(
            column=1, row=1, sticky=(W), pady=5)

        self.isSinglePixelCheck.grid(column=0, row=2,  pady=5)

        self.buttonCustomScan.grid(column=2, row=1, sticky=(E), padx=5)

    def activateSinglePixelScan(self):
        if(self.isSinglePixelVal.get() == True):
            self.communicationService.setCustomSinglePixel(True)

            self.endPixelSelectionLabel["text"] = "Pixel index"
            self.startPixelSelectionSpinbox["state"] = "disabled"
            self.startPixelSelectionLabel["text"] = ""
        else:
            self.communicationService.setCustomSinglePixel(False)
            self.endPixelSelectionLabel["text"] = "Start pixel range"
            self.startPixelSelectionSpinbox["state"] = "normal"
            self.startPixelSelectionLabel["text"] = "End pixel range"

    def setAll(self, event):
        self.communicationService.setCustomStart(
            self.startPixelSelectionVal.get())
        self.communicationService.setCustomEnd(self.endPixelSelectionVal.get())
        self.communicationService.printCustomScanSettings()
