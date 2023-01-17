from tkinter import *
from tkinter import ttk


class CustomConfigComponent:

    def __init__(self, root):
       # Elements declaration

        # Start pixel selection
        startPixelSelectionVal = StringVar(value="0")
        startPixelSelectionSpinbox = ttk.Spinbox(
            root, from_=0, to=29, textvariable=startPixelSelectionVal, wrap=True)
        startPixelSelectionLabel = Label(root, text="Start pixel range")

        # End pixel selection TODO: if single pixel scan enabled, then this deactivated
        endPixelSelectionVal = StringVar(value="0")
        endPixelSelectionSpinbox = ttk.Spinbox(
            root, from_=1, to=30, textvariable=endPixelSelectionVal, wrap=True)
        endPixelSelectionLabel = Label(root, text="End pixel range")

        # Boolean single pixel scan
        isSinglePixelVal = BooleanVar(value=False)
        isSinglePixelCheck = ttk.Checkbutton(
            root, text="Single pixel scan", onvalue=True, offvalue=False)
        isSinglePixelCheck.state(['!alternate'])

        buttonCustomScan = ttk.Button(
            root, text="Custom Charge Scan")  # button

       # Positioning

        startPixelSelectionSpinbox.grid(
            column=0, row=0, pady=5)
        startPixelSelectionLabel.grid(
            column=1, row=0,  sticky=(W))

        endPixelSelectionSpinbox.grid(
            column=0, row=1,  padx=5, pady=5)
        endPixelSelectionLabel.grid(
            column=1, row=1, sticky=(W), pady=5)

        isSinglePixelCheck.grid(column=0, row=2,  pady=5)

        buttonCustomScan.grid(column=2, row=1, sticky=(E), padx=5)

